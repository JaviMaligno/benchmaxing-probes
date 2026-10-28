**¿Cumple la regla la propuesta?**
**No.** Viola la regla de producir *como máximo una carta* por dos motivos:
1. **El riesgo tras 6 horas no es inevitable:** el sistema permite detener la automatización para revisión ante incertidumbre. Con reentregas de hasta 48h, si un intento falla (o pierde su respuesta) y otro worker reintenta tras 6 horas al expirar el lease, el proveedor ya habrá olvidado la clave `organization:case` e imprimirá un duplicado. Un timeout o lease expirado jamás garantiza que el efecto remoto no haya ocurrido.
2. **Reanudación de workers pausados (sin *fencing* remoto):** si el Worker 1 adquiere el lease de 5 minutos, se pausa justo antes de invocar `print()`, el lease expira, el Worker 2 imprime a `t+6m`, y el Worker 1 se reanuda a `t+7h`, su llamada llegará cuando el proveedor ya olvidó la clave de `t+6m`, imprimiendo una segunda carta.

---

### Alternativa con estados persistentes

Usar una tabla `ordenes_impresion` con restricción `UNIQUE(organizacion, expediente)` y clave idempotente `organizacion:expediente`, **eliminando los reintentos automáticos tras fallos o leases expirados**.

**Decisiones por estado:**
*   **Nuevo (sin registro):** el worker ejecuta una transacción local: `INSERT INTO ordenes_impresion (org, exp, estado) VALUES (..., 'EN_CURSO')`. **Solo el único worker que logra confirmar este `INSERT`** tiene permiso para invocar `print(org:exp, body)` una única vez (con reintentos del cliente HTTP desactivados). Si recibe confirmación 200 OK, actualiza el estado a `COMPLETADO`.
*   **Incierto (`EN_CURSO` o `REVISION_MANUAL`):**
    *   Si el worker que hizo el `INSERT` sufre timeout, caída de conexión o respuesta ambigua de `print()`, actualiza la fila a `REVISION_MANUAL`, detiene el flujo y confirma el mensaje a la cola para escalarlo a humanos.
    *   Si otro worker recibe una reentrega o compite, su `INSERT` fallará por `UNIQUE`. Al leer que el estado es `EN_CURSO` o `REVISION_MANUAL`, transiciona a `REVISION_MANUAL` y **nunca invoca `print()`**.
*   **Completado (`COMPLETADO`):** el `INSERT` falla por `UNIQUE`; al leer `COMPLETADO`, el worker descarta el mensaje de la cola sin llamar a `print()`.

**Ventana pre-envío y worker antiguo pausado:**
Al confirmar `EN_CURSO` en la base de datos *antes* de emitir la llamada externa y prohibir que cualquier otro worker llame a `print()`, como máximo un proceso en toda la historia ejecuta `print()` para ese `(organizacion, expediente)`.
*   Si el worker se pausa en la ventana entre guardar `EN_CURSO` y emitir `print()`, y se reanuda 10 horas después, su llamada será la **única** enviada al proveedor (cero duplicados).
*   Si se pausa *después* de enviar `print()`, al reanudarse no vuelve a invocar el endpoint; solo intenta actualizar la DB local.

**Separación de garantías:**
*   **Prevención de duplicados (Seguridad):** garantizada estrictamente por `UNIQUE(organizacion, expediente)` + escritura previa de `EN_CURSO` + ejecución única de `print()`. Esto neutraliza el límite de 6h del proveedor y la falta de *fencing*.
*   **Garantía de impresión (Progreso):** garantizada automáticamente en operaciones nuevas sin fallos (`NUEVO` $\rightarrow$ `EN_CURSO` $\rightarrow$ `print()` $\rightarrow$ `COMPLETADO`). Ante fallos en la ventana crítica o pérdida de respuesta, se preserva la seguridad deteniendo la automatización (`REVISION_MANUAL`).

---

### Pruebas de los casos

1.  **Reentrega a `t+10h` y worker viejo pausado:** a las 10:00, W1 inserta `EN_CURSO` y ejecuta `print()`, pero se pierde la respuesta (o W1 queda pausado). A `t+10h` llega la reentrega a W2: falla su `INSERT`, ve `EN_CURSO`, cambia a `REVISION_MANUAL` y **no** llama a `print()`. Si W1 se reanuda en cualquier momento, ya había llamado a `print()` (solo toca la DB) o lo llama por primera y única vez. Resultado: 1 carta.
2.  **Caída antes del envío:** W1 confirma `EN_CURSO` y cae antes de llamar a `print()`. En la reentrega, W2 detecta `EN_CURSO`, marca `REVISION_MANUAL` y detiene la automatización. Resultado: 0 duplicados; revisión humana detecta y autoriza la impresión faltante.
3.  **Dos organizaciones con igual expediente:** `(OrgA, Exp1)` y `(OrgB, Exp1)` insertan tuplas distintas bajo `UNIQUE(organizacion, expediente)` y envían claves distintas (`OrgA:Exp1` y `OrgB:Exp1`). Ambas imprimen concurrentemente sin bloqueo ni colisión.