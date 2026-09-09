## Veredicto: la propuesta no cumple

Tres fallos:

1. **El lease de 5 minutos asume que "expiró = no se hizo"**, exactamente la inferencia prohibida. Un worker pausado puede reanudarse tras la expiración y enviar de nuevo; no hay forma de cercarlo en el proveedor.
2. **El duplicado post-6h no es "inevitable"**: la regla permite detener la automatización en casos inciertos. Aceptar reimpresión tras 6h es elegir violar el máximo de una carta cuando existía la opción legítima de parar.
3. La implementación original usa `attempt_uuid` como clave: cada reentrega trae uno nuevo, así que la deduplicación del proveedor nunca actúa. Usar `organization:case` es lo único correcto de la propuesta.

## Alternativa: máquina de estados persistente

Tabla `receipts` con `UNIQUE(organization, case)` y columnas `state ∈ {SENDING, DONE, NEEDS_REVIEW}`, `first_sent_at`, `deadline = first_sent_at + 6h − margen` (margen amplio, p. ej. 30 min).

**Protocolo (intención durable antes del efecto externo):**

1. `INSERT (org, case, SENDING)` en transacción. Si viola UNIQUE, leer la fila existente y saltar al paso según su estado.
2. Antes de llamar al proveedor, escribir `first_sent_at = now` si era NULL (write-ahead: nunca se envía sin registro previo).
3. Releer/verificar `now < deadline` **inmediatamente antes** de `print("org:case", body)`.
4. Con aceptación confirmada → `state = DONE`, ack del mensaje.

**Decisiones por estado:**

- **Nuevo** (sin fila): insertar, marcar `first_sent_at`, imprimir, marcar DONE. Operación sana → imprime sin fricción.
- **Incierto** (SENDING con `first_sent_at` puesto): si `now < deadline`, reenviar con la **misma clave**; es seguro porque el proveedor dedupica, no porque asumamos que no se imprimió. Si pasó el deadline → `NEEDS_REVIEW`, detener automatización, verificación humana con el proveedor.
- **Completado** (DONE): ack de la reentrega sin imprimir.

**Ventana entre guardar estado y emitir el efecto:** caída tras el INSERT pero antes de `print` deja `first_sent_at = NULL`, prueba durable de que nunca se envió; cualquier worker puede enviar con seguridad (marcando `first_sent_at` primero). Caída tras enviar deja SENDING con timestamp: dentro de la ventana se reenvía idempotentemente; fuera, revisión humana.

**Worker antiguo reanudado:** su reenvío usa la misma clave; dentro de las 6h el proveedor lo absorbe. La verificación de `deadline` justo antes de la llamada, con margen amplio, cubre casi todo. Residuo honesto: un worker congelado entre esa verificación y la llamada de red podría duplicar tras 6h; sin fencing del proveedor es irreducible a cero, solo minimizable (margen grande, verificación pegada al envío). La propuesta, en cambio, duplica en el caso *común* de t+10h.

**Separación de garantías:** la prevención de duplicados descansa en UNIQUE + clave estable + nunca enviar tras el deadline (seguridad). La garantía de impresión descansa en las reentregas de 48h, un job que barre filas SENDING, y la resolución manual de NEEDS_REVIEW (vivacidad). Detener sacrifica vivacidad, nunca seguridad — el orden de prioridades que la regla exige.

## Pruebas

1. **t+10h:** aceptación a las 10:00 con respuesta perdida → fila SENDING, deadline vencido. Reentrega → NEEDS_REVIEW, cero impresiones nuevas. (La propuesta imprimiría duplicado.)
2. **Caída antes del envío:** fila SENDING con `first_sent_at` NULL → reentrega envía, carta sale exactamente una vez.
3. **Dos organizaciones, mismo expediente:** claves `orgA:caso` y `orgB:caso` distintas, dos filas UNIQUE → dos cartas correctas, sin colisión cruzada.