### ¿Cumple la propuesta la regla?
**No.** La regla exige producir *como máximo una carta* y permite detener la automatización ante incertidumbre; aceptar duplicados tras 6 horas viola el requisito existiendo la parada segura. Además, un *lease* de 5 minutos no cerca (*fencing*) al proveedor:
1. Si a las 10:00 `print` se acepta pero se pierde la respuesta, el *lease* expira a las 10:05. En la reentrega a `t+10h` (caducada la ventana de 6h del proveedor), otro worker tomaría el *lease* y reimprimiría.
2. Si el worker 1 obtiene el *lease*, se pausa antes de invocar `print` y despierta >6h después de que otro worker ya imprimió, enviará un duplicado.

### Alternativa con estados persistentes
Tabla `impresiones` con `UNIQUE (organizacion, expediente)` y columna `estado` (`INCIERTO`, `COMPLETADO`). La clave remota es `"organizacion:expediente"` (nunca `attempt_uuid`).

*   **Nuevo (sin fila previa):** El worker ejecuta en transacción local:
    `INSERT INTO impresiones (organizacion, expediente, estado, attempt_uuid) VALUES (org, exp, 'INCIERTO', att_id) ON CONFLICT DO NOTHING`.
    Si inserta 1 fila, hace *commit* y ejecuta **una sola vez** `print("org:exp", body)`, sin reintentos automáticos. Si inserta 0 filas, consulta el estado existente.
*   **Completado:** Si `print` devuelve éxito, ejecuta `UPDATE impresiones SET estado='COMPLETADO' WHERE organizacion=org AND expediente=exp` y confirma (ACK) el mensaje. En reentregas futuras, al leer `COMPLETADO`, hace ACK sin invocar `print`.
*   **Incierto:** Si `print` falla o da *timeout* (jamás asumimos que un *timeout* implica que el trabajo remoto no se hizo), o si otro worker lee `INCIERTO`, **se detiene la automatización**: no se invoca `print`, se alerta para revisión humana y se retira el mensaje del flujo automático.

### Ventana pre-envío y reanudación del worker antiguo
*   **Ventana entre guardar estado y efecto externo:** Confirmar `INCIERTO` en DB *antes* de llamar a `print` bloquea permanentemente a futuros workers.
*   **Reanudación del worker antiguo:**
    *   Si se pausó *antes* del `INSERT`, al reanudarse chocará con `UNIQUE`, leerá `INCIERTO`/`COMPLETADO` y abortará sin llamar a `print`.
    *   Si se pausó *después* del `INSERT`, ningún otro worker habrá llamado a `print` (pues `INCIERTO` prohíbe reenvíos). Solo este worker emitirá su única llamada; si se pausó tras el *timeout* de las 10:00 y despierta a `t+10h`, no reintenta y finaliza en `INCIERTO`.

### Prevención de duplicados vs. Garantía de impresión
*   **Prevención de duplicados (*Safety*):** Garantizada por el registro previo de `INCIERTO` y la prohibición de reintentos automáticos. Ni las reentregas durante 48h ni el olvido de claves tras 6h producen duplicados.
*   **Garantía de impresión (*Liveness*):** En operaciones nuevas sin fallos, el ganador imprime y pasa a `COMPLETADO`. Ante caídas en la ventana pre-envío o *timeouts*, se sacrifica la *liveness* automática para preservar la *safety*, delegando la resolución a revisión humana.

### Pruebas
1.  **Reentrega a `t+10h` y worker antiguo:** A las 10:00, W1 inserta `INCIERTO`, llama a `print("org1:exp1", body)` (aceptado) y pierde la respuesta. A `t+10h` llega reentrega (nuevo `attempt_uuid`) a W2: el `INSERT` falla por `UNIQUE`, W2 lee `INCIERTO`, no llama a `print` y deriva a revisión. W1 se reanuda, registra el fallo de red sin reintentar y termina. Resultado: 1 carta.
2.  **Caída antes del envío:** W1 confirma `INSERT` (`INCIERTO`) y cae antes de invocar `print`. La reentrega lee `INCIERTO`, no imprime y escala a revisión humana. Resultado: 0 duplicados.
3.  **Dos organizaciones con igual expediente:** `(orgA, exp1)` y `(orgB, exp1)` no colisionan en `UNIQUE (organizacion, expediente)`. Envían claves `"orgA:exp1"` y `"orgB:exp1"`, ambos imprimen y pasan a `COMPLETADO`.