No cumple. `organization:case` como clave estable y el `UNIQUE(organization, case)` evitan duplicados concurrentes durante seis horas, pero el lease de cinco minutos autoriza reenvíos. Tras esa ventana, tanto una reentrega como el worker antiguo pueden producir una segunda impresión. No es un riesgo inevitable: puede evitarse deteniendo los reintentos automáticos. Además, usar `attempt_uuid` en la implementación original es incorrecto porque cambia entre reentregas.

**Alternativa**

Tabla con `UNIQUE(organization, case)`, clave externa estable `organization:case` y estados `ENVIANDO`, `INCIERTO`, `COMPLETADO`. Cada registro admite como máximo una llamada a `print`; el lease, si se usa para supervisión, nunca concede permiso para reenviar.

- **Nuevo:** en una transacción local, insertar `ENVIANDO`. Solo el worker que ganó la inserción puede efectuar la única llamada `print(organization:case, body)`. Si recibe confirmación inequívoca de aceptación, actualiza a `COMPLETADO`. Sin fallos, la carta se imprime.
- **Incierto:** timeout, respuesta perdida, caída o pausa recuperable dejan el registro en `INCIERTO` —o `ENVIANDO`, interpretado como incierto al recuperar— y detienen esa carta para revisión. No se reenvía por haber expirado un lease ni por haber transcurrido seis horas. La revisión solo debe autorizar otro intento si existe certeza de que no hubo aceptación; si no, permanece detenida.
- **Completado:** no se vuelve a llamar a `print`; las reentregas se descartan.

La ventana entre persistir y emitir se resuelve **guardando antes la intención de un único envío**. Si se cae antes de llamar, queda un falso incierto que requiere revisión: es el precio permitido para no arriesgar duplicados. No se presume que el efecto no ocurrió.

Un worker antiguo no puede iniciar otro envío al reanudarse: su intento ya consumió la única llamada permitida. Solo puede terminar la actualización condicional de su propio registro; si la respuesta se perdió, no inventa un `COMPLETADO`. El fencing de DB no puede cercar al proveedor, por lo que no sustituye esta restricción.

**Pruebas**

1. **t+10h:** aceptación a las 10:00 y respuesta perdida; la reentrega no llama a `print`. Si despierta el worker viejo, tampoco reenvía. Permanece incierto hasta revisión.
2. **Caída antes del envío:** existe `ENVIANDO`, pero ninguna llamada llegó al servicio; la recuperación y las reentregas no imprimen automáticamente.
3. **Dos organizaciones, mismo expediente:** existen dos filas y dos claves distintas; se imprime una carta para cada organización.
4. **Workers concurrentes:** el perdedor del `UNIQUE` no imprime.

La prevención de duplicados es compatible con detener casos inciertos. Garantizar además que toda carta termine impresa es imposible con este endpoint ante respuestas perdidas: reintentar puede duplicar y no reintentar puede dejar una carta sin imprimir.