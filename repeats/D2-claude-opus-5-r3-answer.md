## Diagnóstico

Tres fallos, no uno:

1. **`key = delivery_id`**: el broker cambia `delivery_id` en cada reenvío, así que la deduplicación de 36 h del proveedor nunca se activa. Cada reenvío es una preparación nueva. Este es el defecto grave.
2. **Sin rastro previo al envío**: la fila se inserta *después* de `prepare`. Una caída en la ventana envío→insert borra toda evidencia de que se envió. Es exactamente el caso de las 09:00.
3. **`UNIQUE` solo en filas finales**: detecta dos éxitos ya escritos, nunca dos llamadas en vuelo.

## Propuesta

Tabla `preparations` con `UNIQUE(warehouse_id, order_id)` —que es también la `idem_key`, resolviendo la colisión de `order_id` entre almacenes— más `state, first_sent_at, owner_id, epoch, lease_expires_at, receipt`.

Estados y transiciones:

- `PENDING` → `SENDING`: `UPDATE ... SET state='SENDING', owner_id=$yo, epoch=epoch+1, lease_expires_at=now()+'60s', first_sent_at=COALESCE(first_sent_at,now()) WHERE (state='PENDING' OR lease_expires_at<now()) RETURNING epoch`. Cero filas ⇒ otro manda. **Commit antes de llamar a `prepare`.**
- `SENDING` → `PREPARED(receipt)` / `FAILED` : solo con `WHERE owner_id=$yo AND epoch=$mi_epoch`.
- `FAILED` → `PENDING` (reintento con la misma `idem_key`: gratis, el proveedor devuelve el resultado previo).
- `SENDING` con lease expirado = **UNKNOWN**. Reconciliador: si `now() < first_sent_at + 30h`, reintenta (resuelve sin intervención). Si no, `BLOCKED_FOR_REVIEW`.
- Regla dura: **ningún worker llama a `prepare` si `now() > first_sent_at + 30h`**; pasa a `BLOCKED_FOR_REVIEW`. El corte de 30 h sobre 36 h es el margen que compra la seguridad.

Dedup del broker: `UNIQUE(event_id)` en una tabla aparte, nunca `delivery_id`.

## Sobre la afirmación del colega

La clave es correcta; el resto, no. Capturar el conflicto `UNIQUE` **no** cubre la concurrencia: lo que impide dos paquetes cuando dos workers consultan en vacío y ambos envían es la deduplicación del proveedor por `idem_key`, no el índice. Y el `UNIQUE` sobre filas finales no existe durante la ventana peligrosa. Su segunda tesis es falsa en la práctica: el caso incierto tras 36 h es inevitable *solo si no se registra la intención antes de enviar*. Con `SENDING` persistido y corte a 30 h, el incierto se vuelve **detectable y bloqueable** en vez de convertirse silenciosamente en un duplicado — que es la prioridad declarada.

## Caídas

- **Justo antes de enviar**: fila en `SENDING`, proveedor intacto. El lease expira, otro worker reenvía la misma clave: sin duplicado, cero intervención.
- **Justo después de enviar**: fila en `SENDING` con `first_sent_at`. Dentro de 30 h el reintento recupera el `receipt`; pasadas 30 h, `BLOCKED_FOR_REVIEW`.

## Trazas adversas

**T1 (el expediente).** 09:00 envío aceptado, respuesta perdida; existe `SENDING(first_sent_at=09:00)`. 09:01 caída. t+50 h: reenvío con `delivery_id` nuevo; 50 h > 30 h ⇒ `BLOCKED_FOR_REVIEW`, no se invoca `prepare`. Un paquete, revisión humana. El pedido homónimo de otro almacén tiene otra `idem_key` y se tramita solo.

**T2 (worker zombi).** W1 toma lease `epoch=1`, envía, se congela. Lease expira; W2 toma `epoch=2`, reenvía la misma clave a las 02:00 h de vida, recibe el mismo `receipt`, escribe `PREPARED`. W1 despierta: su `UPDATE ... WHERE epoch=1` afecta 0 filas, descarta su resultado. El proveedor nunca ve un token: el *fencing* funciona porque todos los workers mandan la **misma clave**, de modo que un envío tardío es un no-op.

## Límites

Un envío tardío de un worker congelado que cruce las 36 h desde la primera aceptación **sí** duplicaría; la regla de corte a 30 h lo acota (exige una pausa >6 h entre comprobación y envío), no lo elimina. Sin `prepare` fencing-aware, búsqueda ni cancelación, esto es irreducible. Un proveedor caído >30 h produce bloqueos, no duplicados: la asimetría pedida.