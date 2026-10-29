Por Cauchy–Schwarz,
\[
\left(\sum_{i=1}^n a_i\right)\left(\sum_{i=1}^n a_i^3\right)
\ge \left(\sum_{i=1}^n a_i^2\right)^2.
\]
Sustituyendo los datos:
\[
96\cdot 216=20736,\qquad 144^2=20736.
\]
Así que se cumple la igualdad en Cauchy–Schwarz. La igualdad ocurre si y solo si los vectores \((\sqrt{a_i})\) y \((a_i^{3/2})\) son proporcionales, es decir, si existe \(\lambda\) tal que
\[
a_i^{3/2}=\lambda \sqrt{a_i}\implies a_i=\lambda
\]
para todo \(i\). Por tanto, todos los \(a_i\) son iguales.

Sea \(a_i=x\) para todo \(i\). Entonces
\[
nx=96,\qquad nx^2=144.
\]
Dividiendo la segunda entre la primera:
\[
x=\frac{144}{96}=\frac32.
\]
Luego
\[
n=\frac{96}{3/2}=64.
\]
La tercera condición también se cumple, ya que
\[
64\left(\frac32\right)^3=64\cdot \frac{27}{8}=216.
\]
Por lo tanto, el único valor posible de \(n\) es \(64\), y la suma de todos los valores posibles es
\[
\boxed{64}.
\]