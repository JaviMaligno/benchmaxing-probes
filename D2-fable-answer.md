## Diagnóstico

El código actual tiene dos fallos: usa `delivery_id` como clave (el broker lo cambia en cada reenvío, así que un reenvío tras 36 h produce una segunda preparación con clave distinta) y llama a `prepare` **antes** de escribir nada durable. Si el worker cae entre la llamada y el INSERT (el escenario de las 09:00), no queda rastro: el reenvío a t+50 h reintenta fuera de la ventana de idempotencia y prepara dos veces.

## Evaluación de la afirmación del colega

Parcialmente correcta. La clave `warehouse_id:order_id` es acertada (estable entre reenvíos, distingue almacenes con el mismo order_id). Pero:

- El UNIQUE solo protege la carrera del INSERT final; la concurrencia real la cubre la clave idempotente del proveedor, no la DB. Y sigue el agujero: caída tras enviar y antes de insertar deja cero filas.
- **Es falso** que el caso incierto post-36 h sea imprevisible. No se puede *resolver* automáticamente, pero sí *prevenir la doble preparación*: basta registrar la intención antes de enviar y negarse a reenviar pasadas las 36 h, bloqueando para revisión — exactamente lo que el requisito prioriza.

## Propuesta

Tabla `preparations` con `UNIQUE(warehouse_id, order_id)` y columnas `state`, `sent_at`, `lease_owner`, `lease_until`, `receipt`.

Estados: `PENDING → SENT → DONE`, más `BLOCKED` (terminal, revisión manual).

Transiciones (cada una en su transacción):

1. **Llega evento**: `INSERT ... ON CONFLICT DO NOTHING` con `state=PENDING`. Si ya existe `DONE` o `BLOCKED`, terminar (dedupe de reenvíos).
2. **Tomar lease**: `UPDATE ... SET lease_owner=yo, lease_until=now()+5min WHERE state IN ('PENDING','SENT') AND (lease_until IS NULL OR lease_until<now())`. Si afecta 0 filas, otro worker lo tiene.
3. **Antes de enviar**: `UPDATE SET state='SENT', sent_at=COALESCE(sent_at, now())` y commit. `sent_at` nunca se sobrescribe.
4. **Decisión de envío** (última instrucción antes de la red): si `now() > sent_at + 36h − margen` (margen ≈ 1 h) y no hay `receipt`, marcar `BLOCKED` y no llamar. Si no, llamar `prepare("wid:oid", payload)`.
5. **Éxito**: `UPDATE SET state='DONE', receipt=... WHERE lease_owner=yo AND lease_until>now()`. Si afecta 0 filas, descartar el resultado; el dueño actual del lease decidirá.

**Caída justo antes de enviar**: existe fila `SENT` con `sent_at`, pero quizá el proveedor nunca recibió nada. El reenvío del broker permite retomar: dentro de `sent_at+36h` reenviar la misma clave es seguro (o es la primera llamada real, o es replay idempotente). Fuera, `BLOCKED`.

**Caída justo después de enviar**: idéntico estado en DB; mismo tratamiento. La ambigüedad es indistinguible y el diseño no necesita distinguirla.

**Worker antiguo pausado**: el proveedor no entiende fencing, así que el fencing se aplica en la DB (paso 5: sin lease vigente, su resultado se descarta) y su envío tardío es inofensivo porque usa la misma clave: dentro de las 36 h el proveedor devuelve el resultado previo.

## Trazas adversas

1. *Escenario dado*: 09:00 fila `SENT`, `sent_at=09:00`; éxito perdido; worker cae. A t+50 h otro worker toma el lease, ve `now > sent_at+36h`, marca `BLOCKED` sin llamar. El pedido del otro almacén tiene clave y fila propias: se tramita normal. Una preparación como máximo.
2. *Pausa larga*: A marca `SENT` a las 10:00 y se pausa antes de llamar. Su lease expira; B reenvía a las 10:30, obtiene receipt, `DONE`. A despierta a las 12:00, pasa el chequeo de plazo, envía la misma clave → replay idempotente; su UPDATE falla por lease. Sin daño.

## Límites

- Queda una ventana teórica: pausa mayor que el margen **entre** el chequeo del paso 4 y la emisión del paquete; el margen la hace despreciable, no imposible.
- Depende de relojes razonablemente sincronizados y de que `sent_at` sea cota inferior de la aceptación del proveedor.
- Los casos `BLOCKED` requieren intervención humana: es el coste asumido de priorizar "nunca dos".