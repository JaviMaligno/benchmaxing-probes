Un número es divisible por \(22\) si y solo si es divisible por \(2\) y por \(11\).

- Para que sea divisible por \(2\), su última cifra debe ser par: \(2,4,6,8\).
- Para que sea divisible por \(11\), la suma alternada de sus cifras debe ser múltiplo de \(11\).

Sea \(S_o\) la suma de las cifras en posiciones impares y \(S_e\) la suma de las cifras en posiciones pares. Como se usan los dígitos \(1,2,\dots,8\),

\[
S_o+S_e=36.
\]

La condición de divisibilidad por \(11\) exige

\[
S_o-S_e\equiv 0 \pmod{11}.
\]

Además, \(S_o-S_e\) tiene la misma paridad que \(S_o+S_e=36\), así que es par. Los posibles múltiplos de \(11\) en el rango de \(S_o-S_e\) son \(-11,0,11\), y el único par es \(0\). Por lo tanto,

\[
S_o=S_e=18.
\]

Los subconjuntos de \(4\) dígitos cuya suma es \(18\) son exactamente \(8\):

\[
\{1,2,7,8\},\{1,3,6,8\},\{1,4,5,8\},\{1,4,6,7\},
\]
\[
\{2,3,5,8\},\{2,3,6,7\},\{2,4,5,7\},\{3,4,5,6\}.
\]

Para cada uno de ellos, los otros \(4\) dígitos van en posiciones pares. En cada complemento hay exactamente \(2\) dígitos pares, así que la última cifra puede elegirse de \(2\) formas.

Para cada subconjunto:

\[
4!\cdot 2\cdot 3! = 24\cdot 2\cdot 6 = 288.
\]

Por tanto,

\[
N=8\cdot 288=2304.
\]

Finalmente,

\[
N-2025=2304-2025=279.
\]

\[
\boxed{279}
\]