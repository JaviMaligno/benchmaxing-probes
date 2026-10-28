## Diagnóstico

El código actual tiene tres fallos: (1) usa `delivery_id` como clave, que cambia en cada reenvío, así que un reenvío tras pérdida de respuesta garantiza una segunda preparación; (2) el patrón "consultar y luego actuar" no serializa la llamada externa: dos workers pueden pasar la consulta y ambos invocar `prepare`; (3) solo persiste estado *después* del éxito, así que una caída entre `prepare` y el INSERT borra todo rastro de que se envió.

## Evaluación de la afirmación del colega

Parcialmente correcta. Usar `warehouse_id:order_id` como key es acertado: es estable entre reenvíos y desambigua pedidos repetidos entre almacenes. Pero el UNIQUE sobre filas *finales* solo serializa el INSERT, no la llamada a `prepare`; dentro de las 36 h eso lo salva la deduplicación del proveedor, no la DB. Y la conclusión fuerte es falsa: el caso incierto tras 36 h **sí se puede prevenir**. No se puede *recuperar* el receipt perdido, pero sí impedir la segunda preparación: basta registrar la intención *antes* de enviar y negarse a reenviar cuando la ventana pudo expirar, bloqueando para revisión, que es exactamente la prioridad declarada.

## Propuesta

Una sola fila por operación con `UNIQUE(warehouse_id, order_id)` y columnas `state, claimed_by, lease_until, first_send_at, attempt, receipt`.

**Estados:** `PENDIENTE` → `ENVIANDO` → `COMPLETADO` | `BLOQUEADO`.

**Transiciones (todas por UPDATE condicional atómico):**
1. Al recibir el evento: `INSERT ... ON CONFLICT DO NOTHING` con `PENDIENTE`.
2. **Reclamo:** `UPDATE SET state='ENVIANDO', claimed_by=yo, attempt=attempt+1, lease_until=ahora+L, first_send_at=COALESCE(first_send_at, ahora) WHERE state='PENDIENTE' OR (state='ENVIANDO' AND lease_until<ahora)`. Solo el que afecta 1 fila continúa.
3. **Guarda de ventana:** si `ahora > first_send_at + 36h − margen`, transición a `BLOQUEADO` y **no** llamar a `prepare`. `first_send_at` es cota inferior de la aceptación, luego es conservador.
4. Si la ventana es válida: `prepare("W:O", payload)`. Reintentar aquí es seguro: si el primer envío llegó, el proveedor devuelve el resultado previo; si no llegó, es un primer envío legítimo.
5. Éxito: `UPDATE SET state='COMPLETADO', receipt=... WHERE claimed_by=yo AND attempt=mi_attempt AND state='ENVIANDO'`.

**Caída justo antes de enviar:** queda `ENVIANDO` con lease; el proveedor nunca recibió nada; otro worker expira el lease y envía dentro de la ventana sin riesgo. **Caída justo después:** mismo estado en DB; el reintento dentro de la ventana obtiene el resultado deduplicado; pasada la ventana, `BLOQUEADO`.

**Worker viejo pausado:** el proveedor no entiende fencing, así que el fencing se aplica donde sí hay transacciones: (a) el worker re-verifica lease y ventana inmediatamente antes de llamar; (b) `attempt` actúa como token en la DB: su UPDATE final no afecta filas si otro tomó el relevo; (c) la regla clave: *nadie* envía fuera de `first_send_at+36h−margen`, luego cualquier envío tardío del zombi cae dentro de la ventana de deduplicación y colapsa con el previo.

## Trazas adversas

1. **09:00:** worker registra `ENVIANDO` (`first_send_at=09:00`), envía, respuesta perdida, cae. A t+50h el reenvío encuentra la fila, la guarda de ventana falla → `BLOQUEADO`, cero segundas preparaciones. El otro almacén tiene otra key y otra fila: independiente.
2. **Zombi:** A reclama, se pausa antes de enviar; lease expira; B reclama (`attempt=2`), envía, completa. A despierta, re-verifica lease → aborta; si se pausó tras verificar, su envío dentro de la ventana deduplica y su UPDATE (`attempt=1`) no afecta filas.

## Límites

Queda un TOCTOU residual: pausa exacta entre verificación y syscall que dure >36 h; irresoluble sin cooperación del proveedor. El receipt de un `BLOQUEADO` es irrecuperable automáticamente (no hay búsqueda). El margen conservador reduce la ventana de autorreintento. Los `BLOQUEADO` requieren operador.