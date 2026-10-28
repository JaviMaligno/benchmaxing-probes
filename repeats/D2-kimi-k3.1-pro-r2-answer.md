### Diagnóstico

La afirmación del colega es incorrecta. Consultar antes de llamar y confiar en `UNIQUE(warehouse_id, order_id)` deja una carrera: dos workers pueden consultar, no encontrar fila y enviar ambos antes de que cualquiera inserte. La restricción evita dos filas finales, pero no dos preparaciones.

Además, la clave actual, `delivery_id`, cambia entre reenvíos; debe usarse siempre una clave lógica estable, por ejemplo `warehouse_id:order_id`. A las 50 horas ya expiró la ventana de 36 horas: reintentar puede preparar otro paquete. El caso incierto sí puede **prevenirse** bloqueándolo; lo imposible con esta API es **resolverlo automáticamente** sin arriesgar un duplicado, porque no hay consulta ni reversión.

### Propuesta implementable

Crear, antes de cualquier llamada, una fila durable de intención con `UNIQUE(warehouse_id, order_id)`, clave estable, payload y estados:

- `NUEVO`: todavía no se autorizó ningún envío.
- `ENVIANDO`: un worker obtuvo, mediante una transición condicional dentro de una transacción, la propiedad del intento; registra `attempt_id`.
- `FINAL`: contiene el recibo devuelto; es terminal.
- `REVISION`: existió un intento cuyo resultado no puede conocerse; nunca vuelve automáticamente a `NUEVO`.

Transiciones:

1. Al recibir un evento, insertar `NUEVO`; si ya existe la fila, no crear otra ni usar `delivery_id`.
2. `NUEVO → ENVIANDO` antes de invocar al proveedor.
3. Invocar `prepare(warehouse_id:order_id, payload)` una sola vez para ese intento.
4. Con respuesta concluyente, `ENVIANDO → FINAL`, condicionando la actualización a `attempt_id`.
5. Ante timeout, respuesta perdida o recuperación de un `ENVIANDO` huérfano: `ENVIANDO → REVISION`. No reenviar, ni siquiera después de 36 horas.

Sin fallos, los pedidos nuevos siguen el recorrido completo sin intervención.

### Dos trazas adversas

**1. Caída inmediatamente antes de enviar.** La fila ya está en `ENVIANDO`, pero no hubo aceptación externa. La recuperación la lleva a `REVISION`; puede quedar bloqueada innecesariamente. Es el precio aceptado para no duplicar. Ningún reenvío del broker a las 96 horas cambia esa decisión.

**2. Respuesta perdida y reenvío a t+50 h.** A las 09:00 el proveedor acepta; queda `ENVIANDO`, no “sin fila”. A las 09:01 cae el worker y el intento pasa a `REVISION`. A t+50 h se reconoce la misma intención y no se llama otra vez. Una orden con el mismo `order_id` en otro almacén tiene otra fila y otra clave, por lo que puede tramitarse independientemente.

### Worker pausado y límites

Un fencing token comprobado en PostgreSQL protege escrituras locales, pero no invalida una llamada externa ya autorizada. Si un worker se pausa después de comprobarlo y otro toma el relevo, el primero puede despertar y enviar también. No hay forma de impedirlo si se permite ese relevo.

Por tanto, **ningún worker puede tomar automáticamente un intento `ENVIANDO`**: debe quedar en revisión aunque el propietario parezca muerto. Así no existe un segundo emisor. El antiguo podría despertar y completar su único envío, pero su escritura final obsoleta se rechaza; nunca habrá una segunda preparación originada por el relevo.