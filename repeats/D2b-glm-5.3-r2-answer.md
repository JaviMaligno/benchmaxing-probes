**No cumple.** El defecto no es solo el riesgo tras seis horas: ese riesgo es una decisión de diseño, y la regla prohíbe duplicados pero permite detener la automatización. Con el lease de cinco minutos, el escenario del enunciado produce justo el duplicado vedado: impresión aceptada a las 10:00, respuesta perdida, ningún recibo insertado; el lease expira; a t+10h cualquier worker reenvía y el proveedor, ya sin memoria, imprime otra vez. El lease clasifica como muerto a un worker solo pausado, y además toda la corrección recae en la memoria de 6h que el propio diseño descarta al vencer. El reenvío tardío no es inevitable: es evitable parando.

**Alternativa.** Tabla `letters` con UNIQUE(organización, expediente): `state` (NEW | SENT | CONFIRMED | REVIEW) y `sent_at`. La key del proveedor es `organization:case` — nunca `attempt_uuid` ni `message_uuid`, porque la reentrega cambia el attempt y la unidad de a-más-de-una-vez es el par. Transiciones por CAS transaccional.

Decisiones:
- **NEW**: en transacción, NEW→SENT con `sent_at=now()`, commitear, y solo entonces `print()`. Si el estado ya no es NEW, releer y no actuar por memoria propia.
- **Respuesta aceptada**: SENT→CONFIRMED, insertar recibo. **Timeout**: dejar SENT; no inferir si el efecto remoto ocurrió.
- **Reentrega con SENT** y `(now − sent_at) + margen < 6h`: reenviar; es idempotente por la memoria del proveedor. El margen cubre el desfase de relojes y que la ventana corre desde la primera *aceptación*, posterior al primer envío.
- **SENT con ventana agotada** (caso t+10h): SENT→REVIEW, detener automatización y avisar. Nunca reenviar.
- **CONFIRMED**: nada; el recibo es por par, no por mensaje.

**Ventana estado→efecto y worker antiguo**: por eso SENT se guarda *antes* del print, no después; el hueco «guardó SENT, murió antes o después de imprimir» es indistinguible y se resuelve con reenvío idempotente dentro de ventana o revisión fuera de ella. El worker viejo que reanuda no usa su memoria: cada acción relee la fila en transacción y su CAS falla si el estado cambió.

**Prevención ≠ garantía de impresión**: sin duplicados salen de los estados, la ventana y REVIEW. Que toda carta se imprima exige además las reentregas de la cola (48h) — que reprocesan NEW y reenvían SENT dentro de ventana — más alertas y cola humana para REVIEW. Seguro parando; completo solo con ese bucle.

**Pruebas**
1. *t+10h*: fila SENT con `sent_at`=10:00; reentrega a las 20:00 ⇒ transición a REVIEW y cero llamadas a `print`; el worker viejo reanuda, lee REVIEW, no imprime.
2. *Caída antes del envío*: NEW→SENT, kill previo al print; reentrega a +1h reenvía, acepta ⇒ CONFIRMED; exactamente una carta física. Es indistinguible de «murió tras imprimir», y ambos quedan bien por la idempotencia dentro de ventana.
3. *Dos organizaciones, mismo expediente*: filas (A,123) y (B,123) y claves distintas ⇒ ambas imprimen, ninguna bloquea a la otra.

El lease sobra: no aporta corrección (la aportan estados y ventana) y genera el reenvío prohibido.