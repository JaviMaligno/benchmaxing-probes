

Parametricemos la parábola original como

\[
P(s)=(s,s^2-5).
\]

Sea \(R\) la rotación de \(60^\circ\) en sentido antihorario:

\[
R(u,v)=\left(\frac{u}{2}-\frac{\sqrt3\,v}{2},\frac{\sqrt3\,u}{2}+\frac{v}{2}\right).
\]

Si \(P(x)=(x,x^2-5)\) es un punto de intersección con la parábola rotada, entonces existe \(t\) tal que

\[
P(x)=R(P(t)).
\]

Como una rotación preserva la distancia al origen,

\[
|P(x)|^2=|P(t)|^2.
\]

Ahora

\[
|P(s)|^2=s^2+(s^2-5)^2=s^4-9s^2+25.
\]

Por tanto,

\[
x^4-9x^2+25=t^4-9t^2+25,
\]

de donde

\[
(x^2-t^2)(x^2+t^2-9)=0.
\]

Así que hay dos posibilidades principales.

---

### Caso 1: \(t=-x\)

El caso \(t=x\) no sirve, porque implicaría que un punto distinto del origen es fijo bajo una rotación de \(60^\circ\).

Si \(t=-x\), entonces

\[
(x,x^2-5)=R(-x,x^2-5).
\]

Mirando la coordenada \(x\):

\[
x=-\frac{x}{2}-\frac{\sqrt3}{2}(x^2-5).
\]

Multiplicando por \(2\):

\[
2x=-x-\sqrt3(x^2-5),
\]

\[
3x=-\sqrt3(x^2-5),
\]

\[
x^2-5=-\sqrt3 x.
\]

Como el punto buscado está en el cuarto cuadrante, debe tener \(x>0\) y \(y<0\). Resolviendo

\[
x^2+\sqrt3 x-5=0,
\]

obtenemos la raíz positiva

\[
x=\frac{\sqrt{23}-\sqrt3}{2}.
\]

La coordenada \(y\) es

\[
y=x^2-5=-\sqrt3 x.
\]

Entonces

\[
y=-\sqrt3\cdot \frac{\sqrt{23}-\sqrt3}{2}
=\frac{3-\sqrt{69}}{2}.
\]

Este punto tiene \(x>0\) y \(y<0\), así que está en el cuarto cuadrante.

---

### Caso 2: \(x^2+t^2=9\)

Este caso no produce puntos en el cuarto cuadrante. Usando las ecuaciones de rotación y \(t^2=9-x^2\), se llega a

\[
3x^2-\sqrt3 x-13=0.
\]

La raíz positiva tiene

\[
x^2=\frac{27+\sqrt{53}}{6}>5,
\]

por lo que \(y=x^2-5>0\), así que no está en el cuarto cuadrante. La raíz negativa tiene \(x<0\), tampoco sirve.

---

Por lo tanto, el único punto del cuarto cuadrante tiene coordenada

\[
y=\frac{3-\sqrt{69}}{2}.
\]

Así,

\[
a=3,\qquad b=69,\qquad c=2,
\]

y

\[
a+b+c=3+69+2=74.
\]

\[
\boxed{74}
\]