**No cumple.** El `UNIQUE` y el lease solo coordinan la DB; no impiden que un worker pausado invoque `print` después. La clave `organization:case` deja de deduplicar a las seis horas, por lo que reenviar al expirar un lease puede producir otra carta. Además, un timeout o una respuesta perdida no demuestran que no se imprimió. El riesgo no es “inevitable”: puede evitarse no reenviando automáticamente casos inciertos.

### Alternativa conservadora

Tabla durable con `UNIQUE(organización, expediente)`, cuerpo persistido y estados:

- **NUEVO**: implícito, si no existe fila.
- **RESERVADO**: existe un único worker autorizado a realizar **una sola** invocación.
- **INCIERTO**: pudo haberse aceptado o no; requiere revisión.
- **COMPLETADO**: se recibió aceptación definitiva.

Decisiones:

1. **Nuevo:** en una transacción, insertar `(organización, expediente, cuerpo, RESERVADO)`. Si hay conflicto, otro worker ya ganó y este no imprime. Tras confirmar la transacción, el ganador llama una vez a  
   `print(clave_estable_organización_expediente, cuerpo)`.  
   Si recibe aceptación, guarda `COMPLETADO`. Así, una operación nueva y sin fallos sí imprime.
2. **Respuesta perdida, timeout o resultado ambiguo:** guardar `INCIERTO`; no reintentar automáticamente, aunque venza cualquier plazo.
3. **Completado:** toda reentrega se confirma como procesada sin imprimir.
4. **Reservado encontrado por otra entrega:** no imprimir. Si el titular desapareció o se desconoce hasta dónde llegó, pasar a `INCIERTO`, no reasignar el envío. No hay leases que autoricen otro intento.

La ventana entre reservar y llamar no puede hacerse atómica con el servicio externo. Si el proceso cae allí, no se sabe si llegó a invocar; por eso se detiene como incierto. La clave estable reduce duplicados durante seis horas, pero la prevención permanente proviene de que solo exista una invocación autorizada.

Si el worker antiguo se reanuda, no recupera ni renueva permisos: como máximo completa su única invocación pendiente o registra su resultado; nunca inicia otra. Ningún worker posterior pudo haber enviado, por lo que su reanudación no crea un segundo envío.

### Dos garantías distintas

- **Prevención de duplicados:** se logra deteniendo la automatización ante incertidumbre.
- **Garantía de impresión:** no puede garantizarse para todos los fallos con este endpoint. Una caída puede dejar una carta sin imprimir y exigir revisión. Reenviar para asegurar entrega reintroduciría el riesgo de duplicado.

### Pruebas

- **t+10h:** aceptación a las 10:00 con respuesta perdida; estado `INCIERTO`. La reentrega con nuevo `attempt_uuid` no imprime y la reanudación del worker viejo tampoco reintenta: una sola carta, aunque la clave ya expiró.
- **Caída antes del envío:** si cae antes de confirmar `RESERVADO`, una entrega posterior lo trata como nuevo e imprime. Si cae después de confirmarlo pero antes de invocar, queda incierto y no hay reenvío automático; puede quedar sin imprimir, pero no duplicarse.
- **Dos organizaciones, mismo expediente:** existen dos filas y dos claves distintas; cada organización imprime exactamente una carta.