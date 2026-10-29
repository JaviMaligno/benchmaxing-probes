Numera las filas y columnas de \(1\) a \(9\). La celda inicial es \((1,1)\).

1. **Movimiento posible.** Desde \((r,c)\), una celda que comparte vértice está en una fila y columna que difieren a lo más en \(1\). Como se prohíbe la misma columna, todo movimiento cambia la columna exactamente en \(1\). Por lo tanto, cada movimiento alterna entre columnas impares y pares.

2. **Cota superior.** Hay \(5\) columnas impares y \(4\) columnas pares, así que hay:
\[
5\cdot 9=45 \text{ celdas en columnas impares},\qquad 4\cdot 9=36 \text{ celdas en columnas pares}.
\]
El recorrido empieza en una columna impar y alterna paridades. Si visita \(e\) celdas de columnas pares, puede visitar a lo más \(e+1\) celdas de columnas impares. Como \(e\le 36\), el total es a lo más
\[
36+37=73.
\]

3. **Construcción con \(73\) celdas.** Recorre las columnas por pares en zigzag:
\[
(1,1),(1,2),(2,1),(2,2),\ldots,(9,1),(9,2),
\]
\[
(9,3),(9,4),(8,3),(8,4),\ldots,(1,3),(1,4),
\]
\[
(1,5),(1,6),(2,5),(2,6),\ldots,(9,5),(9,6),
\]
\[
(9,7),(9,8),(8,7),(8,8),\ldots,(1,7),(1,8),(1,9).
\]
Esto visita \(4\cdot 18+1=73\) celdas distintas, con movimientos válidos.

\[
\boxed{73}
\]