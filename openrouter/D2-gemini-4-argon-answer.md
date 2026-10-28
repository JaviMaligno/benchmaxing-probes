### 1. Diagnóstico y Evaluación
**Fallo actual:** Usar `delivery_id` como clave anula la idempotencia en reenvíos. En el incidente (`09:00`), `prepare` tiene éxito pero se pierde la respuesta y el worker cae (`09:01`) sin escribir en DB. A `t+50h`, el broker reenvía con nuevo `delivery_id` y fuera de la ventana de 36h; al no haber fila, se ordena un **segundo paquete**.

**Evaluación del colega:**
* **Acierto:** `key = warehouse_id:order_id` evita colisiones entre almacenes con igual `order_id` y neutraliza el cambio de `delivery_id`.
* **Error 1 (Concurrencia/Pausa):** Consultar DB, llamar a `prepare` e insertar al final es *check-then-act*. Si W1 consulta (sin fila) y sufre una pausa (GC/red), W2 consulta, ejecuta `prepare` e inserta. Si W1 despierta tras >36h, ya superó la consulta inicial y llamará a `prepare` duplicando el paquete *antes* de chocar con `UNIQUE`.
* **Error 2 (>36h "imposible"):** Falso. Como no duplicar prioriza sobre autocompletar, basta registrar la intención en DB *antes* de invocar al proveedor y bloquear estados inciertos sin reintentar.

### 2. Propuesta Implementable
**Tabla `ordenes`:** `(warehouse_id, order_id, estado, receipt)` con `UNIQUE(warehouse_id, order_id)`. Estados: `EN_VUELO`, `COMPLETADO`, `BLOQUEADO`. Clave externa: `key = warehouse_id || ':' || order_id`.

**Transiciones:**
1. **Reclamo (Tx1):** `INSERT INTO ordenes VALUES (:w, :o, 'EN_VUELO', NULL) ON CONFLICT (warehouse_id, order_id) DO NOTHING RETURNING 1`.
2. **Si Tx1 no inserta (ya existe fila):** Leer `estado`:
   * `COMPLETADO`: ACK al broker y terminar.
   * `EN_VUELO` o `BLOQUEADO`: `UPDATE ordenes SET estado='BLOQUEADO' WHERE warehouse_id=:w AND order_id=:o AND estado='EN_VUELO'`. ACK al broker y **abortar sin llamar a `prepare`** (prohibido el *takeover* automático).
3. **Efecto externo (solo si Tx1 insertó):** Invocar `r = prepare(w || ':' || o, payload)`.
4. **Cierre (Tx2):**
   * Éxito: `UPDATE ordenes SET estado='COMPLETADO', receipt=:r WHERE warehouse_id=:w AND order_id=:o` (prevalece sobre `BLOQUEADO` al existir certeza). ACK.
   * Error/Timeout: `UPDATE ordenes SET estado='BLOQUEADO' WHERE warehouse_id=:w AND order_id=:o AND estado='EN_VUELO'`.

### 3. Caídas, Worker Pausado y Trazas Adversas
* **Caída justo antes vs. justo después de enviar:**
  * *Antes de enviar (tras Tx1):* Queda `EN_VUELO` con 0 paquetes en el proveedor. El reenvío pasa la fila a `BLOQUEADO` sin enviar (falso positivo seguro).
  * *Después de enviar (antes de Tx2):* El proveedor prepara 1 paquete y se pierde la respuesta. El reenvío ve `EN_VUELO`, pasa a `BLOQUEADO` y jamás reenvía.
* **Impedir envío de worker antiguo pausado (zombie):**
  * Si W1 se pausa *antes* de Tx1 y W2 toma el pedido, al despertar W1 falla en Tx1 (`ON CONFLICT`) y aborta.
  * Si W1 se pausa *después* de Tx1 (antes del socket), **ningún otro worker se hace cargo del envío**. Si W1 despierta, será el único en enviar. Si un humano reintenta tras revisión, antes debe matar el proceso/red de W1 (STONITH), pues el proveedor no admite *fencing tokens*.

**Traza 1 (Incidente t+50h y colisión entre almacenes):**
1. `09:00` W1 procesa `(AlmA, Ped1)`: gana Tx1 (`EN_VUELO`), llama `prepare("AlmA:Ped1")`, pierde respuesta y cae (`09:01`).
2. `09:02` W2 procesa `(AlmB, Ped1)`: gana Tx1 para `AlmB`, llama `prepare("AlmB:Ped1")` y cierra Tx2 (`COMPLETADO`).
3. `t+50h` Reenvío de `(AlmA, Ped1)` con otro `delivery_id`. W2 falla en Tx1, ve `EN_VUELO`, marca `BLOQUEADO` y aborta.

**Traza 2 (Carrera y pausa de 40h):**
1. `t=0` W1 y W2 reciben `(AlmA, Ped2)`. W1 se pausa antes de Tx1.
2. `t=1s` W2 gana Tx1 (`EN_VUELO`), llama `prepare("AlmA:Ped2")` y marca `COMPLETADO`.
3. `t=40h` W1 despierta, falla en Tx1 por `UNIQUE`, lee `COMPLETADO` y termina sin enviar.

### 4. Límites
* **Incertidumbre irreducible:** Sin API de búsqueda, caer justo antes o después de `prepare` es indistinguible y requiere revisión manual (`BLOQUEADO`).
* **Sin takeover automático:** Permitir a W2 reintentar un `EN_VUELO` en <36h arriesga que un W1 pausado tras Tx1 despierte a las 40h y duplique el paquete por falta de *fencing* en el proveedor.