Para \(a+b\) y \(c\) fijos, el numerador es constante y \(ab\le \frac{(a+b)^2}{4}\). Por tanto, la expresión se minimiza cuando \(a=b\).

Sea \(a=b=x\) y \(c=tx\), con \(t>0\). Sustituyendo:
\[
\frac{(2x+tx)\big[4x^2+(2x+4tx)^2\big]}{tx^3}
=8\left(\frac2t+5+6t+2t^2\right).
\]
Definimos
\[
g(t)=\frac2t+5+6t+2t^2.
\]
Entonces
\[
g'(t)=-\frac2{t^2}+6+4t.
\]
La condición \(g'(t)=0\) equivale a
\[
2t^3+3t^2-1=0
\iff (2t-1)(t+1)^2=0,
\]
cuya única solución positiva es \(t=\frac12\). Como \(g(t)\to\infty\) cuando \(t\to0^+\) o \(t\to\infty\), allí se alcanza el mínimo:
\[
g\left(\frac12\right)=4+5+3+\frac12=\frac{25}{2}.
\]
Así, el valor mínimo es \(8\cdot\frac{25}{2}=100\), alcanzado cuando \((a,b,c)=(2\lambda,2\lambda,\lambda)\) para cualquier \(\lambda>0\).

\[
\boxed{100}
\]