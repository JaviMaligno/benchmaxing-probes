

**¿Cumple la propuesta? No.**

1. **Reenviar al expirar el lease trata el timeout como "no se hizo"**. A las 10:00 la impresión *fue aceptada*; la reentrega a t+10h reenviaría con la misma key fuera ya de la ventana de 6h del proveedor → segunda carta. Ese riesgo **no es inevitable**: el enunciado permite detener la automatización en casos inciertos; se gestiona parando, no aceptándolo.
2. **El lease no cerca (fence)**: el worker viejo puede reanudarse y enviar en paralelo. Dentro de 6h la key estable salva; fuera, duplicado.
3. **Insertar el recibo después de `print` deja ventana**: caída tras aceptación y antes del INSERT → sin recibo → la reentrega reenvía. El estado debe persistirse *antes* del efecto externo.
4. En la implementación base, usar `attempt_uuid` como key anula la deduplicación del proveedor (cada reentrega trae uno nuevo).

**Alternativa con estados persistentes**

Tabla `recibos` con UNIQUE(organización, expediente); columnas: `estado` ∈ {RESERVADO, ENVIADO, CONFIRMADO, REVISIÓN}, `lease_token`, `lease_expira`, `sent_at`, `message_uuid`.

Invariante clave: `sent_at` se fija mediante CAS atómico (`UPDATE ... WHERE sent_at IS NULL`) **antes** de llamar a `print`. Solo el ganador del CAS puede enviar; `sent_at` nunca se resetea automáticamente. Key del proveedor: serialización canónica de `(org, expediente)` —estable entre intentos—, no el attempt_uuid.

Decisiones al llegar mensaje:
- **Sin fila (nuevo)**: INSERT RESERVADO → CAS `sent_at` → `print` → si aceptación: CONFIRMADO y ACK; si rechazo definitivo: REVISIÓN; si timeout: queda ENVIADO (estado ya persistido), resultado desconocido.
- **CONFIRMADO**: ACK (reentrega de algo ya completado).
- **ENVIADO con lease vigente de otro**: no enviar; reencolar.
- **ENVIADO, lease expirado, <6h desde `sent_at`**: otro worker toma el lease y reenvía con la *misma* key. Es seguro: si el primero fue aceptado, el proveedor deduplica; si no llegó, este realiza la impresión.
- **ENVIADO >6h sin confirmación (incierto)**: REVISIÓN; **no reenviar**, aparcar y alertar. Aquí se resuelve el escenario de t+10h.
- **Worker antiguo reanudado**: revalida lease/CAS antes de actuar y renueva el lease como último paso previo a `print` (minimiza la ventana zombi). Si quedó pausado entre su CAS y la llamada, es el único poseedor de `sent_at`: nadie más enviará, y el sistema no autoriza ningún envío tras 6h, por lo que no existe duplicado *autorizado* por el diseño.

**Separación de garantías**
- *No duplicación*: UNIQUE + CAS sobre `sent_at` (como máximo un emisor autorizado) + key estable + deduplicación del proveedor ≤6h + prohibición de reenviar pasadas 6h.
- *Toda carta se imprime*: reentregas de la cola hasta 48h, reintentos seguros ≤6h y toma de leases expirados; nada se pierde en silencio: todo mensaje termina en CONFIRMADO o REVISIÓN (solo se ACK en estados terminales).

**Pruebas**
1. **t+10h**: aceptar impresión a las 10:00 y perder la respuesta. Reentrega a las 20:00: la fila está ENVIADO con `sent_at`=10:00; 20:00 > 10:00+6h → transición a REVISIÓN, **cero llamadas nuevas a `print`**, alerta emitida, mensaje aparcado.
2. **Caída antes del envío**: worker inserta RESERVADO y muere. Expira el lease; un segundo worker gana el CAS (`sent_at` nulo demuestra que nada se envió) e imprime: exactamente una carta. Subcaso: caída tras el CAS pero antes de la llamada → reintento ≤6h con la misma key: o la primera llamada no llegó (el reintento es la única impresión) o llegó (el proveedor deduplica): una carta en ambos casos.
3. **Dos organizaciones, mismo expediente**: org A y B con expediente 123 → filas y keys distintas (`A/123`, `B/123`); cada una imprime exactamente una vez; verificar además que la serialización canónica evita colisiones por separadores (org `a:1` + expediente `2` frente a org `a` + expediente `1:2`), p. ej. con longitudes fijas o hash de campos normalizados.

No se inventan endpoints: nunca se consulta al proveedor; el timeout se trata siempre como resultado desconocido, jamás como fallo.