Sea \(s=a+b>0\). Entonces la expresión es

\[
E=\frac{(s+c)\bigl(s^2+(s+4c)^2\bigr)}{abc}.
\]

Para \(s\) y \(c\) fijos, minimizar \(E\) equivale a maximizar \(ab\) bajo \(a+b=s\). Por la desigualdad AM-GM,

\[
ab\le \left(\frac{a+b}{2}\right)^2=\frac{s^2}{4},
\]

con igualdad si y solo si \(a=b\). Por tanto, en el mínimo debe cumplirse \(a=b=x\).

Sustituyendo \(a=b=x\), \(c=y\) y \(t=\frac yx\):

\[
E=\frac{(2x+y)\bigl((2x)^2+(2x+4y)^2\bigr)}{x^2y}.
\]

Como

\[
(2x)^2+(2x+4y)^2=8x^2+16xy+16y^2=8(x^2+2xy+2y^2),
\]

se tiene

\[
E=8\cdot \frac{(2+t)(1+2t+2t^2)}{t}
=8\left(\frac2t+5+6t+2t^2\right).
\]

Definimos

\[
g(t)=\frac2t+5+6t+2t^2,\qquad t>0.
\]

Derivando:

\[
g'(t)=-\frac2{t^2}+6+4t
=\frac{4t^3+6t^2-2}{t^2}
=\frac{4(t-\frac12)(t+1)^2}{t^2}.
\]

Así, \(g\) decrece para \(t<\frac12\) y crece para \(t>\frac12\), por lo que el mínimo se alcanza en \(t=\frac12\). Entonces

\[
g\left(\frac12\right)=4+5+3+\frac12=\frac{25}{2}.
\]

Luego

\[
E_{\min}=8\cdot \frac{25}{2}=100.
\]

\[
\boxed{100}
\]