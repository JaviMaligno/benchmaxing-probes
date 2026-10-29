

Sean \(p_k=\sum_{i=1}^n a_i^k\). Tenemos

\[
p_1=96,\quad p_2=144,\quad p_3=216.
\]

Observamos que

\[
p_1p_3=96\cdot 216=20736=144^2=p_2^2.
\]

Por Cauchy-Schwarz,

\[
\left(\sum_{i=1}^n a_i^2\right)^2
=
\left(\sum_{i=1}^n \sqrt{a_i}\,a_i^{3/2}\right)^2
\le
\left(\sum_{i=1}^n a_i\right)\left(\sum_{i=1}^n a_i^3\right).
\]

Es decir,

\[
p_2^2\le p_1p_3.
\]

Como aquí se tiene igualdad, la condición de igualdad de Cauchy-Schwarz implica que

\[
a_i^{3/2}=\lambda \sqrt{a_i}
\]

para todo \(i\). Como \(a_i>0\), esto da \(a_i=\lambda\) para todo \(i\). Por tanto, todos los términos son iguales.

Sea \(a_i=c\). Entonces

\[
nc=96,\qquad nc^2=144.
\]

Dividiendo la segunda ecuación entre la primera,

\[
c=\frac{144}{96}=\frac32.
\]

Luego

\[
n=\frac{96}{3/2}=64.
\]

Finalmente comprobamos:

\[
64\left(\frac32\right)^3=64\cdot \frac{27}{8}=216.
\]

Así, el único valor posible de \(n\) es \(64\).

\[
\boxed{64}
\]