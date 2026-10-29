

Factorizamos:

\[
2025=45^2=(3^2\cdot 5)^2=3^4\cdot 5^2.
\]

Los divisores de \(2025\) tienen la forma \(3^a5^b\), con \(0\le a\le 4\) y \(0\le b\le 2\). Por tanto,

\[
|A|=(4+1)(2+1)=15.
\]

Hay \(2^{15}\) subconjuntos posibles de \(A\).

Queremos que el mínimo común múltiplo de los elementos de \(B\) sea \(2025=3^4\cdot 5^2\). Esto ocurre si y solo si entre los elementos de \(B\) aparece al menos un divisor con exponente \(a=4\) y al menos uno con exponente \(b=2\).

Contamos por inclusión-exclusión.

- Subconjuntos donde ningún elemento tiene \(a=4\): solo usan \(a\le 3\), así que hay \(4\cdot 3=12\) divisores posibles:

\[
2^{12}.
\]

- Subconjuntos donde ningún elemento tiene \(b=2\): solo usan \(b\le 1\), así que hay \(5\cdot 2=10\) divisores posibles:

\[
2^{10}.
\]

- Subconjuntos donde fallan ambas condiciones: \(a\le 3\) y \(b\le 1\), con \(4\cdot 2=8\) divisores posibles:

\[
2^8.
\]

Entonces el número de subconjuntos con \(\mathrm{lcm}(B)=2025\) es

\[
2^{15}-2^{12}-2^{10}+2^8.
\]

La probabilidad es

\[
\frac{2^{15}-2^{12}-2^{10}+2^8}{2^{15}}
=1-\frac{1}{2^3}-\frac{1}{2^5}+\frac{1}{2^7}.
\]

Simplificando:

\[
1-\frac{1}{8}-\frac{1}{32}+\frac{1}{128}
=\frac{128-16-4+1}{128}
=\frac{109}{128}.
\]

Así, \(m=109\) y \(n=128\), por lo que

\[
m+n=217.
\]

\[
\boxed{217}
\]