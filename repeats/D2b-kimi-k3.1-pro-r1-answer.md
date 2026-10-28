**No cumple.** La restricción `UNIQUE` solo protege la DB: no deshace una impresión ya aceptada. Con respuesta perdida no hay recibo; la reentrega a t+10h vuelve a llamar y, como expiró la retención de seis horas, puede imprimir otra copia. El lease tampoco ayuda: expirar no demuestra que el worker anterior no envió ni que no continuará. El riesgo no es inevitable; es consecuencia de reintentar una operación incierta.

**Alternativa persistente**

Crear en una transacción local una fila con `UNIQUE(organización, expediente)` y estados:

- **NUEVO:** todavía no se autorizó ningún envío.
- **EN_PROCESO:** un worker obtuvo, mediante actualización condicional atómica, el derecho exclusivo a realizar el primer envío; guarda propietario y lease.
- **INCERTO:** pudo haberse enviado, pero no consta aceptación.
- **COMPLETADO:** se recibió aceptación.

Decisiones:

- **Nuevo:** solo el worker que cambia `NUEVO → EN_PROCESO` llama una vez a `print(organización:expediente, body)`. `attempt_uuid` sirve como propietario interno, nunca como clave de impresión. Sin fallos, la operación nueva se imprime. Si recibe aceptación, persiste `COMPLETADO`.
- **Completado:** toda reentrega se ignora; nunca se vuelve a imprimir.
- **Incierto:** timeout, respuesta perdida, caída tras entrar en `EN_PROCESO`, expiración del lease o imposibilidad de guardar la aceptación llevan a `INCERTO` y detienen la automatización. Ninguna reentrega ni expiración —ni a las seis horas ni a las 48— autoriza otro envío. Solo un rechazo inequívoco de no aceptación permitiría volver a `NUEVO`.

La ventana crítica queda cubierta porque el estado se guarda **antes** del efecto. Si el proceso cae entre ambos, no se puede saber si llegó a enviar: queda incierto, aunque realmente no lo hiciera. El lease sirve para detectar esa incertidumbre, no para transferir permiso de impresión.

El worker antiguo, al reanudarse, no puede “continuar” con otro intento: solo puede registrar el resultado de su llamada original si lo conoce. Si aún no llamó, comprueba propiedad y estado antes de hacerlo y aborta si perdió el lease. Ningún sustituto envía mientras tanto, por lo que no existe una segunda llamada concurrente.

**Garantías separadas**

- **Duplicados:** se evita reenviar resultados ambiguos; como máximo existe una llamada autorizada por `(organización, expediente)`, sin depender de la memoria de seis horas.
- **Impresión de toda carta:** se garantiza en operaciones nuevas sin fallos. Tras una caída o respuesta perdida no se puede garantizar simultáneamente impresión eventual y ausencia de duplicados con este único endpoint; la carta puede requerir revisión.

**Pruebas**

1. **t+10h:** aceptación a las 10:00, respuesta perdida y reentrega: estado `INCERTO`, cero llamadas adicionales, una sola carta.
2. **Caída antes del envío:** queda `EN_PROCESO/INCERTO`; la reentrega no imprime automáticamente; el worker reanudado tampoco reintenta.
3. **Dos organizaciones, mismo expediente:** existen dos filas y dos claves distintas; cada organización imprime exactamente una carta.