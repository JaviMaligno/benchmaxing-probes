Sea \(E=(0,0)\) y \(D=(13,0)\). Como \(EA=26\) y \(\angle E=60^\circ\), el pentágono convexo da

\[
A=(26\cos 60^\circ,26\sin 60^\circ)=(13,13\sqrt3).
\]

Sea \(B=(x,y)\). De \(AB=14\), \(BC=7\) y \(\angle B=60^\circ\) se obtiene

\[
C=B+\frac12 R_{60^\circ}(A-B)
=\left(\frac{3x+\sqrt3 y-26}{4},\frac{3y-\sqrt3 x+26\sqrt3}{4}\right).
\]

La condición \(CD=24\) con \(D=(13,0)\) da

\[
(x-26)^2+y^2=768.
\]

Junto con

\[
(x-13)^2+(y-13\sqrt3)^2=196
\]

se resuelve, tomando la solución convexa,

\[
B=(26,16\sqrt3),\qquad C=(25,12\sqrt3).
\]

Entonces

\[
BE^2=26^2+(16\sqrt3)^2=676+768=1444=38^2,
\]

así que \(BE=38\).

Además, el triángulo \(ACD\) tiene lados

\[
AC=7\sqrt3,\qquad CD=24,\qquad AD=13\sqrt3.
\]

Su área es

\[
\Delta=\frac12(13\sqrt3)(12)=78\sqrt3.
\]

Para un triángulo cuyos ángulos son todos menores que \(120^\circ\), la suma mínima de distancias a sus vértices, alcanzada en el punto de Fermat, vale

\[
\sqrt{\frac{a^2+b^2+c^2}{2}+2\sqrt3\,\Delta}.
\]

Aplicándolo a \(ACD\):

\[
\frac{AC^2+CD^2+AD^2}{2}
=\frac{147+576+507}{2}=615,
\]

y

\[
2\sqrt3\,\Delta=2\sqrt3\cdot 78\sqrt3=468.
\]

Por tanto,

\[
XA+XC+XD\ge \sqrt{615+468}=\sqrt{1083}=19\sqrt3.
\]

El punto de Fermat de \(ACD\) está sobre el segmento \(BE\), como se comprueba con la construcción usual de triángulos equiláteros exteriores. Así existe un punto \(X\) para el que

\[
XA+XC+XD=19\sqrt3
\]

y simultáneamente

\[
XB+XE=BE=38.
\]

Para cualquier otro punto \(Y\),

\[
YA+YC+YD\ge 19\sqrt3,\qquad YB+YE\ge 38,
\]

de modo que

\[
f(Y)\ge 38+19\sqrt3.
\]

El valor mínimo es, por tanto,

\[
38+19\sqrt3.
\]

Entonces \(m=38\), \(n=19\), \(p=3\), y

\[
\boxed{60}
\]