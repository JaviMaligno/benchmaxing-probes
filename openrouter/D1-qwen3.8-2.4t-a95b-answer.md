

## Diagnóstico del incidente D1

### Causa observada (12:00 – 12:02)

La captura duplicada de la orden 41 del tenant A (p77 y p78) se explica por una única cadena causal:

1. **GUARD='0' en el manifiesto de despliegue.** La guarda Redis está desactivada; `bootstrap.py` instancia `Worker(..., guard=False)`, por lo que la rama `redis.set(..., nx=True)` nunca se ejecuta.
2. **La clave de idempotencia enviada al proveedor es `e.request_id`.** El reintento upstream conserva el event ID (E9) pero genera un nuevo request ID (R2). El proveedor recibe una clave distinta y trata la segunda llamada como una operación nueva → captura p78.
3. **Timeout del cliente en R1.** El proveedor ya había confirmado p77, pero el worker no recibió la respuesta y no insertó la fila en BD. Al no haber restricción `UNIQUE` en la tabla, nada impide un segundo `INSERT`.

Resultado: dos capturas reales (p77 huérfana, p78 registrada) para el mismo (tenant, order). El evento de tenant B (p79) es legítimo porque las reglas permiten reutilizar `order_id` entre tenants.

### Riesgos latentes que el incidente no exhibió pero que el código contiene

- **Clave Redis sin tenant:** `'seen:'+e.order_id` → `seen:41`. Como Redis es compartido, si la guarda estuviera activa, el evento de tenant B habría sido rechazado como "duplicado" del tenant A.
- **TTL Redis de 3 600 s**, muy inferior a la ventana de reintento upstream de 72 h.
- **Ledger del proveedor de 24 h**, inferior a las 72 h de reintentos.
- **Despliegues reinician el worker:** eventos en vuelo pueden reprocesarse sin que Redis ni la BD los detecten si la fila aún no se insertó.

### Evaluación de la propuesta del compañero

| Cambio propuesto | Veredicto |
|---|---|
| `GUARD=1` | Necesario, pero insuficiente: la clave debe ser `'seen:'+tenant+':'+order_id` y el TTL ≥ 72 h. |
| Idempotency key = `order_id` | **Incorrecto.** Tenants distintos reutilizan `order_id`; el proveedor deduplicaría capturas de tenants diferentes. Además, tras 24 h el ledger expira y un reintento tardío capturaría de nuevo. |
| `UNIQUE(order_id)` | **Incorrecto.** Debe ser `UNIQUE(tenant, order_id)`. Aun así, la restricción solo evita el `INSERT`; la captura en el proveedor ya ocurrió y no existe API de reversa ni consulta por orden, así que un choque concurrente dejaría una captura huérfana irreconciliable de forma automática. |
| "Garantiza exactly-once; ship it" | **Falso.** Ninguna combinación de estas tres medidas cubre la brecha 24-72 h ni la colisión entre tenants. |

### Reparación mínima

1. **Manifiesto:** `GUARD='1'`.
2. **Clave Redis:** `'seen:'+e.tenant+':'+e.order_id`, TTL ≥ 72 h (o igual a la ventana máxima de reintento).
3. **Idempotency key al proveedor:** `f"{e.tenant}:{e.order_id}"`. Esto deduplica reintentos dentro de las 24 h del ledger.
4. **BD:** `UNIQUE(tenant, order_id)`. En el `INSERT`, capturar la violación: registrar alerta y no reintentar la captura.
5. **Manejo del timeout en R1:** reintentar la inserción en BD tras un error de red antes de declarar el evento como nuevo.

### Verificación de regresión

- Test unitario: mismo `(tenant, order)` con dos `request_id` distintos → una sola captura y una sola fila.
- Test de colisión entre tenants: tenant A y B con `order_id` idéntico → dos capturas, dos filas.
- Test de expiración: simular reintento a las 25 h (ledger vencido) → la restricción en BD debe bloquear el `INSERT` y generar alerta.
- Test con `GUARD` desactivado accidentalmente → la restricción en BD actúa como última barrera.

### Límites de certeza

- **p77 no puede revertirse ni confirmarse programáticamente** (sin API de consulta por orden ni de reversa). Requiere conciliación manual con el proveedor.
- La ventana 24-72 h queda cubierta solo por la restricción en BD; si el `INSERT` original falló y el Redis expiró, un reintento a las 30 h produciría una segunda captura antes de que la BD la bloquee.
- Una caída de Redis elimina el estado de la guarda hasta que se repueble.
- No se puede afirmar "exactly-once" absoluto con la interfaz actual del proveedor; lo alcanzable es **at-most-once en la BD** y **best-effort en el proveedor**, con monitoreo para detectar capturas huérfanas.