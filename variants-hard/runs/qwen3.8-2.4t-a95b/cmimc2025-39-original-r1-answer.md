

Tomemos \(A,B,C\) en sentido antihorario y sea \(J\) la rotación de \(90^\circ\) en sentido antihorario. Los cuadrados se nombran cíclicamente: en \(ABXY\), \(X\) es adyacente a \(B\) y \(Y\) a \(A\), etc.

Para los cuadrados exteriores:

\[
X=B-J(B-A),\quad Y=A-J(B-A),
\]
\[
P=C-J(C-B),\quad Q=B-J(C-B).
\]

En el cuadrado sobre \(AC\), al recorrer \(A\to C\), el interior del triángulo queda a la derecha, así que el exterior queda a la izquierda:

\[
M=C+J(C-A),\quad N=A+J(C-A).
\]

Los puntos medios son:

\[
L_1=\frac{M+P}{2}=C+\frac12J(B-A),
\]
\[
L_2=\frac{Q+X}{2}=B-\frac12J(C-A),
\]
\[
L_3=\frac{N+Y}{2}=A+\frac12J(C-B).
\]

Traslademos \(A\) al origen y definamos \(u=B-A\), \(v=C-A\). Entonces:

\[
L_1=v+\frac12Ju,\qquad
L_2=u-\frac12Jv,\qquad
L_3=\frac12J(v-u).
\]

Sea \(K=u\times v=2[ABC]\), donde \(\times\) denota el determinante 2D. Usando

\[
x\times Jy=x\cdot y,\qquad Jx\times y=-x\cdot y,\qquad Jx\times Jy=x\times y,
\]

calculamos:

\[
L_1-L_3=v-\frac12Jv+Ju,
\]
\[
L_2-L_3=u+\frac12Ju-Jv.
\]

Entonces,

\[
(L_1-L_3)\times(L_2-L_3)
=
u\cdot v-|u|^2-|v|^2-\frac74K.
\]

Al tomar valor absoluto,

\[
[L_1L_2L_3]
=
\frac12\left(|u|^2+|v|^2-u\cdot v+\frac74K\right).
\]

Como

\[
|u|^2+|v|^2-u\cdot v
=
\frac{|u|^2+|v|^2+|v-u|^2}{2}
=
\frac{AB^2+AC^2+BC^2}{2},
\]

y \(K=2[ABC]\), obtenemos la fórmula

\[
[L_1L_2L_3]
=
\frac{AB^2+BC^2+CA^2}{4}
+
\frac74[ABC].
\]

Ahora calculamos \([ABC]\) por Herón. El semiperímetro es

\[
s=\frac{78+50+112}{2}=120.
\]

\[
[ABC]=\sqrt{120(120-78)(120-50)(120-112)}
=\sqrt{120\cdot42\cdot70\cdot8}=1680.
\]

Además,

\[
78^2+50^2+112^2=6084+2500+12544=21128.
\]

Por tanto,

\[
[L_1L_2L_3]
=
\frac{21128}{4}+\frac74\cdot1680
=
5282+2940
=
8222.
\]

\[
\boxed{8222}
\]