

Numeremos las celdas como \((f,c)\), donde \(f\) es la fila y \(c\) la columna, con la casilla inicial \((1,1)\).

Un movimiento permitido va desde \((f,c)\) hasta una celda que comparta al menos un vértice con ella, pero no en la misma columna. Por tanto, el movimiento siempre cambia la columna en \(1\), y la fila puede cambiar en \(-1,0\) o \(+1\). Es decir, cada movimiento cambia la paridad de la columna.

En una cuadrícula \(7\times 7\):

- Columnas impares: \(1,3,5,7\), con \(4\cdot 7=28\) celdas.
- Columnas pares: \(2,4,6\), con \(3\cdot 7=21\) celdas.

Como la casilla inicial está en una columna impar y cada movimiento cambia la paridad de la columna, cualquier recorrido alterna entre columnas impares y pares. Si visita \(e\) celdas de columnas pares, puede visitar a lo sumo \(e+1\) celdas de columnas impares. Como solo hay \(21\) celdas pares,

\[
\text{longitud máxima} \le 21+(21+1)=43.
\]

Ahora mostramos que \(43\) sí es posible. Un recorrido válido es:

\[
(1,1)
\]

luego bajar alternando las columnas \(2\) y \(3\):

\[
(1,2),(1,3),(2,2),(2,3),\dots,(7,2),(7,3),
\]

pasar a la columna \(4\) y subir alternando las columnas \(4\) y \(5\):

\[
(7,4),(7,5),(6,4),(6,5),\dots,(1,4),(1,5),
\]

pasar a la columna \(6\) y bajar alternando las columnas \(6\) y \(7\):

\[
(1,6),(1,7),(2,6),(2,7),\dots,(7,6),(7,7).
\]

Este recorrido visita todas las celdas de las columnas \(2,3,4,5,6,7\), más la celda inicial \((1,1)\), sin repetir ninguna:

\[
1+14+14+14=43.
\]

Por tanto, el máximo número de celdas visitables es

\[
\boxed{43}
\]