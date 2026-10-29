

Sea \(x\) una raíz de

\[
x^{10}+(11x-1)^{10}=0.
\]

Como \(x=0\) no es raíz, podemos dividir por \(x^{10}\):

\[
1+\left(\frac{11x-1}{x}\right)^{10}=0.
\]

Definamos

\[
z=\frac{11x-1}{x}=11-\frac1x.
\]

Entonces

\[
z^{10}=-1.
\]

Así, las 10 raíces \(z\) son las raíces décimas de \(-1\), todas con \(|z|=1\). Además,

\[
\frac1x=11-z \qquad\Longrightarrow\qquad x=\frac1{11-z}.
\]

Para cada raíz \(x\),

\[
\frac1{x\overline{x}}=\frac1{|x|^2}=|11-z|^2.
\]

Como \(|z|=1\),

\[
|11-z|^2=(11-z)(11-\overline{z})
=121-11(z+\overline{z})+z\overline{z}
=122-22\operatorname{Re}(z).
\]

Ahora sumamos sobre las 10 raíces \(z\) de \(z^{10}=-1\). La suma de todas ellas es \(0\), por lo que la suma de sus partes reales también es \(0\). Entonces

\[
\sum_{\text{10 raíces }x}\frac1{x\overline{x}}
=
\sum_{z^{10}=-1}\left(122-22\operatorname{Re}(z)\right)
=10\cdot 122-22\cdot 0
=1220.
\]

Las 10 raíces de \(x\) vienen en 5 pares conjugados, y cada par aporta dos veces el mismo valor de \(\frac1{s\overline{s}}\). Por tanto, la suma pedida sobre \(s_1,\dots,s_5\) es la mitad:

\[
\frac{1220}{2}=610.
\]

\[
\boxed{610}
\]