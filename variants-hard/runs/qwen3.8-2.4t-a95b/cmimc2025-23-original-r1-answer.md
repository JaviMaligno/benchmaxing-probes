Coloquemos coordenadas en el plano de modo que

\[
A=(0,0),\qquad B=(1,0).
\]

### 1. Puntos \(C\) y \(D\)

Los círculos \(\odot A\) y \(\odot B\) tienen radio \(1\), así que sus ecuaciones son

\[
x^2+y^2=1,\qquad (x-1)^2+y^2=1.
\]

Restando ambas ecuaciones se obtiene \(x=\frac12\). Luego

\[
y^2=1-\frac14=\frac34,
\]

de modo que los puntos de intersección son

\[
\left(\frac12,\pm \frac{\sqrt3}{2}\right).
\]

Sin pérdida de generalidad, tomamos

\[
C=\left(\frac12,\frac{\sqrt3}{2}\right),\qquad
D=\left(\frac12,-\frac{\sqrt3}{2}\right).
\]

Entonces

\[
CD=\sqrt3.
\]

### 2. Puntos \(E\) y \(F\)

Ahora dibujamos los círculos centrados en \(C\) y \(D\) con radio \(CD=\sqrt3\). Sus intersecciones están sobre la mediatriz de \(CD\), que es la recta \(AB\), es decir, el eje \(x\).

Sea \((x,0)\) una de estas intersecciones. Su distancia a \(C\) debe ser \(\sqrt3\):

\[
\left(x-\frac12\right)^2+\left(0-\frac{\sqrt3}{2}\right)^2=3.
\]

Así,

\[
\left(x-\frac12\right)^2+\frac34=3
\]

\[
\left(x-\frac12\right)^2=\frac94,
\]

por lo que

\[
x-\frac12=\pm \frac32.
\]

Entonces \(x=-1\) o \(x=2\). Como el orden pedido es \(E,A,B,F\), tenemos

\[
E=(-1,0),\qquad F=(2,0).
\]

Por tanto,

\[
EF=3.
\]

### 3. Punto \(H\)

Los círculos \(\odot E\) y \(\odot F\) tienen radio \(EF=3\). Sus centros son \((-1,0)\) y \((2,0)\), así que sus intersecciones están sobre la mediatriz de \(EF\), que es la recta vertical \(x=\frac12\).

Sea \(\left(\frac12,y\right)\) una intersección. Su distancia a \(E=(-1,0)\) es \(3\):

\[
\left(\frac12+1\right)^2+y^2=9.
\]

Es decir,

\[
\left(\frac32\right)^2+y^2=9,
\]

\[
\frac94+y^2=9,
\]

\[
y^2=\frac{27}{4}.
\]

Por tanto,

\[
y=\pm \frac{3\sqrt3}{2}.
\]

Como \(C\) está por encima de la recta \(AB\) y \(H\) debe estar en el lado opuesto, tomamos

\[
H=\left(\frac12,-\frac{3\sqrt3}{2}\right).
\]

### 4. Área del pentágono \(ACFHE\)

Los vértices, en el orden pedido, son

\[
A=(0,0),\quad
C=\left(\frac12,\frac{\sqrt3}{2}\right),\quad
F=(2,0),\quad
H=\left(\frac12,-\frac{3\sqrt3}{2}\right),\quad
E=(-1,0).
\]

Usamos la fórmula de los cordones:

\[
\sum x_i y_{i+1}
=
0\cdot \frac{\sqrt3}{2}
+\frac12\cdot 0
+2\cdot\left(-\frac{3\sqrt3}{2}\right)
+\frac12\cdot 0
+(-1)\cdot 0
=
-3\sqrt3,
\]

\[
\sum y_i x_{i+1}
=
0\cdot \frac12
+\frac{\sqrt3}{2}\cdot 2
+0\cdot \frac12
+\left(-\frac{3\sqrt3}{2}\right)\cdot(-1)
+0\cdot 0
=
\frac{5\sqrt3}{2}.
\]

Por tanto, el área es

\[
\frac12\left|-3\sqrt3-\frac{5\sqrt3}{2}\right|
=
\frac12\cdot \frac{11\sqrt3}{2}
=
\frac{11\sqrt3}{4}.
\]

\[
\boxed{\frac{11\sqrt{3}}{4}}
\]