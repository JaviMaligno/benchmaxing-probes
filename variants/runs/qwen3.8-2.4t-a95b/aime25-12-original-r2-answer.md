

Restamos los términos consecutivos de la cadena de desigualdades:

\[
(x-yz)-(y-zx)=x-y+zx-yz=(x-y)(1+z),
\]

\[
(y-zx)-(z-xy)=y-z+xy-zx=(y-z)(1+x).
\]

Por lo tanto, las desigualdades

\[
x-yz<y-zx<z-xy
\]

equivalen a

\[
(x-y)(1+z)<0,\qquad (y-z)(1+x)<0.
\]

Ahora analizamos los signos de \(1+x\) y \(1+z\) en el plano \(x+y+z=75\).

- Si \(x>-1\) y \(z>-1\), entonces \(x-y<0\) y \(y-z<0\), así que

\[
x<y<z.
\]

Como \(z\) es el mayor y \(x+y+z=75\), automáticamente \(z\ge 25>-1\). La condición relevante es entonces \(x>-1\). Esta región está acotada.

- Las otras combinaciones posibles producen regiones no acotadas.
- Si \(x<-1\) y \(z<-1\), se tendría \(x>y>z\), lo cual es imposible porque la suma sería menor que \(-3\), no \(75\).

Así que la única región finita es

\[
x+y+z=75,\qquad x>-1,\qquad x<y<z.
\]

Usamos \(z=75-x-y\). Las condiciones se convierten en

\[
x>-1,\qquad y>x,\qquad 75-x-y>y.
\]

La última es

\[
x+2y<75.
\]

En el plano \(xy\), esto es un triángulo con vértices en las intersecciones de

\[
x=-1,\qquad y=x,\qquad x+2y=75.
\]

Los vértices son:

\[
(-1,-1),\qquad (-1,38),\qfty (25,25).
\]

En coordenadas \((x,y)\), el área proyectada del triángulo es

\[
\frac12 \cdot 39 \cdot 26 = 507.
\]

Pero el plano \(x+y+z=75\) tiene elemento de área

\[
\sqrt{1+1+1}=\sqrt{3}
\]

respecto a la proyección sobre el plano \(xy\). Por tanto, el área real de la región finita es

\[
507\sqrt{3}.
\]

Así,

\[
a=507,\qquad b=3,
\]

y

\[
a+b=510.
\]

\[
\boxed{510}
\]