

Etiquetamos los vértices como \(0,1,\dots,23\) módulo \(24\).

La longitud de un segmento entre dos vértices depende únicamente de la distancia cíclica mínima

\[
d\in\{1,2,\dots,12\}.
\]

Para cada \(d\), contamos cuántos emparejamientos perfectos hay usando solo segmentos cuya distancia cíclica es \(d\), y luego sumamos.

Para \(1\le d\le 11\), cada vértice puede unirse a \(i+d\) o \(i-d\). El grafo resultante se descompone en

\[
\gcd(24,d)
\]

ciclos, cada uno de longitud

\[
\frac{24}{\gcd(24,d)}.
\]

Un ciclo de longitud par tiene exactamente \(2\) emparejamientos perfectos; uno de longitud impar tiene \(0\).

Para \(d=12\), cada vértice solo puede unirse con su opuesto, así que hay \(1\) emparejamiento.

Ahora calculamos:

\[
\begin{array}{c|c|c|c}
d & \gcd(24,d) & \text{longitud del ciclo} & \#\text{ de emparejamientos}\\
\hline
1 & 1 & 24 & 2\\
2 & 2 & 12 & 4\\
3 & 3 & 8 & 8\\
4 & 4 & 6 & 16\\
5 & 1 & 24 & 2\\
6 & 6 & 4 & 64\\
7 & 1 & 24 & 2\\
8 & 8 & 3 & 0\\
9 & 3 & 8 & 8\\
10 & 2 & 12 & 4\\
11 & 1 & 24 & 2\\
12 & - & - & 1
\end{array}
\]

Sumando:

\[
2+4+8+16+2+64+2+0+8+4+2+1=113.
\]

\[
\boxed{113}
\]