Sea \(n\) el número de monedas en cada una de las nueve bolsas originales.

Antes de encontrar la bolsa extra tenías \(9n\) monedas. Después de añadirla, tienes:

\[
9n+47
\]

Para poder repartir todas las monedas en 10 bolsas con la misma cantidad, ese total debe ser divisible entre 10:

\[
9n+47 \equiv 0 \pmod{10}
\]

Como \(47 \equiv 7 \pmod{10}\) y \(9 \equiv -1 \pmod{10}\):

\[
-n+7 \equiv 0 \pmod{10}
\]

\[
n \equiv 7 \pmod{10}
\]

Además, el total debe ser mayor que 300:

\[
9n+47>300
\]

\[
9n>253
\]

\[
n>28.11\ldots
\]

Los valores posibles de \(n\) son \(7,17,27,37,\dots\), pero debe ser mayor que \(28.11\), así que el menor es:

\[
n=37
\]

Antes de encontrar la bolsa tenías:

\[
9\cdot 37=333
\]

\[
\boxed{333}
\]