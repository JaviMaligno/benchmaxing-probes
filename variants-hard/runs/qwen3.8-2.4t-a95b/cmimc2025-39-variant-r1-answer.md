

Tomamos los vértices de cada cuadrado en orden cíclico: \(ABXY\) significa \(A\to B\to X\to Y\), y análogamente para los otros.

Colocamos
\[
A=(0,0),\qquad B=(80,0).
\]
Sea \(C=(x,y)\) con \(y>0\). Como \(AC=102\) y \(BC=26\),
\[
x^2+y^2=102^2,\qquad (x-80)^2+y^2=26^2.
\]
Restando,
\[
160x-6400=102^2-26^2=9728,
\]
de donde
\[
x=\frac{504}{5}.
\]
Luego
\[
y^2=102^2-\left(\frac{504}{5}\right)^2=\frac{6084}{25},
\]
así que
\[
C=\left(\frac{504}{5},\frac{78}{5}\right).
\]

Ahora hallamos los vértices exteriores de los cuadrados.

- En \(AB\), el triángulo está arriba de \(AB\), por lo que el cuadrado exterior está abajo:
\[
X=(80,-80),\qquad Y=(0,-80).
\]

- Para \(BC\), el vector es
\[
\overrightarrow{BC}=\left(\frac{104}{5},\frac{78}{5}\right).
\]
El exterior está a la derecha de \(B\to C\), así que rotamos este vector \(90^\circ\) en sentido horario:
\[
\left(\frac{78}{5},-\frac{104}{5}\right).
\]
Por tanto,
\[
P=C+\left(\frac{78}{5},-\frac{104}{5}\right)
=\left(\frac{582}{5},-\frac{26}{5}\right),
\]
\[
Q=B+\left(\frac{78}{5},-\frac{104}{5}\right)
=\left(\frac{478}{5},-\frac{104}{5}\right).
\]

- Para \(AC\), el vector es
\[
\overrightarrow{AC}=\left(\frac{504}{5},\frac{78}{5}\right).
\]
El exterior está a la izquierda de \(A\to C\), así que rotamos \(90^\circ\) en sentido antihorario:
\[
\left(-\frac{78}{5},\frac{504}{5}\right).
\]
Por tanto,
\[
M=C+\left(-\frac{78}{5},\frac{504}{5}\right)
=\left(\frac{426}{5},\frac{582}{5}\right),
\]
\[
N=A+\left(-\frac{78}{5},\frac{504}{5}\right)
=\left(-\frac{78}{5},\frac{504}{5}\right).
\]

Los puntos medios son:
\[
L_1=\frac{M+P}{2}
=\left(\frac{504}{5},\frac{278}{5}\right),
\]
\[
L_2=\frac{Q+X}{2}
=\left(\frac{439}{5},-\frac{252}{5}\right),
\]
\[
L_3=\frac{N+Y}{2}
=\left(-\frac{39}{5},\frac{52}{5}\right).
\]

Usamos el determinante para el área de \(L_1L_2L_3\). Tomando vectores desde \(L_1\),
\[
L_2-L_1=(-13,-106),
\]
\[
L_3-L_1=\left(-\frac{543}{5},-\frac{226}{5}\right).
\]
Entonces
\[
\left|\det\right|
=
\left|
(-13)\left(-\frac{226}{5}\right)
-
(-106)\left(-\frac{543}{5}\right)
\right|.
\]
\[
=
\left|
\frac{2938}{5}-\frac{57558}{5}
\right|
=
10924.
\]
El área es la mitad:
\[
\frac{10924}{2}=5462.
\]

\[
\boxed{5462}
\]