

Coloquemos \(B=(0,0)\) y \(C=(7,0)\). Como \(AB=6\) y \(AC=8\), las coordenadas de \(A\) son

\[
A=\left(\frac{3}{2},\frac{3\sqrt{15}}{2}\right).
\]

Sea \(P=(x,y)\), con \(y>0\) porque \(P\) está dentro del triángulo.

Por la condición \(\frac{BP}{PC}=\frac12\), tenemos \(PC=2BP\). Entonces

\[
(x-7)^2+y^2=4(x^2+y^2),
\]

que se simplifica a

\[
3x^2+3y^2+14x-49=0. \tag{1}
\]

Ahora usamos \(\angle ABP=\angle ACP\). Como los ángulos son iguales, sus cosenos son iguales.

Para \(\angle ABP\):

\[
\cos \angle ABP
=
\frac{\overrightarrow{BA}\cdot \overrightarrow{BP}}{|BA||BP|}
=
\frac{x+\sqrt{15}y}{4BP}.
\]

Para \(\angle ACP\), usando \(PC=2BP\):

\[
\cos \angle ACP
=
\frac{\overrightarrow{CA}\cdot \overrightarrow{CP}}{|CA||CP|}
=
\frac{-11x+77+3\sqrt{15}y}{32BP}.
\]

Igualando:

\[
\frac{x+\sqrt{15}y}{4}
=
\frac{-11x+77+3\sqrt{15}y}{32}.
\]

Esto da

\[
19x+5\sqrt{15}y=77. \tag{2}
\]

De (2),

\[
y=\frac{77-19x}{5\sqrt{15}}.
\]

Sustituyendo en (1):

\[
184x^2-294x-49=0.
\]

Las raíces son

\[
x=\frac{161}{92}
\qquad\text{o}\qquad
x=-\frac{7}{46}.
\]

Como \(P\) está dentro del triángulo, tomamos \(x=\frac{161}{92}\). Entonces

\[
y=\frac{805}{92\sqrt{15}}.
\]

Los triángulos \(BPC\) y \(ABC\) comparten la base \(BC\), así que la razón de sus áreas es la razón de sus alturas sobre \(BC\):

\[
\frac{[BPC]}{[ABC]}
=
\frac{y}{\frac{3\sqrt{15}}{2}}
=
\frac{\frac{805}{92\sqrt{15}}}{\frac{3\sqrt{15}}{2}}
=
\frac{7}{18}.
\]

\[
\boxed{\frac{7}{18}}
\]