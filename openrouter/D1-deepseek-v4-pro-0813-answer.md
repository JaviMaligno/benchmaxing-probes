No, la propuesta no cumple las reglas de producto ni garantiza exactamente una captura.

**Causa observada del duplicado**

El incidente se produjo porque el despliegue tiene `GUARD='0'`, es decir, la guarda Redis está desactivada, y porque el worker usa `idempotency_key=e.request_id`.

A las 12:00, para `tenant A / order 41 / event E9`, el worker llamó al proveedor con `request R1`. El proveedor capturó `p77`, pero el cliente agotó el tiempo de espera y no llegó a insertarse fila en DB.

A las 12:02, el reintento de E9 trajo un nuevo request `R2`. Como la clave de idempotencia era `request_id`, cambió. El proveedor no reconoció el intento como el mismo y capturó `p78`. Luego sí se insertó la fila en DB.

Por tanto, la causa directa no fue la ausencia de constraint en DB, sino la combinación de guarda Redis desactivada y una clave de idempotencia inestable en reintentos.

**Por qué la propuesta falla**

1. **Redis guard con `order_id` sin tenant.**  
   La clave `seen:<order_id>` no distingue tenants. En el escenario observado, habría bloqueado la operación legítima de `tenant B / order 41` a las 12:03, incumpliendo “exactamente una captura por `(tenant, order)`”.

2. **Usar `order_id` como idempotency key del proveedor también colisiona entre tenants.**  
   `tenant A order 41` y `tenant B order 41` compartirían clave de idempotencia. El proveedor podría devolver la captura de A para B, omitir la de B o generar estados incorrectos.

3. **Unique constraint solo sobre `order_id` es incorrecto.**  
   Debe ser `UNIQUE(tenant, order)`. Sin embargo, aun con constraint compuesto, la DB no evita capturas duplicadas en el proveedor; solo puede rechazar una inserción posterior, dejando una captura huerfana y sin compensación.

4. **La idempotencia del proveedor dura 24 h; el reintento puede durar 72 h.**  
   Aunque se use una clave estable, un reintento posterior a 24 h puede volver a capturar. Con la interfaz indicada y sin lookup por orden ni API de reversa, no se puede garantizar exactamente una vez en el horizonte completo de 72 h.

**Reparación mínima**

- Activar `GUARD=1`.
- Usar clave Redis compuesta por tenant y orden, con TTL amplio:  
  `seen:{tenant}:{order_id}` con `ex >= 72 h` o superior.
- Usar como idempotency key del proveedor un identificador estable de la operación lógica, por ejemplo `tenant:event_id`, no `request_id`.
- Añadir `UNIQUE(tenant, order)` en DB.

**Chequeo de regresión**

- Reintentar `E9` con timeout en `R1` y nuevo request `R2`; debe resultar una sola captura para `tenant A / order 41`.
- Inmediatamente enviar `tenant B / order 41` con `E10/R3`; debe capturar `p79` sin ser bloqueado por colisión con A.
- Verificar que en DB y en el proveedor exista exactamente una captura para A y una para B.

**Límites de certeza**

Con la interfaz declarada no puede garantizarse exactly-once absoluto. Redis puede perder datos, el guard actual con `set` previo puede producir at-most-once si el worker muere antes de capturar, y el ledger del proveedor es menor que la ventana de reintentos. Además, el duplicado ya ocurrido `p77` no puede revertirse sin API de reversa.