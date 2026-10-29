

Sea \(g=\gcd(m,n)=2310\). Escribimos

\[
m=ga,\qquad n=gb,
\]

con \(\gcd(a,b)=1\). Como

\[
\operatorname{lcm}(m,n)=gab=2310^3=g^3,
\]

se tiene

\[
ab=g^2.
\]

Ahora

\[
2310=2\cdot 3\cdot 5\cdot 7\cdot 11,
\]

así que

\[
g^2=2^2\cdot 3^2\cdot 5^2\cdot 7^2\cdot 11^2.
\]

Como \(\gcd(a,b)=1\), cada factor primo al cuadrado debe ir completo a \(a\) o completo a \(b\). Hay \(5\) primos, por lo que hay

\[
2^5=32
\]

formas de asignar los factores a \((a,b)\).

Cada asignación produce un par ordenado \((m,n)\) con \(m\neq n\), y exactamente la mitad cumple \(m<n\). Por tanto, el número de valores posibles de \(m\) es

\[
\frac{32}{2}=16.
\]

\[
\boxed{16}
\]