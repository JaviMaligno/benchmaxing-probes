

Sea
\[
f(x,y)=\frac{x-y}{x^4+y^4+6}.
\]

Como \(f(1,-1)=\frac{2}{1+1+6}=\frac14>0\), el máximo debe ocurrir cuando \(x-y>0\). Definamos
\[
t=x-y>0.
\]

Para un valor fijo de \(t\), el numerador es constante, así que para maximizar la fracción debemos minimizar el denominador \(x^4+y^4\) sujeto a \(x-y=t\). Escribiendo \(y=x-t\), minimizamos
\[
x^4+(x-t)^4.
\]
Derivando:
\[
4x^3+4(x-t)^3=0
\]
\[
x^3+(x-t)^3=0.
\]
Esto implica \(x+(x-t)=0\), es decir,
\[
x=\frac t2,\qquad y=-\frac t2.
\]
En ese punto,
\[
x^4+y^4=2\left(\frac t2\right)^4=\frac{t^4}{8}.
\]

Por tanto,
\[
f(x,y)\le \frac{t}{\frac{t^4}{8}+6}.
\]
Ahora maximizamos
\[
h(t)=\frac{t}{\frac{t^4}{8}+6},\qquad t>0.
\]
Derivando:
\[
h'(t)=\frac{\frac{t^4}{8}+6-t\cdot \frac{t^3}{2}}{\left(\frac{t^4}{8}+6\right)^2}
=\frac{6-\frac{3t^4}{8}}{\left(\frac{t^4}{8}+6\right)^2}.
\]
El signo de \(h'(t)\) depende de
\[
6-\frac{3t^4}{8}=0
\]
\[
t^4=16
\]
\[
t=2.
\]
Así, el máximo de \(h\) ocurre en \(t=2\), y vale
\[
h(2)=\frac{2}{\frac{16}{8}+6}=\frac{2}{2+6}=\frac14.
\]

Este valor se alcanza con \(t=2\), \(x=\frac t2=1\), \(y=-\frac t2=-1\).

\[
\boxed{\frac14}
\]