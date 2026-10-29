

Sea \(x\) el número de monedas que había en cada una de las 9 bolsas.

Antes de encontrar la bolsa extra, tenías:

\[
9x
\]

Después de encontrar la bolsa con 47 monedas, el total es:

\[
9x + 47
\]

Como luego repartes todas las monedas en 10 bolsas iguales, el total debe ser divisible entre 10:

\[
9x + 47 \equiv 0 \pmod{10}
\]

Como \(47 \equiv 7 \pmod{10}\),

\[
9x + 7 \equiv 0 \pmod{10}
\]

\[
9x \equiv 3 \pmod{10}
\]

Como \(9 \equiv -1 \pmod{10}\),

\[
-x \equiv 3 \pmod{10}
\]

\[
x \equiv 7 \pmod{10}
\]

Además, después de encontrar la bolsa tienes más de 300 monedas:

\[
9x + 47 > 300
\]

\[
9x > 253
\]

Los valores posibles de \(x\) terminan en 7: \(7, 17, 27, 37, \dots\)

Probamos:

- Si \(x = 27\), entonces \(9x = 243\), y el total sería \(243 + 47 = 290\), que no es mayor que 300.
- Si \(x = 37\), entonces \(9x = 333\), y el total sería \(333 + 47 = 380\), que sí es mayor que 300 y divisible entre 10.

Por lo tanto, el menor número de monedas que podías haber tenido antes es:

\[
\boxed{333}
\]