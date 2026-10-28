### 1. ¿Cumple la regla la propuesta?
**No.** La regla exige *como máximo una carta* y permite detener la automatización ante incertidumbre. El riesgo tras 6 horas no es «inevitable»: nace de reintentar automáticamente al expirar el *lease*.
* Si a las 10:00 `print` fue aceptado pero se perdió la respuesta, a `t+10h` el proveedor ya olvidó `organization:case`; otro worker tomará el *lease*, reenviará e imprimirá un duplicado.
* Un *lease* de 5 minutos en DB no cerca (*fence*) al proveedor: si el Worker 1 se pausa justo antes de enviar por red, el *lease* expira, el Worker 2 imprime a `t+5m`, y el Worker 1 se reanuda a `t+7h`, el proveedor imprimirá dos veces.

### 2. Alternativa con estados persistentes
Tabla `impresiones` con `UNIQUE (organization, case)` y columna `estado` (`RESERVADO`, `COMPLETADO`, `INCIERTO`). Clave externa: `"{organization}:{case}"`. Sin reintentos automáticos.

**Decisiones por estado:**
* **Nuevo (sin fila):** En transacción local, hacer `INSERT (org, case, 'RESERVADO')` y `COMMIT` **antes** del efecto externo. Solo quien logra este `INSERT` puede invocar una única vez `print("org:case", body)`:
  * Si recibe confirmación exitosa: actualiza a `COMPLETADO` y confirma (ACK) el mensaje.
  * Si hay *timeout* o error de red/5xx: **no** se asume que el trabajo remoto no se hizo; actualiza a `INCIERTO`, envía a revisión manual y hace ACK en cola.
* **Completado (`COMPLETADO`):** El `INSERT` falla por `UNIQUE`. No llama a `print`, hace ACK y termina.
* **Incierto (`RESERVADO` o `INCIERTO`):** El `INSERT` falla por `UNIQUE`. Como el resultado del primer worker es desconocido (pudo imprimir o seguir pausado), actualiza a `INCIERTO`, detiene la automatización para revisión manual, hace ACK y **nunca** llama a `print`.

### 3. Ventana crítica y reanudación del worker antiguo
* **Ventana entre guardar `RESERVADO` y emitir `print`:** Si el worker cae tras el `COMMIT` y antes de enviar a red, la fila queda en `RESERVADO`. Cualquier reentrega la pasará a `INCIERTO` y detendrá la automatización sin reenviar.
* **Reanudación del worker antiguo:** Como ningún otro worker llama a `print` tras ver la fila existente, solo el worker original que ganó el `INSERT` emite la petición. Si se pausó antes de escribir en el socket y despierta a `t+10h`, hará esa única llamada; si se pausó después de enviar, no reintenta y solo intenta actualizar la DB. Así se evitan duplicados sin *fencing* remoto.

### 4. Prevención de duplicados vs. Garantía de impresión
* **Prevención de duplicados (*Safety*):** Se garantiza persistiendo `RESERVADO` antes de llamar a `print` y prohibiendo que un segundo worker reenvíe.
* **Garantía de impresión (*Liveness*):** Sin fallos, toda operación nueva imprime. Ante caídas en la ventana previa al envío o *timeouts*, se prioriza no duplicar: la carta puede no haberse impreso y queda en `INCIERTO` hasta resolución manual.

### 5. Pruebas requeridas
1. **Reentrega a `t+10h` y worker antiguo:** Worker 1 inserta `RESERVADO` (10:00) y llama a `print("org1:expA", body)`; se acepta pero se pierde la respuesta. A `t+10h`, la reentrega en Worker 2 choca con `UNIQUE(org1, expA)`, marca `INCIERTO` y **no** llama a `print`. Si Worker 1 se reanuda, ya ejecutó su único envío. Resultado: 1 carta.
2. **Caída antes del envío:** Worker 1 hace `COMMIT` de `RESERVADO` y cae antes de invocar `print`. La reentrega detecta `RESERVADO`, marca `INCIERTO` y escala a revisión manual sin llamar a `print`. Resultado: 0 impresiones automáticas, 0 duplicados.
3. **Dos organizaciones con igual expediente:** Llegan `(org1, expA)` y `(org2, expA)`. `UNIQUE(organization, case)` permite ambos `INSERT` en `RESERVADO`; se invoca `print("org1:expA", ...)` y `print("org2:expA", ...)` y pasan a `COMPLETADO`. Resultado: 2 cartas (una por organización).