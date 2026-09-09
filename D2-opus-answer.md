## Diagnóstico

Tres fallos independientes:

1. **Clave errónea.** `prepare(delivery_id,...)`: el broker cambia `delivery_id` en cada reenvío, así que la deduplicación del proveedor nunca se activa. Cada reenvío es una preparación nueva.
2. **Trabajo invisible.** La fila se escribe *después* de la llamada. Entre el envío y el commit no existe rastro durable: una caída deja un paquete real sin registro.
3. **UNIQUE inútil para el riesgo.** Protege el estado final, no la ventana peligrosa (el envío). Dos workers leen "no hay fila" y ambos llaman.

## Evaluación de la afirmación del colega

Parcialmente correcta y peligrosamente incompleta.

- **Correcto:** la clave debe ser `warehouse_id:order_id` (los `order_id` se repiten entre almacenes; solo el par es único).
- **Incorrecto sobre concurrencia:** capturar el conflicto UNIQUE ocurre *después* del envío. Lo que evita el duplicado real no es la DB, es la deduplicación de 36 h del proveedor. Se está delegando el invariante a una caché ajena.
- **Incorrecto sobre lo inevitable:** el reenvío del broker dura 96 h > 36 h, así que la ventana *siempre* puede expirar. El caso incierto no se resuelve automáticamente, pero **sí se previene**: basta no reintentar fuera de ventana y bloquear para revisión. "No preparar dos" tiene prioridad; el sistema debe rendirse, no adivinar.

## Propuesta

Dos tablas. `inbox(event_id PK)` — ignorar `delivery_id`. Y `job` con `UNIQUE(warehouse_id, order_id)`, columnas `state`, `lease_id`, `lease_expira`, `first_sent_at`, `receipt`.

Estados y transiciones:

- **NEW → SENDING**: `UPDATE ... SET state='SENDING', lease_id=$nuevo, first_sent_at=coalesce(first_sent_at, now()) WHERE state IN ('NEW') ` — **commit antes de llamar**. Insertar NEW con `ON CONFLICT DO NOTHING` da el candado natural.
- **SENDING → DONE**: `UPDATE ... SET receipt=$r, state='DONE' WHERE lease_id=$mío AND state='SENDING'`. Cero filas ⇒ perdí el lease: descarto el resultado y no vuelvo a llamar.
- **SENDING → SENDING (reintento seguro)**: solo si `now() < first_sent_at + 36h - margen`. Como la aceptación del proveedor es posterior o igual a `first_sent_at`, la ventana de dedup cubre con seguridad ese intervalo: el reintento devuelve el resultado previo, nunca prepara otro.
- **SENDING → UNCERTAIN**: al expirar el lease sin receipt y superado `first_sent_at + 36h`. Terminal automático.
- **UNCERTAIN → DONE_MANUAL / CANCELLED**: solo operador.

**Caída justo antes de enviar:** hay fila SENDING sin paquete. Otro worker reintenta dentro de las 36 h; si nadie lo toma a tiempo, queda UNCERTAIN — conservador, correcto.

**Caída justo después de enviar:** idéntico registro. Esa indistinguibilidad es deliberada: ambos casos son seguros bajo la misma regla.

**Worker viejo pausado:** no se le puede impedir llamar a `prepare` (el proveedor no entiende fencing). Se acota el daño: (a) su llamada usa la misma clave, absorbida por el dedup si sigue dentro de 36 h; (b) su escritura de resultado se rechaza por `WHERE lease_id=$mío`; (c) **ningún worker adquiere un lease sobre SENDING pasadas las 36 h** — se pasa a UNCERTAIN. Así nunca coexisten dos envíos fuera de ventana.

## Trazas adversas

**A.** 09:00 envío, respuesta perdida, worker cae; con el diseño nuevo existe SENDING con `first_sent_at=09:00`. t+50 h: reenvío del broker, `event_id` ya en inbox, job en SENDING, 50 h > 36 h ⇒ **UNCERTAIN**, no se llama. El paquete real no se duplica. El pedido homónimo de otro almacén tiene clave distinta y fluye normal.

**B.** Worker 1 toma lease, se pausa tras enviar (t+2 h). Worker 2 hereda a t+5 h, reintenta (dentro de 36 h), recibe el mismo receipt, escribe DONE. Worker 1 despierta, su UPDATE afecta 0 filas y se descarta.

## Límites

Sin búsqueda ni cancelación, UNCERTAIN es irreducible y requiere conciliación humana fuera de banda. La regla de 36 h depende del reloj: usar margen amplio. Un `payload` distinto con la misma clave devolvería el resultado viejo silenciosamente.