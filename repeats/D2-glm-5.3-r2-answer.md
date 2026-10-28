## Diagnóstico

El diseño actual usa `delivery_id` como key. Como el broker cambia `delivery_id` en cada reenvío, dos intentos del mismo (almacén, pedido) llegan al proveedor con claves distintas: el cache de 36 h no los deduplica y se preparan dos paquetes. Además, IDs de pedido repetidos entre almacenes hacen obligatorio incluir `warehouse_id`. El colega acierta en la key (`warehouse_id:order_id`) y en que UNIQUE cubre la carrera de inserción entre dos workers; pero "consultar la DB" no cubre a un worker pausado que despierta, y la afirmación de que >36 h es "imposible de prevenir" es cierta para la segunda preparación física, no para toda la política: lo que sí se puede es no *enviar* de nuevo después de expirar el cache sin revisión humana, que es exactamente la prioridad exigida.

## Propuesta implementable

Dos tablas: `claims` con UNIQUE(warehouse_id, order_id), columnas `state`, `owner_id`, `lease_expires`, `sent_at`; y la fila final existente.

Estados de `claims`: `ACTIVE` (worker envió y espera respuesta), `DONE`, `QUARANTINE` (enviado sin confirmación y el primer envío tiene más de 36 h).

Transiciones, todo en transacciones PostgreSQL:

1. **Adquisición**: `INSERT ... ON CONFLICT DO NOTHING` con `owner_id` y `lease_expires = now()+T`. Si la fila existe y su lease no venció, el worker no envía nada. Si venció, `UPDATE ... SET owner_id=nuevo` (la DB serializa; el perdedor aborta).
2. **Antes de enviar** y **antes de escribir la fila final**, el worker verifica en la misma transacción que `owner_id` sigue siendo el suyo y su lease sigue viva; si no, aborta sin insertar. Esto es el fencing, resuelto en la DB porque el proveedor no entiende tokens.
3. Tras respuesta con receipt: transacción única que verifica propiedad del claim y hace `INSERT` en la fila final; `UNIQUE` final atrapa cualquier carrera residual.
4. **Corte de 36 h**: si `state=ACTIVE` y `now() > sent_at+36h` sin fila final → `QUARANTINE`, y ningún worker puede enviar con esa clave. Solo revisión humana la desbloquea.

## Trazas adversas

**T1 — caída justo antes de enviar.** Worker A adquiere claim, cae antes de `prepare`. Lease vence; worker B toma el claim (nuevo `owner_id`), envía con la misma key `w:o`, inserta fila final. Si A despierta: su verificación de propiedad falla y no envía ni escribe. Una preparación total.

**T2 — el escenario real (09:00).** A envía `prepare(w:o)`; el proveedor acepta a las 09:00 (arranca el reloj de 36 h) y la respuesta se pierde; A cae; no hay fila. Con reintentos agresivos, B reenvía antes de las 21:00 del día siguiente: el proveedor, con la misma key, devuelve el resultado cacheado; B escribe fila final; cero preparaciones extra. Variante adversa: nadie reenvía, a t+50 h B quiere enviar — el guardián del punto 4 ya marcó `QUARANTINE` (t+36 h desde `sent_at`) y se niega: **no** se ejecuta la segunda preparación; la orden queda para revisión, cumpliendo "no preparar dos tiene prioridad". El colega habría reenviado a t+50 h y provocado la doble preparación que creía inevitable. El otro almacén con el mismo ID es irrelevante porque la key lo separa.

Caída **justo después de enviar**, con B reenviando dentro de la ventana: idéntica a T2; el cache responde el receipt original.

## Límites

- La segunda preparación física sigue siendo posible si un envío llega al proveedor pero nunca queda registrado como `sent_at` (caída entre el `prepare` y el `UPDATE` a `ACTIVE`): escriba `sent_at` *antes* de enviar, no después.
- No hay atomicidad entre proveedor y DB; el diseño solo garantiza *a lo sumo un envío por ventana de 36 h más ningún envío tras ella sin revisión*, no exactamente un paquete en todos los mundos.
- La ventana depende de relojes de los workers; use `now()` de PostgreSQL, no relojes locales.
- `QUARANTINE` rompe "sin intervención", pero solo bajo el fallo real descrito, que es la prioridad declarada.