Vamos a resolver el problema paso a paso.

Buscamos el mayor entero \( n < 2010 \) tal que:

\[
n \equiv 5 \pmod 7
\]
\[
n \equiv 10 \pmod{11}
\]
\[
n \equiv 10 \pmod{13}
\]

Observamos que las dos últimas congruencias se pueden combinar usando el teorema chino del resto: como \( 11 \) y \( 13 \) son coprimos, tenemos

\[
n \equiv 10 \pmod{143}.
\]

Entonces \( n = 143k + 10 \). Sustituimos en la primera congruencia:

\[
143k + 10 \equiv 5 \pmod 7.
\]

Como \( 143 = 7 \cdot 20 + 3 \), queda

\[
3k + 10 \equiv 5 \pmod 7,
\]

es decir,

\[
3k \equiv -5 \equiv 2 \pmod 7.
\]

Buscamos el inverso de \( 3 \) módulo \( 7 \). Como \( 3 \cdot 5 = 15 \equiv 1 \pmod 7 \), el inverso es \( 5 \). Multiplicamos:

\[
k \equiv 2 \cdot 5 = 10 \equiv 3 \pmod 7.
\]

Así \( k = 7m + 3 \), y por tanto

\[
n = 143(7m + 3) + 10 = 1001m + 429 + 10 = 1001m + 439.
\]

Los números que cumplen las tres congruencias son

\[
n \equiv 439 \pmod{1001}.
\]

Queremos el mayor entero menor que \( 2010 \). Tomamos \( m \) tal que

\[
1001m + 439 < 2010.
\]

Probamos:

- Para \( m = 1 \): \( 1001 + 439 = 1440 \).
- Para \( m = 2 \): \( 2002 + 439 = 2441 \), que excede \( 2010 \).

Entonces el mayor valor con \( m = 1 \) es \( 1440 \), y no hay otro valor de la forma \( 1001m + 439 \) entre \( 1440 \) y \( 2010 \), porque el siguiente sería \( 2441 \).

Por lo tanto, la respuesta es

\[
\boxed{1440}
\]