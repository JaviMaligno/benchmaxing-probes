## Causa observada

La doble captura de tenant A / order 41 (p77 y p78) tiene una causa directa: **la clave de idempotencia del proveedor es

**`e.request_id`, que cambia en cada reintento upstream.** El evento E9 se reintentó con R1 y R2: dos claves distintas → dos capturas reales. El ledger del proveedor nunca tuvo ocasión de deduplicar.

Causa contribuyente: el guard de Redis estaba **desactivado en producción**. El manifiesto fija `GUARD='0'` y `bootstrap.py` usa `'0'` como default, así que el comentario «enabled by default» de `worker.py` es falso. No hubo segunda línea de defensa.

Nótese también que a las 12:00 el proveedor capturó p77 pero **no se insertó fila en DB**: p77 quedó huérfano. Ese es un fallo distinto (captura sin registro) y no lo arregla ninguna clave de idempotencia.

## La propuesta del compañero no cumple las reglas

Los tres puntos están mal dimensionados por olvidar el tenant:

1. **`idempotency_key = order_id`**: colisiona entre tenants. En el evento de las 12:03, tenant B / order 41 reutilizaría la clave de tenant A; el proveedor devolvería la captura ya existente y la fila de B quedaría apuntando a un `provider_id` ajeno. Tenant B nunca cobra y el registro miente. Es peor que el bug actual.
2. **`GUARD=1` con `seen:'+e.order_id`**: mismo defecto en Redis, que además es compartido entre tenants. El evento legítimo de tenant B se habría descartado como `'duplicate'`.
3. **`UNIQUE(order_id)`**: rechaza la fila de tenant B. La regla es una captura por **(tenant, order)**, no por order.

Y «guarantees exactly once» es falso en cualquier variante: el hueco entre `provider.capture` y `db.insert` sigue abierto, que es exactamente lo que produjo p77.

## Riesgos latentes (aún no observados)

- **Ledger 24h vs reintentos 72h**: pasadas 24h, la misma clave estable ya no deduplica. Un reintento en la hora 30 captura de nuevo. Ningún diseño de clave resuelve esto.
- **Guard antes de capturar, TTL 3600s**: si el proceso muere tras capturar, el guard bloquea 1h y luego expira, habilitando recaptura.
- **Sin `UNIQUE`, con concurrencia**: dos workers pueden insertar el mismo (tenant, order).
- **Reinicios por deploy** convierten cualquier ventana entre capture e insert en huérfanos silenciosos.

## Reparación mínima

1. `idempotency_key = f"{e.tenant}:{e.order_id}"` (estable entre reintentos, aislado por tenant).
2. `UNIQUE(tenant, order_id)` en DB.
3. **Escribir la intención antes de capturar**: insertar `(tenant, order, key, status='pending')`; si el `UNIQUE` falla, no capturar. Tras la respuesta, actualizar con `provider_id` y `status='captured'`. Así una captura sin registro deja rastro `pending` reconciliable a mano, en vez de un huérfano invisible.
4. Guard de Redis: `seen:{tenant}:{order}`, o eliminarlo — con (1)+(3) es solo una optimización, y su TTL desalineado añade riesgo.
5. **Rechazar o apartar eventos con antigüedad > 24h** en vez de capturarlos: fuera del ledger no hay garantía, y sin lookup por order no se puede comprobar.
6. Corregir el default de `bootstrap.py` y el manifiesto para que coincidan con el comentario.

## Qué se puede garantizar de verdad

Con la interfaz declarada: **como máximo una captura por (tenant, order) dentro de 24h**, más un registro reconciliable de lo que se intentó. No «exactly once». Sin lookup por order ni API de reversión, p77 no es detectable ni reversible por código: requiere conciliación manual contra el extracto del proveedor.

## Límites de certeza

- No consta si el ledger del proveedor está **aislado por cuenta de tenant**. Si cada tenant tiene su propia cuenta, la colisión cross-tenant de la propuesta podría no materializarse — no puedo verificarlo con la evidencia dada, y aun así el `UNIQUE(order_id)` seguiría roto.
- Asumo que el importe de E9 fue idéntico en R1 y R2; no está afirmado.
- No sé si p77 y p78 llegaron ambos a liquidación o solo se autorizaron.
- Con solo tres eventos no puedo estimar cuántos huérfanos previos existen; hay que auditar el histórico buscando capturas del proveedor sin fila en DB.