## Diagnóstico

El código actual tiene dos fallos: usa `delivery_id` como clave (cambia en cada reenvío, así que un reenvío tras 36 h dispara una segunda preparación) y escribe en la DB solo *después* de llamar a `prepare`. Si el worker cae entre la llamada y el INSERT —el escenario de las 09:00— no queda rastro: el reenvío a t+50 h no encuentra fila, llama a `prepare` fuera de la ventana de idempotencia y el proveedor ejecuta una segunda preparación. Viola la prioridad máxima.

## Evaluación de la afirmación del colega

Parcialmente correcta, con un error grave. Acierta en usar `warehouse_id:order_id` como key (estable ante reenvíos, desambigua pedidos repetidos entre almacenes). El UNIQUE sí resuelve la carrera de inserción, y si dos workers llaman a `prepare` concurrentemente con la misma key dentro de la ventana, el proveedor devuelve el mismo resultado: inocuo.

Pero el caso incierto tras 36 h **sí es prevenible**: lo que no puede garantizarse es completarlo automáticamente, que es distinto. El enunciado lo permite: un resultado incierto puede quedar bloqueado. Su diseño, sin registro previo a la llamada, no distingue "nunca enviado" de "enviado sin confirmación", y por eso reintenta a ciegas y duplica.

## Propuesta

Tabla `preparaciones` con `UNIQUE(warehouse_id, order_id)` y columnas: `estado`, `first_attempt_at`, `lease_owner`, `lease_expires_at`, `receipt`.

**Estados:** `EN_VUELO`, `COMPLETADO`, `BLOQUEADO`.

**Transiciones:**
1. Al recibir un evento: `INSERT` de fila `EN_VUELO` con lease. Si hay conflicto UNIQUE, leer la fila:
   - `COMPLETADO` → ACK (reenvío ya tramitado).
   - `BLOQUEADO` → ACK sin llamar al proveedor.
   - `EN_VUELO` con lease vigente → otro worker trabaja; no hacer nada.
   - `EN_VUELO` con lease vencido y `now() − first_attempt_at < 30 h` (margen frente a las 36 h) → tomar el lease con `UPDATE … WHERE lease_expires_at < now()` y reintentar `prepare` con la misma key: el proveedor devuelve el resultado previo si ya ejecutó.
   - `EN_VUELO` con antigüedad ≥ 30 h sin resultado → transición a `BLOQUEADO`, revisión manual. Nadie vuelve a llamar a `prepare`.
2. Tras éxito de `prepare`: `UPDATE … SET estado='COMPLETADO', receipt=… WHERE estado='EN_VUELO'`.
3. Regla invariante: comprobar el reloj contra `first_attempt_at + 30 h` inmediatamente antes de enviar; si se superó, abortar.

**Caída justo antes de enviar:** existe fila `EN_VUELO`, el proveedor nunca recibió nada. El reintento dentro de la ventana llama con la misma key y el proveedor ejecuta por primera vez. Correcto.

**Caída justo después de enviar:** la fila `EN_VUELO` conserva la intención. Reintento dentro de la ventana → misma key → recupera el recibo previo. Reintento tardío → `BLOQUEADO`, sin segunda preparación.

**Worker zombi:** dentro de la ventana es inofensivo (misma key, mismo resultado; su `UPDATE` condicionado por estado no pisa nada). Fuera de la ventana lo mitiga la comprobación de reloj justo antes de enviar.

## Trazas adversas

1. **09:00 revisitado:** fila `EN_VUELO` a las 09:00; caída a las 09:01. A t+50 h el reenvío encuentra `EN_VUELO` con 50 h > 30 h → `BLOQUEADO`. Cero preparaciones duplicadas. El pedido del otro almacén tiene key distinta y se tramita normal.
2. **Zombi:** A inserta `EN_VUELO` en T0 y se pausa. En T0+2 h expira el lease, B lo toma, llama a `prepare`, marca `COMPLETADO`. A despierta en T0+3 h, llama con la misma key, recibe el mismo resultado; su `UPDATE` afecta 0 filas.

## Límites

Queda una carrera residual: una pausa del zombi *entre* su comprobación final de reloj y el envío de red no es bloqueable sin fencing en el proveedor; el margen de 6 h la reduce, no la elimina. Las 36 h corren desde la aceptación del proveedor; registrar `first_attempt_at` antes de enviar es conservador, pero exige margen por desfase de relojes. Los casos bloqueados requieren intervención humana: es el coste aceptado de priorizar no duplicar.