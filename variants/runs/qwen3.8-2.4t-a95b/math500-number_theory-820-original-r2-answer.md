

Sea \(g=\gcd(a,b)=210\). Entonces podemos escribir

\[
a=210x,\qquad b=210y
\]

con \(\gcd(x,y)=1\).

Como

\[
\operatorname{lcm}(a,b)=210xy
\]

cuando \(\gcd(x,y)=1\), la condición \(\operatorname{lcm}(a,b)=210^3\) implica

\[
210xy=210^3 \quad\Longrightarrow\quad xy=210^2.
\]

Factorizando:

\[
210=2\cdot 3\cdot 5\cdot 7,
\]

así que

\[
210^2=2^2\cdot 3^2\cdot 5^2\cdot 7^2.
\]

Como \(x\) y \(y\) son coprimos, cada bloque \(p^2\) debe ir completo a uno de los dos números. Para cada uno de los 4 primos hay 2 elecciones, así que hay

\[
2^4=16
\]

pares ordenados \((x,y)\).

La condición \(a<b\) equivale a \(x<y\). Como no puede haber empate \(x=y\) (sería incompatible con \(\gcd(x,y)=1\) y \(xy=210^2\)), exactamente la mitad de los pares cumplen \(x<y\). Por tanto,

\[
\frac{16}{2}=8.
\]

\[
\boxed{8}
\]