

Para \(b,c\) fijos, la condición de triángulo no degenerado es

\[
|b-c|<a<b+c.
\]

Como \(a\) es un entero positivo, esto significa

\[
a=|b-c|+1,\ |b-c|+2,\ \dots,\ b+c-1.
\]

Entonces la suma interior sobre \(a\) es geométrica:

\[
\sum_{a=|b-c|+1}^{b+c-1}3^a
=\frac{3^{b+c}-3^{|b-c|+1}}{2}.
\]

Por lo tanto, la suma pedida es

\[
\Sigma=\frac12\sum_{b,c\ge 1}
\left(
\frac{3^{b+c}}{4^b5^c}
-
\frac{3^{|b-c|+1}}{4^b5^c}
\right).
\]

El primer término es separable:

\[
\frac12\sum_{b,c\ge1}\frac{3^{b+c}}{4^b5^c}
=
\frac12
\left(\sum_{b\ge1}\left(\frac34\right)^b\right)
\left(\sum_{c\ge1}\left(\frac35\right)^c\right).
\]

Como

\[
\sum_{b\ge1}\left(\frac34\right)^b=3,
\qquad
\sum_{c\ge1}\left(\frac35\right)^c=\frac32,
\]

obtenemos

\[
\frac12\cdot 3\cdot \frac32=\frac94.
\]

Ahora el segundo término:

\[
\frac12\sum_{b,c\ge1}\frac{3^{|b-c|+1}}{4^b5^c}
=
\frac32\sum_{b,c\ge1}\frac{3^{|b-c|}}{4^b5^c}.
\]

Dividimos en los casos \(b\ge c\) y \(c>b\).

Si \(b\ge c\), sea \(k=b-c\ge0\):

\[
\sum_{b\ge c\ge1}\frac{3^{b-c}}{4^b5^c}
=
\sum_{c\ge1}\frac1{20^c}\sum_{k\ge0}\left(\frac34\right)^k
=
\frac1{19}\cdot 4
=
\frac4{19}.
\]

Si \(c>b\), sea \(m=c-b\ge1\):

\[
\sum_{c>b\ge1}\frac{3^{c-b}}{4^b5^c}
=
\sum_{b\ge1}\frac1{20^b}\sum_{m\ge1}\left(\frac35\right)^m
=
\frac1{19}\cdot \frac32
=
\frac3{38}.
\]

Así,

\[
\frac32\sum_{b,c\ge1}\frac{3^{|b-c|}}{4^b5^c}
=
\frac32\left(\frac4{19}+\frac3{38}\right)
=
\frac32\cdot\frac{11}{38}
=
\frac{33}{76}.
\]

Finalmente,

\[
\Sigma=\frac94-\frac{33}{76}
=\frac{171}{76}-\frac{33}{76}
=\frac{138}{76}
=\frac{69}{38}.
\]

\[
\boxed{\frac{69}{38}}
\]