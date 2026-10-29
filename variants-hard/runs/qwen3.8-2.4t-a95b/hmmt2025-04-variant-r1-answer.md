

Sea

\[
S=\sum_{k=-1200}^{1200}\left\lfloor\frac{3150}{k+0.5}\right\rfloor.
\]

Notemos que

\[
\frac{3150}{k+0.5}=\frac{6300}{2k+1}.
\]

Además, los términos se pueden emparejar usando \(k\) y \(-k-1\), ya que

\[
(-k-1)+0.5=-(k+0.5).
\]

En el rango \(k=-1200,\dots,1200\), todos los términos se emparejan excepto \(k=1200\).

Para cada pareja con denominador positivo \(a=k+0.5\), tenemos

\[
\left\lfloor \frac{3150}{a}\right\rfloor+\left\lfloor -\frac{3150}{a}\right\rfloor.
\]

Si \(\frac{3150}{a}\) es entero, esta suma es \(0\). Si no es entero, entonces

\[
\lfloor x\rfloor+\lfloor -x\rfloor=-1.
\]

Los denominadores positivos corresponden a \(k=0,1,\dots,1199\), es decir,

\[
a=\frac{2k+1}{2},
\]

con \(2k+1\) impar desde \(1\) hasta \(2399\). Hay \(1200\) impares positivos en ese rango.

Ahora,

\[
\frac{3150}{a}=\frac{6300}{2k+1}
\]

es entero exactamente cuando el impar \(2k+1\) divide a \(6300\).

Factorizando:

\[
6300=2^2\cdot 3^2\cdot 5^2\cdot 7.
\]

Sus divisores impares son los divisores de

\[
3^2\cdot 5^2\cdot 7,
\]

cuya cantidad es

\[
(2+1)(2+1)(1+1)=18.
\]

Todos estos divisores impares son menores que \(2399\), así que de las \(1200\) parejas, \(18\) suman \(0\) y las otras

\[
1200-18=1182
\]

suman \(-1\). Por tanto, la contribución de las parejas es

\[
-1182.
\]

Falta el término no emparejado \(k=1200\):

\[
\left\lfloor\frac{3150}{1200.5}\right\rfloor
=
\left\lfloor\frac{6300}{2401}\right\rfloor
=2.
\]

Así,

\[
S=-1182+2=-1180.
\]

\[
\boxed{-1180}
\]