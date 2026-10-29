

Representamos los asientos ocupados como una cadena binaria de longitud 16 con exactamente ocho 1. La condición “ninguna persona se sienta junto a otras dos” equivale a no tener tres 1 consecutivos.

Los 1 ocupados se agrupan en bloques consecutivos de longitud 1 o 2. Sea \(a\) el número de bloques de longitud 2. Entonces hay \(8-2a\) bloques de longitud 1, y el número total de bloques es

\[
m=a+(8-2a)=8-a.
\]

Para cada \(a\):

- Ordenar los bloques: elegir cuáles de los \(m\) bloques son de longitud 2:

\[
\binom{8-a}{a}.
\]

- Hay 8 sillas vacías. Se necesita al menos una silla vacía entre bloques, usando \(m-1\). Quedan

\[
8-(m-1)=8-(7-a)=a+1
\]

sillas vacías extra, que se distribuyen en los \(m+1\) huecos posibles:

\[
\binom{(a+1)+(m+1)-1}{(m+1)-1}
=
\binom{9}{8-a}.
\]

Por tanto,

\[
N=\sum_{a=0}^{4} \binom{8-a}{a}\binom{9}{8-a}.
\]

Calculando:

\[
\begin{aligned}
a=0 &: \binom{8}{0}\binom{9}{8}=9,\\
a=1 &: \binom{7}{1}\binom{9}{7}=7\cdot36=252,\\
a=2 &: \binom{6}{2}\binom{9}{6}=15\cdot84=1260,\\
a=3 &: \binom{5}{3}\binom{9}{5}=10\cdot126=1260,\\
a=4 &: \binom{4}{4}\binom{9}{4}=1\cdot126=126.
\end{aligned}
\]

\[
N=9+252+1260+1260+126=2907.
\]

El residuo de \(2907\) entre \(1000\) es

\[
\boxed{907}
\]