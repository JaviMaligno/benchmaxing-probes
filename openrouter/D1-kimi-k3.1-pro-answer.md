**Diagnóstico**

La propuesta **no cumple** las reglas y no debe desplegarse tal cual.

La causa observada de las dos capturas de A/41 es el uso de `request_id` como clave de idempotencia: R1 produjo p77 y R2, al tener otra clave, produjo p78. Además, `GUARD='0'` desactiva el guarda pese al comentario del código. La ausencia de una restricción durable permitiría también carreras y filas duplicadas, aunque en este incidente sólo se insertó una fila.

p79 para B/41 **no es un duplicado según las reglas**: B es otro tenant y puede reutilizar el order ID.

**Defectos de la propuesta y riesgos latentes**

- Activar el guarda actual usaría `seen:41` para ambos tenants. Habría podido suprimir indebidamente a B.
- Tras el timeout de R1, el guarda habría rechazado R2 como `duplicate`, dejando p77 sin fila en la base de datos: evitaría la segunda captura, pero no repararía la importación.
- El TTL de Redis es de una hora, por lo que no cubre los reintentos. Un reinicio del worker tampoco resuelve la ventana entre la captura y el `insert`.
- `order_id` como clave del proveedor puede mezclar A/41 y B/41. La clave debe incluir el tenant.
- Un índice único sólo sobre `order_id` rechazaría órdenes legítimas de otros tenants.
- Incluso con claves correctas, el proveedor olvida la idempotencia a las 24 h, mientras pueden existir reintentos durante 72 h. Una restricción única en la base de datos evita filas duplicadas, **no capturas duplicadas**.

**Reparación mínima**

1. Usar siempre una clave estable y sin colisiones, por ejemplo `capture:<tenant>:<order>`, independientemente de `request_id` y de reinicios.
2. Crear una restricción única sobre `(tenant, order)`, tras limpiar datos existentes si fuera necesario. Consultar ese registro durable antes de capturar y guardar `provider_id` al recibir respuesta; quien pierda una carrera de inserción debe releer el registro existente.
3. No depender de Redis para la corrección. Si se conserva como optimización, debe incluir tenant y order y tener un comportamiento seguro al expirar o rechazar un evento.

Esto permite que, dentro de las 24 h, un reintento tras un timeout obtenga el mismo resultado del proveedor y pueda insertar p77. No deshace p77/p78 ya producidos; sin consulta ni API de reversa, su remedio financiero requiere reconciliación o intervención externa.

**Comprobación de regresión**

Con un proveedor simulado: hacer que R1 capture y luego venza el cliente antes de insertar; reiniciar el worker y reintentar E9 con R2. Verificar que ambas llamadas llevan la misma clave estable, que sólo existe una captura y que la única fila A/41 contiene ese mismo `provider_id`. Repetir con operaciones concurrentes y comprobar la restricción compuesta. Procesar después B/41 y verificar que obtiene su propia captura y fila, sin colisión con A.

**Límite de la garantía**

Con la interfaz actual no puede prometerse *exactly once* durante las 72 h: si queda una captura incierta, sin `provider_id` persistido, y se reintenta después de expirar el ledger, el proveedor puede capturar otra vez. Para cerrar esa brecha se necesita idempotencia del proveedor durante toda la ventana —con margen—, una consulta/reconciliación por la clave estable, o detener los reintentos automáticos inciertos para intervención manual; esta última opción prioriza no duplicar, pero puede dejar la operación incompleta.