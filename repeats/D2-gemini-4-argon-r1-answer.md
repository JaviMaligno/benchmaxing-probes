### 1. Diagnóstico

* **Fallo actual y escenario (09:00 a t+50h)**: Usar `delivery_id` como clave anula la idempotencia del proveedor porque cambia en cada reentrega del broker. A las 09:00 el proveedor prepara el paquete, la respuesta se pierde y el worker cae a las 09:01 sin fila en DB. A t+50h (dentro de las 96h del broker, pero fuera de las 36h del proveedor), el reenvío no ve fila y llama a `prepare` de nuevo, causando **doble preparación**. Además, como `order_id` se repite entre almacenes, colisionaría sin `warehouse_id` en la clave.
* **Evaluación del colega**: Su afirmación es **falsa**.
  1. Consultar la DB antes de `prepare` y capturar `UNIQUE` al insertar *después* deja una ventana TOCTOU: dos workers concurrentes leen que no hay fila, invocan `prepare` y el conflicto `UNIQUE` salta cuando la llamada externa ya se ejecutó.
  2. El duplicado tras 36h **sí es prevenible**: insertando la intención en DB *antes* de llamar a `prepare`. Así, a t+50h la fila existe en estado incierto y bloquea el reenvío para revisión.
* **Caída justo antes vs. justo después de enviar**: Persistiendo la intención antes de llamar a `prepare`, ambos fallos dejan el mismo estado en DB (`EN_VUELO` sin recibo). Sin API de búsqueda en el proveedor, son **indistinguibles**.
* **Worker pausado (zombie) sin fencing tokens**:
  * Si W1 se pausa *antes* de persistir `EN_VUELO`, al despertar choca con `UNIQUE` en PostgreSQL y aborta antes de enviar.
  * Si se pausa *después* de persistir `EN_VUELO` (justo antes del socket), como el proveedor no valida fencing tokens, si otro worker tomara el relevo, W1 podría despertar >36h después y duplicar el pedido. Se impide **prohibiendo el relevo automático** de filas `EN_VUELO` (si expira su lease, pasan a `BLOQUEADO`), o —si se permite reintento dentro de `<30h` con igual `key`— verificando un reloj monotónico local justo antes del socket junto a un watchdog de proceso.

---

### 2. Propuesta implementable

Tabla `preparations(warehouse_id, order_id, state, owner_id, first_attempt_at, lease_until, receipt)` con `UNIQUE(warehouse_id, order_id)`. Clave externa: `key = warehouse_id || ':' || order_id`.

**Estados (`EN_VUELO`, `COMPLETADO`, `BLOQUEADO`) y transiciones**:
1. **Reserva (`[inexistente] -> EN_VUELO`)**:
   ```sql
   INSERT INTO preparations
   VALUES (:w, :o, 'EN_VUELO', :worker, now(), now() + interval '2m', NULL)
   ON CONFLICT (warehouse_id, order_id) DO NOTHING RETURNING *;
   ```
   * Si inserta: ir al paso 2.
   * Si no inserta, hacer `SELECT`:
     * `COMPLETADO` o `BLOQUEADO`: confirmar al broker y salir.
     * `EN_VUELO` con `lease_until > now()`: salir (worker activo).
     * `EN_VUELO` con `lease_until <= now()`:
       * Si `now() >= first_attempt_at + interval '30h'` (o bajo política de cero relevo): `UPDATE preparations SET state='BLOQUEADO' WHERE warehouse_id=:w AND order_id=:o AND state='EN_VUELO' AND lease_until <= now()`, y alertar a revisión.
       * Si `< 30h` (y se habilita reintento acotado): tomar relevo actualizando `owner_id` y `lease_until` con `WHERE state='EN_VUELO' AND lease_until <= now() AND now() < first_attempt_at + interval '30h'`.
2. **Envío**: Verificar reloj monotónico local `< lease_until` e invocar `prepare(w:o, payload)`.
3. **Cierre (`EN_VUELO -> COMPLETADO | BLOQUEADO`)**:
   * Éxito: `UPDATE preparations SET state='COMPLETADO', receipt=:r WHERE warehouse_id=:w AND order_id=:o`.
   * Timeout/error incierto: `UPDATE preparations SET state='BLOQUEADO' WHERE warehouse_id=:w AND order_id=:o AND state='EN_VUELO'`.

---

### 3. Dos trazas adversas

* **Traza 1 (Fallo 09:00 + caída 09:01 + reenvío t+50h)**:
  09:00: W1 inserta `EN_VUELO` (`first_attempt_at=09:00`), hace commit y llama `prepare("W1:O9", payload)`. El proveedor prepara el paquete, la respuesta se pierde y W1 cae (09:01). A t+50h llega el reenvío: W2 ejecuta `INSERT` (0 filas por `UNIQUE`), ve `EN_VUELO` con `now() >= first_attempt_at + 30h`, pasa la fila a `BLOQUEADO` y no invoca `prepare`.
* **Traza 2 (Concurrencia y pausa)**:
  W1 y W2 reciben `(W1, O9)` a la vez. W2 se pausa antes del `INSERT`. W1 inserta `EN_VUELO`, llama `prepare` y actualiza a `COMPLETADO`. Cuando W2 despierta, su `INSERT ... DO NOTHING` devuelve 0 filas, lee `COMPLETADO` y termina sin llamar al proveedor.

---

### 4. Límites

* **Bloqueos conservadores**: Sin API de consulta, caer justo *antes* de emitir el paquete por red deja la fila en `EN_VUELO`; si no hay reintento antes de 30h, queda `BLOQUEADO` aunque el proveedor nunca recibiera la orden.
* **Ventana física pre-syscall**: Si se permite relevo `<30h`, una pausa del kernel en W1 justo entre la lectura del reloj monotónico y la instrucción `write()` del socket que dure >36h no puede ser frenada por el proveedor al carecer de fencing tokens.