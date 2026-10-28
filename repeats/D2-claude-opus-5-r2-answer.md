## Diagnóstico

Dos fallos independientes en el código actual:

1. **Clave equivocada**: `delivery_id` cambia en cada reenvío del broker, así que la deduplicación de 36 h del proveedor nunca se activa. Cada reenvío = un paquete nuevo.
2. **Orden equivocado**: la fila se escribe *después* de `prepare`. La ventana 09:00–09:01 deja el sistema sin ninguna huella de un paquete que sí existe. Y el broker reenvía 96 h, más que las 36 h de dedupe: la brecha es estructural, no una rareza.

## La afirmación del colega

La clave `warehouse_id:order_id` es correcta (los `order_id` colisionan entre almacenes) y el `UNIQUE` sirve, pero "basta consultar la DB" es justo lo que falla en la traza dada: a t+50 h la DB dice "no hay nada", y es mentira. Y "el caso incierto tras 36 h es imposible de prevenir" confunde dos cosas: *resolverlo* automáticamente es imposible (no hay búsqueda), *prevenir el duplicado* no lo es, si se registra la intención **antes** de llamar.

## Propuesta

Tabla `attempt` con `UNIQUE(warehouse_id, order_id)`, más `UNIQUE(event_id)` para dedupe del broker (nunca `delivery_id`). Campos: `state`, `intent_at`, `payload_hash`, `owner`, `epoch`, `lease_until`, `receipt`.

Estados: `INTENT → SENT_OK | BLOCKED | FAILED_CLEAN`.

Transiciones:
- **(nada) → INTENT**: `INSERT ... ON CONFLICT DO NOTHING` con `intent_at = now()`, `epoch = 1`, **commit antes de tocar al proveedor**. `intent_at` es cota inferior conservadora de la primera aceptación, así que `intent_at + 36h` es un deadline más corto que la ventana real.
- **tomar el trabajo**: `UPDATE ... SET owner=:me, epoch=epoch+1, lease_until=now()+L WHERE lease_until < now() RETURNING epoch`.
- **INTENT → SENT_OK**: solo si `now() + skew < intent_at + 36h`; se llama `prepare(wh:order, payload)` y se persiste el `receipt` con `UPDATE ... WHERE epoch=:mi_epoch AND state='INTENT'`.
- **INTENT → BLOCKED**: si vence el deadline de 36 h, si el `UPDATE` final afecta 0 filas, o si el `payload_hash` entrante difiere del registrado. Nunca se reenvía desde `BLOCKED`.
- **FAILED_CLEAN**: reservado a rechazos explícitos del proveedor (nunca a timeouts).

Fencing sin cooperación del proveedor: el `epoch` no viaja al proveedor; es el permiso local. Un worker pausado, al despertar, hace CAS del lease antes del envío; si falla, aborta el proceso sin enviar. Si ya envió antes de pausarse, el envío cayó dentro de las 36 h y la misma clave devuelve el resultado previo: un solo paquete, y su `UPDATE` con `epoch` viejo se descarta.

## Trazas adversas

**T1 (la del expediente)**: `INTENT` commiteado 08:59:59, `prepare` acepta a las 09:00, respuesta perdida, caída 09:01. A t+50 h el broker reenvía: `event_id` nuevo pero `(wh1, ord)` existe en `INTENT` con deadline vencido → `BLOCKED`, cero envíos. `(wh2, ord)` es otra fila y se tramita sin intervención.

**T2 (worker zombi)**: W1 queda en `INTENT`, epoch 1, pausado justo antes de enviar. Lease expira, W2 toma epoch 2, envía dentro de ventana, escribe `SENT_OK`. W1 despierta: CAS falla → no envía. Si W1 hubiera enviado antes de pausarse, el proveedor devuelve el mismo receipt y su escritura se rechaza por epoch.

## Límites

Entre el CAS y la syscall de envío no hay garantía absoluta: se mitiga con `L` ≫ pausa plausible y abortando el proceso al perder el lease. Depende de `now()` de PostgreSQL y de un margen de skew. No se puede distinguir "no recibido" de "recibido y perdido": el sesgo es bloquear, y `BLOCKED` exige resolución humana fuera de banda. Si el proveedor cachea también los errores, los reintentos dentro de 36 h no sirven.