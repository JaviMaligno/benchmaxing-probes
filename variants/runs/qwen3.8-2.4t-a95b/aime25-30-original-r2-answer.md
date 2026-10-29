

Sea \(m\) el valor mínimo de \(f\) en \(x>0\), y supongamos que se alcanza exactamente en dos puntos positivos distintos \(r\) y \(s\).

Como \(x>0\), podemos multiplicar por \(x\) sin cambiar signos:

\[
N(x)=x(f(x)-m)=(x-18)(x-72)(x-98)(x-k)-mx.
\]

Para todo \(x>0\), se tiene \(N(x)\ge 0\), y además \(N(r)=N(s)=0\). Como \(N\) es un polinomio mónico de grado \(4\), cada cero positivo debe tener multiplicidad par; por tanto,

\[
N(x)=(x-r)^2(x-s)^2.
\]

Sea

\[
a=r+s,\qquad b=rs.
\]

Entonces

\[
(x-r)^2(x-s)^2=(x^2-ax+b)^2
=x^4-2ax^3+(a^2+2b)x^2-2abx+b^2.
\]

Por otro lado,

\[
(x-18)(x-72)(x-98)(x-k)
\]

tiene coeficientes:

\[
\sigma_1=18+72+98+k=188+k,
\]

\[
\sigma_2=18\cdot72+18\cdot98+72\cdot98+k(18+72+98)=10116+188k,
\]

\[
\sigma_4=18\cdot72\cdot98\cdot k=127008k.
\]

Comparando coeficientes de \(x^3\), \(x^2\) y el término constante:

\[
2a=188+k,
\]

\[
a^2+2b=10116+188k,
\]

\[
b^2=127008k.
\]

De las dos primeras,

\[
a=\frac{188+k}{2},
\]

\[
b=\frac{10116+188k-a^2}{2}
=\frac{5120+376k-k^2}{8}.
\]

Como \(r,s>0\), tenemos \(b=rs>0\). Luego

\[
\left(\frac{5120+376k-k^2}{8}\right)^2=127008k.
\]

Tomando la raíz positiva,

\[
5120+376k-k^2=2016\sqrt{2k}.
\]

Sea \(y=\sqrt{2k}>0\), de modo que \(k=y^2/2\). Sustituyendo:

\[
5120+188y^2-\frac{y^4}{4}=2016y.
\]

Multiplicando por \(4\):

\[
20480+752y^2-y^4=8064y,
\]

\[
y^4-752y^2+8064y-20480=0.
\]

Este polinomio se factoriza como

\[
(y-4)(y-8)(y-20)(y+32)=0.
\]

Como \(y>0\), las soluciones son

\[
y=4,\quad y=8,\quad y=20.
\]

Por tanto,

\[
k=\frac{y^2}{2}=8,\quad 32,\quad 200.
\]

Para cada uno de estos valores, \(b>0\) y \(a^2-4b>0\), así que \(r,s\) son positivos y distintos; además, eligiendo \(m\) para ajustar el coeficiente lineal, se cumple

\[
f(x)-m=\frac{(x-r)^2(x-s)^2}{x}\ge 0,
\]

con igualdad exactamente en dos puntos positivos. Así, los tres valores son válidos.

La suma pedida es

\[
8+32+200=240.
\]

\[
\boxed{240}
\]