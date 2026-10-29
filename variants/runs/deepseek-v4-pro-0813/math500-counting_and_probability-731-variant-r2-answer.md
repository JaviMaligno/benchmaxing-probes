El triángulo equilátero \(PQR\) tiene centro \(O\). Como el triángulo es equilátero, \(O\) es a la vez el centroide, el circuncentro y el incentro.

**Paso 1: elegir coordenadas convenientes**

Coloquemos el triángulo en el plano con \(O\) en el origen. Podemos elegir:

\[
P=(1,0),\quad Q=\left(-\frac12,\frac{\sqrt3}{2}\right),\quad R=\left(-\frac12,-\frac{\sqrt3}{2}\right)
\]

Esto es un triángulo equilátero con circunradio \(1\), de modo que \(|OP|=|OQ|=|OR|=1\).

**Paso 2: condición del problema**

Para un punto \(X\), queremos que \(X\) esté más cerca de \(O\) que de cualquiera de los vértices. Esto ocurre si y solo si para cada vértice \(V\in\{P,Q,R\}\):

\[
|XO| < |XV|
\]

Elevando al cuadrado, para \(V\) con \(|OV|=1\):

\[
|XO|^2 < |XV|^2
\]

Si \(X=(x,y)\) y \(V=(v_x,v_y)\), entonces

\[
x^2+y^2 < (x-v_x)^2+(y-v_y)^2
\]

\[
x^2+y^2 < x^2+y^2 - 2(xv_x+yv_y)+1
\]

\[
0 < - 2(xv_x+yv_y)+1
\]

\[
xv_x+yv_y < \frac12
\]

Es decir, \(X\) debe estar en el semiplano que contiene a \(O\) definido por la mediatriz \(xv_x+yv_y=\frac12\) de cada segmento \(OV\).

**Paso 3: interpretación geométrica**

Cada condición \(xv_x+yv_y<\frac12\) corresponde a un semiplano limitado por la mediatriz del segmento \(OV\). Como \(O\) está en el origen, la región donde \(X\) está más cerca de \(O\) que de todos los vértices es la intersección de los tres semiplanos que contienen a \(O\), es decir, un triángulo (en realidad un hexágono o triángulo, según la configuración), formado por las mediatrices de \(OP\), \(OQ\) y \(OR\).

**Paso 4: identificar la región**

Las tres rectas mediatrices son:

\[
x=\frac12,\quad -\frac12 x+\frac{\sqrt3}{2}y=\frac12,\quad -\frac12 x-\frac{\sqrt3}{2}y=\frac12
\]

La intersección de los tres semiplanos correspondientes es el triángulo con vértices en los puntos medios de \(OP\), \(OQ\), \(OR\), es decir, un triángulo equilátero con vértices:

\[
\left(\frac12,0\right),\quad \left(-\frac14,\frac{\sqrt3}{4}\right),\quad \left(-\frac14,-\frac{\sqrt3}{4}\right)
\]

Este es el triángulo medial de \(OPQ\) y \(OPR\), con centro en \(O\). De hecho, es un triángulo equilátero semejante al original, pero con razón de semejanza \(\frac12\), y su orientación es la misma que la del triángulo \(PQR\), pero está "invertido" respecto de las mediatrices consideradas.

**Paso 5: cálculo del área**

El triángulo \(PQR\) original tiene circunradio \(1\). Su área es:

\[
\text{Área}(PQR)=\frac{3\sqrt3}{4}\cdot 1^2=\frac{3\sqrt3}{4}
\]

(Para un triángulo equilátero con circunradio \(R\), el lado es \(R\sqrt3\), y el área es \(\frac{\sqrt3}{4}(R\sqrt3)^2=\frac{3\sqrt3}{4}R^2\).)

El triángulo pequeño de puntos más cercanos a \(O\) es semejante al original con razón de semejanza \(1/2\). Su área es:

\[
\text{Área}(\text{región favorable})=\left(\frac12\right)^2\cdot \frac{3\sqrt3}{4}=\frac{3\sqrt3}{16}
\]

**Paso 6: probabilidad**

La probabilidad es el cociente de áreas:

\[
\frac{\text{Área}(\text{región favorable})}{\text{Área}(PQR)}
=
\frac{\frac{3\sqrt3}{16}}{\frac{3\sqrt3}{4}}
=
\frac{1}{4}
\]

Por lo tanto, la probabilidad es:

\[
\boxed{\frac14}
\]