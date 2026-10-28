**Veredicto: la propuesta no cumple.** Acierta en usar `organization:case` como clave determinista (el código actual usa `attempt_uuid`, que cambia en cada reentrega y anula la deduplicación del proveedor). Pero falla en dos puntos:

1. El lease de 5 minutos no es mecanismo de corrección: que expire no significa que el titular murió (puede estar pausado indefinidamente). Solo sirve para reducir llamadas concurrentes.
2. El "riesgo inevitable tras seis horas" no es inevitable: la regla permite detener la automatización en casos inciertos. Aceptar duplicados rutinarios viola "como máximo una carta".

**Alternativa: máquina de estados persistente**

Tabla `receipts` con PK/UNIQUE `(organization, case)` y columnas `state ∈ {INTENT, DONE, REVIEW}`, `intent_at`.

- **Nuevo:** transacción que inserta `(org, case, INTENT, now)`. Si el INSERT tiene éxito, llamar `print("org:case", body)`. Con respuesta OK → `UPDATE state=DONE` y ack. Sin respuesta → dejar `INTENT` (nunca asumir que un timeout significa que no se imprimió).
- **Incierto (fila existe en INTENT):** decidir por edad. Si `now − intent_at < 5h` (6h menos margen), reenviar `print` con la misma clave: es seguro, porque si ya se aceptó el proveedor deduplica, y si nunca llegó, imprime una vez. Luego marcar DONE. Si edad ≥ 5h, no podemos distinguir "aceptada y ventana expirada" de "nunca enviada": transición a `REVIEW` y detener para revisión humana. Esto es exactamente el caso permitido por la regla.
- **Completado (DONE o REVIEW):** ack sin llamar al proveedor.

**Ventana entre estado y efecto externo:** se persiste `INTENT` *antes* de llamar a `print` (write-ahead del intento). Si el worker cae entre INSERT y envío, no hay duplicado; la reentrega de la cola encuentra `INTENT` joven y reenvía con la misma clave, recuperando la impresión. El orden inverso (imprimir y luego insertar) sería peor: una caída tras imprimir dejaría la DB sin rastro y el siguiente worker reimprimiría tras las 6h.

**Worker antiguo que reanuda:** antes de cada llamada a `print` debe releer su fila y comprobar `now < intent_at + 5h`; si no, abortar y pasar a REVIEW. Como nadie reenvía pasadas las 5h, el único riesgo residual es que el worker se pause *entre* esa comprobación y la llamada durante más de una hora, cruzando la frontera de 6h. Sin cercado en el proveedor ni transacción que abarque la llamada externa, ese riesgo es irreducible; el margen lo hace extremadamente improbable, a diferencia de la propuesta, que acepta duplicados en el flujo normal.

**Separación de garantías:** la prevención de duplicados la dan la clave determinista, el UNIQUE, la regla de 5h y el estado REVIEW. La garantía de impresión la dan las reentregas de la cola durante 48h (que reintentan todo INTENT joven) y la resolución humana de los REVIEW; ninguna carta se pierde silenciosamente, y las operaciones nuevas sin fallos imprimen sin fricción.

**Pruebas:**

1. **t+10h:** aceptación a las 10:00, respuesta perdida, fila en INTENT. Reentrega con edad 10h ≥ 5h → REVIEW, cero llamadas a `print`, cero duplicados.
2. **Caída antes del envío:** fila INTENT sin impresión. Reentrega a los minutos → edad < 5h → reenvía con la misma clave → exactamente una carta.
3. **Dos organizaciones, mismo expediente:** claves `org1:case` y `org2:case` distintas, dos filas, dos cartas; el UNIQUE compuesto no las confunde.