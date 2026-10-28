

## Diagnóstico

El código actual usa `delivery_id` como clave del proveedor. El bróker cambia `delivery_id` en cada reintento, así que un reenvío genera una **segunda preparación real**. Además, al no incluir `warehouse_id` en la clave, dos almacenes con el mismo `order_id` colisionarían o quedarían desprotegidos. La ventana crítica está entre `prepare()` y el `INSERT` final: una caída ahí deja la preparación hecha sin registro durable.

## Evaluación de la afirmación del colega

Acertada en parte: `warehouse_id:order_id` como clave elimina la colisión entre almacenes y el problema del `delivery_id` cambiante; el `UNIQUE` cubre la carrera de inserción. **Pero es incompleta.** Decir que el caso incierto tras 36 h "es imposible de prevenir" ignora que sí puede **detectarse y bloquearse** antes de reinvocar. El requisito exige que no-preparar-dos gane a completar-automáticamente; por tanto, la incertidumbre se trata como estado de revisión, no como fatalidad silenciosa.

## Propuesta implementable

**Estados** (fila en tabla `dispatch`, `UNIQUE(warehouse_id, order_id)`):

| Estado | Significado |
|---|---|
| `CLAIMED` | Fila pendiente con `generation`, `leased_at`, `worker_id` |
| `FINAL` | Receipt confirmado |
| `REVIEW` | Incertidumbre; intervención humana |

**Transiciones:**

1. **NEW → CLAIMED.** Worker ejecuta `INSERT … ON CONFLICT DO NOTHING`. Si no inserta, lee la fila existente y salta al paso que corresponda.
2. **CLAIMED → llamada a proveedor.** Antes de `prepare(wh:ord, payload)`, el worker hace `UPDATE dispatch SET generation=g+1, leased_at=now(), worker_id=$me WHERE warehouse_id=… AND order_id=… AND generation=$leído`. Si `affected_rows=0`, otro worker tomó el control → aborta.
3. **Llamada → FINAL.** Tras recibir respuesta, el worker abre transacción: re-verifica con `SELECT generation … FOR UPDATE` que sigue siendo dueño. Si coincide, `UPDATE … SET state='FINAL', receipt=…`. Si no coincide, descarta el resultado y pasa a `REVIEW`.
4. **Llamada → REVIEW.** Si la respuesta se pierde (timeout) o la verificación de lease falla, se marca `REVIEW`. Nunca se reintenta `prepare` automáticamente.
5. **CLAIMED (lease expirado) → nuevo CLAIMED.** Otro worker incrementa `generation` y repite desde el paso 2. Si han pasado >36 h desde `leased_at` original, salta directamente a `REVIEW` (la idempotencia del proveedor expiró; no hay forma de saber si ya preparó).

**Fencing sin tokens del proveedor:** el mecanismo es la `generation` en PostgreSQL. Un worker pausado que despierte fallará en el `UPDATE` de re-verificación (su `generation` ya no coincide) y no escribirá `FINAL`. La llamada a `prepare` no puede evitarse a nivel de red, pero su resultado se descarta si el lease se perdió.

## Trazas adversas

**T1 – Respuesta perdida + reenvío a t+50 h.** 09:00: worker A inserta `CLAIMED` (gen 1), llama a `prepare(wh1:ord7)`, el proveedor acepta, la respuesta se pierde, A cae a las 09:01. No hay `FINAL`. A t+50 h el bróker reenvía. Worker B lee `CLAIMED` con `leased_at` de hace 50 h > 36 h → transición directa a `REVIEW`. No se invoca `prepare` de nuevo.

**T2 – Dos workers simultáneos + pedido homónimo en otro almacén.** W₁ y W₂ toman `(wh1, ord7)`. W₁ inserta `CLAIMED`; W₂ recibe conflicto `UNIQUE`, lee la fila, ve lease activo → se retira. Paralelamente `(wh2, ord7)` tiene su propia fila; la clave compuesta impide interferencia.

## Límites

- La ventana de 36 h del proveedor es el horizonte máximo de idempotencia; el bróker reintenta hasta 96 h, dejando 60 h donde la re-preparación es indetectable por API.
- Sin cancelación ni búsqueda, un `REVIEW` solo se resuelve con verificación operativa externa.
- Dos workers pausados que despierten dentro de la misma `generation` se resuelven por `FOR UPDATE`, pero la llamada ya emitida no se retira; el resultado se descarta, no se revierte.