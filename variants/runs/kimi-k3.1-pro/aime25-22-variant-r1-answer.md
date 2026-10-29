Factorizamos \(675=3^3\cdot 5^2\). Sus divisores tienen la forma \(3^a5^b\), con \(0\le a\le3\) y \(0\le b\le2\), así que hay \(4\cdot3=12\) divisores y \(2^{12}\) subconjuntos posibles.

Para que el mínimo común múltiplo sea \(675\), el subconjunto debe contener:
- al menos un divisor con \(a=3\);
- al menos un divisor con \(b=2\).

Estas condiciones ya garantizan que sea no vacío. Por inclusión-exclusión, el número de subconjuntos válidos es
\[
2^{12}-2^9-2^8+2^6=3392,
\]
donde se restan los subconjuntos sin exponente \(a=3\) o sin \(b=2\), y se suman los que carecen de ambos.

Por tanto, la probabilidad es
\[
\frac{3392}{4096}=\frac{53}{64}.
\]
Así, \(m+n=53+64\), y la respuesta es

\[
\boxed{117}
\]