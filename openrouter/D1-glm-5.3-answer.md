**Causa observada (12:00–12:02).** La captura p77 (R1) sí se ejecutó en el proveedor, pero el cliente no recibió respuesta y no hubo INSERT. El reintento de las 12:02 conservó el event_id (E9) pero trajo un request_id nuevo (R2); como la clave de idempotencia del proveedor es `request_id`, el ledger no pudo deduplicar y creó p78: **doble captura del pedido 41 del tenant A**. La defensa que la habría frenado —el guard de Redis— estaba desactivada: el código lo activa por defecto, pero `bootstrap.py` exige `GUARD=='1'` y el manifiesto fija `GUARD='0'` (deriva de configuración). La BD, sin constraint único, tampoco detectó nada; y como las operaciones son concurrentes, nada serializó los dos intentos. Causa directa: **clave de idempotencia inestable entre reintentos + guard desactivado por el despliegue**. La captura p79 (12:03) es legítima: es otro pedido; el ID 41 se reutiliza entre tenants.

**Riesgos latentes (presentes, no causa del incidente):**
- El guard usa `order_id` sin tenant: con GUARD=1 habría bloqueado el evento de B como "duplicate" (falso positivo).
- TTL del guard 1h < ledger 24h < ventana de reintento 72h: los reintentos tardíos pasan.
- `return 'duplicate'` sin verificar BD: si hubo captura sin fila (patrón de las 12:00), el reintento se descarta y la captura queda huérfana e invisible.
- Redis es compartido y es caché, no frontera de corrección; y la BD sin constraint no frena la carrera antes de capturar dinero.

**La propuesta NO cumple las reglas.** Usar `order_id` como clave de idempotencia hace que el tenant B reutilice la clave "41" del tenant A: el proveedor (ledger presumiblemente global) devolvería la captura de A —monte y pedido equivocados—. El unique sobre `order_id` sin tenant rechazaría la fila legítima de B, pero **después** de que p79 ya capturó dinero: captura sin registro. Y nada cubre reintentos >24h, así que "garantiza exactamente una" es falso. No embarcar.

**Reparación mínima:**
1. Clave de idempotencia **estable y con tenant**: `f"{tenant}:{order_id}"` (o event_id, que el upstream preserva).
2. Constraint único compuesto `(tenant, order_id)` e insertar la fila en estado *pending* **antes** de capturar, actualizándola con `provider_id` después: el constraint aborta concurrentes antes de mover dinero, y un crash intermedio se recupera en el reintento (misma clave → mismo capture id dentro de 24h).
3. Corregir el manifiesto/deriva de config para activar el guard, pero con clave compuesta y como optimización: ante "duplicate", verificar BD, no descartar a ciegas.
4. Reintentos posteriores a 24h: fallar cerrado / revisión manual; no capturar.

**Prueba de regresión (replay del incidente):**
- R2 (mismo E9) con la misma clave → el proveedor devuelve p77, no p78; la fila se inserta con p77.
- E10 del tenant B → clave distinta → captura normal y fila aceptada por el constraint compuesto.
- Dos eventos concurrentes del mismo (tenant, pedido) → uno gana el INSERT previo; el otro aborta antes de capturar.
- Restart entre captura y respuesta → el reintento recupera p77 vía la clave estable.
- Verificar en runtime (log/assert) que el guard está activo y que las claves usadas son las compuestas.

**Qué se puede garantizar y límites de certeza.** Con esta interfaz, el proveedor solo promete: misma clave dentro de las 24h → misma captura. Por tanto, lo alcanzable es **a lo sumo una captura por (tenant, pedido) para reintentos que lleguen dentro de las 24h del primer intento**, más a lo sumo una fila BD vía constraint. "Exactamente una" extremo a extremo en la ventana de 72h **no es demostrable**: un reintento entre las 24h y las 72h genera una captura nueva e indetectable (no hay lookup por pedido), y sin API de reversión no se puede remediar automáticamente. Se requeriría que el proveedor extienda el ledger, ofrezca consulta por pedido/referencia, o aceptar fallar cerrado. Incertidumbre adicional: solo vemos pseudocódigo y tres eventos —puede haber capturas no listadas—, desconocemos la política de expulsión de Redis, si el ledger es global o por tenant, y si puede existir un segundo evento lógico para el mismo (tenant, pedido), lo que obligaría a incluir el event_id en la clave.