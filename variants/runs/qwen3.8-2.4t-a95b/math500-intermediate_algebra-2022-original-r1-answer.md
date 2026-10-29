

Sean \(a_1,\dots,a_n>0\) con

\[
\sum_{i=1}^n a_i=96,\qquad \sum_{i=1}^n a_i^2=144,\qquad \sum_{i=1}^n a_i^3=216.
\]

Aplicamos Cauchy-Schwarz a los vectores \(\bigl(\sqrt{a_i}\bigr)\) y \(\bigl(a_i^{3/2}\bigr)\):

\[
\left(\sum_{i=1}^n a_i^2\right)^2
\le
\left(\sum_{i=1}^n a_i\right)\left(\sum_{i=1}^n a_i^3\right).
\]

Sustituyendo los valores dados,

\[
144^2 \le 96\cdot 216.
\]

Pero

\[
144^2=20736,\qquad 96\cdot 216=20736,
\]

así que se tiene igualdad. La igualdad en Cauchy-Schwarz ocurre solo si los vectores son proporcionales, es decir,

\[
a_i^{3/2}=\lambda \sqrt{a_i}
\]

para todo \(i\). Como \(a_i>0\), esto implica \(a_i=\lambda\) para todo \(i\). Por tanto, todos los términos son iguales.

Si \(a_i=c\) para todo \(i\), entonces

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

Finalmente, comprobamos:

\[
64\left(\frac32\right)^3=64\cdot \frac{27}{8}=216,
\]

así que \(n=64\) es posible. El único valor posible de \(n\) es \(64\), por lo que la suma de todos los valores posibles es

\[
\boxed{64}
\]