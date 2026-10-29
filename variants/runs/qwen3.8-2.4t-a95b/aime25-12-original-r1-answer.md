

Sea

\[
x-yz<y-zx<z-xy.
\]

La doble desigualdad equivale a que las dos diferencias consecutas sean positivas:

\[
(y-zx)-(x-yz)>0,\qquad (z-xy)-(y-zx)>0.
\]

Factorizamos cada una:

\[
(y-zx)-(x-yz)=y-x+z(y-x)=(y-x)(1+z),
\]

\[
(z-xy)-(y-zx)=z-y+x(z-y)=(z-y)(1+x).
\]

Así, necesitamos

\[
(y-x)(1+z)>0,\qquad (z-y)(1+x)>0.
\]

Definamos

\[
u=y-x,\qquad v=z-y.
\]

Como \(x+y+z=75\), tenemos

\[
y=x+u,\qquad z=x+u+v,
\]

y por tanto

\[
3x+2u+v=75 \implies x=\frac{75-2u-v}{3}.
\]

Luego

\[
z=\frac{75+u+2v}{3}.
\]

Entonces

\[
1+z=\frac{78+u+2v}{3},\qquad 1+x=\frac{78-2u-v}{3}.
\]

Las desigualdades se convierten en

\[
u(78+u+2v)>0,\qquad v(78-2u-v)>0.
\]

Analizamos los signos de \(u\) y \(v\):

1. Si \(u>0\) y \(v>0\), entonces \(78+u+2v>0\) automáticamente, y necesitamos

\[
78-2u-v>0 \iff 2u+v<78.
\]

Esta región es un triángulo acotado en el plano \((u,v)\).

2. Si \(u>0\) y \(v<0\), se obtiene una región no acotada.

3. Si \(u<0\) y \(v>0\), también se obtiene una región no acotada.

4. Si \(u<0\) y \(v<0\), la segunda desigualdad sería imposible, porque \(78-2u-v>78\).

Por tanto, la única región finita corresponde a

\[
u>0,\qquad v>0,\qquad 2u+v<78.
\]

Sus fronteras son \(u=0\), \(v=0\) y \(2u+v=78\). Los vértices del cierre triangular son:

- \(u=v=0\):

\[
(x,y,z)=(25,25,25).
\]

- \(u=0,\ v=78\):

\[
(x,y,z)=(-1,-1,77).
\]

- \(v=0,\ u=39\):

\[
(x,y,z)=(-1,38,38).
\]

Sean

\[
P=(25,25,25),\quad Q=(-1,-1,77),\quad R=(-1,38,38).
\]

Los vectores desde \(P\) son

\[
\overrightarrow{PQ}=(-26,-26,52),\qquad \overrightarrow{PR}=(-26,13,13).
\]

Su producto cruz es

\[
\overrightarrow{PQ}\times \overrightarrow{PR}=(-1014,-1014,-1014),
\]

cuya norma es

\[
\sqrt{3\cdot 1014^2}=1014\sqrt{3}.
\]

El área del triángulo es la mitad:

\[
\frac{1014\sqrt{3}}{2}=507\sqrt{3}.
\]

Así, \(a=507\) y \(b=3\), con \(b\) libre de cuadrados. Entonces

\[
a+b=507+3=510.
\]

\[
\boxed{510}
\]