# Diagnóstico — incidente D1

## Causa observada

El duplicado de (A, 41) tiene una causa proximal y una habilitante:

1. **El guard estaba apagado.** `bootstrap.py` usa `'0'` como default y el manifiesto fija `GUARD='0'`. El comentario del código ("enabled by default") contradice la configuración real. Sin guard, el reintento de E9 a las 12:02 pasó directo al provider.
2. **La clave de idempotencia es `request_id`.** El enunciado dice que un reintento upstream conserva el event ID pero genera un request ID nuevo. Por construcción, R1 y R2 son claves distintas: el ledger del provider nunca pudo deduplicar. La protección del provider estaba anulada por diseño, no por configuración.

Cualquiera de las dos, corregida sola, habría evitado *este* duplicado; ambas estaban rotas a la vez.

Aparte: a las 12:00 hubo captura (p77) **sin fila en DB**. El `db.insert` va después de `provider.capture`, así que un timeout o un restart por deploy deja capturas huérfanas sin registro. p77 y p78 son hoy un cobro doble real y, sin API de reversión, no se resuelve desde el código.

## La propuesta no cumple las reglas

Tiene la intuición correcta (clave estable por pedido) con el alcance equivocado en los tres puntos:

- **`seen:'+order_id` sin tenant.** Redis es compartido. Con `GUARD=1`, el evento de las 12:03 (tenant B, order 41) habría devuelto `'duplicate'` y B **nunca se habría cobrado**. La propuesta convierte un falso negativo en un falso positivo silencioso, que es peor: no deja rastro.
- **`order_id` como idempotency_key.** Si el ledger del provider es global entre tenants, B colisiona con A y recibe la respuesta de p77.
- **`UNIQUE (order_id)`.** Rechaza la fila legítima de B. Debe ser `UNIQUE (tenant, order)`.

Y "exactly once" no se sostiene: el guard tiene `ex=3600`, el ledger dura 24 h y upstream reintenta hasta 72 h. Un reintento a las 30 h no encuentra ni Redis ni ledger y captura de nuevo. Además la unique constraint se evalúa *después* del cobro: impide la fila duplicada, no el movimiento de dinero.

## Reparación mínima

1. Manifiesto `GUARD='1'` y default `'1'` en `bootstrap.py` (fail-safe).
2. Guard con `seen:{tenant}:{order_id}`.
3. `idempotency_key = f"{tenant}:{order_id}"` — determinista, estable entre reintentos, seguro aunque el ledger sea global.
4. `UNIQUE (tenant, order)` en DB.
5. **Insertar una fila de intención `(tenant, order, status='pending')` antes de llamar al provider**, y completarla con `provider_id` después. Esto mueve la barrera durable a la DB, que sobrevive los 72 h, los restarts y la evicción de Redis. Redis pasa a ser optimización, no el mecanismo de corrección.

## Qué se puede garantizar realmente

Con la interfaz dada: **at-most-once dentro de la ventana del ledger (24 h)** y **como máximo una captura *registrada* por (tenant, order) de forma permanente**. Exactly-once no es alcanzable: sin lookup por order y sin reversión, una captura confirmada por el provider pero no registrada localmente no se puede reconciliar ni deshacer. Lo máximo es reducir la ventana de riesgo a la que va entre el insert de intención y la respuesta del provider, y dejarla auditable.

## Chequeo de regresión

Reproducir los tres eventos y esperar: 12:00 → captura + fila `pending`; 12:02 → **sin captura nueva**, fila reconciliada a p77; 12:03 → tenant B capturado, **no** `'duplicate'`. Añadir: (A, 41, E9, R4) a t+30 h con Redis vaciado → sin captura nueva; restart del worker entre 12:00 y 12:02; 12:02 y 12:03 concurrentes.

## Límites de certeza

No sé si el ledger del provider está aislado por tenant, ni qué devuelve ante clave repetida (respuesta original o error) — el punto 3 asume lo primero y hay que cubrir la otra rama. No puedo confirmar el estado real de p77 ni cuántas huérfanas más existen: requiere conciliación manual con el provider. El análisis se apoya en tres eventos y en pseudocódigo; no verifiqué semántica transaccional real.