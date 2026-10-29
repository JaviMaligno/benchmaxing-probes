Un subconjunto válido equivale a una cadena binaria de 17 asientos con exactamente 9 asientos ocupados y 8 vacíos, donde ningún asiento ocupado tiene vecinos ocupados a ambos lados. Es decir, no puede haber tres asientos ocupados consecutivos.

Separamos los 9 asientos ocupados en bloques consecutivos. Como no puede haber bloques de longitud 3 o más, cada bloque tiene tamaño 1 o 2.

Sea $k$ el número de bloques. Entonces $5 \le k \le 9$.

Si hay $9-k$ bloques de tamaño 2 y $2k-9$ bloques de tamaño 1, el número de formas de ordenarlos es

\[
\binom{k}{9-k}.
\]

Los 8 asientos vacíos deben incluir al menos uno entre cada par de bloques, usando $k-1$ vacíos. Quedan

\[
8-(k-1)=9-k
\]

vacíos extra para distribuir entre los $k+1$ espacios: antes del primer bloque, entre bloques y después del último. Esto da

\[
\binom{9}{k}
\]

formas.

Por lo tanto,

\[
N=\sum_{k=5}^{9} \binom{k}{9-k}\binom{9}{k}.
\]

Calculamos:

\[
\begin{array}{c|c|c|c}
k & \binom{k}{9-k} & \binom{9}{k} & \text{producto}\\
\hline
5 & 5 & 126 & 630\\
6 & 20 & 84 & 1680\\
7 & 21 & 36 & 756\\
8 & 8 & 9 & 72\\
9 & 1 & 1 & 1
\end{array}
\]

Así,

\[
N=630+1680+756+72+1=3139.
\]

El resto al dividir entre 1000 es

\[
\boxed{139}
\]