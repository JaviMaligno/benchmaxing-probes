No cumple. `UNIQUE(organización, expediente)` evita recibos duplicados, no impresiones duplicadas. El lease no invalida al worker antiguo ni impide que reanude una llamada. Además, `attempt_uuid` cambia entre reentregas, por lo que no sirve como clave idempotente. Con `organization:case`, reenviar tras seis horas puede imprimir otra vez: no es un riesgo inevitable, sino consecuencia de reintentar automáticamente un resultado incierto.

**Alternativa persistente**

Tabla con `UNIQUE(organización, expediente)`, cuerpo, clave estable —codificación no ambigua de ambos identificadores— y estados `EN_CURSO`, `INCIERTO` y `COMPLETADO`.

- **Nuevo:** en una transacción, insertar `EN_CURSO`. El worker que logra insertar obtiene el único permiso lógico de envío; los competidores no envían. Confirmar la transacción antes de llamar a `print(clave_estable, cuerpo)`. Sin fallos, realiza esa única llamada.
- **Completado:** únicamente tras una respuesta afirmativa, actualizar a `COMPLETADO`. Toda reentrega posterior termina sin llamar a `print`.
- **Incierto:** timeout, respuesta perdida o caída después de confirmar `EN_CURSO` dejan el envío indeterminado. Registrar `INCIERTO` —o convertir a ese estado un `EN_CURSO` abandonado— y detener la automatización para revisión. No reenviar al expirar un lease ni después de seis horas. Un timeout nunca se interpreta como “no impreso”.

La ventana entre confirmar `EN_CURSO` y emitir el efecto no puede cerrarse atómicamente con el proveedor. Por eso el permiso de envío es único y no transferible: expirar un lease no crea otro. El worker antiguo, al reanudarse, puede como máximo terminar su llamada original y registrar su resultado; nunca inicia un reintento. No hace falta ni es posible cercarlo remotamente, porque ningún otro worker obtiene autorización para enviar esa carta.

**Duplicados frente a impresión garantizada**

La prevención consiste en una única autorización persistente por `(organización, expediente)`, clave estable y ausencia de reenvíos ante incertidumbre. La garantía de progreso es distinta: una operación nueva sin fallos se imprime y queda `COMPLETADO`; una carta `INCIERTA` puede haberse impreso o no, y solo la revisión permite resolverlo. Sin consulta remota, no se puede prometer simultáneamente impresión automática de todos los casos fallidos y ausencia de duplicados.

**Pruebas**

1. **t+10h:** aceptación a las 10:00 y respuesta perdida; queda `INCIERTO`. La reentrega con nuevo `attempt_uuid` no imprime. Reanudar el worker antiguo tampoco genera otro envío. Total: una impresión.
2. **Caída antes del envío:** caída tras confirmar `EN_CURSO`, antes de `print`. Recuperación lo marca `INCIERTO`; no hay impresión automática ni falso `COMPLETADO`. Si la caída ocurre antes de confirmar la inserción, una entrega posterior sigue siendo nueva y puede imprimir.
3. **Dos organizaciones, mismo expediente:** existen dos filas y dos claves distintas; se imprime una carta para cada organización, sin colisión del `UNIQUE`.