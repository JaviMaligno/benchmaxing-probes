## ¿Cumple la propuesta?

No. La clave `organization:case` es correcta, pero el lease de cinco minutos con reenvío automático al expirar viola la regla: en el escenario de las 10:00, la impresión fue aceptada pero la respuesta se perdió, no se insertó recibo, y a t+10h el proveedor ya olvidó la clave (6h desde la aceptación). Otro worker reenvía y se imprime una segunda carta física. Además, el duplicado "inevitable" no lo es: la regla permite explícitamente detener la automatización en casos inciertos, y la propuesta elige reenviar en lugar de detenerse. Afirmar que un lease expirado implica que el trabajo no se hizo es la misma falacia que asumir que un timeout significa "no impreso".

## Alternativa: máquina de estados persistente

Tabla `letters(org, case, state, first_sent_at, …)` con `UNIQUE(org, case)`. Clave externa determinista: `org:case` (nunca `attempt_uuid`, que cambia en cada reentrega y anula la deduplicación del proveedor). Estados y decisiones:

1. **NUEVO**: no existe fila. Transacción: `INSERT state=SENDING, first_sent_at=now()`. Commit **antes** de llamar a `print(org:case, body)`. Registrar la intención antes del efecto externo garantiza que nunca hay una impresión de la que la DB no sepa nada. Tras aceptación confirmada: `UPDATE state=PRINTED` y ack del mensaje. Operaciones nuevas sin fallos imprimen siempre.

2. **SENDING (incierto)**: una reentrega encuentra `SENDING`. Si `now() − first_sent_at < 4h` (margen bajo las 6h; el proveedor cuenta desde la aceptación, que es posterior a nuestro envío, así que nuestro reloj es conservador), reintentar con la **misma clave**: si la primera fue aceptada, el proveedor deduplica; si no, se imprime una vez. Si supera la ventana: `state=NEEDS_REVIEW`, no imprimir, alertar a un humano. No se puede saber si la carta salió; la regla permite parar aquí.

3. **PRINTED / NEEDS_REVIEW**: ack sin imprimir / mantener detenido hasta resolución humana (verificación fuera de banda; el humano marca PRINTED o autoriza reenvío).

**Worker antiguo reanudado**: no se puede cercar en el proveedor. La clave determinista es la mitigación: si se reanuda y llama a `print` dentro de las 6h posteriores a cualquier aceptación con esa clave, el proveedor deduplica. Riesgo residual honesto: worker pausado entre el commit de `SENDING` y la llamada, reanudado >6h después de una aceptación. No es eliminable sin fencing remoto; se reduce releyendo el estado justo antes de llamar y se acota porque los reenvíos humanos reutilizan la misma clave (reabren la ventana de deduplicación).

**Separación de garantías**: la prevención de duplicados la dan el `UNIQUE`, el orden intención→efecto, la clave determinista y detenerse ante incertidumbre. La garantía de impresión la dan la reentrega de la cola (48h), los reintentos dentro de la ventana segura y la revisión humana que resuelve todo `NEEDS_REVIEW`; ninguna carta se abandona silenciosamente.

## Pruebas

- **t+10h**: simular aceptación con respuesta perdida a las 10:00; inyectar reentrega 10h después. Afirmar: cero llamadas a `print`, estado `NEEDS_REVIEW`, alerta emitida. (La propuesta original imprime dos veces aquí.)
- **Caída antes del envío**: commit `SENDING`, matar el worker antes de `print`. Reentrega dentro de la ventana → exactamente una aceptación, estado final `PRINTED`.
- **Dos organizaciones, mismo expediente**: mensajes para `orgA:case123` y `orgB:case123`. Afirmar dos filas, dos impresiones, una por organización; el `UNIQUE` compuesto no las colisiona.