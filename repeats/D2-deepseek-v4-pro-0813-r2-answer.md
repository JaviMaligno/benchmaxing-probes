**Diagnóstico.** La afirmación del colega es insuficiente. `UNIQUE(warehouse_id,order_id)` solo impide duplicar el registro final; no impide ejecutar `prepare` dos veces pasadas las 36 h. Sin un estado previo al envío, nadie recuerda el intento de las 09:00.

**Propuesta.** Añadir `prep_intent(warehouse_id, order_id, key, status, owner_token, lease_until, first_attempt_at, receipt, PRIMARY KEY(warehouse_id,order_id))` y `fulfillment(warehouse_id, order_id, receipt, status, UNIQUE(warehouse_id,order_id))`. La clave de `prepare` es `warehouse_id:order_id`.

Estados: `NEW`, `CLAIMED`, `PREPARING`, `DONE`, `BLOCKED`.

Transiciones:
- Al recibir el evento: `INSERT … ON CONFLICT DO NOTHING`; si ya existe en `DONE`/`BLOCKED`, no actuar.
- Reclamación (`NEW` o `PREPARING` con lease vencido → `CLAIMED`): `UPDATE … SET status='CLAIMED', owner_token=…, lease_until=now()+L WHERE … AND (lease_until IS NULL OR lease_until<now())`; si `rowcount=0`, no reclamaste.
- Guard pre-envío (`CLAIMED` → `PREPARING`, atómico): verificar `owner_token` y lease vigente; fijar `first_attempt_at` si es nulo; renovar lease.
- Llamar `prepare(key,payload)` fuera de transacción.
- Éxito/idempotente (`PREPARING` → `DONE`): en transacción, verificar token, guardar `receipt`, insertar `fulfillment` capturando `UNIQUE`.
- Sin respuesta: permanecer `PREPARING`.
- Al reclamar un `PREPARING` vencido: si `now()-first_attempt_at > 36h`, transición a `BLOCKED` (revisión manual, nunca reintentar); si `<36h`, reintentar con la misma clave (es idempotente).

**Caídas.** *Justo antes de enviar* (tras el guard, sin HTTP): queda `PREPARING` con lease. Si expira y otro worker reclama en `<36h`, reintenta la misma clave: si el primer envío no salió, prepara ahora; si salió, `prepare` devuelve el resultado previo. A `>36h` no reintenta: bloquea. *Justo después de enviar* (respuesta perdida): idéntico; el reintento temprano se resuelve por idempotencia y el tardío por bloqueo.

**Fencing local.** Cada reclamación genera `owner_token` nuevo (generación). Toda transacción de guard/envío comprueba que el token siga siendo suyo. Un worker pausado que despierta tras perder el lease falla la comprobación y aborta sin invocar `prepare`.

**Trazas adversas.**
1. 09:00 worker1 reclama, guard, `prepare` tiene éxito pero la respuesta se pierde; 09:01 cae. A t+50h el broker reenvía (mismo `event_id`, nuevo `delivery_id`). Worker2 reclama el lease vencido, ve `PREPARING` con `first_attempt_at` >36h, pasa a `BLOCKED` y no llama a `prepare`. La orden de igual ID en otro almacén usa otra `warehouse_id:order_id`; no colisiona.
2. Worker1 hace el guard y se pausa antes del HTTP; el lease expira; worker2 reclama con token nuevo. Worker1 despierta, su transacción falla por token inválido y no envía. Worker2 prepara e inserta; `UNIQUE` cierra la carrera.

**Límites.** Pasadas 36 h, con esta API es imposible distinguir «no se ejecutó» de «se ejecutó y se perdió la respuesta»; por eso `BLOCKED` manual es la única opción segura. La ventana guard→HTTP no es atómica: un proceso pausado justo después del guard más de 36 h podría enviar tarde; sin un *fencing token* que el proveedor valide no se elimina por completo esa ventana. No se inventan APIs del proveedor.