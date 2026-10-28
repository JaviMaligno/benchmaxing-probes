### ¿Cumple la regla?

**No.** Ni la implementación actual ni la propuesta garantizan *como máximo una carta*:

1. **Implementación actual:** Consulta sin bloqueo previo, guarda el recibo *después* de `print` (perder la respuesta a las 10:00 deja la DB vacía) y usa `attempt_uuid` como clave (cambia en cada reentrega, anulando la deduplicación remota incluso dentro de las 6h).
2. **Propuesta recibida:** Aunque usa `organization:case` y `UNIQUE(organization, case)`, el *lease* de 5m con reenvío automático falla:
   - Un *timeout* o *lease* expirado no prueba que el trabajo remoto no se haya ejecutado.
   - El riesgo tras 6h **no es inevitable**: la regla permite detener la automatización ante incertidumbre. Reenviar automáticamente a `t+10h` (expirado el TTL de 6h) duplica la carta.
   - Sin *fencing* remoto, si W1 toma el *lease*, se pausa antes de enviar por red, W2 toma el *lease* a los 5m e imprime, y W1 despierta a `t+10h` y envía, el proveedor imprimirá dos veces.

### Alternativa con estados persistentes

Tabla con `UNIQUE(organization, case)` y `estado` (`INCIERTO`, `COMPLETADO`). Clave remota: `organization:case`, sin reintentos de red.

- **Nuevo (sin fila):** `INSERT (organization, case, 'INCIERTO')` con *commit* **antes** de `print(organization:case, body)`. Solo quien logra el `INSERT` invoca `print` una sola vez.
- **Completado (`print` exitoso):** Actualizar a `COMPLETADO` con *commit*. Reentregas posteriores ven `COMPLETADO` y terminan sin llamar a `print`.
- **Incierto (`INSERT` falla por `UNIQUE` con estado `INCIERTO`, o `print` falla/expira):** **No reintentar.** Al desconocerse si el proveedor aceptó la orden, se mantiene `INCIERTO` y se detiene la automatización para revisión manual.

**Ventana pre-envío y worker antiguo:**
- **Ventana entre *commit* de `INCIERTO` y `print`:** Si el worker cae antes de enviar, la fila queda en `INCIERTO` sin haberse impreso; las reentregas detectan `INCIERTO` y pasan a revisión sin enviar.
- **Reanudación del worker antiguo:** Ningún otro worker toma elrelevo ni reenvía sobre una fila `INCIERTO`; solo el creador de la fila puede llamar a `print`. Si se pausó tras enviar a las 10:00 y despierta a `t+10h`, recibe error de red y termina sin reintentar. Si se pausó antes de enviar y despierta a `t+10h`, realiza como máximo ese único envío.

### Prevención de duplicados vs. garantía de impresión

- **Prevención de duplicados (*Safety*):** Asegurada persistiendo `INCIERTO` antes del efecto externo y prohibiendo reenvíos automáticos.
- **Garantía de impresión (*Liveness*):** Imposible de automatizar al 100% junto con *at-most-once* sin consulta remota, transacciones distribuidas ni *fencing*. Sin fallos siempre imprime; ante caídas pre-envío o respuestas perdidas, se preserva la unicidad delegando la entrega a revisión manual.

### Pruebas

1. **`t+10h` (reentrega y worker antiguo):** A las 10:00, W1 inserta `(orgA, exp1, 'INCIERTO')`, llama a `print("orgA:exp1", body)`, el proveedor imprime, se pierde la respuesta y W1 se pausa. A `t+10h`, W2 recibe la reentrega, choca con `UNIQUE`, lee `INCIERTO`, no llama a `print` y escala a revisión. W1 despierta, recibe error de red y termina sin reenviar. **Resultado:** 1 carta.
2. **Caída pre-envío:** W1 confirma `INSERT (orgA, exp2, 'INCIERTO')` y cae antes de `print`. W2 recibe la reentrega, lee `INCIERTO`, no llama a `print` y escala a revisión. **Resultado:** 0 impresiones automáticas (0 duplicados).
3. **Mismo expediente en dos organizaciones:** W1 procesa `(orgA, exp1)` y W2 `(orgB, exp1)`. `UNIQUE(organization, case)` permite ambos `INSERT`; se invoca `print("orgA:exp1", ...)` y `print("orgB:exp1", ...)`, pasando ambos a `COMPLETADO`. **Resultado:** 1 carta por organización.