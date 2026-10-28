## Veredicto: no cumple

La implementación actual falla de raíz: `print(attempt_uuid, body)` usa una clave que cambia en cada reentrega, así que la memoria de 6 h del proveedor nunca se activa. Además el recibo se inserta *después* del envío: una caída intermedia deja estado cero con carta impresa.

La propuesta mejora la clave (`organization:case` + UNIQUE compuesto es correcto), pero el lease de cinco minutos es un **generador** de duplicados, no una protección. Un lease expirado no prueba que el worker murió; sólo que está pausado. "Cualquier otro vuelve a enviar" es seguro únicamente mientras la clave siga viva en el proveedor. El escenario planteado —reentrega a t+10 h— cae exactamente fuera: a esa hora la clave ya caducó y el reenvío imprime una segunda carta. Y eso no es "riesgo inevitable que debemos aceptar": la regla autoriza **detener para revisión** en casos inciertos. Imprimir a ciegas es elegir violar la invariante cuando existía una salida permitida.

## Alternativa: intención escrita antes del efecto

Tabla `letter_receipts` con `UNIQUE(organization, case_id)`, columnas `state`, `first_attempt_at`, `owner_token`.

**Flujo:** insertar fila `INTENT` con `first_attempt_at=now()` y commit → `print("org:case", body)` → `UPDATE … state='DONE'`. Si el UNIQUE falla, releer y decidir por estado.

- **Nuevo** (sin fila): el ganador del UNIQUE inserta, imprime, confirma. Operación nueva sin fallos previos: imprime, como exige el requisito.
- **Incierto** (`INTENT`): si `now() - first_attempt_at < 5 h 30 min` (margen bajo los 6 h, con reloj conservador), reenviar con la **misma** clave es inocuo —el proveedor colapsa el duplicado— y se marca `DONE`. Si supera el umbral, pasar a `NEEDS_REVIEW`, **no imprimir**, alertar y hacer ack del mensaje.
- **Completado** (`DONE` / `NEEDS_REVIEW`): no-op, ack.

**Ventana entre estado y efecto:** es irreducible, por eso el estado se escribe *antes*. Una caída ahí deja `INTENT`, que es honesto: "quizá se imprimió". Nunca deja silencio.

**Worker antiguo que reanuda:** antes de llamar a `print` revalida con `UPDATE … WHERE state='INTENT' AND owner_token=:mío` y aborta si afecta 0 filas; y compara su propio `first_attempt_at` contra el umbral: si lo excedió mientras estaba pausado, aborta y marca `NEEDS_REVIEW`. No se transfiere propiedad para reenviar fuera de la ventana segura. Dentro de la ventana, una doble emisión es absorbida por la clave estable; no hace falta cercar al worker desde el proveedor.

Un timeout no significa que la impresión no ocurrió: por eso el timeout conduce a `INTENT`, nunca a "reintentar como si fuera nuevo".

## Las dos garantías son distintas

- **No duplicar** (invariante dura): clave estable + UNIQUE + emitir sólo dentro de la ventana de 6 h.
- **Que toda carta salga** (best-effort): reentregas de la cola durante 48 h más un barrido de filas `INTENT` estancadas. Fuera de las 6 h no es automatizable sin endpoint de consulta; se degrada deliberadamente a revisión humana.

## Pruebas

1. **t+10 h:** aceptar print a las 10:00, perder la respuesta, reentregar a las 20:00 → el worker encuentra `INTENT` vencido, no llama a `print`, la fila queda `NEEDS_REVIEW` y se emite la alerta. Contador de llamadas al proveedor: 1.
2. **Caída antes del envío:** matar el proceso entre el commit del `INTENT` y el `print` → la reentrega a t+1 min reenvía con la misma clave; el proveedor deduplica o imprime por primera vez; carta física única, fila `DONE`.
3. **Dos organizaciones, mismo expediente:** `A:2026-77` y `B:2026-77` en paralelo → dos filas, dos claves, dos cartas. Verifica que el UNIQUE y la clave incluyen la organización.
4. **Carrera entre workers:** arranque simultáneo → un INSERT gana, el perdedor lee estado y no emite.