

La condición “ningún invitado está sentado junto a otros dos invitados” significa que no puede haber tres asientos ocupados consecutivos. Así, contamos cadenas binarias de longitud 17 con exactamente nueve unos y sin tres unos seguidos.

Los nueve asientos ocupados deben dividirse en bloques consecutivos de longitud 1 o 2. Sea \(r\) el número de bloques.

- Como cada bloque tiene a lo más 2 asientos ocupados, se necesita \(r \ge \lceil 9/2\rceil = 5\).
- Como hay 8 asientos vacíos y se necesita al menos uno entre bloques consecutivos, \(r-1 \le 8\), así que \(r \le 9\).

Para un \(r\) fijo:

1. Elegir las longitudes de los bloques: cada bloque aporta 1 o 2, y la suma debe ser 9. Si hay \(9-r\) bloques de longitud 2, el número de formas es
   \[
   \binom{r}{9-r}.
   \]

2. Distribuir los 8 asientos vacíos en los \(r+1\) espacios alrededor y entre bloques, con al menos un vacío entre bloques. Tras colocar un vacío en cada uno de los \(r-1\) espacios interiores, quedan
   \[
   8-(r-1)=9-r
   \]
   vacíos por distribuir libremente en \(r+1\) espacios. Esto da
   \[
   \binom{(9-r)+(r+1)-1}{(r+1)-1}=\binom{9}{r}.
   \]

Por tanto,
\[
N=\sum_{r=5}^{9}\binom{r}{9-r}\binom{9}{r}.
\]

Calculamos:

\[
\begin{aligned}
r=5 &: \binom{5}{4}\binom{9}{5}=5\cdot126=630,\\
r=6 &: \binom{6}{3}\binom{9}{6}=20\cdot84=1680,\\
r=7 &: \binom{7}{2}\binom{9}{7}=21\cdot36=756,\\
r=8 &: \binom{8}{1}\binom{9}{8}=8\cdot9=72,\\
r=9 &: \binom{9}{0}\binom{9}{9}=1\cdot1=1.
\end{aligned}
\]

Sumando,

\[
N=630+1680+756+72+1=3139.
\]

El residuo de \(3139\) módulo \(1000\) es

\[
\boxed{139}
\]