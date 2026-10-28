## Diagnóstico

El código actual no es ni seguro ni idempotente. El `UNIQUE(warehouse_id, order_id)` no protege contra duplicados al proveedor: las filas finales solo se insertan **después** de `prepare`, y como `prepare` recibe `delivery_id` (único por reintento) y no `(warehouse_id, order_id)`, la misma orden puede prepararse dos veces. El caso de las 09:00 lo demuestra: `prepare` tuvo éxito, la respuesta se perdió, el worker cayó, y a t+50h el broker reenvía con otro `delivery_id`; sin fila intermedia que registre la aceptación, se invoca `prepare` de nuevo. Si la primera ejecución sigue dentro de las 36h, el proveedor devolverá el resultado previo (bien); si han pasado más de 36h (t+50h), ejecutará una **segunda preparación real**, violando «no preparar dos».

## Propuesta implementable

Sustituir la tabla actual por un registro de intenciones con estados, usando `warehouse_id || ':' || order_id` como clave lógica y `UNIQUE(warehouse_id, order_id)` como candado.

**Tabla `preparations`:** `warehouse_id`, `order_id`, `state`, `delivery_id`, `receipt`, `lease_owner`, `lease_until`, `updated_at`.

**Estados y transiciones** (todo en una transacción PostgreSQL por paso):

1. `RESERVED`: el worker hace `INSERT ... ON CONFLICT (warehouse_id, order_id) DO NOTHING`. Si inserta cero filas, otro worker ya es dueño → terminar. Tras insertar, fija `lease_owner` y `lease_until` (arrendamiento, p. ej. 10 min).

```
INSERT INTO preparations(warehouse_id,order_id,state,lease_owner,lease_until)
VALUES($1,$2,'RESERVED',$3,now()+interval '10 min')
ON CONFLICT DO NOTHING
```

2. `SENDING` (transición anterior a `prepare`): el worker **debe renovar el lease** con `UPDATE ... SET lease_until=now()+interval '10 min' WHERE lease_owner=$me AND state='RESERVED'`. Si la actualización afecta 0 filas, el lease expiró o fue tomado → abortar sin enviar.
3. Invocar `prepare(delivery_id, payload)` fuera de la transacción.
4. `DONE`: tras éxito, `INSERT` en la fila final (o `UPDATE` de `preparations`) con `UNIQUE(warehouse_id, order_id)`; el conflicto `UNIQUE` es señal de que otro ya completó → descartar.
5. `BLOCKED`: si el resultado es incierto (excepción, timeout, respuesta perdida), `UPDATE ... SET state='BLOCKED'` y **no reintentar automáticamente**.
6. Reintento solo con intervención humana o renovación de lease: para `BLOCKED` tras >36h, un operador decide si reenviar con nuevo `delivery_id`.

La clave para `prepare` debe seguir siendo `delivery_id` (único), pero el `UNIQUE` y el lease sobre `(warehouse_id, order_id)` impiden duplicados en origen.

## Trazas adversas

**A) Caída justo antes de enviar:** el worker reserva (`RESERVED`), renueva lease, y cae **antes** de llamar a `prepare`. No hay fila final. A t+50h el broker reenvía. El nuevo worker ve `RESERVED` con `lease_until` vencido, toma el lease (`UPDATE ... SET lease_owner=$yo2, lease_until=... WHERE lease_until<now()`), y procede. No hay doble preparación: el primer `prepare` nunca se ejecutó.

**B) Caída justo después de enviar:** `prepare` se ejecuta y devuelve éxito, pero el worker cae antes de insertar la fila final. La fila sigue en `SENDING` (lease expirado). A t+50h, el nuevo worker toma el lease y llama a `prepare` de nuevo. Si el proveedor aún guarda el resultado (≤36h), devuelve el previo y se completa sin duplicado. Si ya pasaron >36h, el proveedor **ejecuta una segunda preparación**, violando el invariante. Por eso el paso 5 es crítico: tras un fallo o incertidumbre, marcar `BLOCKED` y no reenviar automáticamente; solo un humano (o una política explícita post-36h) decide.

## Límites

- **Las 36h son un agujero irresoluble con esta API:** si la respuesta se pierde y pasan >36h, no hay forma de saber si la primera preparación se completó. Ningún esquema con solo `prepare(key,payload)` puede garantizar «no preparar dos» en ese caso; solo puede **bloquear y pedir revisión**, que es lo correcto.
- **Fencing sin soporte del proveedor:** el proveedor no entiende `fencing token`; no se puede impedir que un `prepare` en vuelo se complete. El lease es solo una barrera de *admisión* local, no revoca llamadas ya enviadas.
- **Worker pausado que despierta tarde:** un worker con lease vencido que reanuda **después** de que otro tomó el lease debe fallar al renovar/actualizar: la condición `WHERE lease_owner=$me AND lease_until>=now()` devuelve 0 filas y le obliga a abortar **antes** de llamar a `prepare`. Si ya llamó a `prepare` antes de pausarse y despierta para insertar la fila final, el `UNIQUE` con `ON CONFLICT DO NOTHING` le hace descartar el resultado sin pisar al otro.
- **Sin búsqueda ni cancelación:** no se puede consultar al proveedor si una clave ya fue preparada; toda la memoria debe estar en la DB local.
- **Dos workers simultáneos:** `UNIQUE` + `INSERT ... ON CONFLICT DO NOTHING` garantiza un único dueño de la reserva; las renovaciones con `WHERE lease_owner=$me` evitan que un worker expropie a otro vivo.
- **Reenvíos del broker (96h):** el broker reenvía con distinto `delivery_id`; la clave lógica `(warehouse_id, order_id)` es la que desduplica, no el `delivery_id`.

## Sobre la afirmación del colega

Parcialmente correcta. Consultar la DB y capturar el conflicto `UNIQUE` **sí** cubre la concurrencia. Pero **no** cubre el caso incierto tras >36h: sin fila intermedia que registre la *aceptación* de `prepare` (aunque la respuesta se pierda), no se puede distinguir «prepare ejecutado, respuesta perdida» de «prepare nunca ejecutado». Su afirmación de que «es imposible de prevenir» es cierta, pero su conclusión de que basta `UNIQUE` es falsa: el `UNIQUE` solo evita duplicados en la fila final, no en el proveedor. La solución correcta es registrar un estado `BLOCKED` cuando el resultado es incierto, y no reenviar automáticamente.