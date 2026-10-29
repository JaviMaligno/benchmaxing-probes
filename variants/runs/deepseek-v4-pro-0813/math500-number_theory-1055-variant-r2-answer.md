**Razonamiento:**

Sea \( x \) el número de monedas que tenías antes de encontrar la bolsa de 47 monedas, y \( t \) el número de monedas en cada bolsa tras la redistribución. Como todo queda repartido en 10 bolsas iguales, se cumple:

\[
x + 47 = 10t
\]

Además, sabemos que \( x > 300 \) (pues tras encontrar la bolsa tienes más de 300 monedas, y antes tenías \( x > 300 - 47 \)).

En realidad, la condición es que **después** de encontrar la bolsa tienes más de 300 monedas:

\[
x + 47 > 300
\]

Es decir:

\[
x > 253
\]

Buscamos el menor \( x > 253 \) tal que \( x + 47 \) sea múltiplo de 10.

\[
x + 47 \equiv 0 \pmod{10}
\]

Como \( 47 \equiv 7 \pmod{10} \):

\[
x + 7 \equiv 0 \pmod{10}
\]

\[
x \equiv 3 \pmod{10}
\]

El menor \( x > 253 \) congruente con \( 3 \pmod{10} \) es \( 263 \), porque \( 253 \equiv 3 \pmod{10} \) y el siguiente es \( 263 \).

Verificación: \( 263 + 47 = 310 = 10 \times 31 \), y \( 310 > 300 \).

\[
\boxed{263}
\]