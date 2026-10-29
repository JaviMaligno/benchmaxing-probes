Como \(P(0)=1\), toda raíz real es distinta de \(0\). Dividiendo entre \(x^2\):

\[
x^2+\frac1{x^2}+a\left(x+\frac1x\right)-b=0.
\]

Sea \(t=x+\frac1x\). Entonces \(x^2+\frac1{x^2}=t^2-2\), y la ecuación se convierte en

\[
t^2+at-b-2=0.
\]

Para que \(t\) venga de un \(x\) real, se necesita \(t\le -2\) o \(t\ge 2\).

Las raíces en \(t\) son

\[
t_{\pm}=\frac{-a\pm\sqrt{a^2+4(b+2)}}2.
\]

La raíz positiva cumple \(t_+\ge 2\) solo si

\[
4b\ge 8a+8 \quad\Longleftrightarrow\quad b\ge 2a+2,
\]

imposible con \(0\le a,b\le 1\). Por lo tanto hay raíz real exactamente cuando

\[
t_-\le -2.
\]

Esto equivale a

\[
\sqrt{a^2+4b+8}\ge 4-a,
\]

es decir,

\[
4b\ge 8-8a \quad\Longleftrightarrow\quad b\ge 2(1-a).
\]

Dentro del cuadrado unitario, esto da el triángulo con vértices

\[
\left(\frac12,1\right),\quad (1,0),\quad (1,1).
\]

Su área es

\[
\int_{1/2}^1 \bigl(1-(2-2a)\bigr)\,da
=\int_{1/2}^1(2a-1)\,da
=\frac14.
\]

\[
\boxed{\frac14}
\]