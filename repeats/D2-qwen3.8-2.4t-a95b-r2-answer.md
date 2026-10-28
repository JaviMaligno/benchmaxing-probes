

## Diagnóstico

El código actual usa `delivery_id` como clave del proveedor, pero el broker lo cambia en cada reenvío. La orden de las 09:00 quedó aceptada sin respuesta y sin fila final; al reenviarse a t+50h con otro `delivery_id`, el proveedor la ve como clave nueva y, habiendo pasado las 36h, puede preparar un segundo paquete. Además, `UNIQUE(warehouse_id, order_id)` solo existe en filas finales: el estado incierto no queda registrado en ningún sitio.

## Evaluación de la afirmación del colega

Acierta en dos puntos: la clave debe ser `warehouse_id:order_id` (estable frente a reenvíos y distinta entre almacenes con IDs repetidos) y el conflicto UNIQUE resuelve la carrera de dos workers insertando la fila final (sus `prepare`, al llevar la misma clave, ya los deduplica el proveedor dentro de las 36h).

Se equivoca en la conclusión: el caso incierto tras 36h **sí puede prevenirse**; lo que la API no permite es *completarlo* automáticamente (no hay búsqueda). Prevenir significa no emitir nunca un segundo `prepare`, y eso se logra registrando durablemente la intención **antes** de llamar, no solo el resultado final. También ignora el problema del worker zombi.

## Propuesta: máquina de estados

Una tabla con `UNIQUE(warehouse_id, order_id)` y estados: **libre** (sin fila), **intentado** (`worker_id`, `lease_until`, `attempted_at`), **final** (`receipt`), **revision**.

1. Sin fila → insertar `intentado` transaccionalmente; después `prepare(warehouse:order, payload)`. Éxito → UPDATE a `final` guardado por `worker_id` y `lease_until` vigentes.
2. Fila `intentado` propia o con lease vencida: si `now − attempted_at < 36h`, reenviar es seguro (el proveedor deduplica o ejecuta por primera vez); se toma la renta con UPDATE condicionado y se reenvía. Si ≥ 36h → `revision` + alerta: **no** reenviar.
3. `final` → acusar recibo. `revision` → ningún envío automático; resolución humana fuera del sistema.
4. Conflicto UNIQUE al insertar o UPDATE guardado devuelve 0 filas → no enviar, releer el estado y seguir su transición.

**Caída justo antes de enviar:** queda `intentado`, nada fue aceptado; el reenvío dentro de 36h ejecuta el primer `prepare` y llega a `final` sin intervención. **Caída justo después (respuesta perdida):** si alguien retoma dentro de 36h, reenvía y recibe el resultado previo, completando sin duplicar; si el reenvío llega a t+50h, pasa a `revision`: sin segundo paquete, bloqueado, que es la prioridad declarada.

**Zombi:** el proveedor no acepta fencing tokens, así que se acota en el emisor: verificar renta y estado inmediatamente antes de enviar y otra vez antes de escribir `final`; si perdió la renta, no escribe. Como la toma de control nunca reenvía fuera de la regla de 36h, un zombi retrasado normalmente solo reenvía una clave ya deduplicada.

## Trazas adversas

**T1 (el caso dado).** 09:00: W1 inserta `intentado`(A:42), llama a `prepare`; el servidor acepta, la respuesta se pierde; 09:01: W1 cae. Sin toma de control intermedia. t+50h: reenvío ve `intentado` con `attempted_at` 09:00 → 50h > 36h → `revision`, sin `prepare`. Duplicación evitada.

**T2 (zombi).** W1 supera las comprobaciones sobre A:42 y el SO lo suspende. W2 retoma a t+1h (lease vencida, <36h), reenvía → deduplicación del resultado de las 09:00 → `final`. W1 se reanuda a t+40h y su HTTP dormido llega al proveedor: han pasado >36h desde la primera aceptación, el proveedor puede preparar de nuevo. W1 falla el UPDATE guardado y no corrompe la DB.

## Límites

- Una pausa >36h entre nuestras comprobaciones y la escritura HTTP no se puede frenar sin fencing en el proveedor; mitigable con supervisión que mata procesos con renta vencida, no eliminable.
- `revision` sacrifica completitud por seguridad, deliberadamente.
- Las 36h las mide el proveedor; conviene usar `attempted_at` con margen de seguridad.