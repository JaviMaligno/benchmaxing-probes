Hay \(2\cdot 11\cdot 10=220\) puertas en total.

Las celdas con número impar de puertas son las \(36\) celdas del borde que no son esquinas: cada una tiene \(3\) puertas. En un recorrido cerrado sin repetir puertas, cada celda usada debe tener un número par de puertas recorridas, así que en cada una de esas \(36\) celdas al menos una puerta debe quedar sin usar.

En cada lado hay \(9\) de esas celdas. Para que sus paridades queden correctas, en cada lado deben quedar sin usar al menos \(5\) puertas (el mínimo se logra dejando sin usar \(4\) puertas entre pares consecutivos de esas celdas y \(1\) puerta que va hacia una esquina). Como hay \(4\) lados, quedan sin usar al menos

\[
4\cdot 5=20
\]

puertas. Por tanto, el máximo es a lo sumo

\[
220-20=200.
\]

Esta cota se puede alcanzar, y queda un subgrafo conexo con todos los grados pares, que admite un circuito euleriano.

\[
\boxed{200}
\]