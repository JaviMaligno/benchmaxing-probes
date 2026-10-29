

Modelamos la cuadrícula como un grafo: las celdas son vértices y las puertas son aristas. Hay

\[
11\cdot 10+11\cdot 10=220
\]

puertas en total.

Un recorrido cerrado que no repite puertas usa un conjunto de puertas tal que cada celda tiene grado par dentro de ese conjunto: cada vez que el recorrido entra a una celda, debe salir de ella, y en la celda inicial/final también se emparejan la primera salida y la última entrada.

**Cota superior.** Coloreamos la cuadrícula como un tablero de ajedrez, con las cuatro esquinas de color negro; esto es posible porque \(11\) es impar, así que todas las esquinas tienen el mismo color. En cada lado hay \(9\) celdas no esquina, alternando colores, y como las esquinas son negras, hay \(5\) celdas blancas no esquina por lado. En total hay

\[
4\cdot 5=20
\]

celdas blancas en el borde no esquina.

Cada una de esas \(20\) celdas tiene exactamente \(3\) puertas. Como su grado usado debe ser par, no puede usar sus \(3\) puertas; debe dejar al menos una puerta incidente sin usar. Además, estas \(20\) puertas sin usar son distintas, porque cada puerta une una celda blanca con una negra, y por tanto no puede incidir en dos de estas celdas blancas del borde. Así que al menos \(20\) puertas quedan sin usar:

\[
\text{máximo de puertas usadas}\le 220-20=200.
\]

**Construcción que alcanza 200.** Elegimos dos esquinas opuestas, por ejemplo la superior derecha y la inferior izquierda. Dejamos sin usar exactamente \(20\) puertas del borde: en los lados superior y derecho, omitimos la puerta del borde de cada celda blanca que apunta hacia la esquina superior derecha; en los lados inferior e izquierdo, omitimos la puerta del borde de cada celda blanca que apunta hacia la esquina inferior izquierda. Son \(5\) puertas por lado.

Entonces:

- cada celda blanca del borde pierde exactamente una puerta, quedando con grado \(2\);
- cada celda negra del borde no esquina pierde exactamente una puerta, quedando con grado \(2\);
- las dos esquinas elegidas pierden sus dos puertas, quedando con grado \(0\);
- las otras dos esquinas conservan sus dos puertas, quedando con grado \(2\);
- todas las celdas interiores conservan sus \(4\) puertas.

Por tanto, todas las puertas restantes forman una red conexa, salvo por las dos esquinas que quedaron aisladas sin puertas, y todos los grados son pares. Por el teorema de Euler, existe un recorrido cerrado que usa cada una de esas puertas exactamente una vez. Usa

\[
220-20=200
\]

puertas.

\[
\boxed{200}
\]