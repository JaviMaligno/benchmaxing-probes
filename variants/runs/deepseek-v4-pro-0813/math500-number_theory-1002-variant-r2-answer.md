El número buscado satisface:

- \(x \equiv 2 \pmod 7\)
- \(x \equiv 8 \pmod {11}\)
- \(x \equiv 8 \pmod {13}\)

Como \(11\) y \(13\) son coprimos, las dos últimas congruencias equivalen a:

\[
x \equiv 8 \pmod {143}
\]

Entonces \(x = 8 + 143k\), y debe cumplir:

\[
8 + 143k \equiv 2 \pmod 7
\]

\[
143 \equiv 3 \pmod 7,\quad 8 \equiv 1 \pmod 7
\]

\[
1 + 3k \equiv 2 \pmod 7
\]

\[
3k \equiv 1 \pmod 7
\]

El inverso de \(3\) módulo \(7\) es \(5\), pues \(3\cdot 5=15\equiv 1 \pmod 7\):

\[
k \equiv 5 \pmod 7
\]

Por tanto, las soluciones son:

\[
x = 8 + 143(5 + 7m) = 8 + 715 + 1001m = 723 + 1001m
\]

Buscamos el mayor \(x < 3000\):

\[
723 + 1001m < 3000
\]

\[
1001m < 2277
\]

\[
m \le 2
\]

Para \(m=2\):

\[
x = 723 + 2002 = 2725
\]

Verificación:

- \(2725 \div 7\): \(7\cdot 389 = 2723\), resto \(2\).
- \(2725 \div 11\): \(11\cdot 247 = 2717\), resto \(8\).
- \(2725 \div 13\): \(13\cdot 209 = 2717\), resto \(8\).

\[
\boxed{2725}
\]