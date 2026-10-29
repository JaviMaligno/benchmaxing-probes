

Reescribimos el tercer radical completando cuadrados:

\[
x^2+y^2-80x-100y+4100=(x-40)^2+(y-50)^2.
\]

Entonces la expresión es

\[
\sqrt{x^2+20^2}+\sqrt{30^2+y^2}+\sqrt{(40-x)^2+(50-y)^2}.
\]

Consideremos los vectores

\[
\vec a=(x,20),\qquad \vec b=(30,y),\qquad \vec c=(40-x,50-y).
\]

Sus longitudes son exactamente los tres términos de la expresión. Además,

\[
\vec a+\vec b+\vec c=(x+30+40-x,\;20+y+50-y)=(70,70).
\]

Por la desigualdad triangular,

\[
\|\vec a\|+\|\vec b\|+\|\vec c\|\ge \|\vec a+\vec b+\vec c\|
=\sqrt{70^2+70^2}=70\sqrt2.
\]

La igualdad ocurre si los tres vectores son paralelos y apuntan en la misma dirección. Como la suma tiene dirección \((1,1)\), necesitamos

\[
(x,20)\parallel(1,1)\implies x=20,
\]
\[
(30,y)\parallel(1,1)\implies y=30,
\]
\[
(40-x,50-y)=(20,20),
\]

lo cual está dentro de las restricciones \(0\le x\le 40\), \(0\le y\le 50\). Por tanto, el mínimo se alcanza en \((x,y)=(20,30)\).

\[
\boxed{70\sqrt{2}}
\]