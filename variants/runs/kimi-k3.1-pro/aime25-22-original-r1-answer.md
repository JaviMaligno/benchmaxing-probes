Factorizamos \(2025=3^4\cdot 5^2\). Sus divisores son de la forma \(3^a5^b\), con \(0\le a\le4\) y \(0\le b\le2\), así que \(A\) tiene \(5\cdot3=15\) elementos y hay \(2^{15}\) subconjuntos posibles.

Para que el mínimo común múltiplo sea \(2025\), el subconjunto debe contener:
- al menos un divisor con \(a=4\);
- al menos un divisor con \(b=2\).

Por inclusión-exclusión, el número de subconjuntos válidos es
\[
2^{15}-2^{12}-2^{10}+2^8=27904.
\]
Aquí, \(2^{12}\) cuenta los subconjuntos sin ningún divisor con \(a=4\), y \(2^{10}\), los que no tienen ninguno con \(b=2\). Todo subconjunto válido es automáticamente no vacío.

Por tanto, la probabilidad es
\[
\frac{27904}{32768}=\frac{109}{128}.
\]
Como \(109\) y \(128\) son coprimos, \(m+n=109+128\).

\[
\boxed{237}
\]