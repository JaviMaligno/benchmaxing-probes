Las desigualdades se factorizan:

\[
x-yz<y-zx
\iff x-y-yz+zx<0
\iff (x-y)(1+z)<0,
\]

y

\[
y-zx<z-xy
\iff y-z-zx+xy<0
\iff (y-z)(1+x)<0.
\]

Entonces las condiciones son

\[
(x-y)(z+1)<0,\qquad (y-z)(x+1)<0.
\]

Como aparece el factor \(x+1\) en la segunda y \(z+1\) en la primera, conviene distinguir los signos de \(x+1\) y \(z+1\).

- Si \(x+1>0\) y \(z+1>0\), entonces

\[
x<y<z.
\]

Junto con \(x+y+z=87\), esto da la región

\[
-1<x<y<z.
\]

Esta es la región acotada.

- Si \(x+1>0\) y \(z+1<0\), se obtiene \(y<z<-1<x\), una región no acotada.
- Si \(x+1<0\) y \(z+1>0\), se obtiene \(x<z<y\), otra región no acotada.
- Si \(x+1<0\) y \(z+1<0\), se obtendría \(x>y>z\) con todas las coordenadas menores que \(-1\), lo cual haría \(x+y+z<-3\), imposible.

Así, la única región finita es

\[
-1<x<y<z,\qquad x+y+z=87.
\]

Su clausura es un triángulo delimitado por las rectas

\[
x=-1,\qquad x=y,\qquad y=z.
\]

Encontramos sus vértices:

- \(x=-1\) y \(x=y\): \((-1,-1,89)\).
- \(x=-1\) y \(y=z\): \((-1,44,44)\).
- \(x=y=z\): \((29,29,29)\).

Sean

\[
P=(-1,44,44),\quad Q=(-1,-1,89),\quad R=(29,29,29).
\]

Entonces

\[
\overrightarrow{PQ}=(0,-45,45),\qquad 
\overrightarrow{PR}=(30,-15,-15).
\]

Estos vectores son perpendiculares, pues

\[
\overrightarrow{PQ}\cdot \overrightarrow{PR}
=0+675-675=0.
\]

Sus longitudes son

\[
|\overrightarrow{PQ}|=45\sqrt2,
\qquad
|\overrightarrow{PR}|=15\sqrt6.
\]

Por lo tanto, el área del triángulo es

\[
\frac12(45\sqrt2)(15\sqrt6)
=\frac12\cdot 675\sqrt{12}
=675\sqrt3.
\]

Así,

\[
a=675,\qquad b=3,
\]

y

\[
a+b=678.
\]

\[
\boxed{678}
\]