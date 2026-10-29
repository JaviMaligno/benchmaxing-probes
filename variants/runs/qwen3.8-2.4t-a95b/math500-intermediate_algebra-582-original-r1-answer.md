

Sea
\[
u=\frac{x}{1-13x}.
\]
Como \(x=0\) y \(x=\frac1{13}\) no son raíces, la transformación es válida. Además, como el exponente es par,
\[
(13x-1)^{10}=(1-13x)^{10},
\]
por lo que la ecuación se puede escribir como
\[
x^{10}+(1-13x)^{10}=0.
\]
Entonces
\[
\left(\frac{x}{1-13x}\right)^{10}=-1,
\]
es decir,
\[
u^{10}=-1.
\]
Así, los valores de \(u\) son las 10 raíces de \(u^{10}+1=0\), todas con \(|u|=1\), agrupadas en 5 pares conjugados.

Despejando \(x\):
\[
u(1-13x)=x \implies x=\frac{u}{1+13u}.
\]

Si \(r\) corresponde a \(u\), entonces \(\overline r\) corresponde a \(\overline u\). Como \(|u|=1\),
\[
r\overline r
=
\frac{u}{1+13u}\cdot \frac{\overline u}{1+13\overline u}
=
\frac{1}{(1+13u)(1+13\overline u)}.
\]
Por tanto,
\[
\frac1{r\overline r}
=(1+13u)(1+13\overline u)
=1+13(u+\overline u)+169
=170+13(u+\overline u).
\]

Al sumar sobre los 5 pares conjugados,
\[
\sum_{i=1}^5 \frac1{r_i\overline r_i}
=
5\cdot 170+13\sum_{\text{todas las raíces }u} u.
\]
Pero las raíces de \(u^{10}+1=0\) suman \(0\), ya que el coeficiente de \(u^9\) es \(0\). Luego,
\[
\sum_{i=1}^5 \frac1{r_i\overline r_i}=850.
\]

\[
\boxed{850}
\]