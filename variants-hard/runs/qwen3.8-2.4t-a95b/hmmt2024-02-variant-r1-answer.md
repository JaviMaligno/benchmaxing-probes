

Sea \(S_P\) la suma de Priya y \(S_T\) la suma de Tomás.

Priya escribe todos los enteros de \(1\) a \(mn\), así que

\[
S_P=1+2+\cdots+mn=\frac{mn(mn+1)}{2}.
\]

Tomás escribe \(ij\) en la casilla \((i,j)\), por lo que

\[
S_T=\sum_{i=1}^m\sum_{j=1}^n ij
=\left(\sum_{i=1}^m i\right)\left(\sum_{j=1}^n j\right)
=\frac{m(m+1)}{2}\cdot \frac{n(n+1)}{2}.
\]

La diferencia es

\[
S_P-S_T
=\frac{mn(mn+1)}{2}-\frac{mn(m+1)(n+1)}{4}.
\]

Factorizando,

\[
S_P-S_T
=\frac{mn}{4}\left(2mn+2-(m+1)(n+1)\right)
\]

\[
=\frac{mn}{4}\left(mn-m-n+1\right)
=\frac{mn(m-1)(n-1)}{4}.
\]

Como la diferencia es \(2100\),

\[
\frac{mn(m-1)(n-1)}{4}=2100,
\]

\[
m(m-1)n(n-1)=8400.
\]

Por simetría, podemos suponer \(m\le n\). Entonces

\[
m(m-1)\le \sqrt{8400}\approx 91.65.
\]

Como \(10\cdot 9=90\) y \(11\cdot 10=110\), tenemos \(m\le 10\).

Probando \(m=2,3,\ldots,10\), el único caso que funciona es

\[
m=5,
\]

pues

\[
m(m-1)=5\cdot 4=20,
\]

y entonces

\[
n(n-1)=\frac{8400}{20}=420=21\cdot 20.
\]

Así que \(n=21\). Por lo tanto,

\[
m+n=5+21=26.
\]

\[
\boxed{26}
\]