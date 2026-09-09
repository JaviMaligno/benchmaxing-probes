## Veredicto: no cumple

La propuesta acierta en la clave estable (`organization:case`) y en el UNIQUE compuesto, pero falla en la conclusión. Dos defectos:

1. **El lease no es una valla.** Expirar un lease no detiene al worker viejo; no se puede cercarlo desde el proveedor. Un worker pausado puede reanudarse y llamar a `print` después. Lo que evita el duplicado *no* es el lease, es que el proveedor colapsa la misma clave durante 6 h. El lease sólo reduce ruido.
2. **El riesgo a las 6 h no es inevitable.** A t+10h la memoria de la clave ya expiró; reenviar produce una segunda carta física real. La regla permite *detener la automatización en casos inciertos*, así que existe una alternativa correcta: no reenviar. Aceptar el duplicado es una decisión, no una fatalidad.

La implementación actual es peor aún: usa `attempt_uuid` como clave (cambia en cada reentrega, la deduplicación del proveedor nunca dispara) e inserta el recibo *después* de imprimir (lee-luego-actúa, sin registro de intención).

## Alternativa

Tabla `letter` con `UNIQUE(organization, case)`. Estados: `PENDING`, `DONE`, `NEEDS_REVIEW`.

**Clave de impresión:** siempre derivada de `organization:case`, nunca del attempt.

**Nuevo:** insertar `PENDING` con `first_send_at = now` y **commit antes** de llamar a `print`. Sólo después emitir el efecto externo. Si la inserción choca con el UNIQUE, el worker perdedor no imprime: releé el estado y aplica la regla correspondiente.

**Incierto** (`PENDING` sin aceptación confirmada; timeout, respuesta perdida, caída):
- Si `now < first_send_at + 6h − margen` (p. ej. 30 min): reenviar con la misma clave. Seguro porque el proveedor deduplica; no depende de interpretar el timeout.
- Si `now ≥` ese horizonte: **no imprimir**. Pasar a `NEEDS_REVIEW`, alertar y parar. Es indistinguible de una aceptación cuya respuesta se perdió.

**Completado:** `DONE` sólo tras aceptación confirmada. Cualquier reentrega (nuevo attempt_uuid, mismo message_uuid) se acusa sin imprimir.

**Ventana estado→efecto:** el registro de intención precede al envío, así que el peor caso es "quizá impreso", nunca "impreso y olvidado". Ese sesgo es deliberado.

**Worker viejo que se reanuda:** justo antes de llamar a `print`, releer la fila y abortar si el estado es `DONE`/`NEEDS_REVIEW` o si se superó el horizonte de 6 h. Es mitigación *best-effort*, no garantía: sin fencing en el proveedor, la única protección real es confinar todo envío a la ventana de 6 h donde el duplicado es inofensivo.

## Prevención ≠ entrega

- **Prevención (garantizable):** clave estable + ventana de 6 h + intención previa + parar tras el horizonte. Da *como máximo una*.
- **Entrega (no garantizable automáticamente):** dentro de las 6 h, las reentregas de la cola (48 h) la logran. Fuera, la cola de `NEEDS_REVIEW` con verificación humana es el mecanismo. No se puede tener ambas sin consulta ni cancelación.

## Pruebas

1. **t+10h:** aceptación a las 10:00, respuesta perdida, fila queda `PENDING`. Reentrega a las 20:00 → aserción: `print` invocado 0 veces adicionales, total 1; estado `NEEDS_REVIEW`; alerta emitida.
2. **Caída antes del envío:** commit de `PENDING`, proceso muerto antes de `print`. (a) Reentrega a +5 min → reenvío con misma clave, exactamente una carta física, `DONE`. (b) Reentrega a +7 h → 0 llamadas, `NEEDS_REVIEW`.
3. **Dos organizaciones, mismo expediente:** A/123 y B/123 concurrentes → dos filas, dos claves distintas, dos cartas, sin colisión de UNIQUE.
4. **Carrera:** dos workers sobre A/123 → un solo `INSERT` gana; el perdedor no imprime.