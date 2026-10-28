Expediente sintético de ingeniería

**Diagnóstico**

El código actual consulta solo la fila final y llama al proveedor sin dejar estado durable previo. Si la respuesta se pierde, no hay rastro hasta insertar la fila final. El `UNIQUE(warehouse_id,order_id)` evita duplicados en la tabla final, pero no evita una segunda preparación real después de 36 h: el proveedor acepta otra ejecución de la misma clave. La afirmación del colega es parcialmente correcta: `warehouse_id:order_id` como clave es adecuada y el conflicto `UNIQUE` cubre la inserción final; dentro de 36 h la deduplicación del proveedor también cubre reintentos concurrentes. Pero no basta consultar la DB y capturar `UNIQUE`: el caso incierto después de 36 h sí es prevenible si se registra la intención antes de enviar y se bloquea si no hay resultado dentro de la ventana.

**Propuesta implementable**

Tabla `prep_ops`:

- PK `(warehouse_id, order_id)`
- `state`: `PENDING | PREPARING | PREPARED | BLOCKED`
- `provider_key`: `warehouse_id:order_id`
- `lease_owner`, `lease_expires`, `attempt_started_at`, `receipt`

Tabla final con `UNIQUE(warehouse_id,order_id)`.

Transiciones:

1. Insertar `prep_ops` en `PENDING` con `ON CONFLICT DO NOTHING`.
2. Adquirir lease atómicamente:
```
UPDATE prep_ops
SET state='PREPARING',
    lease_owner=:worker,
    lease_expires=now()+interval '5 min',
    attempt_started_at=COALESCE(attempt_started_at, now())
WHERE warehouse_id=:w AND order_id=:o
  AND (state='PENDING'
       OR (state='PREPARING' AND lease_expires<now()))
RETURNING 1;
```
3. Revalidar justo antes de enviar:
```
SELECT 1 FROM prep_ops
WHERE warehouse_id=:w AND order_id=:o
  AND lease_owner=:worker AND lease_expires>now();
```
Si no devuelve fila, abortar.
4. Llamar `prepare(provider_key, payload)`.
5. Ante éxito, en una transacción:
```
WITH upd AS (
  UPDATE prep_ops
  SET state='PREPARED', lease_owner=NULL, receipt=:r
  WHERE warehouse_id=:w AND order_id=:o
    AND lease_owner=:worker
  RETURNING 1
)
INSERT INTO final(warehouse_id, order_id, receipt)
SELECT :w, :o, :r FROM upd
ON CONFLICT (warehouse_id, order_id) DO NOTHING;
```
6. Ante error de red o timeout, dejar `PREPARING` con `attempt_started_at` intacto. Si un worker ve `PREPARING` con lease vencido:
   - si `now() - attempt_started_at < 36 h`: volver al paso 2 con la misma `provider_key`;
   - si `>= 36 h`: marcar `BLOCKED` y no reenviar.

**Caídas antes y después de enviar**

- *Antes de enviar*: ya existe fila `PREPARING` confirmada. Si el worker cae, no hubo efecto externo. Otro worker toma el lease vencido y llama; si el primero no envió, el proveedor ejecuta una única preparación. Si el primero sí envió y dentro de 36 h, el proveedor devuelve el resultado previo.
- *Después de enviar*: el proveedor pudo aceptar. La fila `PREPARING` con `attempt_started_at` es el rastro durable. Un reintento antes de 36 h con la misma clave recupera el resultado; después de 36 h se bloquea y no se duplica.

**Trazas adversas**

1. W1 crea `PREPARING` a las 09:00, envía, el proveedor acepta, la respuesta se pierde y W1 cae. A las 09:10 W2 toma el lease vencido, ve menos de 36 h, reenvía `warehouse:order`. El proveedor devuelve el resultado previo. W2 inserta la fila final. No hay duplicado.
2. W1 envía a las 09:00, la respuesta se pierde y cae. Nadie reintenta hasta t+50 h. W2 ve `attempt_started_at=09:00`, detecta que pasaron más de 36 h, no llama a `prepare` y marca `BLOCKED` para revisión. Un pedido con igual `order_id` en otro almacén queda en otra fila y no se bloquea.

**Límites**

Un worker antiguo pausado puede reenviar si ya superó la revalidación de lease y queda justo antes de la llamada. Sin fencing tokens soportados por el proveedor, la comprobación y el envío no son atómicos: no hay forma de reducir ese riesgo a cero. Se minimiza revalidando inmediatamente antes de enviar y confirmando la escritura solo si `lease_owner` sigue siendo el worker.