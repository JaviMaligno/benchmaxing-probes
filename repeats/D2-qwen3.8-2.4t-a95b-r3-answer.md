**Evaluación del colega**: parcialmente falsa. La clave compuesta `warehouse_id:order_id` sí es correcta (los IDs de pedido se repiten entre almacenes), pero «consultar la DB y capturar el conflicto UNIQUE» es insuficiente: el UNIQUE está solo en la fila final, y si el worker cae después de que `prepare` fue aceptado y antes del insert, no queda ninguna fila: no hay conflicto posible y el reenvío a t+50h (fuera de la ventana de 36h) provoca una segunda preparación. Contrario a lo que afirma, el caso incierto tras 36h **sí** se puede prevenir persistiendo la intención **antes** de enviar.

**Diagnóstico del código actual**: usa `delivery_id` como clave (el broker lo cambia en cada reenvío → clave nueva → preparación nueva); envía antes de registrar nada (sin traza durable ante caída); confía en el UNIQUE a posteriori, cuando el perdedor ya preparó.

**Propuesta** — una tabla con `UNIQUE(warehouse_id, order_id)`, `state`, `first_claimed_at` (hora de DB, inmutable), `gen`, `lease_expires_at`, `receipt`, `event_id`.

Estados: `CLAIMED → DONE`; `CLAIMED → REVIEW`; `REVIEW → CLAIMED` (reintento manual).

Transiciones:
1. **Reclamo**: `INSERT ... ON CONFLICT DO NOTHING` de fila `CLAIMED` (`gen=1`, lease corto, p. ej. 2 min). Conflicto: si `DONE`, ack; si `REVIEW`, aparcar y alertar; si `CLAIMED` con lease vencido, tomar posesión.
2. **Toma de posesión**: `UPDATE` condicional que incrementa `gen` y renueva el lease, solo si `now() < first_claimed_at + 36h − Δ` (margen, p. ej. 1h). Si excede: `state='REVIEW'` y bloqueo.
3. **Envío**: solo el poseedor del lease, renovándolo en la misma transacción y revalidando la ventana; luego `prepare("w:o", payload)`.
4. **Confirmación**: `UPDATE ... SET state='DONE', receipt=... WHERE gen=mi_gen AND state='CLAIMED'`.

Clave del razonamiento: la aceptación ocurrió en algún instante ≥ `first_claimed_at`, así que la ventana del proveedor (aceptación+36h) termina **después** de `first_claimed_at+36h`; enviar antes de esa cota siempre cae dentro del dedup o es la primera aceptación. Nunca dos ejecuciones.

**Traza 1 — caída justo después de enviar (09:00)**: A reclama a las 09:00 (gen=1, lease hasta 09:02), envía, el proveedor acepta, la respuesta se pierde, A muere a las 09:01. Queda fila `CLAIMED`. A las 09:03 B toma posesión (gen=2); dentro de la ventana, reenvía la misma clave → el proveedor devuelve el resultado de las 09:00 → B confirma `DONE` con gen=2. Un solo paquete.

**Traza 2 — caída justo antes de enviar**: A reclama y muere sin llamar al proveedor. B toma posesión y reenvía la misma clave → primera aceptación → `DONE`. Un solo paquete. Si nada se confirma y el reenvío llega a t+50h: la toma de posesión detecta `now() ≥ first_claimed_at+36h−Δ` → `REVIEW`; no se re-ejecuta; un operador verifica fuera de banda. El otro almacén con el mismo order_id usa la clave `w2:o7`: fila independiente, sin interferencia.

**Worker pausado**: el proveedor no acepta fencing tokens, así que el cercado se hace en la DB: toda escritura es condicional a `gen`. Al tomar posesión B, `gen` sube; cuando A despierta, su `UPDATE` afecta 0 filas y su receipt local no vale. Para enviar es obligatorio renovar el lease justo antes; si A estuvo pausado, su renovación falla (gen ajeno o `REVIEW`) y no envía. Riesgo residual: que A pasara la compuerta y quedara pausado entre compuerta y envío, despertando fuera de la ventana; se acota con Δ y un deadline HTTP corto en la llamada.

**Límites**: el broker reintenta 96h > ventana de 36h: más allá no hay garantía automática posible; bloquear para revisión es el comportamiento exigido. Sin cancelación ni reversión: un `DONE` erróneo exige procedimiento operativo manual. Sin búsqueda en el proveedor, resolver `REVIEW` es manual. La seguridad depende de usar la hora de la DB, no la de cada worker.