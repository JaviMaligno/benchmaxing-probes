Dividimos la ecuación por \(x^{10}\) (notando que \(x=0\) no es raíz):

\[
1+\left(\frac{13x-1}{x}\right)^{10}=0,
\]

por lo que si

\[
w=\frac{13x-1}{x}=13-\frac1x,
\]

entonces

\[
w^{10}=-1.
\]

Así, las raíces \(x\) cumplen

\[
x=\frac1{13-w},
\]

donde \(w\) recorre las 10 raíces décimas de \(-1\).

Entonces

\[
\frac1{x\overline x}=|13-w|^2=(13-w)(13-\overline w).
\]

Como \(|w|=1\), se tiene \(w\overline w=1\), luego

\[
|13-w|^2=169-13(w+\overline w)+1=170-13(w+\overline w).
\]

Sumando sobre las 10 raíces \(w\) de \(w^{10}=-1\):

\[
\sum_w |13-w|^2
=1700-13\sum_w (w+\overline w).
\]

Las sumas de las raíces y de sus conjugadas son ambas \(0\), porque el coeficiente de \(w^9\) en \(w^{10}+1=0\) es \(0\). Por tanto,

\[
\sum_w |13-w|^2=1700.
\]

Esta es la suma sobre las 10 raíces de \(1/(x\overline x)\). Como las raíces van en 5 pares conjugados, la suma pedida es la mitad:

\[
\frac12\cdot 1700=850.
\]

\[
\boxed{850}
\]