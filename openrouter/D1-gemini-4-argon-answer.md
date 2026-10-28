### 1. Diagnóstico: Causa observada vs. Riesgos latentes

**Causa observada (incidente 12:00–12:02):**
1. **Clave de idempotencia incorrecta:** `provider.capture` usa `e.request_id`. Como el sistema *upstream* genera un nuevo `request_id` en cada reintento (`R1` → `R2` para el mismo evento `E9`), el proveedor trató a `R2` como un cobro nuevo (`p78`) en lugar de devolver `p77`.
2. **Guardia desactivada y falta de estado previo:** Aunque `Worker` define `guard=True` por defecto, `bootstrap.py` y el manifiesto fuerzan `GUARD='0'`. Además, la base de datos (BD) solo escribe *después* del cobro; al ocurrir el *timeout* en `R1` (12:00), no quedó registro local del intento.

**Riesgos latentes (no detonados o enmascarados por `GUARD='0'`):**
1. **Colisión entre *tenants* en Redis:** Redis es compartido y la clave `'seen:' + e.order_id` omite el `tenant`. Si `GUARD='1'` hubiese estado activo, el pedido 41 del *tenant* A habría bloqueado erróneamente al pedido 41 del *tenant* B (12:03).
2. **Pérdida de registro en BD tras *timeout*:** Con `GUARD='1'`, `R1` habría fijado la clave en Redis antes del *timeout*. El reintento `R2` (12:02) habría devuelto `'duplicate'` sin insertar jamás la fila en la BD.
3. **Brechas de expiración (1h vs. 24h vs. 72h):** El TTL de Redis (1h) y la idempotencia del proveedor (24h) son menores que la ventana de reintentos de *upstream* (72h).
4. **Concurrencia y reinicios:** Sin restricción `UNIQUE` en la BD y con reinicios del *worker* en despliegues, peticiones concurrentes pueden duplicar cobros o perder escrituras en BD.

---

### 2. Evaluación de la propuesta del compañero

**No cumple las reglas del producto.** 
* **Rompe el aislamiento multi-*tenant*:** Usar solo `order_id` en el proveedor, en Redis (`GUARD=1`) y como restricción `UNIQUE` en BD bloquea a distintos *tenants* que reutilicen el mismo `order_id` (ej. el *tenant* B a las 12:03 fallaría).
* **No garantiza *exactly-once*:** Si `GUARD=1` bloquea `R2` tras el *timeout* de `R1`, la BD queda sin registro del cobro `p77`. Además, tras 1h expira Redis y tras 24h expira el libro del proveedor, permitiendo cobros duplicados en reintentos tardíos (hasta 72h).

---

### 3. Qué se puede garantizar realmente con la interfaz actual

Sin búsqueda por orden en el proveedor ni API de reversión, **es imposible garantizar simultáneamente "cero cobros duplicados" y "100% de registros completados en BD" durante las 72h**.
* **Dentro de las primeras 24h:** Se puede garantizar **exactamente un cobro** y la recuperación del `provider_id` en BD tras un *timeout* si se reintenta ante el proveedor con una clave determinista por `(tenant, order_id)`.
* **Entre 24h y 72h:** Si un intento quedó en estado incierto (*timeout* o caída del *worker*) y no se resolvió en 24h, el proveedor olvida la clave. Solo se puede garantizar **a lo sumo un cobro (*at-most-once*)** bloqueando en la BD cualquier reintento a partir de las 24h y marcándolo para conciliación manual.

---

### 4. Reparación mínima

1. **Esquema y estado en BD:** Añadir restricción `UNIQUE(tenant, order)` y una columna `status` (`PENDING`, `COMPLETED`) con marca de tiempo (`created_at`), haciendo de la BD la fuente de verdad durable antes de llamar al proveedor.
2. **Clave compuesta:** Usar `idempotency_key = f"{e.tenant}:{e.order_id}"` en `provider.capture`.
3. **Flujo en `handle(e)`:**
   * Eliminar el bloqueo ciego de Redis (o usarlo solo como *mutex* de corta duración con clave `lock:{tenant}:{order_id}`).
   * Intentar insertar `(tenant, order, status='PENDING')` en BD.
   * Si ya existe:
     * Si es `COMPLETED`, devolver `'duplicate'`.
     * Si es `PENDING` y tiene **< 24h**, continuar a `provider.capture` con la clave `f"{e.tenant}:{e.order_id}"` para recuperar `r.id` de forma idempotente y actualizar la fila a `COMPLETED`.
     * Si es `PENDING` y tiene **≥ 24h**, abortar sin llamar al proveedor (evita doble cobro tras expirar el libro de 24h).

---

### 5. Prueba de regresión

1. Ejecutar `(tenant=A, order=41, req=R1)` simulando *timeout* tras `provider.capture` (`p77`): verificar que la BD conserva `(A, 41, status='PENDING')`.
2. Reenviar `(tenant=A, order=41, req=R2)` (< 24h): verificar que llama al proveedor con clave `'A:41'`, recupera `p77` sin crear `p78`, y actualiza la BD a `COMPLETED` con `p77`.
3. Enviar `(tenant=B, order=41, req=R3)`: verificar que usa clave `'B:41'`, captura `p79` e inserta `(B, 41, p79)` sin colisión.
4. Simular un registro `PENDING` con > 24h de antigüedad: verificar que un reintento no invoca `provider.capture`.

---

### 6. Límites de certeza

* Se asume que el proveedor devuelve el `r.id` original (`p77`) al recibir la misma `idempotency_key` dentro de las 24h y que acepta el formato `tenant:order_id`.
* Sin API de reversión ni consulta, el cobro huérfano `p77` ya ocurrido a las 12:00 no puede conciliarse ni anularse automáticamente desde este servicio.