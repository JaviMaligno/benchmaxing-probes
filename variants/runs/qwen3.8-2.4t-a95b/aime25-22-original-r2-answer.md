

Factorizamos
\[
2025=81\cdot 25=3^4\cdot 5^2.
\]
Los divisores de \(2025\) son de la forma \(3^i5^j\), con \(0\le i\le 4\) y \(0\le j\le 2\). Por tanto,
\[
|A|=(4+1)(2+1)=15,
\]
y hay \(2^{15}\) subconjuntos posibles de \(A\).

Para que el mínimo común múltiplo de los elementos de \(B\) sea \(2025\), necesitamos que entre los divisores elegidos haya al menos uno con exponente máximo de \(3\), es decir \(i=4\), y al menos uno con exponente máximo de \(5\), es decir \(j=2\).

Contamos por inclusión-exclusión.

- Subconjuntos que no contienen ningún divisor con \(i=4\): hay \(4\cdot 3=12\) divisores posibles, así que hay \(2^{12}\).
- Subconjuntos que no contienen ningún divisor con \(j=2\): hay \(5\cdot 2=10\) divisores posibles, así que hay \(2^{10}\).
- Subconjuntos que no contienen ninguno con \(i=4\) ni con \(j=2\): hay \(4\cdot 2=8\) divisores posibles, así que hay \(2^8\).

Entonces el número de subconjuntos con \(\operatorname{lcm}=2025\) es
\[
2^{15}-2^{12}-2^{10}+2^8.
\]
La probabilidad es
\[
\frac{2^{15}-2^{12}-2^{10}+2^8}{2^{15}}
=1-\frac18-\frac1{32}+\frac1{128}
=\frac{128-16-4+1}{128}
=\frac{109}{128}.
\]
Así, \(m=109\) y \(n=128\), por lo que
\[
m+n=109+128=237.
\]

\[
\boxed{237}
\]