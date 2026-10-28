**Diagnóstico y evaluación del colega**

Acierta en dos cosas: la clave del proveedor debe ser estable —`warehouse_id:order_id`—, no `delivery_id` (el broker lo cambia en cada reenvío; y el order_id se repite entre almacenes, por eso hay que incluir el almacén). Y el `UNIQUE(warehouse_id,order_id)` evita duplicar filas finales. Pero es insuficiente: **no hay fila durable antes de llamar a `prepare`**, así que dos workers pueden ver simultáneamente “no hay fila” y ambos invocar `prepare`; capturar el conflicto UNIQUE solo protege el *insert final*, no la invocación externa. Y su frase final es falsa en la dirección: lo **imposible es resolver automáticamente** el caso ambiguo tras 36 h; **sí se puede prevenir el duplicado**, a costa de bloquear para revisión.

**Propuesta implementable**

Añadir `prep_intents(warehouse_id, order_id, provider_key, state, generation, first_attempt_at, lease_until, receipt)` con `UNIQUE(warehouse_id,order_id)`. Estados y transiciones:

1. **AUSENTE → RECLAMADO**: al recibir el evento, `INSERT ... ON CONFLICT DO NOTHING` con `first_attempt_at=now`, `generation=1`, `lease_until=min(now+Δ, first_attempt_at+36h)`. Quien inserta es el primario; un conflicto no da derecho a llamar.
2. **RECLAMADO → PREPARADO**: solo el primario con generación vigente y `now<lease_until` llama `prepare(provider_key, payload)`. Si hay éxito definitivo, en una transacción `UPDATE ... WHERE generation=…` y se inserta la fila final (el UNIQUE captura colisiones reales).
3. **RECLAMADO → FALLO_CIERTO**: si `prepare` responde fallo definitivo, marcarlo; reintentar solo tras 36 h (misma clave devolvería el fallo previo).
4. **RECLAMADO (ambiguo) → PREPARADO/FAIL**: respuesta perdida, timeout o caída. Si `now < first_attempt_at definitive success → PREPARADO
- definitive failure → FALLO_CIERTO
- ambiguous or no row after claim → CLAIMED/UNCERTAIN
- after 36h unresolved → BLOQUEADO

Maybe `CLAIMED/UNCERTAIN` same state but with flag `outcome_unknown`.

Fencing sequence:
1. `UPDATE prep_intents SET generation=generation+1, lease_until=min(now+lease, first_attempt_at+36h), owner=:me WHERE warehouse_id=:w AND order_id=:o AND generation=:prev` and ensure 1 row affected.
2. Before send: re-`UPDATE ... SET lease_until=... WHERE generation=:gen`; if 0 rows, abort.
Wait if B takes over after second update but before A sends? Our second update is preflight; race remains. We can say unavoidable micro-race. But to "impedir que worker antiguo envíe después de que otro se haga cargo", if B has already taken over (increment generation) before A's preflight, A's update affects 0 => no send. That's the scenario "pausado y luego otro se hace cargo" — A resumes and tries preflight; B already took over so blocked. Good. The only unblocked scenario is when B takes over after A's preflight and before actual send; acknowledge residual in limits.

Could add optional stronger: use `pg_advisory_xact_lock` held across call? But that can deadlock/availability; not necessary. But maybe mention if absolute fencing required hold a row lock across the call; but then long transaction risk. The user didn't ask for that extreme and word budget. Just mention as limit.

Need ensure "new orders process without intervention if no failures" — our design: if call succeeds/fails definitively, auto-finalizes; if ambiguous and under 36h, another worker resolves automatically; if no failure at all, automatic. Good.

Let's count words in draft. I'll write in final directly.

Need maybe mention "delivery_id no debe ser key porque broker la cambia en reenvíos; usar W:O" in diagnosis.

Let's ensure the answer explicitly addresses "una caída justo antes de enviar y justo después de enviar" — yes in trace B.

Let's write finalFalló tu colega en ambos extremos. Su esquema sí cubre la *escritura final*, pero no la invocación externa: dos workers pueden leer “no hay fila” a la vez e invocar `prepare` dos veces; el `UNIQUE` solo impide el segundo `INSERT`, no el segundo `prepare`. Y su frase postrera está invertida: lo que la API de 36 h hace **imposible es resolver en automático** un resultado incierto pasado ese plazo; **el duplicado sí es prevenible** — a costa de bloquear para revisión, que es justo lo que exige la prioridad “no preparar dos”.

**Estados (tabla `prepare_state`)**

Añade `prepare_state(warehouse_id, order_id, provider_key, state, generation, first_attempt_at, lease_until, receipt)` con `UNIQUE(warehouse_id,order_id)`. Clave del proveedor: `key = warehouse_id||':'||order_id` (estable ante reenvíos; distingue almacenes).

Transiciones, siempre con `WHERE generation=:gen` y verificación de filas afectadas:

1. **AUSENTE → RECLAMADO**: `INSERT … ON CONFLICT DO NOTHING`, `first_attempt_at=now()`, `generation=1`, `lease=min(now()+Δ, first_attempt_at+36h)`. Solo el insertor es primario.
2. **RECLAMADO → PREPARADO/FALLO_CIERTO**: solo el primario con `now()<lease_until` llama a `prepare`. Éxito definitivo → en una transacción `UPDATE state='PREPARADO', receipt=…` e `INSERT` de la fila final (el `UNIQUE` captura colisiones reales). Fallo definitivo → `FALLO_CIERTO`; reintento solo tras 36 h (la clave devolvería el fallo previo).
3. **RECLAMADO (ambiguo) → PREPARADO/FALLO_CIERTO**: si la llamada no da resultado, se marca `outcome_unknown`. Cualquier worker puede, mientras `now() < first_attempt_at+36h`, invocar `prepare` con la misma clave: si arroja definitiva, la transcribe; si no, amplía el lease.
4. **RECLAMADO ambiguo → BLOQUEADO**: al vencer 36 h sin resultado definido, sin `receipt`, se marca `BLOQUEADO` para revisión humana. Nunca más `prepare`.
5. Reenvíe posterior a 36 h de una orden ya `BLOQUEADA` o `PREPARADA`: se ignora; el estado es la fuente de verdad.

El `lease` se envía hardcodeado a 96 h (broker). No confíes en él; confía en el estado.

**Traza adversa A — caída justo antes de enviar**

09:00 el worker `W1` reclama y falla justo antes de emitir `prepare`. No hay llamada ni respuesta. Reescalado: `W2` toma la cuenta (incrementa `generation`), ve `now<36h`, llama y obtiene definitiva → `PREPARADO` + fila final. Al reenviarse a t+50h no se actúa. Correcto y automático.

**Traza adversa B — caída justo después de enviar**

09:00 `W1` emite `prepare`, el proveedor **ejecuta** la preparación; la respuesta se pierde y `W1` cae. `W2` toma la cuenta y, como `now<first_attempt_at+36h`, llama con la misma clave: el proveedor devuelve el resultado previo → lo transcribe a `PREPARADO` o `FALLO_CIERTO`. No hay segundo `prepare`. Si `W2` no llega antes de 36 h: `BLOQUEADO`. Nunca duplicado.

**Fencing (sin tokens del proveedor)**

El primario no envía directamente: antes de cada `prepare` ejecuta un *preflight* `UPDATE prepare_state SET lease_until=… WHERE generation=:gen`, y solo envía si afecta exactamente 1 fila. El relevo se hace con `UPDATE … SET generation=generation+1 WHERE generation=:antigua`, que también exige 1 fila. Así, un worker pausado que despierta tras el relevo falla el preflight y no envía.

**Límites**

(1) Carrera residual irreductible: si el relevo ocurre entre el preflight de `W1` y el envío real, ambos pueden emitir; mitigable solo reteniendo un `LOCK` de fila durante la llamada, con el coste de transacciones largas y posible bloqueo de otros workers. (2) Tras 36 h sin `receipt` no hay recuperación automática: solo revisión humana. (3) Si el proveedor ignora su propio TTL/`lease`, nada lo impide en el lado cliente: nuestro dique es solo la ventana de 36 h. (4) La deduplicación del broker no es confiable; el estado durable es la única verdad.