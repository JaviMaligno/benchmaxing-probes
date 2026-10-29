Para resolver el problema paso a paso, establecemos un sistema de coordenadas cartesianas aprovechando las longitudes de los lados de $\triangle ABC$.

### Paso 1: Configuración geométrica y coordenadas
Dado que $AB = 6$, $BC = 8$ y $AC = 10$, observamos que:
$$AB^2 + BC^2 = 6^2 + 8^2 = 36 + 64 = 100 = 10^2 = AC^2$$
Por lo tanto, $\triangle ABC$ es un triángulo rectángulo en $B$ ($\angle ABC = 90^\circ$), y la hipotenusa $AC$ es el diámetro de la circunferencia circunscrita $\omega$.

Situamos el origen en $B$:
- $B = (0, 0)$
- $C = (8, 0)$
- $A = (0, 6)$

La circunferencia circunscrita $\omega$ tiene centro en el punto medio de $AC$, que es $(4, 3)$, y radio $R = 5$. Su ecuación es:
$$X^2 + Y^2 - 8X - 6Y = 0$$

### Paso 2: Posición de $P$, $J$, $Q$ y $M$ en función de $\theta$
Como $AC$ es diámetro de $\omega$, cualquier punto $P$ sobre $\omega$ cumple $\angle APC = 90^\circ$. Además, como $P$ está en el arco $BC$ que no contiene a $A$, $P$ se encuentra en el cuarto cuadrante ($X > 0, Y < 0$).

Los puntos $J$ y $Q$ son los pies de las perpendiculares desde $P$ hacia $BC$ y $AC$, respectivamente ($\angle PJC = \angle PQC = 90^\circ$). Por lo tanto, el cuadrilátero $PJCQ$ es cíclico con diámetro $PC$. En esta circunferencia:
$$\angle QPC = \angle QJC = \theta$$
En el triángulo rectángulo $\triangle APC$ con altura $PQ \perp AC$, tenemos $\angle PAC = \angle QPC = \theta$. Con $x = \cos\theta$ e $y = \sin\theta$ ($x^2 + y^2 = 1$):
- $AP = AC \cos\theta = 10x$ y $PC = AC \sin\theta = 10y$.
- $AQ = AP \cos\theta = 10x^2$, $QC = PC \sin\theta = 10y^2$ y $PQ = 10xy$.

Como $Q$ divide al segmento $AC$ en razón $AQ : QC = x^2 : y^2$, sus coordenadas son:
$$Q = y^2 A + x^2 C = (8x^2, 6y^2)$$
El punto medio $M$ de $BQ$ es:
$$M = \left(4x^2, 3y^2\right)$$
Por la ley de los senos en el cuadrilátero cíclico $PJCQ$ de diámetro $PC = 10y$, como $\sin(\angle QCA) = \frac{6}{10}$, la longitud de $JQ$ es:
$$JQ = PC \sin(\angle QCA) = 10y \cdot \frac{6}{10} = 6y$$
Como $\angle QJC = \theta$, el vector $\overrightarrow{JQ}$ es $6y(x, y) = (6xy, 6y^2)$, de donde se obtiene el pie $J$ sobre $BC$:
$$J = (8x^2 - 6xy, 0)$$

### Paso 3: Condición de ciclicidad de $B, J, U, M$ y pendiente de la recta $l$
Como $B, J, U, M$ son concíclicos, aplicando la potencia del punto $Q$ respecto a la circunferencia $(BJM)$ en las secantes $QMB$ y $QUJ$:
$$QJ \cdot QU = QM \cdot QB$$
Dado que $M$ es el punto medio de $BQ$, tenemos $QM = \frac{1}{2}BQ$, por lo que:
$$QU = \frac{BQ^2}{2 \cdot QJ} = \frac{BQ^2}{12y}$$
Por otro lado, proyectando $BQ$ en las direcciones perpendicular y paralela a $JQ$, tenemos:
$$BQ^2 = x^2 y^2 (8x - 6y)^2 + (8x - 8xy^2 + 6y^3)^2 = 64x^4 + 36y^4$$
Sustituyendo esto en la ecuación dada en el enunciado:
$$768xy = (16 - 8x^2 + 6xy) \cdot BQ^2 \implies \frac{BQ^2}{12y} = \frac{64x}{16 - 8x^2 + 6xy}$$
De este modo, la distancia dirigida $QU$ a lo largo de $QJ$ es:
$$QU = \frac{64x}{16 - 8x^2 + 6xy}$$
Como $U = Q - QU \cdot (x, y) = (X_U, Y_U)$, calculamos $X_U$ y la relación con la recta $AC$ ($3X + 4Y = 24$):
$$X_U = 8x^2 - \frac{64x^2}{16 - 8x^2 + 6xy} = \frac{64x^2(1 - x^2) + 48x^3 y}{16 - 8x^2 + 6xy} = \frac{16x^2 y(3x + 4y)}{16 - 8x^2 + 6xy} = \frac{xy(3x + 4y)}{4} QU$$
y como $3X_Q + 4Y_Q = 24(x^2 + y^2) = 24$, tenemos:
$$24 - 3X_U - 4Y_U = (3X_Q + 4Y_Q) - (3X_U + 4Y_U) = (3x + 4y) QU$$

Ahora hallamos la pendiente $m = \frac{Y_I}{X_I}$ de la recta $l = BI$. La recta $CM$ pasa por $C(8, 0)$ y $M(4x^2, 3y^2)$, por lo que su ecuación es:
$$3y^2 X + (8 - 4x^2)Y = 24y^2 \implies 6 = \frac{3}{4}X + \frac{2 - x^2}{y^2}Y$$
Para el punto $I(X_I, Y_I)$ sobre $CM$, restamos $Y_I$ en ambos lados (usando $2 - x^2 - y^2 = 1$):
$$6 - Y_I = \frac{3}{4}X_I + \frac{1}{y^2}Y_I \implies \frac{6 - Y_I}{X_I} = \frac{3}{4} + \frac{m}{y^2}$$
Como $A(0, 6)$, $I$ y $U$ son colineales, se cumple $\frac{6 - Y_I}{X_I} = \frac{6 - Y_U}{X_U}$, de donde:
$$\frac{m}{y^2} = \frac{6 - Y_U}{X_U} - \frac{3}{4} = \frac{24 - 3X_U - 4Y_U}{4X_U} = \frac{(3x + 4y)QU}{xy(3x + 4y)QU} = \frac{1}{xy}$$
Por consiguiente:
$$m = \frac{y}{x} = \tan\theta$$
Esto significa que la recta $l$ (es decir, $BK$) es paralela a $JQ$ y forma un ángulo $\theta$ con $BC$.

### Paso 4: Cálculo de $BL$
La recta $BK$ pasa por el origen $B(0, 0)$ con vector director unitario $(x, y) = (\cos\theta, \sin\theta)$. Cualquier punto sobre esta recta tiene coordenadas $(tx, ty)$, donde $t = BL > 0$. Sustituyendo en la ecuación de la circunferencia $\omega$ ($X^2 + Y^2 - 8X - 6Y = 0$):
$$t^2(x^2 + y^2) - t(8x + 6y) = 0 \implies BL = t = 8x + 6y$$

Sustituyendo los valores numéricos dados $x \approx 0.72951$ e $y \approx 0.68400$:
$$BL = 8(0.72951) + 6(0.68400) = 5.83608 + 4.10400 = 9.94008 \approx 9.94$$

\boxed{9.94}