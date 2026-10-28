## No cumple

El lease serializa workers, pero no resuelve la ambigüedad del efecto externo. Al expirar, "cualquier worker vuelve a enviar": si el original sí envió (respuesta perdida a las 10:00) y ha pasado más de 6 h desde la primera aceptación — exactamente t+10 h — el proveedor ya no recuerda la key e imprime otra vez. Usa la memoria del proveedor como mecanismo de corrección, pero la ventana de fallo del sistema (48 h de reentregas más workers pausados indefinidamente) excede esas 6 h. Y "riesgo tras 6 h que debemos aceptar" es innecesario: la regla permite detener la automatización ante incertidumbre.

## Alternativa: estados persistentes con WAL

Tabla `cartas` con UNIQUE(organization, case_number); key de negocio `organization:case`. Estados y decisiones:

- **`claimed`** — INSERT con owner y lease renovada por heartbeat, antes de cualquier efecto. Una reentrega (mismo message_uuid, nuevo attempt_uuid) que encuentra fila existente solo hace ack.
- **`dispatched`** — UPDATE ... WHERE owner=yo, en transacción inmediatamente **antes** de `print()`. Como el commit precede a la llamada, una fila huérfana `claimed` ⇒ nunca se envió; huérfana `dispatched` ⇒ pudo enviarse.
- **`printed`** — aceptación confirmada; terminal. Toda reentrega solo ack.
- **`uncertain`** — relevo de `dispatched` huérfana o respuesta perdida/error. **No se reenvía**: se detiene y va a revisión (permitido por regla). Sin endpoint de consulta no hay verificación automática posible.

**Nuevo**: gana el INSERT por UNIQUE; el perdedor relee y actúa según estado, nunca envía. Tras aceptar → `printed`.
**Incierto**: jamás reintento automático de `print` (a t+10 h la key del proveedor ya no protege); humano cierra como `printed` o reemite documentado.
**Completado**: `printed`; ack idempotente para todo lo posterior.

## Ventana estado→efecto y reanudación

No hay transacción distribuida DB+proveedor; la única forma de no duplicar es que la decisión persistida preceda al efecto y que ningún relevo posterior pueda revertirla a "reenviar". El WAL de dos pasos acota la ambigüedad a `dispatched`. Relevo con lease muerta: `claimed` → puede reintentar otro worker (se sabe que no hubo envío); `dispatched` → `uncertain`. Worker viejo que reanuda: antes de cualquier efecto, revalidar en transacción `WHERE owner=yo AND state=dispatched`; cero filas ⇒ abortar. Su respuesta tardía de aceptación puede promocionar `uncertain→printed` idempotentemente.

## Prevención vs liveness

Son propiedades distintas: `printed`/`uncertain` previenen duplicados automatizados; la garantía de que toda carta se imprima requiere revisión con SLA sobre `uncertain` (no hay forma mecánica de distinguir "se imprimió" de "no llegó" tras 6 h).

## Pruebas

1. **t+10 h**: reentrega encuentra fila `uncertain` (respuesta de las 10:00 perdida) → ack + revisión; ningún segundo `print` automático.
2. **Caída antes del envío**: worker muere tras commit de `claimed`, antes de `dispatched`; relevo ve `claimed` huérfana y reenvía — sin duplicado posible.
3. **Dos organizaciones, igual expediente**: UNIQUE compuesto y keys `org1:C-123` / `org2:C-123` distintas → dos filas → ambos imprimen correctamente.