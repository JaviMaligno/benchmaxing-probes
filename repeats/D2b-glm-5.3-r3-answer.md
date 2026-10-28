## Veredicto: no cumple la regla

La propuesta acierta la parte fácil —clave estable `organization:case` (el `attempt_uuid` rompía la idempotencia, porque las reentregas traen uno nuevo) y el `UNIQUE` compuesto (los expedientes se repiten entre organizaciones)— pero falla en lo esencial:

1. **El "riesgo tras seis horas" no es inevitable, es una decisión.** Al expirar el lease, otro worker reenvía; si pasaron más de 6 horas desde la primera aceptación, el proveedor imprime otra vez. La regla prohíbe el duplicado pero **permite expresamente detener la automatización en casos inciertos**. Reenviar tras la ventana es elegir el duplicado que la regla veta.
2. **El lease no cerca al worker viejo.** El proveedor no valida tokens de fencing, así que la exclusión mutua sobre el efecto externo no existe: el worker pausado reanudado puede emitir `print` fuera de todo control. El lease solo ordena reintentos; la seguridad nunca puede depender de él.
3. **Insertar el recibo después de `print`** deja la ventana clásica: respuesta perdida ⇒ sin recibo ⇒ reenvío ciego.

## Alternativa con estados persistentes

Tabla por `(organización, expediente)` —`UNIQUE` compuesto, transiciones condicionales (compare-and-set)— con `estado`, `first_send_at` y clave `organization:case`:

- **NEW:** transacción local que fija `estado=SENDING`, `first_send_at=now` **antes** de emitir nada; luego `print(organization:case, body)`. Respuesta OK ⇒ `COMPLETED`. Timeout ⇒ **no** interpretarlo como "no se imprimió": queda `SENDING`.
- **SENDING / incierto (dentro de ventana):** si `now < first_send_at + 6h − margen`, reintentar con **la misma clave**, coordinado por lease corto (evita avalanchas; no garantiza exclusión). Si el primer envío llegó, el proveedor deduplica; si no, se imprime una vez —se cumple "las nuevas sí se imprimen".
- **Fuera de ventana:** `BLOCKED`, escalar a revisión humana. Jamás reenviar tras 6 horas de la primera aceptación: eso imprime de nuevo.
- **COMPLETED:** ACK a la cola; reentrega con el mismo `message_uuid` relee la fila y termina; un `message_uuid` distinto sobre el mismo par choca contra el `UNIQUE` ⇒ marcar duplicado lógico y ACK sin imprimir.

**Ventana estado→efecto y worker reanudado:** la incertidumbre es inevitable (efecto externo no transaccional), pero se anuncia *antes* de emitirla y se resuelve por reenvío idempotente dentro de la ventana, no por suposiciones. El worker viejo, al reanudarse, debe **releer el estado en transacción** y solo actuar si su transición condicional gana; si ya es `COMPLETED` o `BLOCKED`, termina sin enviar.

**Separación de propiedades:** *a lo más una* = clave estable + regla "solo se imprime con esa clave y antes de `first_send_at+6h−m`". *Que toda carta se imprima* = reintentos frecuentes multi-worker; como red de seguridad, `BLOCKED` lo resuelve una persona — la regla lo permite; el duplicado, no.

## Pruebas

- **t+10h:** aceptada a las 10:00, respuesta perdida, reentrega a las 20:00. El worker nuevo lee `SENDING` con `first_send_at=10:00`, límite vencido ⇒ `BLOCKED`, sin `print`; el viejo reanudado relee y no envía. Cero duplicados. Variante con reentrega a las 11:00: reenvío con la misma clave ⇒ el proveedor deduplica (o imprime si nunca llegó) ⇒ exactamente una.
- **Caída antes del envío:** `SENDING` escrito, `print` nunca emitido. El reintentador envía la misma clave dentro de la ventana ⇒ se imprime una vez; el caído, al volver, ve `COMPLETED` y no envía. Si la ventana se agota sin éxito ⇒ `BLOCKED`.
- **Dos organizaciones, igual expediente:** claves distintas `orgA:C` / `orgB:C`, ambas imprimen una vez cada una. Dos workers simultáneos sobre la misma organización: el segundo `INSERT` falla por el `UNIQUE`, relee y no imprime; la reentrega del mismo `message_uuid` no crea fila nueva.