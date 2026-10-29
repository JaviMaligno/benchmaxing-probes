El problema pide la mínima distancia entre el origen y un punto de la curva

\[
y=\frac{1}{\sqrt{3}}\left(x^2-5\right).
\]

Sea \(d^2=x^2+y^2\). Sustituimos \(y\):

\[
d^2=x^2+\frac{1}{3}\left(x^2-5\right)^2.
\]

Queremos minimizar \(f(x)=d^2\).

Calculamos la derivada:

\[
f'(x)=2x+\frac{2}{3}\left(x^2-5\right)(2x)
=2x+\frac{4x}{3}\left(x^2-5\right).
\]

Factorizamos \(2x\):

\[
f'(x)=2x\left(1+\frac{2}{3}\left(x^2-5\right)\right)
=2x\left(1+\frac{2x^2-10}{3}\right)
=2x\cdot \frac{2x^2-7}{3}.
\]

Entonces

\[
f'(x)=\frac{2x(2x^2-7)}{3}.
\]

Los puntos críticos son:

\[
x=0,\quad x=\pm\sqrt{\frac72}.
\]

Evaluamos \(f\).

Para \(x=0\):

\[
y=\frac{1}{\sqrt3}(-5)=-\frac{5}{\sqrt3},
\]

\[
f(0)=0+\frac{25}{3}=\frac{25}{3}.
\]

Para \(x=\sqrt{\frac72}\):

\[
x^2=\frac72,
\]

\[
x^2-5=\frac72-5=\frac{7-10}{2}=-\frac32,
\]

\[
y=\frac{1}{\sqrt3}\left(-\frac32\right)=-\frac{3}{2\sqrt3}=-\frac{\sqrt3}{2}.
\]

Entonces

\[
f=x^2+y^2=\frac72+\frac34
=\frac{14}{4}+\frac34
=\frac{17}{4}.
\]

Por tanto la distancia mínima es

\[
d=\sqrt{\frac{17}{4}}=\frac{\sqrt{17}}{2}.
\]

Así, \(a=17\) y \(b=2\), de modo que

\[
a+b=17+2=19.
\]

\[
\boxed{19}
\]