Por la ley de cosenos en \(\triangle PQR\),
\[
PR^2=38^2+19^2-2(38)(19)\cos60^\circ=1083,
\]
de modo que \(PR=19\sqrt3\). Análogamente, \(PS=19\sqrt3\).

Como \(RS=48\), la altura de \(P\) a \(RS\) es
\[
\sqrt{PR^2-24^2}=\sqrt{1083-576}=13\sqrt3.
\]
Podemos por tanto situar
\[
P=(0,0),\qquad R=(-24,-13\sqrt3),\qquad S=(24,-13\sqrt3).
\]
Las condiciones de longitud y convexidad dan entonces
\[
Q=(-37,-5\sqrt3),\qquad T=(37,-5\sqrt3).
\]

Consideremos el punto \(O=(0,-5\sqrt3)\). Sus distancias a los vértices son
\[
OP=5\sqrt3,\qquad OQ=OT=37,
\]
y
\[
OR=OS=\sqrt{24^2+(8\sqrt3)^2}=16\sqrt3.
\]
Así,
\[
g(O)=5\sqrt3+2(37)+2(16\sqrt3)=74+37\sqrt3.
\]

Para comprobar que es el mínimo, observemos que \(g\) es convexa e invariante por reflexión respecto del eje \(x=0\). Por la desigualdad triangular, basta minimizar sobre dicho eje. Escribiendo \(Y=(0,y)\), tenemos
\[
g(Y)=|y|+2\sqrt{37^2+(y+5\sqrt3)^2}
+2\sqrt{24^2+(y+13\sqrt3)^2}.
\]
En \(y=-5\sqrt3\), su derivada es
\[
-1+0+2\frac{8\sqrt3}{16\sqrt3}=0.
\]
Por convexidad, este punto proporciona el mínimo global.

Por tanto, \(m=74\), \(n=37\) y \(p=3\), de donde
\[
\boxed{114}
\]