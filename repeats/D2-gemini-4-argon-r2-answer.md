### 1. Diagnóstico y evaluación del colega

El código actual tiene tres defectos críticos: usa `delivery_id` (que cambia en cada reenvío del broker) anulando la deduplicación del proveedor; ejecuta `prepare()` antes de escribir en PostgreSQL, permitiendo llamadas concurrentes y perdiendo el rastro si el worker cae tras enviar; y no aísla el `order_id` por almacén en la clave externa.

La afirmación del colega es **parcialmente incorrecta**:
1. **Clave**: Acerta al usar `warehouse_id:order_id`, evitando colisiones entre almacenes y tolerando el cambio de `delivery_id`.
2. **Concurrencia**: Capturar `UNIQUE` **después** de `prepare()` no evita que dos workers invoquen simultáneamente al proveedor antes del `INSERT`.
3. **Ventana >36h**: **Sí se puede prevenir** el duplicado persistiendo una fila de intención con marca temporal (`first_attempt_at`) **antes** de invocar `prepare()`. A `t+50h`, el sistema detecta que el intento incierto superó el margen seguro (<36h) y bloquea el pedido sin llamar al proveedor.
4. **Caída justo antes vs. justo después de enviar**: Sin API de consulta en el proveedor, ambos fallos dejan la fila sin confirmación y son **indistinguibles** (resultado incierto).
5. **Worker antiguo pausado**: Sin *fencing tokens* en el proveedor, un *lease* en BD no cancela una escritura TCP en curso cuando un proceso pausado despierta. Para evitar duplicados: (a) ningún segundo worker toma el relevo tras una caída o expiración de *lease* si se prioriza riesgo cero (o solo reintenta con la misma clave dentro de `<24h` desde `first_attempt_at`, donde el proveedor absorbe ambos envíos salvo pausas >36h); (b) se valida el reloj monótono local justo antes del socket; y (c) se aísla o mata el contenedor/proceso (*STONITH* / revocación de red) al vencer su *lease*.

---

### 2. Propuesta implementable

**Esquema (`order_preparations`)**:
`warehouse_id`, `order_id`, `provider_key` (`warehouse_id || ':' || order_id`), `state` (`SENDING`, `COMPLETED`, `BLOCKED`), `attempt_id`, `first_attempt_at`, `lease_until`, `receipt`, con `UNIQUE (warehouse_id, order_id)`.

**Estados y transiciones**:
1. **Tx1 (Reserva previa al envío)**:
   `INSERT INTO order_preparations VALUES (..., 'SENDING', gen_random_uuid(), now(), now()+'60s', NULL) ON CONFLICT (warehouse_id, order_id) DO NOTHING`.
   - Si inserta 1 fila: ir al Paso 2.
   - Si hay conflicto, `SELECT ... FOR UPDATE`:
     - `COMPLETED` o `BLOCKED`: hacer ACK al broker y salir.
     - `SENDING` con `now() < lease_until`: otro worker activo; salir sin enviar.
     - `SENDING` con `now() >= lease_until`: si `now() >= first_attempt_at + '24 hours'` (margen de seguridad de 12h sobre las 36h), actualizar `state='BLOCKED'`, hacer ACK y alertar a revisión. Si `< 24h`, renovar `attempt_id` y `lease_until = now()+'60s'`, e ir al Paso 2.
2. **Invocación externa (fuera de Tx)**:
   Verificar reloj monótono local (`< lease_until` y `< first_attempt_at + 24h`). Llamar `prepare(provider_key, payload)` con timeout `< 30s`.
3. **Tx2 (Cierre)**:
   - Si devuelve `receipt`: `UPDATE order_preparations SET state='COMPLETED', receipt=$1 WHERE warehouse_id=$2 AND order_id=$3`. Hacer ACK.
   - Si hay error/timeout: si `now() >= first_attempt_at + '24 hours'`, pasar a `state='BLOCKED'` y ACK; si no, mantener `SENDING` para reintento tras vencer `lease_until`.

---

### 3. Dos trazas adversas

- **Traza 1 (Respuesta perdida a las 09:00, caída a las 09:01, reenvío a t+50h y otro almacén)**:
  `09:00`: Worker 1 ejecuta Tx1 para `(W1, O9)` (`SENDING`, `first_attempt_at=09:00`) e invoca `prepare("W1:O9", payload)`. El proveedor prepara el paquete, la respuesta se pierde y Worker 1 cae a las `09:01`. En paralelo, `(W2, O9)` inserta su propia fila (`"W2:O9"`) y pasa a `COMPLETED` sin interferencia. A `t+50h`, el broker reenvía `(W1, O9)` con nuevo `delivery_id`. Worker 2 ejecuta Tx1, ve `SENDING` con `50h >= 24h`, transiciona a `BLOCKED` y hace ACK sin llamar a `prepare()`.
- **Traza 2 (Concurrencia y caída justo antes de enviar)**:
  Worker 1 y Worker 2 reciben `(W1, O5)` a la vez. Worker 1 gana Tx1 (`SENDING`, `lease_until=09:01`); Worker 2 ve el *lease* vigente y aborta. Worker 1 cae justo antes del socket `prepare()`. A las `09:02` (`< 24h`), Worker 2 toma el *lease* vencido, llama `prepare("W1:O5", payload)` y cierra en `COMPLETED`.

---

### 4. Límites

- **Ventana irreducible pre-syscall**: Sin *fencing* en el proveedor, si una pausa del SO congela a un worker justo entre el chequeo del reloj local y la escritura TCP durante >36h mientras otro worker completó el pedido, ocurrirá un duplicado. Evitarlo al 100% exige transicionar cualquier `SENDING` expirado directo a `BLOCKED` (cero reintentos automáticos) y matar el nodo original antes de resolver manualmente.
- **Reconciliación manual**: Los pedidos en `BLOCKED` requieren verificación humana externa con el proveedor.