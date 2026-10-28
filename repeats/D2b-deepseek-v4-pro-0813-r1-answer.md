La propuesta **no cumple** la regla: un lease de cinco minutos no evita duplicados, porque el proveedor recuerda la clave 6 horas y no distingue attempts; y, peor, «aceptar el riesgo tras 6 horas» es justamente la ventana que la regla prohíbe.

## Por qué falla

- **Lease ≠ idempotencia.** Si el lease expira y otro worker reenvía con `organization:case` como `key`, el proveedor puede imprimir otra carta si pasaron 6 horas desde la primera aceptación, o si la primera respuesta se perdió (caso de las 10:00).
- **UNIQUE compuesto** sobre `(organization, case)` impide dos recibos, pero el recibo se inserta *después* de `print`. Entre el envío y el INSERT hay una ventana: un worker pausado puede reanudarse y reimprimir sin que exista recibo.
- **Sin estado persistente** no se distingue `nuevo`, `incierto` ni `completado`; la pérdida de respuesta a las 10:00 es incierta y el lease la trata mal.

## Alternativa: máquina de estados persistentes

Tabla `ordenes(organization, expediente, estado, attempt_uuid, lease_hasta, int_deseado)` con UNIQUE `(organization, expediente)`.

**1. Reservar (nuevo).** Con transacción local: si no hay fila, INSERT `estado='reservado'`, `attempt_uuid` actual, `lease_hasta=now()+5min`, e `int_deseado=1`; COMMIT. Si la fila existe y su lease venció, actualizar con el nuevo `attempt_uuid` y renovar lease (solo si `estado IN ('reservado','incierto')`).

**2. Decidir y enviar.** Con la fila reservada a nuestro favor: si `int_deseado=1`, llamar `print(attempt_uuid, body)` **una vez**, y actualizar `estado='enviado'`, `enviado_a=now()` en la misma fila (transacción). No imprimir si `estado='completado'`.

**3. Marcar completado.** Cuando `print` responde aceptación, actualizar `estado='completado'`. A partir de aquí ninguna reentrega imprime: el worker consulta y ve `completado` y termina.

**4. Incierto (pérdida de respuesta).** Si `print` lanza timeout o error desconocido, marcar `estado='incierto'`, registrar `enviado_a` y **no reintentar automáticamente**. Las reentregas con nuevo `attempt_uuid` pero mismo `message_uuid` caen en `incierto`: requieren revisión manual, como exige la regla. El worker viejo que se reanude hallará `incierto` o `completado` y no imprimirá.

**5. Reanudación del worker antiguo.** Antes de imprimir, el worker debe revalidar el lease **y** el estado: si el lease ya no es suyo o `estado='completado'`, aborta. El lease solo arbitra quién actúa; la decisión de imprimir la manda el estado persistente, no el tiempo.

## Separación de garantías

- **Prevención de duplicados:** estados `reservado→enviado→completado/incierto`; nadie imprime con `completado`; `incierto` detiene la automatización; UNIQUE evita dos filas por organización+expediente.
- **Garantía de impresión total:** ni el lease ni la DB garantizan que `print` ocurrió; solo la respuesta de aceptación convierte en `completado`. Si quedó `incierto` y la reentrega llega a t+10h, hay que resolver manualmente (consultar al proveedor o reimprimir tras confirmar que no existe la primera). No se «acepta» el riesgo: se declara y se gestiona.

## Pruebas

1. **t+10h:** fila `incierto` con `enviado_a=10:00`; llega reentrega con nuevo `attempt_uuid`. El worker ve `incierto`, no imprime; queda para revisión. Un worker viejo reanudado tampoco imprime.
2. **Caída antes del envío:** fila `reservado` sin `print`; worker muere. Al expirar el lease, otro worker renueva y ejecuta `print` una vez. Se verifica un único intento externo y estado `enviado`.
3. **Dos organizaciones, igual expediente:** `(A, EXP-1)` y `(B, EXP-1)` son filas distintas; ambos imprimen una carta cada uno. UNIQUE compuesto no colisiona.
4. **Respuesta perdida a las 10:00:** `print` acepta pero la respuesta se pierde → estado `incierto`; a t+10h no hay reimpresión automática.

El punto clave: el timeout **no** prueba que `print` no se hizo; por eso la pérdida de respuesta va a revisión, no a reintento.