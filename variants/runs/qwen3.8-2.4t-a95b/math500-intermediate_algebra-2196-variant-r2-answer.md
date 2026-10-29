

Sea \(d=a-b\). Si \(d\le 0\), la expresión es \(\le 0\), y como podemos obtener un valor positivo, el máximo debe darse con \(d>0\).

Escribamos
\[
a=x+\frac d2,\qquad b=x-\frac d2,
\]
donde \(x=\frac{a+b}{2}\). Entonces
\[
a^4+b^4=\left(x+\frac d2\right)^4+\left(x-\frac d2\right)^4
=2x^4+3d^2x^2+\frac{d^4}{8}.
\]
Esto es mínimo cuando \(x=0\), así que, para \(d\) fijo,
\[
a^4+b^4 \ge \frac{d^4}{8}.
\]
Por tanto,
\[
\frac{a-b}{a^4+b^4+96}
\le \frac{d}{\frac{d^4}{8}+96}.
\]

Ahora maximizamos
\[
f(d)=\frac{d}{\frac{d^4}{8}+96},\qquad d>0.
\]
Derivando,
\[
f'(d)=\frac{\frac{d^4}{8}+96-d\cdot \frac{d^3}{2}}{\left(\frac{d^4}{8}+96\right)^2}
=\frac{96-\frac{3d^4}{8}}{\left(\frac{d^4}{8}+96\right)^2}.
\]
El punto crítico satisface
\[
96=\frac{3d^4}{8}
\quad\Longrightarrow\quad
d^4=256
\quad\Longrightarrow\quad
d=4.
\]
Así,
\[
f(4)=\frac{4}{\frac{256}{8}+96}
=\frac{4}{32+96}
=\frac{4}{128}
=\frac{1}{32}.
\]

La igualdad se alcanza con \(x=0\) y \(d=4\), es decir, \(a=2\) y \(b=-2\).

\[
\boxed{\frac{1}{32}}
\]