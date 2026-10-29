

Sea \(P=(x,y)\) un punto de intersección entre la parábola original y su imagen rotada \(60^\circ\) en sentido antihorario.

Como \(P\) está en la parábola original,

\[
y=x^2-5.
\]

Además, si \(P\) está en la imagen rotada, entonces al rotar \(P\) en \(-60^\circ\) debe obtenerse un punto de la parábola original. Sea

\[
Q=R_{-60^\circ}(P)=(u,v).
\]

Usando \(\cos 60^\circ=\frac12\) y \(\sin 60^\circ=\frac{\sqrt3}{2}\),

\[
u=\frac{x}{2}+\frac{\sqrt3\,y}{2},
\qquad
v=-\frac{\sqrt3\,x}{2}+\frac{y}{2}.
\]

Como \(Q\) está en la parábola,

\[
v=u^2-5.
\]

Por tanto,

\[
u^2=v+5=-\frac{\sqrt3\,x}{2}+\frac{y}{2}+5.
\]

También, como \(y=x^2-5\), tenemos \(x^2=y+5\). Restando,

\[
u^2-x^2=-\frac{\sqrt3\,x}{2}-\frac{y}{2}
=-\frac{\sqrt3 x+y}{2}.
\]

Pero

\[
u^2-x^2=(u-x)(u+x).
\]

Calculamos

\[
u-x=\frac{\sqrt3 y-x}{2},
\]

y

\[
u+x=\frac{3x+\sqrt3 y}{2}
=\frac{\sqrt3(\sqrt3 x+y)}{2}.
\]

Así,

\[
\frac{\sqrt3}{4}(\sqrt3 y-x)(\sqrt3 x+y)
=-\frac12(\sqrt3 x+y).
\]

Factorizando,

\[
(\sqrt3 x+y)\left(\sqrt3(\sqrt3 y-x)+2\right)=0.
\]

Entonces hay dos casos.

**Caso 1:** \(\sqrt3 x+y=0\), es decir,

\[
y=-\sqrt3 x.
\]

Sustituyendo en \(y=x^2-5\),

\[
x^2-5=-\sqrt3 x
\]

\[
x^2+\sqrt3 x-5=0.
\]

Luego

\[
x=\frac{-\sqrt3\pm\sqrt{23}}{2}.
\]

Para estar en el cuarto cuadrante necesitamos \(x>0\), así que

\[
x=\frac{\sqrt{23}-\sqrt3}{2}.
\]

Entonces

\[
y=-\sqrt3 x
=-\sqrt3\cdot \frac{\sqrt{23}-\sqrt3}{2}
=\frac{3-\sqrt{69}}{2}.
\]

Este punto sí está en el cuarto cuadrante.

**Caso 2:**

\[
\sqrt3(\sqrt3 y-x)+2=0
\]

\[
3y-\sqrt3 x+2=0.
\]

Esto no produce ningún punto en el cuarto cuadrante: una solución queda en el primer cuadrante y la otra en el tercer cuadrante.

Por lo tanto, la coordenada \(y\) del único punto de intersección en el cuarto cuadrante es

\[
\frac{3-\sqrt{69}}{2}.
\]

Así,

\[
a=3,\qquad b=69,\qquad c=2.
\]

Como \(a\) y \(c\) son primos relativos,

\[
a+b+c=3+69+2=74.
\]

\[
\boxed{74}
\]