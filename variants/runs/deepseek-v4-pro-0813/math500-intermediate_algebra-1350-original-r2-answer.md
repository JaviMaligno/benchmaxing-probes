**Idea clave:** Al factorizar, si las raíces son enteros distintos \(r_1,r_2,\dots,r_n\), entonces

\[
f(x)=2(x-r_1)(x-r_2)\cdots(x-r_n),
\]

por lo que

\[
a_0=2(-1)^n r_1r_2\cdots r_n=66,
\]

es decir,

\[
r_1r_2\cdots r_n=33(-1)^n.
\]

Además,

\[
a_{n-1}=-2(r_1+r_2+\cdots+r_n),
\]

así que debemos minimizar \(|\text{suma de raíces}|\).

Como el producto de las raíces en valor absoluto es \(33=3\cdot 11\), las raíces solo pueden tener valores absolutos \(1,3,11,33\), y a lo sumo podemos usar dos raíces con valor absoluto \(1\) (los enteros \(1\) y \(-1\)). Por tanto, \(n\le 4\).

Enumeramos las posibilidades con menor \(|\text{suma}|\):

- \(n=3\), raíces \(\{1,3,-11\}\): producto \(-33\), que corresponde a \(33(-1)^3\), y suma \(-7\).
- \(n=4\), raíces \(\{11,-3,1,-1\}\): producto \(33\), suma \(8\).
- \(n=2\), la mejor opción \(\{3,11\}\) da suma \(14\).

La menor suma en valor absoluto es \(7\), lograda con \(\{1,3,-11\}\). Entonces

\[
a_{n-1}=-2(1+3-11)=-2(-7)=14,
\]

y

\[
|a_{n-1}|=14.
\]

Verificando: \(f(x)=2(x-1)(x-3)(x+11)=2x^3+14x^2-82x+66\), que tiene \(a_3=2\), \(a_0=66\) y raíces enteras distintas \(1,3,-11\).

\[
\boxed{14}
\]