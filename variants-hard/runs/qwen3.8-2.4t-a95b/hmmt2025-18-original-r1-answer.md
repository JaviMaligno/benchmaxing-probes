

Sea \(n=2025\). Tras \(s\) segundos, por inducción,

\[
a_i^{(s)}=\max\{a_{i-s}^{(0)},a_{i-s+1}^{(0)},\ldots,a_{i+s}^{(0)}\},
\]

con índices módulo \(2025\). Así, tras \(100\) segundos, cada número es el máximo de un bloque cíclico de longitud

\[
2\cdot 100+1=201.
\]

Como los valores iniciales son continuos e independientes, con probabilidad \(1\) todos son distintos. Por tanto, los valores distintos que quedan después de \(100\) segundos están en correspondencia biyectiva con los índices iniciales \(j\) tales que \(a_j\) es el máximo de algún bloque cíclico de longitud \(201\).

Fijemos un índice, digamos \(j=0\), y sea \(X=a_0\). Condicionado a \(X=x\), cada otro número es menor que \(x\) con probabilidad \(x\) y mayor que \(x\) con probabilidad \(1-x\), independientemente.

El valor \(a_0\) aparece después de \(100\) segundos si y solo si existe un bloque de longitud \(201\) que contenga la posición \(0\) y no contenga ningún valor mayor que \(x\). Si \(l\) y \(r\) son las distancias al valor mayor más cercano a la izquierda y a la derecha de \(0\), entonces el intervalo consecutivo sin valores mayores que contiene a \(0\) tiene longitud \(l+r-1\). La condición de fallo es

\[
l+r-1\le 200 \quad\Longleftrightarrow\quad l+r\le 201.
\]

Para \(l,r\ge 1\) con \(s=l+r\le 201\), la probabilidad condicional de que los mayores más cercanos estén exactamente a distancias \(l\) y \(r\) es

\[
x^{s-2}(1-x)^2,
\]

pues las \(s-2\) posiciones interiores deben ser menores que \(x\), y los dos extremos deben ser mayores. Hay \(s-1\) pares \((l,r)\) con suma \(s\). Integrando sobre \(x\sim \mathrm{Unif}[0,1]\),

\[
\mathbb{P}(\text{fallo})
=
\sum_{s=2}^{201} (s-1)\int_0^1 x^{s-2}(1-x)^2\,dx.
\]

La integral vale

\[
\int_0^1 x^{s-2}(1-x)^2\,dx
=
\frac{2}{(s-1)s(s+1)}.
\]

Por tanto,

\[
\mathbb{P}(\text{fallo})
=
\sum_{s=2}^{201}\frac{2}{s(s+1)}
=
2\sum_{s=2}^{201}\left(\frac1s-\frac1{s+1}\right)
=
2\left(\frac12-\frac1{202}\right)
=
\frac{100}{101}.
\]

Así,

\[
\mathbb{P}(a_0\text{ aparece})=1-\frac{100}{101}=\frac1{101}.
\]

Por linealidad de la esperanza, el número esperado de valores distintos es

\[
2025\cdot \frac1{101}=\frac{2025}{101}.
\]

\[
\boxed{\frac{2025}{101}}
\]