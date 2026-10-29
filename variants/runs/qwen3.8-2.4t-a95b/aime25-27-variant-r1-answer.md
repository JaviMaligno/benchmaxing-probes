

Sea \(\theta=\angle B_iB_1B_{i+1}\). Como \(\cos\theta=\frac45\) y \(\theta\) es un ángulo de triángulo, se tiene \(\sin\theta=\frac35\).

Definamos \(r_i=B_1B_i\). Por el área del triángulo \(B_iB_1B_{i+1}\),

\[
1=\frac12 r_i r_{i+1}\sin\theta
=\frac12 r_i r_{i+1}\cdot \frac35,
\]

de donde

\[
r_i r_{i+1}=\frac{10}{3}\qquad (2\le i\le 10).
\]

Por tanto,

\[
r_{i+2}=\frac{10/3}{r_{i+1}}=r_i,
\]

así que las distancias se alternan. Escribamos

\[
r_2=r_4=\cdots=r_{10}=a,\qquad
r_3=r_5=\cdots=r_{11}=b,
\]

con

\[
ab=\frac{10}{3}.
\]

Cada lado \(B_iB_{i+1}\) para \(2\le i\le 10\) tiene la misma longitud \(\ell\). Por la ley de cosenos,

\[
\ell^2=a^2+b^2-2ab\cos\theta
=a^2+b^2-2\cdot \frac{10}{3}\cdot \frac45
=a^2+b^2-\frac{16}{3}.
\]

Sea

\[
X=a+b=B_1B_2+B_1B_{11}.
\]

Como \(a^2+b^2=(a+b)^2-2ab=X^2-\frac{20}{3}\), obtenemos

\[
\ell^2=X^2-\frac{20}{3}-\frac{16}{3}=X^2-12.
\]

El perímetro del polígono es

\[
X+9\ell=20.
\]

Así,

\[
9\sqrt{X^2-12}=20-X.
\]

Elevando al cuadrado,

\[
81(X^2-12)=(20-X)^2,
\]

\[
81X^2-972=X^2-40X+400,
\]

\[
80X^2+40X-1372=0,
\]

\[
20X^2+10X-343=0.
\]

La raíz positiva es

\[
X=\frac{-10+\sqrt{100+4\cdot 20\cdot 343}}{40}
=\frac{-10+\sqrt{27540}}{40}.
\]

Como \(27540=324\cdot 85\),

\[
X=\frac{-10+18\sqrt{85}}{40}
=\frac{9\sqrt{85}-5}{20}.
\]

Entonces

\[
m=9,\quad n=85,\quad p=5,\quad q=20,
\]

y

\[
m+n+p+q=9+85+5+20=119.
\]

\[
\boxed{119}
\]