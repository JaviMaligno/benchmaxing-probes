

**¿Cumple la propuesta?** No. Acierta en la clave estable `org:case` y en el UNIQUE compuesto, pero falla en lo esencial:

- Expirar el lease y reenviar trata el resultado desconocido como «no se hizo», justo lo prohibido: un timeout no demuestra que la impresión no ocurriese.
- No se puede cercar al worker pausado: si el lease expira y otro worker reenvía, el antiguo puede despertar y reenviar también. Dentro de 6h la clave externa deduplica; después, duplicado real.
- El riesgo tras 6h **no es inevitable**: nace de no persistir el intento antes del efecto y de reintentar lo incierto. La regla permite expresamente detenerse en casos inciertos.

**Alternativa** — tabla `cartas(org_id, case_id, estado, token, intento_ts, recibo)` con UNIQUE(org_id, case_id). Decisiones al llegar un mensaje:

- **Sin fila (nuevo)**: una transacción inserta `estado=intentando, token=uuid`. El perdedor del UNIQUE relee y se inhibe. Solo quien gana esa inserción queda autorizado a llamar a `print(key="org:case", body)`.
- **`intentando` reciente**: otro worker es dueño; inhibirse sin imprimir.
- **`intentando` viejo (incierto)**: no imprimir; enviar a revisión.
- **`completado`**: no-op idempotente, ack.
- **Fallo definitivo** (rechazo explícito, no timeout): se sabe que no se imprimió → reintentar con nuevo token hasta un máximo; luego, revisión.

Transiciones: éxito confirmado → `UPDATE estado=completado, recibo WHERE token=el_mío`. Timeout o respuesta perdida → el estado sigue `intentando`; nunca se reenvía automáticamente.

**Ventana estado→efecto**: el intento se persiste *antes* de llamar a `print`. Caer en esa ventana deja `intentando` sin confirmación → revisión. Es el único sesgo seguro: puede mandar a revisión una carta que no llegó a imprimirse, jamás duplica. El error simétrico sería marcar `completado` sin confirmación: cartas que nadie imprime.

**Worker antiguo reanudado**: la autorización de imprimir no la da un lease temporal, sino haber ganado la inserción `nuevo→intentando`. Todo proceso reanudado relee el estado en vez de ejecutar una intención caducada, y toda escritura exige su token, por lo que no puede pisar `completado`. Un worker pausado entre la inserción y la llamada que despierta 20h después e imprime no duplica: nadie más imprimió, porque todos vieron `intentando` y pararon.

**Prevención ≠ cobertura**: la prevención de duplicados viene del UNIQUE, la clave externa estable, persistir el intento y no reintentar lo incierto; no depende de la ventana de 6h. La garantía de que toda carta se imprima es vivacidad: la cola reentrega ante fallos definitivos; los casos inciertos los cierra revisión (el humano es el único fence posible: el proveedor no ofrece consulta ni cancelación).

**Pruebas**:

1. **t+10h**: a las 10:00 `print` acepta y se pierde la respuesta; el worker queda pausado. Reentrega a las 20:00: lee `intentando` viejo → revisión, cero llamadas a `print`. El worker viejo despierta a las 20:30: relee, su token ya no autoriza → no imprime. Aserciones: `print` invocado exactamente una vez en total; ninguna llamada después de las 16:00.
2. **Caída antes del envío**: inserta `intentando` y muere antes de `print()`. Reentrega → revisión. Aserciones: cero impresiones; revisión autoriza la impresión (nada fue aceptado) y termina `completado`.
3. **Dos organizaciones, mismo expediente**: (orgA, X) y (orgB, X) concurrentes. Ambas inserciones caben en el UNIQUE compuesto; claves externas distintas → una impresión por organización, dos recibos. Aserciones: ninguna violación de UNIQUE bloquea a la segunda; la reentrega de cualquiera es no-op.