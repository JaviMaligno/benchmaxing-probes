

Sea
\[
A=x-yz,\qquad B=y-zx,\qquad C=z-xy.
\]
Queremos \(A<B<C\).

Primero factorizamos las desigualdades:

\[
x-yz<y-zx
\iff x-y+zx-yz<0
\iff (x-y)(1+z)<0.
\]

\[
y-zx<z-xy
\iff y-z+xy-zx<0
\iff (y-z)(1+x)<0.
\]

Ahora hacemos el cambio de coordenadas
\[
u=x+1,\qquad v=y+1,\qquad w=z+1.
\]
Entonces
\[
u+v+w=(x+y+z)+3=90,
\]
y las desigualdades se convierten en
\[
(u-v)w<0,\qquad (v-w)u<0.
\]
La desigualdad implicada \(A<C\) equivale también a
\[
(u-w)v<0.
\]

Analizamos los signos posibles de \(u,v,w\). Como \(u+v+w=90>0\), no pueden ser todos negativos. Los casos consistentes con
\[
(u-v)w<0,\qquad (v-w)u<0,\qquad (u-w)v<0
\]
son exactamente tres:

1. \(u,v,w>0\) y \(u<v<w\).
2. \(u<0\), \(v>w>0\).
3. \(u>0\), \(v<w<0\).

Estas son las tres regiones convexas. La única acotada es la primera, pues impone
\[
u>0,\quad v>0,\quad w>0,\quad u+v+w=90.
\]

En el plano \(u+v+w=90\), la región \(u,v,w>0\) es un triángulo equilátero con vértices
\[
(90,0,0),\quad (0,90,0),\quad (0,0,90).
\]
La distancia entre dos vértices cualesquiera es
\[
\sqrt{90^2+90^2}=90\sqrt2,
\]
así que su área es
\[
\frac{\sqrt3}{4}(90\sqrt2)^2
=\frac{\sqrt3}{4}\cdot 16200
=4050\sqrt3.
\]

Las rectas \(u=v\), \(v=w\), \(w=u\) dividen ese triángulo en \(6\) regiones congruentes, una para cada orden de \(u,v,w\). Nuestra región finita corresponde a \(u<v<w\), por lo que su área es
\[
\frac{4050\sqrt3}{6}=675\sqrt3.
\]

Así,
\[
a=675,\qquad b=3,
\]
y por tanto
\[
a+b=678.
\]

\[
\boxed{678}
\]