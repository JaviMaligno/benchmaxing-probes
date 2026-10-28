## Diagnóstico

El código actual tiene una ventana mortal: `prepare()` ocurre **antes** de cualquier escritura durable. Si la respuesta se pierde (09:00) no queda rastro, y `UNIQUE(warehouse_id, order_id)` sobre filas finales no protege nada, porque nunca se llegó a insertar. Además usar `delivery_id` como key es un error puro: el broker lo cambia en cada reenvío, así que la deduplicación del proveedor nunca se activa para el mismo pedido.

## Evaluación de la afirmación

Dos aciertos y un error.

Correcto: la key debe ser `warehouse_id:order_id` (los IDs de pedido se repiten entre almacenes, así que `order_id` solo provocaría colisiones cruzadas), y el UNIQUE cubre la carrera de dos workers *en la escritura final*.

Incorrecto: el UNIQUE sobre filas finales no cubre la concurrencia donde importa, porque los dos workers pueden llamar a `prepare()` y el conflicto se detecta después del efecto externo. Dentro de las 36 h eso es inofensivo (misma key ⇒ mismo paquete), pero el UNIQUE no es lo que salva, sino la dedupe del proveedor.

Y sobre «el caso incierto tras 36 h es imposible de prevenir»: lo imposible es **resolverlo automáticamente** (no hay búsqueda). Prevenir el doble paquete sí es posible: basta **no reintentar** fuera de la ventana. Eso exige registrar el intento antes de enviar, que es justo lo que falta.

## Propuesta

Tabla `preparation` con `PRIMARY KEY (warehouse_id, order_id)`, más `state`, `first_attempt_at`, `dedupe_until`, `lease_owner`, `lease_epoch`, `lease_expires_at`, `receipt`. Tabla `processed_event(event_id)` para descartar reenvíos ya consumidos (`delivery_id` se ignora siempre).

Estados y transiciones:

1. `NEW` → `SENDING`: en una transacción, `INSERT ... ON CONFLICT DO NOTHING`, fijando `first_attempt_at = now()`, `dedupe_until = first_attempt_at + 30h` (margen bajo 36 h), `lease_epoch = 1`, lease de minutos. Commit **antes** de tocar al proveedor.
2. `SENDING` → `SENDING` (reintento): solo si `lease_expires_at < now()` **y** `now() < dedupe_until`; `UPDATE ... SET lease_epoch = lease_epoch+1 RETURNING lease_epoch`.
3. `SENDING` → `DONE`: tras recibir receipt, `UPDATE ... SET state='DONE', receipt=$r WHERE lease_epoch = $mi_epoch AND state='SENDING'`. Si afecta 0 filas, el worker no escribe nada y aborta.
4. `SENDING` → `UNCERTAIN` (absorbente, revisión manual): cuando `now() >= dedupe_until` sin receipt. Nunca sale de aquí automáticamente.
5. `SENDING` → `NEW` solo si el proveedor devolvió rechazo explícito y determinista.

Caída **justo antes** de enviar: queda `SENDING` sin receipt, indistinguible de «justo después». Se trata igual, de forma conservadora: reintentar con la misma key dentro de la ventana es seguro (o devuelve el resultado previo, o prepara el único paquete). Fuera de la ventana, `UNCERTAIN`.

Fencing sin cooperación del proveedor: el epoch vive en PostgreSQL. El worker zombi revalida lease y `dedupe_until` inmediatamente antes de enviar, y su escritura final está condicionada a su epoch, así que no puede corromper el resultado. Su llamada tardía es inofensiva mientras caiga dentro de las 36 h reales.

## Trazas adversas

**T1.** 08:59:59 `SENDING` commit; 09:00 éxito perdido; 09:01 caída; t+50 h llega reenvío con nuevo `delivery_id` → la fila existe, `now() >= dedupe_until` → `UNCERTAIN`, cero segundos paquetes. El pedido homónimo de otro almacén tiene clave distinta y se tramita normal.

**T2.** A en `SENDING` epoch 1 se pausa; lease expira; B toma epoch 2, llama `prepare()` a t+2 h, obtiene receipt, `DONE`. A despierta: su `UPDATE ... WHERE lease_epoch=1` afecta 0 filas y aborta.

## Límites

El margen de 30 h es heurístico: `dedupe_until` se calcula desde nuestro envío, no desde la aceptación real del proveedor. Un zombi puede pasar el check y pausarse horas antes de la llamada TCP; eso reduce la ventana, no la elimina, y sin consulta ni cancelación no hay cierre perfecto. Los pedidos sin fallos se tramitan solos; algunos que nunca se enviaron quedarán bloqueados de más, coste aceptado por la prioridad declarada.