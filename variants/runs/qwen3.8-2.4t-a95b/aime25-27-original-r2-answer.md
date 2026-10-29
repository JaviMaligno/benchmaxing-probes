

Sea \(r_i = A_1A_i\), y sea \(\theta = \angle A_iA_1A_{i+1}\). Como

\[
\cos\theta=\frac{12}{13},
\]

entonces \(\theta\) es agudo y

\[
\sin\theta=\frac{5}{13}.
\]

El área de cada triángulo \(\triangle A_iA_1A_{i+1}\) es

\[
1=\frac12 r_i r_{i+1}\sin\theta
=\frac12 r_i r_{i+1}\cdot \frac{5}{13}.
\]

Por tanto,

\[
r_i r_{i+1}=\frac{26}{5}.
\]

Así, las distancias desde \(A_1\) alternan:

\[
r_2=r_4=r_6=r_8=r_{10}=x,
\]
\[
r_3=r_5=r_7=r_9=r_{11}=y,
\]

con

\[
xy=\frac{26}{5}.
\]

Queremos

\[
A_1A_2+A_1A_{11}=x+y.
\]

Llamemos \(S=x+y\). Por la ley de los cosenos, cada lado \(A_iA_{i+1}\) para \(2\le i\le 10\) tiene longitud \(L\), donde

\[
L^2=x^2+y^2-2xy\cos\theta.
\]

Como

\[
x^2+y^2=(x+y)^2-2xy=S^2-\frac{52}{5},
\]

y

\[
2xy\cos\theta=2\cdot \frac{26}{5}\cdot \frac{12}{13}=\frac{48}{5},
\]

tenemos

\[
L^2=S^2-\frac{52}{5}-\frac{48}{5}=S^2-20.
\]

Así,

\[
L=\sqrt{S^2-20}.
\]

El perímetro del polígono es

\[
A_1A_2+\sum_{i=2}^{10}A_iA_{i+1}+A_{11}A_1
=x+9L+y=S+9L.
\]

Dado que el perímetro es \(20\),

\[
S+9\sqrt{S^2-20}=20.
\]

Entonces

\[
9\sqrt{S^2-20}=20-S.
\]

Elevando al cuadrado:

\[
81(S^2-20)=(20-S)^2,
\]

\[
81S^2-1620=S^2-40S+400,
\]

\[
80S^2+40S-2020=0,
\]

\[
4S^2+2S-101=0.
\]

Por la fórmula cuadrática,

\[
S=\frac{-2+\sqrt{4+1616}}{8}
=\frac{-2+\sqrt{1620}}{8}
=\frac{-2+18\sqrt5}{8}
=\frac{9\sqrt5-1}{4}.
\]

Por lo tanto,

\[
A_1A_2+A_1A_{11}=\frac{9\sqrt5-1}{4}.
\]

Así, \(m=9\), \(n=5\), \(p=1\), \(q=4\), y

\[
m+n+p+q=9+5+1+4=19.
\]

\[
\boxed{19}
\]