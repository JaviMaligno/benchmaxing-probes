

Sea \(g=\gcd(a,b)=210\). Escribimos

\[
a=210x,\qquad b=210y,
\]

con \(\gcd(x,y)=1\). Como \(a<b\), también \(x<y\).

Sabemos que

\[
\operatorname{lcm}(a,b)=\frac{ab}{\gcd(a,b)}=210xy.
\]

Dado que \(\operatorname{lcm}(a,b)=210^3\), tenemos

\[
210xy=210^3 \implies xy=210^2.
\]

Ahora factorizamos:

\[
210=2\cdot 3\cdot 5\cdot 7,
\]

por lo que

\[
210^2=2^2\cdot 3^2\cdot 5^2\cdot 7^2.
\]

Como \(\gcd(x,y)=1\), cada factor primo al cuadrado debe ir completo a \(x\) o completo a \(y\). Hay \(4\) primos, así que hay

\[
2^4=16
\]

formas de asignarlos entre \(x\) y \(y\).

Ninguna de estas asignaciones tiene \(x=y\), porque eso implicaría \(\gcd(x,y)>1\) o una división igual de los factores, imposible con \(\gcd(x,y)=1\). Por simetría, exactamente la mitad cumple \(x<y\):

\[
\frac{16}{2}=8.
\]

Cada valor de \(x\) da un único valor de \(a=210x\). Por lo tanto, hay

\[
\boxed{8}
\]