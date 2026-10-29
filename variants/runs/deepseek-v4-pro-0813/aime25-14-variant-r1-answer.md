El pentágono es convexo y simétrico respecto a la bisectriz de los ángulos en \(Q\) y \(T\). Voy a razonar la geometría.

**1. Colocar coordenadas**

Tomemos el eje de simetría como el eje \(y\). Los ángulos \(\angle Q=\angle T=60^\circ\) están en los lados horizontales inferiores/superiores. Por la simetría, el pentágono queda:

- \(Q\) en el origen, con \(PQ=38\), \(QR=19\).
- \(\angle Q=60^\circ\): los rayos \(QP\) y \(QR\) forman \(60^\circ\).
- Es más cómodo usar coordenadas.

Pongamos el lado \(PQ\) sobre el eje \(x\), de modo que:

\[
Q=(0,0), \quad P=(38,0).
\]

Como \(\angle Q=60^\circ\) y \(QR=19\), con el pentágono convexo, el punto \(R\) está girado \(60^\circ\) hacia adentro (arriba):

\[
R=(19\cos 60^\circ, 19\sin 60^\circ)=\left(\frac{19}{2}, \frac{19\sqrt3}{2}\right).
\]

Ahora, \(RS=48\). Por simetría con respecto a la bisectriz del pentágono, la figura es:

\[
P=(38,0),\quad Q=(0,0),\quad R=\left(\frac{19}{2},\frac{19\sqrt3}{2}\right),
\]

\[
S=\left(\frac{19}{2},\frac{19\sqrt3}{2}+48\right),\quad T=(0,19\sqrt3+48).
\]

Verifiquemos los lados y ángulos:

- \(QR=19\). ✓
- \(RS=48\) (vertical). ✓
- \(ST=19\): la distancia entre \(S=(\frac{19}{2},\frac{19\sqrt3}{2}+48)\) y \(T=(0,19\sqrt3+48)\) es

\[
\sqrt{\left(\frac{19}{2}\right)^2+\left(\frac{19\sqrt3}{2}\right)^2}
= \sqrt{\frac{361}{4}+\frac{1083}{4}}
= \sqrt{\frac{1444}{4}}=19.
\]

✓

- \(TP=38\): distancia entre \(T=(0,19\sqrt3+48)\) y \(P=(38,0)\):

\[
\sqrt{38^2+(19\sqrt3+48)^2}
\]

no parece \(38\). Necesito ajustar la simetría.

**2. Usar la condición \(TP=38\)**

En realidad, conviene imponer la simetría de forma que \(Q\) y \(T\) estén sobre el eje \(y\). Probemos:

Por simetría, \(Q=(0,a)\), \(T=(0,-a)\) quizá, con los lados \(PQ=TP=38\) y \(QR=ST=19\) simétricos.

Sea:

\[
P=(x,h),\quad Q=(0,q),\quad R=(-u,q+v),\quad S=(-u,-q-v),\quad T=(0,-q)
\]

Alternativamente, es más fácil razonar directamente.

**3. Método del problema: mínimo de la suma de distancias**

La función \(g(Y)=PY+QY+RY+SY+TY\) es la suma de distancias a los 5 vértices. El mínimo de la suma de distancias a varios puntos (el punto de Fermat–Weber generalizado) ocurre en un punto donde la suma de los vectores unitarios desde \(Y\) a cada vértice es cero:

\[
\sum_{i=1}^5 \frac{\vec{V_i Y}}{|V_iY|}=0.
\]

Por la simetría del pentágono respecto al eje \(y\), el minimizador \(Y\) estará sobre el eje de simetría. Sea \(Y=(0,y)\).

Ahora los cinco vértices simétricos son:

Con la construcción correcta, el pentágono es simétrico respecto a la bisectriz de \(Q\) y \(T\). Usemos la siguiente configuración consistente con todos los datos:

El ángulo en \(Q\) es \(60^\circ\), formado por \(PQ\) y \(QR\). El ángulo en \(T\) es \(60^\circ\), formado por \(ST\) y \(TP\). Por la simetría, \(Q\) y \(T\) están en posiciones simétricas respecto al eje \(y\), y los lados \(PQ=TP=38\), \(QR=ST=19\).

Coloquemos el eje de simetría vertical \(x=0\), con:

- \(Q=(19,0)\),
- \(R=(0, h)\), donde \(h=19\sin 60^\circ\) por el lado \(QR=19\) con ángulo en \(Q\) de \(60^\circ\),
- \(P=(0,-a)\): veamos.

Si \(Q=(19,0)\), \(R=(0,h)\). El vector \(\overrightarrow{QR}=(-19,h)\) tiene longitud \(19\):

\[
19^2+h^2=19^2 \implies h=0.
\]

No, error.

**4. Configuración correcta**

Probemos con \(Q=(0,0)\) como antes y calculemos \(T\) ajustando. La clave es que el pentágono es convexo y los ángulos en \(Q\) y \(T\) son \(60^\circ\).

Sea el eje de simetría la recta \(y=x\) quizá no; la simetría debe intercambiar los lados \(PQ=TP\) y \(QR=ST\), es decir, una reflexión respecto a la bisectriz del ángulo en \(S\) (o del pentágono).

Coloquemos \(P\) y \(T\) en el eje \(x\):

- \(P=(0,0)\).
- \(PQ=38\), \(\angle Q=60^\circ\): el giro desde \(PQ\) hacia \(QR\) es \(60^\circ\). Como el pentágono es convexo, \(Q=(38\cos 0 + ?, ...)\). 

Mejor usemos la simetría de reflexión que manda \(P \leftrightarrow T\) y \(Q \leftrightarrow S\), quedando \(R\) fijo.

Entonces \(R\) está en el eje de simetría. Como \(QR=ST=19\) y \(PQ=TP=38\), los puntos opuestos son \(P,T\) y \(Q,S\).

Coloquemos el eje de simetría como el eje \(y\), con \(R\) sobre él. Los ángulos en \(Q\) y \(T\) son \(60^\circ\).

Pongamos:

\[
R=(0,r).
\]

Dado \(QR=19\) y \(\angle Q=60^\circ\), y por simetría \(S\) es el reflejo de \(Q\) respecto al eje \(y\): \(Q=(-x_Q, y_Q)\), \(S=(x_Q, y_Q)\).

Análogamente \(P=(-x_P, y_P)\), \(T=(x_P, y_P)\).

Además \(PQ=38\) y \(TP=38\) automáticamente por reflexión.

Ahora usemos \(QR=19\) y \(PQ=38\) junto con los ángulos.

Sea \(Q=(-a,0)\) por conveniencia (está en \(y=0\)). Como \(R=(0,r)\), entonces:

\[
QR=\sqrt{a^2+r^2}=19.
\]

El ángulo en \(Q\) es entre \(QP\) y \(QR\). El vector \(\overrightarrow{QP}=P-Q=(-x_P+a, y_P)\), y \(\overrightarrow{QR}=(a,r)\).

Por el ángulo de \(60^\circ\):

\[
\cos 60^\circ=\frac{\overrightarrow{QP}\cdot \overrightarrow{QR}}{|QP|\,|QR|}
=\frac{(-x_P+a)a+y_P r}{38\cdot 19}.
\]

Para simplificar, pongamos \(P=(0,0)\) quizá no. La simetría no es sobre el eje vertical si fijamos \(Q\) en \(y=0\).

**5. Simplificar con coordenadas concretas**

La forma más sencilla: notemos que dos lados iguales (\(PQ=TP=38\)) y otros dos (\(QR=ST=19\)), con \(RS=48\). Los ángulos en \(Q\) y \(T\) son \(60^\circ\). Esto sugiere que el pentágono se puede descomponer.

De hecho, podemos pensar el pentágono como una "casa" simétrica:

Construyamos:

- \(P=(0,0)\), \(Q=(38,0)\).
- En \(Q\), el ángulo interior es \(60^\circ\). Como \(QR=19\), y \(R\) debe estar "hacia arriba e izquierda" para convexidad:

\[
R=\left(38-19\cos 60^\circ,\ 19\sin 60^\circ\right)
=\left(38-\frac{19}{2}, \frac{19\sqrt3}{2}\right)
=\left(\frac{57}{2}, \frac{19\sqrt3}{2}\right).
\]

- \(RS=48\). ¿Dirección? Para mantener simetría y convexidad, \(S\) debe estar de modo que \(ST=19\) y \(TP=38\) y el ángulo en \(T\) sea \(60^\circ\).

La condición \(TP=38\), con \(T\) tal que \(\angle T=60^\circ\).

Probemos \(S=\left(\frac{57}{2}, \frac{19\sqrt3}{2}+48\right)\), \(T=(38,0)\) más cambios.

Si \(T=(38,0)\) no funciona porque \(TP=38\) sí, \(ST=19\) requiere \(S\) a distancia \(19\) de \(T=(38,0)\).

Con \(S=(\frac{57}{2},\frac{19\sqrt3}{2}+48)\), la distancia a \(T=(38,0)\) es enorme. No.

**6. Configuración definitiva**

Debido a la simetría, la mediatriz de \(PQ\) y \(TP\) no; la figura tiene un eje de simetría que pasa por \(R\) y por el punto medio de \(PT\). Llamemos \(A\) al punto medio de \(P\) y \(T\). La distancia \(PT\) es el doble de la proyección.

Tomemos como eje de simetría vertical, con \(R\) en la parte superior sobre el eje \(x=0\), y \(P\), \(T\) abajo simétricos, \(Q\), \(S\) intermedios simétricos.

Geometría con triángulos:

Sea \(R=(0,h_R)\). \(Q\) y \(S\) tienen coordenada \(y=h_Q\) con \(x=\pm a\). \(P\) y \(T\) tienen coordenada \(y=h_P\) con \(x=\pm b\).

Los lados:

- \(RS=48\): distancia entre \((0,h_R)\) y \((a,h_Q)\):

\[
a^2+(h_R-h_Q)^2=48^2. \tag{1}
\]

- \(QR=19\): distancia entre \((-a,h_Q)\) y \((0,h_R)\):

\[
a^2+(h_R-h_Q)^2=19^2.
\]

¡Contradicción con (1)! No puede ser.

Entonces \(R\) no está sobre el mismo eje con \(Q,S\). Reconsideremos.

Los lados \(QR=19\), \(RS=48\), \(ST=19\) forman una cadena. El lado \(RS=48\) es largo comparado con \(QR=ST=19\). La simetría no manda \(Q\leftrightarrow S\), sino \(Q\leftrightarrow T\) y \(P\leftrightarrow S\), o algo así.

**7. Simetría correcta**

Dados \(PQ=TP=38\) (lados extremos iguales) y \(QR=ST=19\), y ángulos en \(Q\) y \(T\) iguales (\(60^\circ\)), el pentágono es simétrico bajo reflexión en la mediatriz de \(QT\), que además intercambia \(P\leftrightarrow R\) y \(S\) fijo... no exactamente.

La reflexión que intercambia:

- el lado \(PQ\) con \(TP\) (ambos \(38\)),
- el lado \(QR\) con \(ST\) (ambos \(19\)),
- \(R\) con \(S\),

es la reflexión respecto a la mediatriz de \(RS\), que también es la mediatriz de \(QT\). Ese eje pasa por el punto medio de \(RS\) y es perpendicular a \(RS\).

Entonces \(RS\) es perpendicular al eje de simetría, y \(R,S\) son simétricos. El lado \(RS=48\) es horizontal, y el eje de simetría es vertical.

Coloquemos:

\[
R=(-24,0),\quad S=(24,0),
\]

de modo que \(RS=48\) y el eje de simetría es \(x=0\).

Como \(QR=ST=19\), con \(Q\) y \(T\) simétricos respecto al eje \(x=0\):

\[
Q=(a, b),\quad T=(-a, b).
\]

La distancia \(QR=19\):

\[
(a+24)^2+b^2=19^2. \tag{2}
\]

La distancia \(ST=19\):

\[
(-a-24)^2+b^2=19^2 \quad \text{(= $(a+24)^2+b^2=361$), mismo resultado.} 
\]

✓ consistente.

Luego los lados \(PQ=38\) y \(TP=38\). Como \(P\) debe ser simétrico a sí mismo (sobre eje \(x=0\)):

\[
P=(0,c).
\]

Distancia \(PQ=38\):

\[
a^2+(b-c)^2=38^2. \tag{3}
\]

Distancia \(TP=38\):

\[
(-a)^2+(b-c)^2=38^2 \quad \text{(= (3)).} ✓
\]

Ahora usemos los ángulos.

**Ángulo en \(Q\)**: entre \(QP\) y \(QR\).

\[
\overrightarrow{QP}=(0-a, c-b)=(-a, c-b),
\]
\[
\overrightarrow{QR}=(-24-a, -b).
\]

Producto punto:

\[
\overrightarrow{QP}\cdot \overrightarrow{QR}=(-a)(-24-a)+(c-b)(-b)
=a^2+24a -b(c-b).
\]

Normas: \(|QP|=38\), \(|QR|=19\).

Como \(\angle Q=60^\circ\):

\[
\cos 60^\circ=\frac12=\frac{a^2+24a-b(c-b)}{38\cdot 19}.
\]

es decir,

\[
a^2+24a-b(c-b)=361. \tag{4}
\]

**Ángulo en \(T\)**: entre \(TP\) y \(TS\).

\[
\overrightarrow{TP}=(0-(-a), c-b)=(a, c-b),
\]
\[
\overrightarrow{TS}=(24-(-a), 0-b)=(24+a, -b).
\]

Producto punto:

\[
a(24+a)+(c-b)(-b)=24a+a^2-b(c-b).
\]

Normas \(|TP|=38\), \(|TS|=19\). Ángulo \(60^\circ\):

\[
\frac12=\frac{24a+a^2-b(c-b)}{38\cdot 19}.
\]

Se obtiene la misma ecuación:

\[
a^2+24a-b(c-b)=361. \tag{5}
\]

✓ consistente con (4), como se esperaba por simetría.

**8. Resolver el sistema**

De (2):

\[
(a+24)^2+b^2=361. \tag{2}
\]

De (4):

\[
a^2+24a-b(c-b)=361.
\]

Notemos que \(a^2+24a=(a+24)^2-576\), pero sigamos.

De (3):

\[
a^2+(b-c)^2=1444. \tag{3}
\]

Sea \(d=c-b\). Entonces \(c-b=d\).

(4) queda:

\[
a^2+24a-bd=361. \tag{4'}
\]

(3) queda:

\[
a^2+d^2=1444. \tag{3'}
\]

(2):

\[
(a+24)^2+b^2=361. \tag{2}
\]

Necesitamos \(a,b,d\).

De (4'):

\[
bd=a^2+24a-361.
\]

De (3'):

\[
d^2=1444-a^2.
\]

Como \(RS=48\) es el lado horizontal en la base de la figura, y el pentágono es convexo, la orientación indica \(b>0\) (los vértices \(Q,T\) están por encima de \(RS\)) y \(d\) probablemente negativo (\(P\) por debajo de \(Q,T\)), así que \(d<0\), \(b>0\).

De (2): \((a+24)^2+b^2=361\), con \(b>0\). Entonces \(a+24\) debe ser menor que \(19\) en valor absoluto:

\[
|a+24|<19 \implies -43<a<-5.
\]

Como \(RS\) va de \(x=-24\) a \(x=24\), y \(Q\) a la derecha de \(R\), probablemente \(a\) está cerca de \(-24\) por la izquierda (lado \(QR\) se eleva a la derecha). Tomemos \(a\) entre \(-43\) y \(-5\).

**9. Calcular \(g(Y)\)**

El punto \(Y\) que minimiza \(g\) está sobre el eje de simetría \(x=0\), digamos \(Y=(0,y)\). Entonces:

- \(PY=|c-y|\).
- \(QY=\sqrt{a^2+(b-y)^2}\).
- \(RY=\sqrt{24^2+y^2}\).
- \(SY=\sqrt{24^2+y^2}\) (por simetría, \(S=(24,0)\)).
- \(TY=\sqrt{a^2+(b-y)^2}\).

Entonces:

\[
g(y)=|c-y|+2\sqrt{a^2+(b-y)^2}+2\sqrt{576+y^2}.
\]

Donde \(c=b+d\).

Para minimizar, derivando:

\[
g'(y)=\operatorname{sgn}(y-c)+2\frac{y-b}{\sqrt{a^2+(y-b)^2}}+2\frac{y}{\sqrt{576+y^2}}.
\]

En el mínimo, si \(y\) está entre \(c\) y \(b\) (probable), \(\operatorname{sgn}(y-c)=-1\) (si \(y<c\)) o \(+1\). El punto óptimo típico de 5 puntos simétricos puede estar en \(y=0\) quizá.

Probemos \(y=0\). Entonces:

- \(RY=SY=24\).
- \(QY=TY=\sqrt{a^2+b^2}\).

De (2): \(a^2+b^2=361-48a-576\)... calculemos:

\[
a^2+b^2=(a+24)^2+b^2-48a-576=361-48a-576=-215-48a.
\]

Como \(a<0\), esto es positivo.

Además \(PY=|c|=|b+d|\). De las ecuaciones, quizá \(c\) dé algo manejable.

**10. Resolver numéricamente las ecuaciones**

Ecuación (2): \((a+24)^2+b^2=361\).
Ecuación (3'): \(a^2+d^2=1444\).
Ecuación (4'): \(a^2+24a-bd=361\).

Tomemos \(a\) como parámetro.

De (2), \(b=\sqrt{361-(a+24)^2}\). Como \(b>0\).

De (3'), \(d=-\sqrt{1444-a^2}\) (elegimos \(d<0\)).

Sustituimos en (4'):

\[
a^2+24a-bd=361,
\]

con \(bd = -b\sqrt{1444-a^2}\), así que:

\[
a^2+24a+\sqrt{361-(a+24)^2}\sqrt{1444-a^2}=361.
\]

Busquemos \(a\) tal que esto se cumpla con \(a\in(-43,-5)\).

Evaluemos en \(a=-24\):

\(a+24=0\), así que \(b=19\).

\(d=-\sqrt{1444-576}=-\sqrt{868}\approx -29.46\).

Entonces \(bd=19(-29.46)\approx -559.7\).

Lado izquierdo de (4'): \(a^2+24a-bd=576-576+559.7=559.7\). Necesitamos \(361\). Demasiado grande.

Probemos \(a=-12\):

\(a+24=12\), \(b=\sqrt{361-144}=\sqrt{217}\approx 14.73\).

\(d=-\sqrt{1444-144}=-\sqrt{1300}\approx -36.06\).

\(bd\approx -530.9\).

Lado izquierdo: \(144-288+530.9=386.9\). Necesitamos \(361\). Sigue grande.

Probemos \(a=-8\):

\(a+24=16\), \(b=\sqrt{361-256}=\sqrt{105}\approx 10.25\).

\(d=-\sqrt{1444-64}=-\sqrt{1380}\approx -37.15\).

\(bd \approx -380.8\).

Lado izquierdo: \(64-192+380.8=252.8\). Necesitamos \(361\). Ahora muy pequeño.

Entonces la raíz está entre \(a=-12\) y \(a=-8\).

Probemos \(a=-10\):

\(a+24=14\), \(b=\sqrt{361-196}=\sqrt{165}\approx 12.845\).

\(d=-\sqrt{1444-100}=-\sqrt{1344}\approx -36.661\).

\(bd\approx -470.9\).

Lado izquierdo: \(100-240+470.9=330.9\). Necesitamos \(361\). Un poco pequeño.

\(a=-10.5\):

\(a+24=13.5\), \(b=\sqrt{361-182.25}=\sqrt{178.75}\approx 13.369\).

\(d=-\sqrt{1444-110.25}=-\sqrt{1333.75}\approx -36.520\).

\(bd\approx -488.3\).

Lado izquierdo: \(110.25-252+488.3=346.5\). Necesitamos \(361\). Más cerca, aún pequeño.

\(a=-11\):

\(a+24=13\), \(b=\sqrt{361-169}=\sqrt{192}\approx 13.856\).

\(d=-\sqrt{1444-121}=-\sqrt{1323}\approx -36.373\).

\(bd\approx -504.0\).

Lado izquierdo: \(121-264+504.0=361.0\). ¡Exactamente!

Entonces \(a=-11\) es la solución.

Calculemos \(b\) y \(d\):

\[
b=\sqrt{192}=8\sqrt3.
\]

\[
d=-\sqrt{1323}.
\]

Factoricemos \(\sqrt{1323}\):

\[
1323=3^3\cdot 7^2=27\cdot 49=1323.
\]

Así que,

\[
\sqrt{1323}=\sqrt{3^3\cdot 7^2}=21\sqrt3.
\]

Por tanto,

\[
d=-21\sqrt3.
\]

Y \(c=b+d=8\sqrt3-21\sqrt3=-13\sqrt3\).

Así que \(P=(0,-13\sqrt3)\), \(Q=(-11, 8\sqrt3)\), \(R=(-24,0)\), \(S=(24,0)\), \(T=(11,8\sqrt3)\).

Verifiquemos \(PQ=38\):

\[
PQ=\sqrt{11^2+(8\sqrt3+13\sqrt3)^2}
=\sqrt{121+(21\sqrt3)^2}
=\sqrt{121+1323}=\sqrt{1444}=38.
\]

✓

**11. Calcular el mínimo de \(g(Y)\)**

Con \(Y=(0,y)\):

\[
g(y)=| -13\sqrt3-y|+2\sqrt{121+(8\sqrt3-y)^2}+2\sqrt{576+y^2}.
\]

Probemos \(y=0\) como candidato. El gradiente en \(y=0\) debe anularse. Derivada en \(y=0\) (usando \(\operatorname{sgn}(y-c)\) con \(c=-13\sqrt3\), para \(y=0\), \(y-c=13\sqrt3>0\), así que signo \(+\)):

La derivada de \(|c-y|\) respecto a \(y\) es \(-1\) para \(y<c\). Como \(0>-13\sqrt3\), \(y>c\), y \(\operatorname{sgn}(y-c)=+1\), es decir la derivada de \(|c-y|\) es \(+1\).

Derivada de \(2\sqrt{121+(8\sqrt3-y)^2}\): respecto a \(y\) es

\[
2\frac{y-8\sqrt3}{\sqrt{121+(y-8\sqrt3)^2}}.
\]

En \(y=0\): \( \frac{2(0-8\sqrt3)}{\sqrt{121+192}} =\frac{-16\sqrt3}{\sqrt{313}}\).

Derivada de \(2\sqrt{576+y^2}\): en \(y=0\) es \(0\).

Suma en \(y=0\):

\[
g'(0)=1-\frac{16\sqrt3}{\sqrt{313}}.
\]

No es cero. Entonces \(y=0\) no es el mínimo.

**12. Resolver la condición de primer orden**

Sea \(c=-13\sqrt3\), \(b=8\sqrt3\), \(a=-11\) (usamos \(|a|=11\)).

Para \(y\) entre \(c\) y \(b\), la derivada:

\[
g'(y)=-1+2\frac{y-b}{\sqrt{121+(y-b)^2}}+2\frac{y}{\sqrt{576+y^2}}=0.
\]

Hagamos el cambio \(u=y-b\), de modo que \(u<0\) (para \(y<b\)), y \(y=u+b\).

\[
-1+2\frac{u}{\sqrt{121+u^2}}+2\frac{u+b}{\sqrt{576+(u+b)^2}}=0.
\]

Con \(b=8\sqrt3\). Probemos valores.

Si \(u=-11\), entonces \(y=b-11=8\sqrt3-11\approx 2.856\).

Evaluemos:

\[
\frac{u}{\sqrt{121+u^2}}=\frac{-11}{\sqrt{121+121}}=\frac{-11}{11\sqrt2}=-\frac1{\sqrt2}.
\]

Entonces \(2\cdot(-1/\sqrt2)=-\sqrt2\approx -1.414\).

Además \(y=8\sqrt3-11\approx 13.856-11=2.856\).

\[
\sqrt{576+y^2}\approx \sqrt{576+8.157}=24.17,
\]

así que \(2y/\sqrt{576+y^2}\approx 2(2.856)/24.17=0.236\).

Suma: \(-1-1.414+0.236=-2.178\), negativo. Necesitamos más \(y\).

Probemos \(u=0\), \(y=b=8\sqrt3\approx 13.856\).

Primer término: \(2\cdot 0=0\).

Segundo: \(2y/\sqrt{576+y^2}\approx 2(13.856)/\sqrt{576+192}=27.71/\sqrt{768}=27.71/27.71=1\).

Suma: \(-1+0+1=0\).

¡Perfecto! Entonces \(y=b=8\sqrt3\) es la solución.

Con \(y=b\), \(QY=TY=\sqrt{121+0}=11\), y \(PY=|c-b|=|-13\sqrt3-8\sqrt3|=21\sqrt3\).

Además \(RY=SY=\sqrt{576+(8\sqrt3)^2}=\sqrt{576+192}=\sqrt{768}=16\sqrt3\).

Entonces:

\[
g_{\min}=PY+2QY+2RY
=21\sqrt3+2(11)+2(16\sqrt3)
=22+21\sqrt3+32\sqrt3
=22+53\sqrt3.
\]

Por tanto,

\[
m=22,\quad n=53,\quad p=3.
\]

\[
m+n+p=22+53+3=78.
\]

\[
\boxed{78}
\]