### Diagnóstico
El diseño actual falla porque usa `delivery_id` como clave (cambia en cada reenvío, anulando la idempotencia del proveedor), omite `warehouse_id` en la clave y escribe en DB *después* del efecto externo.

**Evaluación del colega:**
1. *Clave y `UNIQUE`*: Usar `warehouse_id:order_id` aísla almacenes y estabiliza la clave, pero consultar la DB antes de `prepare()` y capturar `UNIQUE` *después* no cubre la concurrencia. Dos workers pueden consultar la DB vacía a la vez, o uno puede pausarse tras la consulta, despertar a `t+40h` (>36h desde que otro completó e insertó la fila) y ejecutar un segundo `prepare()` antes de intentar su `INSERT`.
2. *Caso >36h "imposible"*: **Falso**. Como la prioridad es no duplicar y se admite bloquear casos inciertos, persistir la intención en DB *antes* de llamar a `prepare()` permite detectar a `t+50h` un intento previo inconcluso y bloquearlo sin invocar al proveedor.

**Caída justo antes vs. justo después de enviar:**
Sin API de búsqueda en el proveedor, ambas caídas son **indistinguibles**: dejan la fila en estado `EN_VUELO` sin respuesta registrada.

**Worker antiguo vivo pero pausado:**
- *Pausa antes de reclamar en DB*: Se neutraliza reclamando mediante un `INSERT ... ON CONFLICT DO NOTHING` atómico previo a `prepare()`. Al despertar, el worker no logra insertar y aborta sin enviar.
- *Pausa tras confirmar `EN_VUELO` en DB, justo antes del envío por red*: Sin *fencing tokens* en el proveedor, la DB ya no puede frenar la llamada en memoria. Se evita el duplicado prohibiendo que otro worker tome el relevo y llame a `prepare()` sobre una fila `EN_VUELO` (pasa a `BLOQUEADO`, garantizando que a lo sumo un worker invoque `prepare()`). Permitir que otro reintente en `<36h` exigiría matar el proceso o cortar la red del worker antiguo en infraestructura propia antes del relevo; de lo contrario, el primero podría despertar a `>36h` y emitir su paquete tardío.

### Propuesta implementable
Tabla `orders` con `UNIQUE(warehouse_id, order_id)`, `state` (`EN_VUELO`, `COMPLETADO`, `BLOQUEADO`), `receipt`, `started_at`. Clave externa: `key = warehouse_id || ':' || order_id`.

**Estados y transiciones:**
1. **`[Inexistente] -> EN_VUELO`:**
   Tx1: `INSERT INTO orders (warehouse_id, order_id, state, started_at) VALUES ($1, $2, 'EN_VUELO', now()) ON CONFLICT DO NOTHING RETURNING 1;`
   - Si inserta: único autorizado para invocar `prepare(key, payload)`.
   - Si no inserta: `SELECT state, started_at FROM orders WHERE warehouse_id=$1 AND order_id=$2`. Si `COMPLETADO`, ACK al broker. Si `BLOQUEADO` o `EN_VUELO` expirado, ir al paso 3.
2. **`EN_VUELO -> COMPLETADO`:**
   Si `prepare()` retorna `receipt`: Tx2: `UPDATE orders SET state='COMPLETADO', receipt=$3 WHERE warehouse_id=$1 AND order_id=$2 AND state='EN_VUELO'`. ACK al broker.
3. **`EN_VUELO -> BLOQUEADO`:**
   Ante error/timeout de `prepare()` o reenvío que halla `EN_VUELO` expirado: Tx2: `UPDATE orders SET state='BLOQUEADO' WHERE warehouse_id=$1 AND order_id=$2 AND state='EN_VUELO'`. ACK al broker y envío a revisión humana.

### Trazas adversas
- **Traza 1 (Pérdida a 09:00, t+50h y colisión de ID):** `09:00` W1 inserta `(W_A, O_1, EN_VUELO)` e invoca `prepare("W_A:O_1", ...)`. El proveedor prepara; se pierde la respuesta y W1 cae (`09:01`). Otro almacén tramita `(W_B, O_1)` insertando su fila y llamando `prepare("W_B:O_1", ...)` sin interferir. A `t+50h` llega reenvío de `(W_A, O_1)`: el `INSERT` de W2 colisiona, detecta `EN_VUELO` expirado, pasa a `BLOQUEADO` y no llama a `prepare()`.
- **Traza 2 (Worker pausado):** W1 y W2 reciben `(W_A, O_2)`. W1 se pausa antes de Tx1. W2 ejecuta `INSERT -> EN_VUELO`, llama `prepare("W_A:O_2", ...)` y marca `COMPLETADO`. W1 despierta a `t+40h`, su `INSERT` no devuelve fila, lee `COMPLETADO` y aborta sin llamar al proveedor.

### Límites
- **Bloqueos conservadores:** Caer tras Tx1 pero antes de transmitir en red deja el pedido `BLOQUEADO` sin haberse preparado, requiriendo conciliación manual con el proveedor.
- **Sin reintento automático post-reclamo:** Sin corte de red/proceso sobre workers pausados, cualquier incertidumbre tras `EN_VUELO` exige bloqueo humano en vez de reintentar dentro de las36h.