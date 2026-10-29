Sea
\[
E=\frac{(a+b+c)\bigl[(a+b)^2+(a+b+4c)^2\bigr]}{abc}.
\]

Para \(s=a+b\) y \(c\) fijos, el numerador depende solo de \(s\) y \(c\), mientras que el denominador es \(c\,ab\). Por tanto, para minimizar \(E\), debemos maximizar \(ab\). Por AM-GM,

\[
ab\le \left(\frac{a+b}{2}\right)^2,
\]

con igualdad si y solo si \(a=b\). Así, el mínimo ocurre cuando \(a=b\).

Sea entonces \(a=b=x>0\) y \(c=tx\), con \(t>0\). Sustituyendo,

\[
E=\frac{(2x+tx)\bigl[(2x)^2+(2x+4tx)^2\bigr]}{x^2(tx)}.
\]

Simplificando,

\[
E=\frac{x(2+t)\cdot 4x^2\bigl[1+(1+2t)^2\bigr]}{t x^3}
=\frac{4(2+t)\bigl[1+(1+2t)^2\bigr]}{t}.
\]

Como

\[
1+(1+2t)^2=2+4t+4t^2,
\]

tenemos

\[
E=\frac{4(2+t)(2+4t+4t^2)}{t}
=16t^2+48t+40+\frac{16}{t}.
\]

Ahora comparamos con \(100\):

\[
E-100=16t^2+48t-60+\frac{16}{t}.
\]

Multiplicando por \(t>0\),

\[
t(E-100)=16t^3+48t^2-60t+16.
\]

Factorizando,

\[
16t^3+48t^2-60t+16=4(2t-1)^2(t+4).
\]

Por tanto,

\[
E-100=\frac{4(2t-1)^2(t+4)}{t}\ge 0.
\]

La igualdad ocurre cuando \(2t-1=0\), es decir, \(t=\frac12\). Esto corresponde a \(a=b\) y \(c=\frac a2\), por ejemplo \(a=b=2,\ c=1\).

Así, el valor mínimo es

\[
\boxed{100}
\]