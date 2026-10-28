## Diagnóstico

Hay dos defectos independientes:
1. **Clave errónea**: se usa `delivery_id`, que cambia en cada reenvío del broker. Cada reenvío genera una clave nueva → el proveedor ejecuta otra preparación aunque estemos dentro de las 36 h. Además, `order_id` se repite entre almacenes, así que la clave debe ser `warehouse_id:order_id`.
2. **Escribir la fila solo al final** hace indistinguible "nunca enviado" de "enviado sin confirmar". Tras pérdida de respuesta + caída, el reenvío a t+50 h supera la ventana de 36 h y el proveedor re-ejecuta → doble paquete, que es justo lo que tiene prioridad absoluta.

## Propuesta: máquina de estados en la misma fila (UNIQUE(warehouse_id, order_id) sobre *todas* las filas)

Estados: `PLANNED` → `IN_FLIGHT` → `DONE | FAILED | BLOCKED`.

Transiciones (cada una en su transacción, con arrendamiento):
- **ABSENT→PLANNED**: `INSERT ... ON CONFLICT DO NOTHING` con `lease_id, lease_expires`. Adquiere el arrendamiento; si conflicto, otro worker ya procesa: salir.
- **PLANNED→IN_FLIGHT**: `UPDATE ... SET state=IN_FLIGHT, sent_at=now() WHERE lease_id=mía`. Commitear **justo antes** de llamar `prepare(warehouse_id:order_id, payload)` y revalidar el lease en esa misma sentencia.
- **IN_FLIGHT→DONE(receipt)** al recibir respuesta; **→FAILED(error)** si error aplicativo.
- Reintento sobre IN_FLIGHT/FAILED: si `now() < sent_at_primera + 36h − margen`, reinvocar `prepare` con la **misma clave** (el proveedor devuelve el resultado previo; seguro tanto si el envío anterior salió como si no, que cubre caída antes y después de enviar). Si `now() ≥ sent_at + 36h − margen` sin DONE → **IN_FLIGHT→BLOCKED**: revisión manual, sin más invocaciones.
- Toma de control: solo con `lease_expires < now()` y `UPDATE ... SET lease_id=nuevo`.

Los pedidos nuevos sin fallos fluyen PLANNED→IN_FLIGHT→DONE automáticamente; solo los inciertos vencidos se bloquean, lo que la especificación permite.

## Traza adversa 1 (la del enunciado, con el diseño del colega)

09:00: `prepare` acepta, respuesta perdida, no hay fila, worker cae. 09:01+50 h: reenvío con `delivery_id` distinto; con el código actual la clave cambia → segunda ejecución → doble paquete. Con la corrección del colega (clave `warehouse_id:order_id`), la clave coincide, pero **ya pasaron 36 h desde la primera aceptación** → el proveedor re-ejecuta igual. El `UNIQUE` no salva: el daño ocurre en el proveedor, antes del `INSERT`. Con mi diseño: la fila quedó en IN_FLIGHT con `sent_at=09:00`; a t+50 h el reintentador ve ventana vencida → BLOCKED, sin invocación. Sin doble.

## Traza adversa 2 (zombi + concurrencia)

Worker A: ABSENT→PLANNED con lease, y se pausa. Su lease expira; B toma el control y completa DONE. A despierta y envía: con `prepare` idempotente por clave, si A envía dentro de las 36 h de la aceptación de B recibe el mismo resultado (inofensivo); **después de 36 h ejecutaría una segunda preparación**. Mitigación sin fencing del proveedor: toda transición y el propio envío exigen `UPDATE ... WHERE lease_id=A`, que falla porque B lo revocó → A aborta antes de enviar. Residual: si A se pausa *entre* la revalidación y la llamada a `prepare` y despierta 36 h después, ninguna comprobación intermedia se ejecuta. Ese hueco a nivel de instrucción no se cierra con esta API; se acorta (lease corto, revalidación como última operación) y se documenta como riesgo aceptado.

## Evaluación de la afirmación del colega

- Clave `warehouse_id:order_id`: **correcta y necesaria** (ni `delivery_id` ni `order_id` solos valen).
- "La concurrencia queda cubierta con UNIQUE": **falso fuera de la ventana de 36 h**; el conflicto se detecta al insertar, después de que ambos workers ya invocaron `prepare` (traza 2) y solo dentro de la ventana la idempotencia los salva.
- "El caso incierto tras 36 h es imposible de prevenir": **falso**. Lo que no se puede es *completarlo automáticamente*; prevenir el doble sí es posible escribiendo la intención (`PLANNED`/`IN_FLIGHT`) **antes** de enviar y bloqueando al vencer la ventana. Su diseño solo escribe filas finales, por eso le parece imposible.

## Límites

- BLOCKED no se resuelve solo: sin búsqueda ni reversión en el proveedor, la revisión es externa (p. ej., confirmación física con el almacén) y puede terminar en DONE o en "doble ya producido".
- El proveedor es de una sola fase: sin cancelación, un FAILED con envío ya aceptado debe tratarse como IN_FLIGHT.
- El residual del zombi pausado entre revalidación y envío, y relojes: usar `sent_at` como cota inferior de la aceptación exige margen (ε) frente a desfases de reloj entre workers y el proveedor.
- El margen ε también implica que pedidos que *sí* podrían haberse completado a los 35,9 h se bloquean por prudencia: coherente con la prioridad de no duplicar.