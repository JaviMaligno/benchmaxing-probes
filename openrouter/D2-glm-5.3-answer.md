## Diagnóstico

- **Bug 1 (clave):** hoy se llama `prepare(delivery_id, …)`. El broker cambia `delivery_id` en cada reenvío, así que el proveedor ve una clave nueva y **puede preparar un segundo paquete**. Además, los `order_id` se repiten entre almacenes. Tu colega acierta en esto: la clave debe ser la identidad de negocio, `warehouse_id:order_id` (guardo también `event_id` solo para auditoría).
- **Bug 2 (estado):** solo existe la fila final. Si la respuesta se pierde (caso 09:00) no queda rastro ni **fecha del intento**. "Consultar la DB" es un check-then-act y no permite saber si la ventana de dedupe de 36 h sigue vigente. Como el broker reenvía 96 h > 36 h, llegarán reenvíos con la ventana del proveedor ya vencida.
- **Evaluación de la afirmación:** clave de negocio + capturar el conflicto UNIQUE es *necesario* (serializa las escrituras en DB; llamadas concurrentes con la misma clave quedan deduplicadas por el proveedor), pero **"basta" es falso**: sin registro previo al envío con marca temporal, el caso incierto tras 36 h produce un reintento arriesgado. Y el "imposible de prevenir" es un error de encuadre: lo que no se puede es **resolverlo automáticamente**; **prevenir el doble paquete sí se puede**: no volver a llamar a `prepare` una vez vencida la ventana, y bloquear para revisión (prioridad declarada: no duplicar > completar en automático).

## Propuesta implementable

Tabla `package_task`, `UNIQUE(warehouse_id, order_id)`: `status`, `key`, `t0` (marca del intento), `epoch`, `owner`, `lease_expira` (heartbeat), `receipt`.

Transiciones, todas con `UPDATE … WHERE <condición>` (no leer-y-decidir):

- `PENDING → INFLIGHT`: commit de `status='INFLIGHT', t0=now(), epoch=epoch+1, owner=yo` donde `status='PENDING'` **o** (`INFLIGHT` y lease vencida y `now() < t0+36h−δ`). Después, una única llamada `prepare(key)`.
- `INFLIGHT → DONE`: `SET status='DONE', receipt=… WHERE id=… AND epoch=mío AND status='INFLIGHT'`; 0 filas ⇒ estoy caducado, descarto.
- `INFLIGHT → BLOCKED`: si `now() ≥ t0+36h−δ` sin receipt: **no llamar** a `prepare`; alerta humana.
- `BLOCKED → DONE/CANCELLED`: solo manual (verificación con operaciones del proveedor; no existe API de búsqueda).
- `DONE` + reenvío: ack, sin efecto.

`t0` se escribe **antes** del envío: es cota inferior de la primera aceptación del proveedor, luego su dedupe cubre **al menos** hasta `t0+36h`. Caída **justo antes de enviar**: fila `INFLIGHT`, proveedor sin llamada; el reintento antes de `t0+36h−δ` o ejecuta por primera vez o devuelve lo cacheado → `DONE`. Caída **justo después de enviar**: respuesta perdida; el reenvío dentro de ventana devuelve el mismo resultado → `DONE`.

## Trazas adversas

1. **Incidente:** A: `INFLIGHT t0=09:00`, `prepare(key)` con éxito en servidor, respuesta perdida, caída 09:01. En t+50 h, B lee `INFLIGHT` con `t0+50h > 36h−δ` → `BLOCKED`; humano cierra con el proveedor. Con el código actual: `prepare(delivery_id nuevo)` ⇒ clave nueva ⇒ **segundo paquete**. Con la variante del colega (misma clave, sin `t0`): 50 h > 36 h ⇒ el proveedor **podría** re-ejecutar ⇒ segundo paquete igualmente. El otro almacén con igual `order_id` usa otra clave: sin interferencia.
2. **Worker pausado:** A reclama `epoch=1` y se congela antes de enviar. Su lease vence; B toma `epoch=2` y reintenta dentro de ventana → `DONE`. A despierta: **revalida `epoch` como paso obligatorio previo a cualquier efecto** → aborta. Si A quedó congelado *después* de revalidar y envía: misma clave dentro de 36 h ⇒ resultado cacheado, sin segundo paquete, y su escritura en DB cae por `epoch`.

## Límites

- No hay atomicidad entre la verificación en DB y la llamada HTTP: un worker congelado ≥36 h dentro de ese hueco puede enviar tras la ventana; con esta API (sin fencing en proveedor, sin cancelación) solo se **reduce**, no se elimina: riesgo residual declarado.
- `t0` usa reloj propio: margen δ obligatorio; tras 36 h el proveedor "podría" re-ejecutar (semántica no garantizada).
- `BLOCKED`/`CANCELLED` exigen canal humano; sin API de búsqueda no hay resolución automática.
- Payload distinto para el mismo `(warehouse_id, order_id)`: cuarentena, nunca sobrescribir.