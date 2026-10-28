## Veredicto: no cumple

Tres fallos:

1. **`print(attempt_uuid, …)`** (implementación actual) desactiva la deduplicación del proveedor: cada reentrega trae `attempt_uuid` nuevo, así que la memoria de 6 h nunca se activa. La key estable `organization:case` de la propuesta sí es correcta (y necesaria, porque los expedientes se repiten entre organizaciones).
2. **El lease de 5 min con reemisión al expirar es un generador de duplicados**, no una protección. Un worker pausado indefinidamente no puede cercarse desde el proveedor; al reanudarse puede emitir después de que otro ya emitió. Si esa reanudación cae fuera de las 6 h, salen dos cartas.
3. **El riesgo tras 6 h no es "inevitable"**: la regla permite detener la automatización en casos inciertos. Reemitir a ciegas pasadas las 6 h es una decisión, no una fatalidad. La reentrega de 48 h excede la memoria de 6 h, luego fuera de ventana la única salida correcta es parar.

## Alternativa: intención escrita antes del efecto

Tabla `receipts` con `UNIQUE(organization, case_id)`, `print_key = organization:case_id`, columnas `state`, `sent_at`, `emitting_attempt`, `version`.

- **NUEVO**: transacción local `INSERT (…, state=PENDING, version=1)`. Quien pierda el UNIQUE no emite nunca; lee el estado y decide. Antes de llamar al proveedor, CAS: `UPDATE … SET state=IN_FLIGHT, sent_at=now(), emitting_attempt=:yo, version=version+1 WHERE version=:leída`. Sólo si el CAS afecta 1 fila se llama `print(print_key, body)`. Respuesta aceptada → `COMPLETED` con el mismo CAS.
- **INCIERTO** (timeout o respuesta perdida): la fila queda en `IN_FLIGHT`. Reintentar **sólo** si `now - sent_at < 6 h - margen` (p. ej. 5 h 30) y con la **misma** `print_key`: ahí el proveedor deduplica si la primera fue aceptada. Pasado el margen → `NEEDS_REVIEW`, alerta, cero emisiones. Nunca se asume que un timeout significa que no se imprimió.
- **COMPLETADO / NEEDS_REVIEW**: la reentrega se confirma (ack) sin emitir.

**Ventana estado↔efecto**: es irreducible, pero se orienta al lado seguro. Escribir `IN_FLIGHT` *antes* de emitir convierte "me caí sin saber" en un estado visible y bloqueante, en lugar de en una fila ausente que invita a reimprimir.

**Worker antiguo**: no hay lease con reemisión. Su CAS por `version` falla si alguien movió la fila (p. ej. a `NEEDS_REVIEW`), y aborta antes de llamar al proveedor. Si ya había iniciado la llamada antes de pausarse, la key estable la deduplica dentro de 6 h; fuera de 6 h nadie más ha reemitido, porque la automatización paró.

## Dos propiedades distintas

- **No duplicar** (seguridad): UNIQUE + emisor único + key estable + CAS por `version` + prohibición de reemitir fuera de ventana. Se garantiza automáticamente.
- **Imprimir toda carta** (vivacidad): **no** se garantiza automáticamente. `NEEDS_REVIEW` es deuda operativa: alerta y resolución humana que imprime manualmente o cierra la fila. Sin consulta ni cancelación en el proveedor, no existe mejor opción.

## Pruebas

1. **t+10 h**: fila `IN_FLIGHT`, `sent_at=10:00`; reentrega a 20:00, mismo `message_uuid`, nuevo `attempt_uuid` → 0 llamadas a `print`, estado `NEEDS_REVIEW`, alerta. Variante a t+1 h → 1 llamada, proveedor falso cuenta **una** carta.
2. **Caída antes del envío**: `PENDING` escrito, proceso muerto; reentrega → se emite exactamente una vez, `COMPLETED`.
3. **Dos organizaciones, mismo expediente**: `A/123` y `B/123` → dos filas, dos keys, **dos** cartas.
4. **Reanudación tardía**: worker pausado; otro lo marca `NEEDS_REVIEW`; al despertar, CAS falla → 0 emisiones.