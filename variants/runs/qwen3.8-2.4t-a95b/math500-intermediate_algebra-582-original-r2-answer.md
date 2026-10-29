

Sea \(x\) una raíz. Como \(x=0\) no satisface la ecuación, podemos dividir por \(x^{10}\):

\[
1+\left(13-\frac1x\right)^{10}=0.
\]

Definamos

\[
w=13-\frac1x.
\]

Entonces \(w^{10}=-1\), así que \(w\) recorre las 10 raíces décimas de \(-1\). Además,

\[
x=\frac1{13-w}.
\]

Para cada raíz \(x\),

\[
\frac1{x\overline{x}}=\left|13-w\right|^2.
\]

Como \(|w|=1\),

\[
|13-w|^2=(13-w)(13-\overline{w})
=169-13(w+\overline{w})+1
=170-13(w+\overline{w}).
\]

Las 10 raíces \(w\) de \(w^{10}=-1\) tienen suma \(0\), pues son las raíces de \(w^{10}+1=0\), cuyo coeficiente de \(w^9\) es \(0\). Por tanto,

\[
\sum_{w^{10}=-1} |13-w|^2
= \sum_{w^{10}=-1} \left(170-13(w+\overline{w})\right)
=10\cdot 170-13(0+0)=1700.
\]

Las raíces \(x\) vienen en pares conjugados, y cada par aporta el mismo valor. La suma pedida usa una raíz de cada par, así que es la mitad de la suma total:

\[
\frac{1700}{2}=850.
\]

\[
\boxed{850}
\]