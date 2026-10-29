Como \(675=3^3\cdot 5^2\), tiene \((3+1)(2+1)=12\) divisores. Por tanto, hay \(2^{12}=4096\) subconjuntos posibles.

Para que el mínimo común múltiplo sea \(675\), el subconjunto debe contener:
- algún divisor con exponente \(3\) en el factor \(3\);
- algún divisor con exponente \(2\) en el factor \(5\).

Usamos inclusión-exclusión:
- Subconjuntos sin exponente \(3\) en el factor \(3\): sus elementos dividen a \(225=3^2\cdot5^2\), que tiene \(9\) divisores. Hay \(2^9=512\).
- Subconjuntos sin exponente \(2\) en el factor \(5\): sus elementos dividen a \(135=3^3\cdot5\), que tiene \(8\) divisores. Hay \(2^8=256\).
- Subconjuntos con ambas restricciones: sus elementos dividen a \(45=3^2\cdot5\), que tiene \(6\) divisores. Hay \(2^6=64\).

Así, el número de subconjuntos favorables es
\[
4096-512-256+64=3392.
\]
Todos son no vacíos, y la probabilidad es
\[
\frac{3392}{4096}=\frac{53}{64}.
\]
Por consiguiente, \(m+n=53+64\), de donde obtenemos

\[
\boxed{117}
\]