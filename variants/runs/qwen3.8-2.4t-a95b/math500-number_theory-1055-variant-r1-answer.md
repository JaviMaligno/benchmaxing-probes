

Sea \(n\) el número de monedas que había inicialmente en cada una de las 9 bolsas. Entonces el número total inicial era \(9n\).

Al encontrar una bolsa con 47 monedas, el total pasa a ser:

\[
9n + 47
\]

Como luego se reparten equitativamente entre 10 bolsas, este total debe ser divisible entre 10:

\[
9n + 47 \equiv 0 \pmod{10}
\]

Como \(9 \equiv -1 \pmod{10}\) y \(47 \equiv 7 \pmod{10}\):

\[
-n + 7 \equiv 0 \pmod{10}
\]

\[
n \equiv 7 \pmod{10}
\]

Además, el total después de encontrar la bolsa es mayor que 300:

\[
9n + 47 > 300
\]

\[
9n > 253
\]

\[
n > 28.1
\]

El menor entero \(n\) mayor que \(28.1\) y congruente con \(7 \pmod{10}\) es:

\[
n = 37
\]

Por tanto, el número inicial de monedas era:

\[
9 \times 37 = 333
\]

\[
\boxed{333}
\]