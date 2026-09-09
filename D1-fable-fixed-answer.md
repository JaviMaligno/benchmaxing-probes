## Veredicto sobre la propuesta

No cumple las reglas de producto. Corrige el síntoma en un tenant y rompe el caso multi-tenant, y la garantía de "exactly once" que promete no es alcanzable con la interfaz declarada del proveedor.

## Causa observada (según la evidencia)

1. **Clave de idempotencia equivocada**: se usa `e.request_id`, pero el upstream genera un request ID nuevo en cada reintento conservando el event ID. Por eso R1 y R2 (mismo evento E9) produjeron dos capturas, p77 y p78. Esta es la causa directa del duplicado.
2. **Guard desactivado**: el comentario dice "enabled by default", pero `bootstrap.py` hace `env.get('GUARD','0') == '1'` y el manifiesto fija `GUARD='0'`. El guard nunca corrió.
3. **p77 es una captura huérfana**: cobrada en el proveedor sin fila en la BD. Sin API de reversa ni lookup por order, requiere conciliación manual con el proveedor; ninguna corrección de código la repara.

## Por qué la propuesta falla

- **Clave de idempotencia = `order_id`**: los tenants reúsan order IDs. La captura legítima de B para el order 41 (E10) colisionaría con la de A: el proveedor la deduplicaría y B nunca se cobraría (o recibiría la respuesta de A). Viola "una captura por *(tenant, order)*".
- **Constraint único sobre `order_id` solo**: rechazaría la fila legítima de B. Debe ser único sobre *(tenant, order)*.
- **GUARD=1 tal como está es dañino**: la clave Redis `seen:<order_id>` no incluye tenant y Redis es compartido → E10 devolvería 'duplicate' falsamente. Además el TTL es 1 h frente a reintentos de 72 h, y el patrón set-antes-de-capturar pierde eventos: si el worker muere entre el `set` y el `capture` (los deploys reinician el worker), el reintento ve 'duplicate' y el cobro nunca ocurre.
- **"Garantiza exactly once"**: falso incluso corregido. El ledger de idempotencia del proveedor dura 24 h y el upstream reintenta hasta 72 h.

## Reparación mínima

1. Clave de idempotencia determinista por operación: `f"{tenant}:{order_id}"` (estable entre reintentos; el event ID también serviría, pero tenant+order es exactamente la unidad de la regla de producto).
2. Constraint único en BD sobre *(tenant, order)*; tratar el conflicto de inserción como éxito idempotente.
3. Antes de llamar al proveedor, consultar la BD por *(tenant, order)*: si ya hay fila, devolver 'ok' sin capturar. Esto extiende la protección más allá de las 24 h del ledger para los casos donde la fila sí se escribió.
4. El guard Redis: eliminarlo o degradarlo a candado advisory con clave `tenant:order`; la corrección no puede depender de él (TTL corto, pérdida ante crash). La concurrencia queda cubierta por el constraint único más la idempotencia del proveedor.
5. `GUARD` deja de ser el mecanismo de corrección; alinear comentario, default y manifiesto para que no vuelva a haber divergencia silenciosa.

## Qué se puede garantizar realmente

- **Dentro de 24 h**: exactly-once efectivo (ledger del proveedor + clave estable + constraint único).
- **Ventana residual no cerrable**: si la captura tiene éxito pero el worker muere antes del insert (el caso E9/R1) y el reintento llega **después de 24 h**, el proveedor ya olvidó la clave y cobrará de nuevo. Sin lookup por order ni API de reversa, esto no es prevenible ni auto-reparable con la interfaz declarada; solo detectable por conciliación de extractos. Hay que asumirlo como riesgo documentado o negociar con el proveedor (ledger ≥ 72 h o lookup por order).

## Verificación de regresión

Con un stub del proveedor que cuenta capturas por clave: (1) mismo evento reenviado con request ID nuevo → 1 captura, 1 fila; (2) tenants A y B con el mismo order ID → 2 capturas, 2 filas; (3) dos workers concurrentes con el mismo evento → 1 captura, 1 fila; (4) crash simulado tras capturar y antes de insertar, luego reintento dentro de 24 h → 1 captura, fila finalmente escrita; (5) reintento tras expirar el ledger → documentar el duplicado como límite conocido, no como fallo de la prueba.

**Límites de certeza**: solo dispongo de pseudocódigo; asumo semántica estándar de `SET NX EX` y que el proveedor deduplica estrictamente por clave dentro de 24 h. La conciliación de p77 queda pendiente como acción operativa.