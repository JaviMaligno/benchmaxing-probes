Voy a resolver el problema paso a paso.

Tenemos que minimizar para $0 \le x \le 40$ y $0 \le y \le 50$:

\[
\sqrt{x^2 + 400} + \sqrt{y^2 + 900} + \sqrt{x^2 + y^2 - 80x - 100y + 4100}.
\]

Primero, reescribo el tercer radical completando cuadrados:

\[
x^2 + y^2 - 80x - 100y + 4100 = (x-40)^2 + (y-50)^2 + 4100 - 1600 - 2500.
\]

Calculo $4100 - 1600 - 2500 = 0$, por lo que:

\[
x^2 + y^2 - 80x - 100y + 4100 = (x-40)^2 + (y-50)^2.
\]

Además, los otros dos radicales se reescriben como:

\[
\sqrt{x^2 + 400} = \sqrt{x^2 + 20^2},
\]

\[
\sqrt{y^2 + 900} = \sqrt{y^2 + 30^2}.
\]

Así, la expresión es:

\[
\sqrt{x^2 + 20^2} + \sqrt{y^2 + 30^2} + \sqrt{(x-40)^2 + (y-50)^2}.
\]

Interpretación geométrica: queremos minimizar la suma de tres distancias. Tomemos puntos $A=(0,0)$, $B=(40,50)$, $C=(x,y)$ variando en el rectángulo $[0,40]\times[0,50]$.

- $\sqrt{x^2 + 20^2}$ es la distancia de $(x,y)$ al punto $(0,20)$ o $(0,-20)$.
- $\sqrt{y^2 + 30^2}$ es la distancia de $(x,y)$ al punto $(30,0)$ o $(-30,0)$.
- $\sqrt{(x-40)^2+(y-50)^2}$ es la distancia de $(x,y)$ al punto $B=(40,50)$.

Para minimizar la suma de distancias con signos coherentes, consideramos la trayectoria desde $(-30,0)$ pasando por $(0,20)$, luego a $(x,y)$, y finalmente a $(40,50)$. Identifico los puntos:

\[
P = (-30, 0), \quad Q = (0, 20), \quad R = (x, y), \quad S = (40, 50).
\]

La expresión queda:

\[
QR + RS + \text{?}.
\]

Observemos con cuidado la asignación. Buscamos:

\[
\sqrt{(x-0)^2+(y-20)^2} + \sqrt{(x-30)^2+(y-0)^2} + \sqrt{(x-40)^2+(y-50)^2}.
\]

Comparando con la original:

- $\sqrt{x^2 + 400} = \sqrt{(x-0)^2 + (y-20)^2}$ solo si $y=20$, pero $y$ es variable. Esto sugiere otra configuración.

Reintentemos la interpretación geométrica correcta. Los tres términos son distancias:

1. $\sqrt{x^2+20^2}$: distancia del punto $(x,y)$ al punto $(0,20)$ en el plano, pero en realidad es la distancia euclidiana entre $(x,y)$ y $(0,20)$ solo si consideramos que la coordenada vertical fija es $20$, no $y$. La distancia entre $(x,y)$ y $(0,20)$ es $\sqrt{x^2+(y-20)^2}$, no $\sqrt{x^2+20^2}$. Así que $\sqrt{x^2+20^2}$ es la distancia entre $(x,0)$ y $(0,20)$... no, eso también es incorrecto porque implica $y=0$.

En realidad, $\sqrt{x^2+20^2}$ se puede ver como la distancia entre el punto $(x,y)$ en el plano $z=y$ y el punto $(0,0)$ en el plano $z=20$, algo así como una distancia en 3D con una componente fija.

Para aplicar desigualdad triangular o reflexión, conviene tratar cada término de forma más directa usando cálculo.

Planteemos el problema de optimización y usemos condiciones de primer orden.

Definimos:

\[
F(x,y) = \sqrt{x^2+400} + \sqrt{y^2+900} + \sqrt{(x-40)^2+(y-50)^2}.
\]

La región es un rectángulo. Como la función es convexa (suma de normas), el mínimo puede estar en el interior o en la frontera.

Si el mínimo es interior, derivamos:

\[
\frac{\partial F}{\partial x} = \frac{x}{\sqrt{x^2+400}} + \frac{x-40}{\sqrt{(x-40)^2+(y-50)^2}} = 0.
\]

\[
\frac{\partial F}{\partial y} = \frac{y}{\sqrt{y^2+900}} + \frac{y-50}{\sqrt{(x-40)^2+(y-50)^2}} = 0.
\]

De la primera ecuación:

\[
\frac{x}{\sqrt{x^2+400}} = \frac{40-x}{\sqrt{(x-40)^2+(y-50)^2}}.
\]

De la segunda:

\[
\frac{y}{\sqrt{y^2+900}} = \frac{50-y}{\sqrt{(x-40)^2+(y-50)^2}}.
\]

Para $x\in(0,40)$, el lado izquierdo de la primera es positivo, así que $40-x>0$. Similarmente, para $y\in(0,50)$, $50-y>0$.

Sea $D = \sqrt{(x-40)^2+(y-50)^2}$. Entonces:

\[
\frac{x}{\sqrt{x^2+400}} = \frac{40-x}{D},
\]

\[
\frac{y}{\sqrt{y^2+900}} = \frac{50-y}{D}.
\]

De aquí, despejamos las relaciones entre $x$ e $y$ con $D$.

La primera implica:

\[
D x = (40-x)\sqrt{x^2+400}.
\]

La segunda:

\[
D y = (50-y)\sqrt{y^2+900}.
\]

Esto sugiere que las tangentes de ciertos ángulos coinciden: el punto $(x,y)$ es tal que el rayo desde $(0,0)$ y el rayo hacia $(40,50)$ cumplen relaciones análogas a la ley de Snell. Podemos intentar la solución usando el principio de Fermat con reflexiones.

Retomemos la interpretación geométrica. Queremos minimizar:

\[
\sqrt{x^2+20^2} + \sqrt{y^2+30^2} + \sqrt{(x-40)^2+(y-50)^2}.
\]

El tercer término es la distancia de $(x,y)$ a $B=(40,50)$.

Ahora, $\sqrt{x^2+20^2}$ es la distancia de $(x,y)$ al punto $A_1=(0,-20)$ o $(0,20)$ si consideramos coordenadas desplazadas. Más precisamente, $\sqrt{x^2+20^2}$ es la distancia entre el punto $(x, y)$ y el punto $(0, y-20)$ o $(0, y+20)$, pero el segundo depende de $y$.

Otra forma: interpretemos el problema como la longitud de una línea quebrada en 3D. Consideremos los puntos en 3D:

- Primer segmento de longitud $\sqrt{x^2+20^2}$: del punto $(0,0,20)$ al punto $(x,0,0)$? No.

Mejor: pensemos en una línea quebrada que une $(0,0,0)$ con $(40,50,0)$ pasando por planos. La longitud total sería la suma de tres segmentos. Los términos $\sqrt{x^2+20^2}$ y $\sqrt{y^2+30^2}$ involucran constantes $20$ y $30$, que son las diferencias de altura entre planos.

Consideremos tres planos paralelos: en $z=0$, $z=20$ y $z=50$. O algo así.

Otra idea estándar: minimizar

\[
\sqrt{x^2+a^2} + \sqrt{(p-x)^2+(q-y)^2} + \sqrt{y^2+b^2}
\]

es como minimizar la longitud de una poligonal que atraviesa tres franjas.

Usemos la interpretación de reflexión. Queremos conectar los puntos:

- $A=(0?, \cdot)$ y $B=(40,50)$.

El término $\sqrt{x^2+20^2}$ es la distancia desde $(x,y)$ hasta la línea vertical $x=0$ con offset $20$ en la dirección vertical: específicamente, es la distancia del punto $(x,y)$ al punto $(0, y\pm 20)$, pero no, porque sería $\sqrt{x^2+20^2}$ sin importar $y$, lo que sugiere que la distancia se mide en el plano $y$ constante con una componente vertical fija de 20.

En realidad, podemos verlo así: en el plano $xz$, la distancia entre $(x,z)$ y $(0,z+20)$ es $\sqrt{x^2+20^2}$. Entonces podemos imaginar que nos movemos en 3D cambiando de altura en 20 al cruzar de $x$ a 0.

Este es el problema clásico de minimizar la longitud de una línea quebrada a través de un "slab". La solución se obtiene desdoblando (unfolding) los planos y uniendo los puntos en línea recta.

Construyamos la configuración desdoblada:

Pensemos en un rectángulo en 2D realmente. Queremos:

\[
\text{distancia}((x,y), (0,20))? 
\]

No, porque sería $\sqrt{x^2+(y-20)^2}$.

Vamos a reinterpretar con un truco: $\sqrt{x^2+20^2}$ es la distancia entre $(x, y)$ y $(0, y-20)$ o $(0, y+20)$; el punto de referencia depende de $y$ y $x$. Eso no ayuda directamente.

Consideremos el enfoque de variables separables y convexidad. La función $F$ es convexa, por lo que las condiciones de primer orden son suficientes. Podemos intentar resolver el sistema numéricamente y luego ver si está dentro del rectángulo.

De las ecuaciones:

\[
\frac{x}{\sqrt{x^2+400}} = \frac{40-x}{D}, \tag{1}
\]

\[
\frac{y}{\sqrt{y^2+900}} = \frac{50-y}{D}. \tag{2}
\]

Elevando al cuadrado y reorganizando:

De (1):

\[
x^2 D^2 = (40-x)^2 (x^2+400).
\]

De (2):

\[
y^2 D^2 = (50-y)^2 (y^2+900).
\]

Dividiendo (1) y (2):

\[
\frac{x^2}{y^2} = \frac{(40-x)^2(x^2+400)}{(50-y)^2(y^2+900)}.
\]

Esto no es trivial. Probemos una solución con proporcionalidad. Supongamos que el punto crítico interior satisface $x/40 = y/50$, es decir, el punto está sobre la diagonal $y = \frac{5}{4}x$. Veamos si es consistente.

Sea $y = \frac{5}{4}x$. Entonces $D = \sqrt{(40-x)^2 + (50 - \frac{5}{4}x)^2}$.

Observemos que $50 - \frac{5}{4}x = \frac{5}{4}(40-x)$. Por lo tanto:

\[
D = |40-x|\sqrt{1+\left(\frac{5}{4}\right)^2} = (40-x)\cdot \frac{\sqrt{41}}{4},
\]

para $x<40$.

Entonces en (1):

Lado izquierdo: $\frac{x}{\sqrt{x^2+400}}$.

Lado derecho: $\frac{40-x}{D} = \frac{40-x}{(40-x)\frac{\sqrt{41}}{4}} = \frac{4}{\sqrt{41}}$.

Por lo tanto, la ecuación (1) exige:

\[
\frac{x}{\sqrt{x^2+400}} = \frac{4}{\sqrt{41}}.
\]

Resolvamos:

\[
x^2 \cdot 41 = 16(x^2+400) \implies 41x^2 = 16x^2 + 6400 \implies 25x^2 = 6400 \implies x^2 = 256 \implies x=16.
\]

Así que $x=16$, $y = \frac{5}{4}\cdot 16 = 20$. Verifiquemos la ecuación (2).

Con $x=16$, $y=20$:

\[
\frac{y}{\sqrt{y^2+900}} = \frac{20}{\sqrt{400+900}} = \frac{20}{\sqrt{1300}} = \frac{20}{10\sqrt{13}} = \frac{2}{\sqrt{13}}.
\]

Por otro lado, $D = \sqrt{(40-16)^2+(50-20)^2} = \sqrt{24^2+30^2} = \sqrt{576+900} = \sqrt{1476} = 6\sqrt{41}$.

Entonces:

\[
\frac{50-y}{D} = \frac{30}{6\sqrt{41}} = \frac{5}{\sqrt{41}}.
\]

Comparando: $\frac{2}{\sqrt{13}} \approx 0.5547$ y $\frac{5}{\sqrt{41}} \approx 0.7809$. No son iguales. Por lo tanto, la suposición $y=5x/4$ no es correcta. El punto crítico interior no está en esa diagonal.

Volvamos a las ecuaciones y tratemos de resolverlas de forma más sistemática.

De (1) y (2), elevamos al cuadrado:

(1'):
\[
x^2 [(x-40)^2+(y-50)^2] = (40-x)^2(x^2+400).
\]

(2'):
\[
y^2 [(x-40)^2+(y-50)^2] = (50-y)^2(y^2+900).
\]

Dividamos (1') por $(40-x)^2$ (asumiendo $x\neq 40$):

\[
\frac{x^2}{(40-x)^2}[(x-40)^2+(y-50)^2] = x^2+400.
\]

Como $(x-40)^2=(40-x)^2$:

\[
x^2 \left(1+\frac{(y-50)^2}{(40-x)^2}\right) = x^2+400.
\]

Esto da:

\[
x^2 \frac{(y-50)^2}{(40-x)^2} = 400.
\]

Es decir:

\[
\frac{x(y-50)}{40-x} = 20, \quad \text{o} \quad \frac{x|y-50|}{|40-x|} = 20.
\]

En la región interior $x<40$ y $y<50$, tenemos $|40-x|=40-x$, $|y-50|=50-y$. Entonces:

\[
\frac{x(50-y)}{40-x} = 20. \tag{3}
\]

Similarmente, de (2'):

\[
y^2 \left(1+\frac{(x-40)^2}{(50-y)^2}\right) = y^2+900.
\]

Entonces:

\[
y^2 \frac{(x-40)^2}{(50-y)^2} = 900.
\]

En la región interior:

\[
\frac{(40-x)y}{50-y} = 30. \tag{4}
\]

Ahora tenemos un sistema más sencillo:

De (3):

\[
x(50-y) = 20(40-x).
\]

De (4):

\[
y(40-x) = 30(50-y).
\]

Desarrollemos (3):

\[
50x - xy = 800 - 20x \implies 70x - xy = 800 \implies x(70-y)=800. \tag{5}
\]

Desarrollemos (4):

\[
40y - xy = 1500 - 30y \implies 70y - xy = 1500 \implies y(70-x)=1500. \tag{6}
\]

Ahora resolvemos el sistema (5) y (6):

De (5): $x = \frac{800}{70-y}$.

De (6): $y = \frac{1500}{70-x}$.

Sustituyamos $x$ en (6):

\[
y = \frac{1500}{70 - \frac{800}{70-y}}.
\]

Multiplicamos numerador y denominador:

\[
y = \frac{1500(70-y)}{70(70-y)-800} = \frac{1500(70-y)}{4900 - 70y - 800} = \frac{1500(70-y)}{4100 - 70y}.
\]

Entonces:

\[
y(4100 - 70y) = 1500(70-y).
\]

\[
4100y - 70y^2 = 105000 - 1500y.
\]

\[
70y^2 - 5600y + 105000 = 0.
\]

Dividimos entre 70:

\[
y^2 - 80y + 1500 = 0.
\]

Resolvemos:

\[
y = \frac{80 \pm \sqrt{6400-6000}}{2} = \frac{80 \pm \sqrt{400}}{2} = \frac{80 \pm 20}{2}.
\]

Entonces $y = 50$ o $y = 30$.

Si $y=50$, de (5): $x(70-50)=800 \implies 20x=800 \implies x=40$. Eso es el punto $(40,50)$, en la esquina, no interior.

Si $y=30$, de (5): $x(70-30)=800 \implies 40x=800 \implies x=20$.

Entonces el punto crítico interior es $(x,y)=(20,30)$.

Verifiquemos que cumple las condiciones. Con $x=20$, $y=30$:

\[
F(20,30) = \sqrt{20^2+400} + \sqrt{30^2+900} + \sqrt{(20-40)^2+(30-50)^2}.
\]

\[
\sqrt{400+400} = \sqrt{800} = 20\sqrt{2}.
\]

\[
\sqrt{900+900} = \sqrt{1800} = 30\sqrt{2}.
\]

\[
\sqrt{(-20)^2+(-20)^2} = \sqrt{400+400} = 20\sqrt{2}.
\]

Entonces:

\[
F(20,30) = 20\sqrt{2} + 30\sqrt{2} + 20\sqrt{2} = 70\sqrt{2}.
\]

Debemos verificar si es el mínimo global comparando con la frontera.

Evaluemos en las esquinas del rectángulo:

- $(0,0)$:

\[
F = \sqrt{0+400} + \sqrt{0+900} + \sqrt{1600+2500} = 20 + 30 + \sqrt{4100} = 50 + 10\sqrt{41} \approx 50 + 64.03 = 114.03.
\]

- $(0,50)$:

\[
F = 20 + \sqrt{2500+900} + \sqrt{0+2500} = 20 + \sqrt{3400} + 50 = 70 + 10\sqrt{34} \approx 70+58.31=128.31.
\]

- $(40,0)$:

\[
F = \sqrt{1600+400} + 30 + \sqrt{0+2500} = \sqrt{2000}+30+50 = 10\sqrt{20}+80 \approx 44.72+80=124.72.
\]

- $(40,50)$:

\[
F = \sqrt{1600+400} + \sqrt{2500+900} + 0 = \sqrt{2000} + \sqrt{3400} \approx 44.72 + 58.31 = 103.03.
\]

El valor $70\sqrt{2} \approx 98.99$ es menor que todos estos valores de esquina. Como la función es convexa y encontramos un punto crítico interior con derivadas nulas, este es el mínimo global.

Además, podemos confirmar la interpretación geométrica: el punto $(20,30)$ minimiza la suma.

Revisemos si la función es convexa en el dominio. La función $f(x,y)=\sqrt{x^2+400}$ es convexa en $(x,y)$ porque es la norma de $(x,20)$ respecto a la norma euclidiana en una dimensión reducida; en realidad $\sqrt{x^2+400}$ es convexa en $x$ (y por tanto en $(x,y)$ como función constante en $y$). La suma de funciones convexas es convexa. Las tres son convexas. En un dominio convexo, un punto crítico interior es mínimo global. El rectángulo es convexo, por lo que $F(20,30)=70\sqrt{2}$ es el mínimo global.

Por lo tanto, el valor mínimo es:

\[
\boxed{70\sqrt{2}}
\]