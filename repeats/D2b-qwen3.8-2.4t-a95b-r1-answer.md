

**¿Cumple la propuesta? No.** Dos defectos la invalidan:

1. Usa `attempt_uuid` como key del proveedor, pero la reentrega trae un `attempt_uuid` nuevo: el `print` externo no deduplica nada entre intentos. La key estable es `message_uuid`.
2. El lease de 5 minutos con reenvío automático al expirar no cerca al worker viejo (no hay fencing del proveedor): si el worker antiguo se reanuda tras perder la respuesta, puede imprimir de nuevo. Hasta t+6h el proveedor deduplicaría por la key estable, pero **a t+10h la ventana de 6h ya pasó** y el reenvío ciego produce un duplicado real. Ese riesgo no es "inevitable y aceptable": es evitable deteniendo la automatización, que el enunciado permite explícitamente.

**Alternativa: máquina de estados durable.**

Tabla `recibos`, clave compuesta `(organization, case)` con UNIQUE, columnas: `estado ∈ {sending, completado, incierto}`, `provider_key = message_uuid`, `lease_expires`, `ultimo_attempt_uuid`.

Regla de oro: **el efecto externo solo se emite si la DB dice `sending` y este worker posee el lease; toda ambigüedad posterior termina en `incierto`, nunca en reenvío ciego.**

**Decisiones:**

- **Nuevo:** transacción `INSERT ... ON CONFLICT DO NOTHING` con `estado=sending` y lease de 5 min. Si el insert gana → `print(message_uuid, body)`. Guardar la intención **antes** del efecto cierra la ventana: cualquier caída antes del envío deja rastro.
- **Existente `completado`:** no llamar a `print`; ack del mensaje.
- **Existente `incierto`:** no imprimir; dejar en revisión.
- **Existente `sending`:** lease vigente → no hacer nada (el dueño legítimo terminará o el mensaje se reentregará). Lease expirado:
  - Dentro de las 6h del proveedor → reenviar con la **misma** `provider_key`; el proveedor deduplica la aceptación de las 10:00.
  - Fuera de las 6h (caso t+10h) → `UPDATE estado=incierto` transaccional y alertar. Sin consulta al proveedor no se puede distinguir "aceptado y confirmación perdida" de "nunca enviado"; se elige no duplicar.
- **Tras la llamada:** OK explícito → `completado`. Error explícito del proveedor → `incierto` con motivo. Timeout/error de red → conservar `sending` y dejar que el lease expire: el outcome es desconocido y **ese worker no reintenta**; el siguiente evento aplica la rama de lease expirado.

**Reanudación del worker antiguo:** si recibe una respuesta tardía, la aplica solo con `UPDATE ... WHERE lease aún es suyo`; si la fila ya cambió, descarta la respuesta sin reenviar. Si perdió la respuesta, se marca `incierto` a sí mismo. Nunca reintenta tras incertidumbre.

**Separación de garantías:**

- *No duplicar:* UNIQUE compuesto + key estable del proveedor + prohibición de reenviar fuera de la ventana de deduplicación + incertidumbre → humano.
- *Toda carta se imprime:* no es automática al 100%. La completitud la da un monitor: lease expirado sin `completado` → alerta; cola `incierto` → revisión humana que imprime manualmente o cierra.

**Pruebas:**

1. **t+10h:** simular aceptación 10:00 con respuesta perdida; reentrega a t+10h. Esperado: fila `sending` con lease expirado, fuera de ventana → **ninguna segunda llamada a `print`**, estado `incierto`, alerta emitida. Variante: worker viejo se reanuda con OK → `UPDATE` con check de lease falla o actualiza a `completado`; jamás segundo `print`.
2. **Caída antes del envío:** matar el worker tras el insert y antes de `print`. Esperado: `print` no invocado ni una vez; lease expira; reentrega dentro de 6h reintenta con la misma key e imprime exactamente una vez; caída repetida fuera de 6h → `incierto` sin duplicado.
3. **Dos organizaciones, mismo expediente:** mismos `case`, distinta `org`. Esperado: dos filas (el UNIQUE compuesto lo permite), dos llamadas a `print` con `provider_key` distintas que incluyan la organización, cada una termina en `completado` sin interferir.

En ningún punto se asume que un timeout implica que el trabajo remoto no se hizo: el timeout se trata siempre como desconocido.