

Coloquemos coordenadas: sea \(Y=(0,0)\), \(Z=(6,0)\). Como \(XY=5\) y \(XZ=7\), si \(X=(a,h)\),

\[
a^2+h^2=25,\qquad (a-6)^2+h^2=49.
\]

Restando, \(-12a+36=24\), así que \(a=1\) y \(h=2\sqrt6\). Luego

\[
X=(1,2\sqrt6).
\]

Sea \(Q=(u,v)\), con \(v>0\). La razón pedida es

\[
t=\frac{[YQZ]}{[XYZ]}=\frac{\frac12\cdot 6\cdot v}{\frac12\cdot 6\cdot 2\sqrt6}
=\frac{v}{2\sqrt6}.
\]

Así, \(v=2\sqrt6\,t\).

Por la condición \(\frac{YQ}{QZ}=\frac12\), tenemos \(QZ=2YQ\). Entonces

\[
(u-6)^2+v^2=4(u^2+v^2).
\]

Simplificando,

\[
u^2+v^2+4u-12=0.
\]

Sustituyendo \(v=2\sqrt6\,t\),

\[
u^2+24t^2+4u-12=0. \tag{1}
\]

Ahora usamos \(\angle XYQ=\angle XZQ\). Igualando cosenos:

\[
\cos\angle XYQ
=
\frac{(1,2\sqrt6)\cdot(u,v)}{5\,YQ}
=
\frac{u+2\sqrt6\,v}{5\,YQ}
=
\frac{u+24t}{5\,YQ}.
\]

Por otro lado,

\[
\cos\angle XZQ
=
\frac{(-5,2\sqrt6)\cdot(u-6,v)}{7\,QZ}
=
\frac{-5u+30+24t}{14\,YQ}.
\]

Igualando:

\[
\frac{u+24t}{5}
=
\frac{-5u+30+24t}{14}.
\]

Esto da

\[
14u+336t=-25u+150+120t,
\]

\[
39u+216t=150,
\]

\[
13u+72t=50. \tag{2}
\]

De (2),

\[
u=\frac{50-72t}{13}.
\]

Sustituyendo en (1):

\[
\left(\frac{50-72t}{13}\right)^2
+4\left(\frac{50-72t}{13}\right)-12+24t^2=0.
\]

Multiplicando por \(169\) y simplificando:

\[
385t^2-456t+128=0.
\]

Las raíces son

\[
t=\frac{456\pm104}{770},
\]

es decir,

\[
t=\frac{8}{11}\quad\text{o}\quad t=\frac{16}{35}.
\]

La raíz \(t=\frac{8}{11}\) corresponde a \(u=-\frac{2}{11}<0\), fuera del triángulo. La raíz válida para \(Q\) interior es

\[
t=\frac{16}{35}.
\]

\[
\boxed{\frac{16}{35}}
\]