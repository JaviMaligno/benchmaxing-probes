**Diagnóstico.** El código usa una clave volátil: cada reenvío puede provocar otra preparación. Además, consultar la DB y luego llamar no es atómico; dos workers pueden ver ausencia de fila y llamar ambos. El `UNIQUE` evita dos filas, pero se detecta después de efectos externos irreversibles. La clave compuesta es necesaria, pero solo deduplica durante 36 horas. El colega acierta en que una incertidumbre antigua no puede resolverse automáticamente con esta API; se equivoca en la concurrencia y en la conclusión operativa: sí puede evitarse el duplicado bloqueando el reintento.

**Propuesta.** Una fila durable por `(warehouse_id,order_id)`, con esa restricción `UNIQUE`, clave estable e inequívoca derivada de ambos campos, payload inmutable, estado, `fence`, propietario, vencimiento de concesión, instante de intención y receipt. Estados y transiciones:

- Alta o reenvío: insertar `PENDIENTE`; si ya existe, no llamar. Así, `event_id` y `delivery_id` no determinan la preparación.
- `PENDIENTE → ENVIANDO`: actualización condicional dentro de una transacción, incrementando `fence` y registrando propietario/concesión. Solo quien complete esta transición puede llamar.
- Tras commit de `ENVIANDO`, comprobar nuevamente propietario/`fence` y llamar `prepare(clave_estable,payload)`.
- Respuesta concluyente: transacción condicionada a estado y `fence`, `ENVIANDO → TERMINADO`, guardando receipt.
- Caída, timeout o concesión vencida en `ENVIANDO`: `ENVIANDO → BLOQUEADO`; nunca vuelve automáticamente a `PENDIENTE`. Reenvíos posteriores solo consultan este estado.

Si la caída ocurre antes del commit de intención, queda `PENDIENTE` y otro worker puede enviar. Si ocurre después del commit pero justo antes de `prepare`, quedará bloqueado aunque realmente no se enviara nada: es un falso incierto aceptable. Si ocurre justo después del envío, la DB presenta exactamente el mismo estado; tampoco se reintenta.

Un worker pausado antes de adquirir `ENVIANDO` pierde el `fence` y su actualización condicional falla. Si ya estaba `ENVIANDO`, nadie lo sustituye **para enviar**: el sustituto solo puede bloquearlo. Una comprobación local no puede retirar físicamente permiso a un proceso pausado después de su última comprobación; por eso no debe existir un segundo emisor.

**Traza adversa 1.** A las 09:00 el proveedor acepta, se pierde la respuesta y no hay fila final; a las 09:01 cae el worker. Con el código actual, a t+50h otro `delivery_id` provoca una segunda preparación. Incluso reutilizando la clave compuesta, la ventana de 36 horas ya expiró. Con el diseño, queda `ENVIANDO/BLOQUEADO` y no hay llamada. El otro almacén con igual `order_id` tiene otra fila y otra clave, por lo que tramita independientemente.

**Traza adversa 2.** Dos workers leen “sin fila” y llaman antes de que cualquiera inserte; uno sufrirá el conflicto `UNIQUE`, pero ambos paquetes pueden existir. Con la transición condicional, solo uno entra en `ENVIANDO`; si queda pausado, el otro no envía.

**Límites.** No hay exactly-once ni recuperación automática garantizada ante resultado incierto, deduplicación finita y ausencia de consulta/cancelación. Se prioriza seguridad sobre disponibilidad; sin fallos, el camino nuevo es completamente automático.