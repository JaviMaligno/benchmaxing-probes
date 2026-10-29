Sea \(d=x-y\). Si \(d\le 0\), entonces \(f(x,y)\le 0\), así que el máximo debe ocurrir con \(d>0\).

Escribimos
\[
x=\frac{x+y}{2}+\frac d2,\qquad y=\frac{x+y}{2}-\frac d2.
\]
Si \(u=\frac{x+y}{2}\), entonces
\[
x^4+y^4=\left(u+\frac d2\right)^4+\left(u-\frac d2\right)^4
=2u^4+3u^2d^2+\frac{d^4}{8}.
\]
Por tanto,
\[
x^4+y^4\ge \frac{d^4}{8},
\]
con igualdad cuando \(u=0\), es decir, cuando \(y=-x\).

Luego, para \(d>0\),
\[
\frac{x-y}{x^4+y^4+6}
\le \frac{d}{\frac{d^4}{8}+6}.
\]
Ahora maximizamos
\[
g(d)=\frac{d}{\frac{d^4}{8}+6}.
\]
Por AM-GM,
\[
\frac{d^4}{8}+6=\frac{d^4+48}{8}
\ge \frac{4\sqrt[4]{d^4\cdot 16\cdot 16\cdot 16}}{8}
=\frac{32d}{8}=4d.
\]
Así,
\[
\frac{d}{\frac{d^4}{8}+6}\le \frac14.
\]
La igualdad ocurre cuando \(d^4=16\), es decir \(d=2\), y además \(x=-y\). Entonces \(x=1\), \(y=-1\), y
\[
\frac{x-y}{x^4+y^4+6}=\frac{2}{1+1+6}=\frac14.
\]

\[
\boxed{\frac14}
\]