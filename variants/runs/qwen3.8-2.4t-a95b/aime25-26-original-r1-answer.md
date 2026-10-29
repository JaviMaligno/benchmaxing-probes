

Numera los vértices del polígono como \(0,1,\dots,23\) en orden cíclico.

La longitud de un segmento entre dos vértices depende solo de la distancia cíclica

\[
d=\min(|i-j|,24-|i-j|),
\]

donde \(1\le d\le 12\). Como la longitud de la cuerda es

\[
2R\sin\left(\frac{d\pi}{24}\right),
\]

y esta función es estrictamente creciente para \(1\le d\le 12\), cada valor de \(d\) da una longitud distinta.

Para un \(d\) fijo, considera el grafo cuyos vértices son los del polígono y cuyas aristas unen vértices a distancia cíclica \(d\). Este grafo se descompone en ciclos según

\[
g=\gcd(24,d).
\]

Hay \(g\) componentes, cada una con \(24/g\) vértices.

- Si \(24/g\) es impar, no hay emparejamiento perfecto.
- Si \(24/g\) es par y mayor que \(2\), cada ciclo par tiene exactamente \(2\) emparejamientos perfectos, así que hay \(2^g\).
- Si \(d=12\), cada componente es una pareja de vértices opuestos, y solo hay \(1\) emparejamiento perfecto.

Contamos para cada \(d\):

\[
\begin{array}{c|c|c|c}
d & \gcd(24,d) & \text{tamaño de ciclo} & \text{número de formas} \\
\hline
1 & 1 & 24 & 2 \\
2 & 2 & 12 & 4 \\
3 & 3 & 8 & 8 \\
4 & 4 & 6 & 16 \\
5 & 1 & 24 & 2 \\
6 & 6 & 4 & 64 \\
7 & 1 & 24 & 2 \\
8 & 8 & 3 & 0 \\
9 & 3 & 8 & 8 \\
10 & 2 & 12 & 4 \\
11 & 1 & 24 & 2 \\
12 & 12 & 2 & 1
\end{array}
\]

Sumando:

\[
2+4+8+16+2+64+2+0+8+4+2+1=113.
\]

\[
\boxed{113}
\]