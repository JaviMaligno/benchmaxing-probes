## ¿Cumple la regla?

No. La propuesta falla en dos frentes:

1. **Duplicados dentro de las 6 horas.** El lease de cinco minutos no impide que el worker viejo, pausado, reanude y reenvíe con la misma `key` mientras el proveedor aún la recuerda. El lease expira, otro worker reenvía, y el viejo despierta y también envía: dos impresiones aceptadas con la misma clave. El UNIQUE compuesto no ayuda porque el recibo se inserta *después* del `print`, no antes.

2. **Pérdida de cartas.** Si el worker cae tras aceptar el `print` pero antes de insertar el recibo, no hay registro; a t+10h la reentrega vuelve a imprimir (duplicado) o, si el lease lo bloquea, nadie imprime. La propuesta confunde "no duplicar" con "imprimir exactamente una vez".

## Alternativa con estados persistentes

Tabla `jobs(organization, expediente, estado, lease_hasta, intento_uuid)` con UNIQUE(organization, expediente). Estados: `nuevo`, `enviando`, `incierto`, `completado`.

**Transición clave — reservar antes de emitir el efecto.** Para pasar de `nuevo` a `enviando`, un worker hace `UPDATE ... SET estado='enviando', lease_hasta=now()+5min WHERE estado='nuevo'` y comprueba que afectó una fila. Solo el ganador emite `print`. Así, dos workers no pueden enviar a la vez: la reserva es atómica y previa al efecto externo.

**Tras el `print`:**
- Respuesta aceptada → `UPDATE estado='completado'`.
- Respuesta rechazada/error definitivo → `estado='nuevo'`, liberar lease.
- Sin respuesta (timeout, caída) → `estado='incierto'`. **No se asume que el trabajo no se hizo**; se asume que pudo haberse hecho.

**Reanudación del worker viejo.** Al despertar, el worker comprueba el estado y el lease. Si el lease expiró, otro worker pudo tomar el job; el viejo **no reenvía** salvo que vuelva a ganar la reserva atómica. El lease no es solo un temporizador: es un candado que se respeta en cada envío.

**Estado `incierto`.** No se reimprime de inmediato. Se reintenta solo cuando el proveedor ya no recuerda la clave (tras 6h desde la primera aceptación) o tras revisión manual. Para t+10h: la reentrega encuentra `incierto` con lease vencido, gana la reserva y reenvía; como han pasado >6h, el proveedor imprime de nuevo. Si el worker viejo despierta antes, no puede duplicar porque no gana la reserva.

## Separación de garantías

- **Prevención de duplicados:** reserva atómica previa al `print` + UNIQUE + estado `incierto` que bloquea reenvíos dentro de la ventana de memoria del proveedor.
- **Garantía de impresión:** estado `incierto` persistente asegura que la reentrega a t+10h (o un barrido periódico) reintente; una caída antes del envío deja `nuevo`, y la reentrega lo imprime.

## Pruebas

1. **t+10h:** job en `incierto`, lease vencido; llega reentrega con nuevo `attempt_uuid`; gana reserva, `print` aceptado, estado `completado`. Verificar un solo `print`.
2. **Caída antes del envío:** worker reserva (`enviando`) y muere sin llamar a `print`; a los 5 min el lease vence; reentrega gana reserva e imprime. Verificar exactamente una impresión.
3. **Dos organizaciones, igual expediente:** `orgA/caso1` y `orgB/caso1` son filas distintas; ambos imprimen. Verificar dos `print` con claves distintas.
4. **Worker viejo reanuda:** tras expirar lease y reenvío exitoso, el viejo despierta e intenta reservar; el `UPDATE` afecta 0 filas (estado `completado`); no imprime.