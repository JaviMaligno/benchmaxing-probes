## Diagnóstico

El código actual tiene tres defectos. Primero, usa `delivery_id` como clave: el broker lo cambia en cada reenvío, así que un reintento genera una clave nueva y una segunda preparación aunque la primera triunfara. Segundo, es *check-then-act*: entre consultar la DB y llamar a `prepare`, otro worker puede hacer lo mismo; el UNIQUE solo frena la inserción final, cuando ambas llamadas al proveedor ya ocurrieron. Tercero, no deja rastro durable antes de enviar: en el escenario de las 09:00, el éxito perdido es invisible, y a t+50h (ya fuera de la ventana de 36 h) el reintento con cualquier clave produce un duplicado real.

## Evaluación de la afirmación del colega

Parcialmente correcta. Usar `warehouse_id:order_id` como clave es acertado (estable entre reenvíos, distingue almacenes). Pero:

- El UNIQUE en filas finales no cubre la concurrencia de la llamada: quien evita el duplicado es la deduplicación del proveedor, y solo dentro de 36 h.
- **El caso incierto tras 36 h sí es prevenible.** Lo imposible es *resolverlo* (no hay consulta); prevenir la segunda preparación es posible registrando la intención y la hora del primer envío *antes* de llamar, y prohibiendo reenvíos fuera de la ventana: el pedido pasa a revisión, que es exactamente la prioridad declarada.

## Propuesta

Una sola tabla `deliveries` con `UNIQUE(warehouse_id, order_id)` y columnas `state`, `lease_owner`, `lease_expires`, `first_sent_at`, `receipt`.

**Estados:** `PENDING → SENDING → DONE | BLOCKED`.

**Transiciones:**

1. **Registro:** al recibir el evento, `INSERT ... ON CONFLICT DO NOTHING` con `state='PENDING'`. Si ya existe en `DONE`, confirmar al broker y terminar.
2. **Reclamo (una sentencia atómica):** `UPDATE ... SET state='SENDING', lease_owner=yo, lease_expires=now()+T, first_sent_at=COALESCE(first_sent_at, now()) WHERE (state='PENDING') OR (state='SENDING' AND lease_expires<now())` devolviendo la fila. Si 0 filas, otro worker la tiene; terminar.
3. **Guardia temporal:** si `now() > first_sent_at + 36h − M` (margen M generoso, p. ej. 6–12 h), transición a `BLOCKED` sin llamar. Nunca se emite `prepare` fuera de la ventana.
4. **Llamada:** `prepare("w:{warehouse_id}:o:{order_id}", payload)`.
5. **Confirmación:** `UPDATE SET state='DONE', receipt=... WHERE lease_owner=yo AND lease_expires>now()`. Si 0 filas, otro worker tomó el relevo: abortar sin escribir.

**Caída justo antes de enviar:** queda `SENDING` sin llamada hecha. Otro worker reclama tras expirar el lease y reenvía con la misma clave; si la llamada original no ocurrió, es la primera; si ocurrió, el proveedor devuelve el resultado previo. Ambos casos convergen.

**Caída justo después de enviar:** mismo estado `SENDING`; la recuperación dentro de la ventana obtiene el recibo cacheado. Fuera de la ventana, `BLOCKED` para revisión — cubre el escenario 09:00/t+50h sin duplicar.

**Worker antiguo pausado:** reverifica su lease y la guardia temporal inmediatamente antes de enviar. Si perdió el lease pero envía dentro de la ventana, la clave idéntica hace que el proveedor devuelva el resultado previo (inocuo); su confirmación falla por la guardia de lease y no pisa la fila.

## Trazas adversas

1. *09:00:* fila queda `SENDING`, `first_sent_at=09:00`. A t+50h el reenvío encuentra `50h > 36h−M` → `BLOCKED`. Cero segundas preparaciones. El pedido del otro almacén usa otra clave y avanza normal.
2. *Pausa larga:* W1 reclama, se pausa; W2 toma el lease, envía, `DONE`. W1 despierta, pasa su chequeo pre-envío por milisegundos, envía la misma clave → proveedor dedupe; su commit falla por lease. Consistente.

## Límites

Sin fencing en el proveedor, una pausa de W1 *entre* su chequeo final y el envío que dure más que el margen M puede duplicar; M grande lo hace prácticamente despreciable, pero no es eliminable con esta API. Los pedidos en `BLOCKED` requieren intervención humana, por diseño.