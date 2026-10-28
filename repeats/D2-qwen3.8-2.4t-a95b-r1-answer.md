**Diagnóstico**
El código usa `delivery_id` como key de `prepare`, y el broker cambia `delivery_id` al reenviar: cada reintento parece nuevo y el proveedor puede ejecutar otra preparación. `UNIQUE(warehouse_id,order_id)` solo protege el INSERT, posterior a la llamada remota; dos workers pueden invocar `prepare` antes de chocar con el UNIQUE. No existe estado previo al envío, así que no se distingue "nunca se ejecutó" de "se ejecutó y se perdió la respuesta".

**Evaluación del colega**
Acierta en la key (`warehouse_id:order_id`: `order_id` se repite entre almacenes) y en el UNIQUE contra inserciones concurrentes. Se equivoca en "imposible": si la respuesta se pierde sin registro local, tras 36 h el proveedor olvida la key y un reintento *sí* ejecuta una segunda preparación. Es evitable registrando intención antes de enviar y bloqueando lo incierto.

**Propuesta: estados y transiciones**
Tabla única por `(warehouse_id,order_id)` con `version`, `owner`, `lease_until`, `first_sent_at`, `receipt`. Estados: `NEW`, `PREPARING`, `DONE`, `UNCERTAIN`, `FAILED`.

- `NEW → PREPARING`: claim atómico `UPDATE … SET owner=yo, version=version+1, lease_until=now()+Δ WHERE (estado='NEW') OR (estado='PREPARING' AND lease_until<now())`, verificando 1 fila afectada.
- Dentro del lease: si `now() ≥ first_sent_at + 36h` (o `first_sent_at` nulo y el evento lleva >36h), ir a `UNCERTAIN` **sin** llamar a `prepare`.
- Si aún hay ventana: registrar `first_sent_at` en transacción, llamar a `prepare(key,payload)`.
- Éxito → `DONE` con receipt; fallo → `FAILED`.
- Reenvío ≥36 h después: nunca re-prepare automático; `UNCERTAIN` se resuelve por revisión manual.

**Traza adversa 1 (el incidente)**
09:00: `prepare` devuelve éxito, la respuesta se pierde, no hay fila. 09:01: cae el worker. t+50 h: reenvío; como no se registró nada, la fila es `NEW`. El worker reclama, ve que aún está dentro de 36 h desde 09:00, registra intención y llama a `prepare`: el proveedor devuelve el resultado previo (dedup por key), se guarda receipt y queda `DONE` sin segunda ejecución. Otro almacén con el mismo `order_id` usa otra key compuesta: sin interferencia.

**Traza adversa 2 (worker antiguo congelado)**
Worker A obtiene lease, registra `first_sent_at`, se congela justo antes de `prepare`. Expira el lease; B reclama (`version+1`), llama y completa `DONE`. A las 36 h llega el reenvío: ve `DONE` y termina sin llamar. A se descongela: su CAS ya no afecta filas (versión/owner cambiaron) y aborta antes de invocar.

**Fencing sin tokens**
- CAS por `version`: el envío exige `UPDATE … SET version=version+1 WHERE version=v_leída AND owner=yo`; si otro se hizo cargo, 0 filas y no se llama al proveedor.
- Chequeo final intra-lease: `SELECT version, first_sent_at WHERE owner=yo FOR UPDATE`; solo se envía si `now() < first_sent_at+36h`.
- Residuo: si el CAS pasó dentro de la ventana pero el request llega al proveedor después de 36 h por una pausa larga, podría ejecutar de nuevo; sin fencing del proveedor no se sella la red. Mitigación: deadline local conservador (<36 h) y `UNCERTAIN` como destino de esa duda.

**Caídas**
Justo antes de enviar: no hubo llamada ni registro; el reenvío reclama y sigue. Justo después: o el receipt persistió (reintento ve `DONE`) o no (reintento dentro de 36 h deduplica; fuera, `UNCERTAIN` bloqueado).

**Límites**
Sin cancelación, reversión, búsqueda ni fencing del proveedor, el resultado incierto >36 h solo se resuelve bloqueando y revisando; el CAS protege la decisión, no la llegada del request; `event_id` no sirve como key (el broker lo conserva pero no identifica el par almacén/pedido de forma accionable en el proveedor).