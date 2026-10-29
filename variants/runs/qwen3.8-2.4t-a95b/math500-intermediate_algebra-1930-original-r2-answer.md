

Sea
\[
P(x)=x^4+ax^3-bx^2+ax+1.
\]
Como \(P(0)=1\), una raíz real \(x\) no puede ser \(0\). Dividiendo por \(x^2\),

\[
x^2+\frac1{x^2}+a\left(x+\frac1x\right)-b=0.
\]

Sea
\[
t=x+\frac1x.
\]
Entonces \(x^2+\frac1{x^2}=t^2-2\), así que la ecuación se convierte en

\[
t^2+at-(b+2)=0.
\]

Para \(x\) real, se tiene \(t\in(-\infty,-2]\cup[2,\infty)\), y recíprocamente todo \(t\) en ese conjunto produce una raíz real \(x\).

Definamos
\[
f(t)=t^2+at-(b+2).
\]
Como \(b+2>0\), \(f(0)<0\), así que la cuadrática tiene una raíz positiva y una negativa.

Para la raíz positiva, evaluamos en \(t=2\):

\[
f(2)=4+2a-(b+2)=2+2a-b.
\]

Con \(0\le a,b\le 1\),

\[
f(2)\ge 2+0-1=1>0,
\]

por lo que la raíz positiva está entre \(0\) y \(2\), y no sirve.

Solo puede servir la raíz negativa, que debe cumplir \(t\le -2\). Esto equivale a

\[
f(-2)\le 0.
\]

Calculamos

\[
f(-2)=4-2a-(b+2)=2-2a-b.
\]

Así que necesitamos

\[
2-2a-b\le 0 \iff b\ge 2-2a.
\]

Dentro del cuadrado \([0,1]^2\), esta región existe para \(a\ge \frac12\). Su área es

\[
\int_{1/2}^{1} \bigl(1-(2-2a)\bigr)\,da
=
\int_{1/2}^{1} (2a-1)\,da
=
\left[a^2-a\right]_{1/2}^{1}
=
\frac14.
\]

\[
\boxed{\frac14}
\]