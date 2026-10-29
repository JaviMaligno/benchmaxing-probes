Sea \(n\) el número de monedas en cada una de las siete bolsas originales. Antes de encontrar la bolsa adicional, tenías \(7n\) monedas.

Después de encontrar las 53 monedas, el total debe dividirse equitativamente entre ocho bolsas:
\[
7n+53\equiv 0\pmod 8.
\]
Como \(7\equiv -1\pmod 8\) y \(53\equiv 5\pmod 8\):
\[
-n+5\equiv 0\pmod 8
\quad\Longrightarrow\quad
n\equiv 5\pmod 8.
\]

Además, el total debe ser mayor que 200:
\[
7n+53>200
\quad\Longrightarrow\quad
n>21.
\]
El menor valor de \(n\) mayor que 21 y congruente con \(5\) módulo \(8\) es \(n=29\).

Así, inicialmente tenías \(7\cdot29=203\) monedas. Al añadir 53, obtienes 256, que se reparten como 32 monedas en cada una de las ocho bolsas.

\[
\boxed{203}
\]