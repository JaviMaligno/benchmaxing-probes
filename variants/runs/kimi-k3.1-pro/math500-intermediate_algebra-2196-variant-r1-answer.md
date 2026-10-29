Sea \(d=a-b\). Para \(d\le 0\), la expresión es no positiva, así que el máximo debe obtenerse con \(d>0\).

Por convexidad, para una diferencia \(d\) fija, \(a^4+b^4\) se minimiza cuando \(a=-b=d/2\). Por tanto,
\[
a^4+b^4\ge 2\left(\frac d2\right)^4=\frac{d^4}{8}.
\]
En consecuencia,
\[
\frac{a-b}{a^4+b^4+96}\le \frac{d}{d^4/8+96}.
\]
Ahora, por AM-GM,
\[
\frac{d^4}{8}+96
=\frac{d^4}{8}+32+32+32
\ge 4\sqrt[4]{\frac{d^4}{8}\cdot 32^3}
=32d.
\]
Así,
\[
\frac{d}{d^4/8+96}\le \frac1{32}.
\]
La igualdad se alcanza cuando \(d^4/8=32\), es decir, \(d=4\), junto con \(a=-b\). Tomando \(a=2\) y \(b=-2\),
\[
\frac{2-(-2)}{2^4+(-2)^4+96}=\frac4{128}=\frac1{32}.
\]

\[
\boxed{\frac{1}{32}}
\]