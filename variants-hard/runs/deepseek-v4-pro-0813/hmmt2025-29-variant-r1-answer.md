Vamos a resolver el problema paso a paso.

Sea el rectángulo \(PQRS\), con \(QR = 30\). Dado que es un rectángulo, \(PQ = RS\) y \(PS = QR = 30\). Llamemos \(PQ = RS = h\).

Un punto \(Y\) está dentro del rectángulo con \(\angle PYQ = 90^\circ\). Además, los triángulos \(\triangle PYS\) y \(\triangle QYR\) son acutángulos, con circunradios \(17\) y \(25\), respectivamente.

---

**Paso 1: relación entre el lado y el circunradio en un triángulo**

Para el triángulo \(\triangle PYS\):

- El lado \(PS = 30\).
- El ángulo \(\angle PYS\) es opuesto a \(PS\).

Por la fórmula del circunradio \(R = \dfrac{a}{2\sin A}\), donde \(a = PS = 30\):

\[
17 = \frac{30}{2\sin(\angle PYS)} \quad\Rightarrow\quad \sin(\angle PYS) = \frac{30}{34} = \frac{15}{17}.
\]

Para el triángulo \(\triangle QYR\):

- El lado \(QR = 30\).
- El ángulo \(\angle QYR\) es opuesto a \(QR\).

\[
25 = \frac{30}{2\sin(\angle QYR)} \quad\Rightarrow\quad \sin(\angle QYR) = \frac{30}{50} = \frac{3}{5}.
\]

Como ambos triángulos son acutángulos, los ángulos \(\angle PYS\) y \(\angle QYR\) son agudos, así que:

\[
\cos(\angle PYS) = \sqrt{1 - \left(\frac{15}{17}\right)^2} = \sqrt{\frac{64}{289}} = \frac{8}{17},
\]

\[
\cos(\angle QYR) = \sqrt{1 - \left(\frac{3}{5}\right)^2} = \sqrt{\frac{16}{25}} = \frac{4}{5}.
\]

---

**Paso 2: geometría del rectángulo y el punto \(Y\)**

Vamos a trabajar con coordenadas. Sean:

\[
P(0,0), \quad Q(h,0), \quad R(h,30), \quad S(0,30).
\]

El punto \(Y = (x,y)\) está dentro del rectángulo, con \(0 < x < h\) y \(0 < y < 30\).

La condición \(\angle PYQ = 90^\circ\) significa que los vectores \(\overrightarrow{YP}\) y \(\overrightarrow{YQ}\) son perpendiculares:

\[
\overrightarrow{YP} = (-x, -y), \qquad \overrightarrow{YQ} = (h-x, -y).
\]

El producto escalar debe ser cero:

\[
(-x)(h-x) + (-y)(-y) = 0.
\]

\[
-x(h-x) + y^2 = 0.
\]

\[
-(xh - x^2) + y^2 = 0.
\]

\[
-xh + x^2 + y^2 = 0.
\]

\[
x^2 + y^2 = xh.
\]

Esta es la primera ecuación.

---

**Paso 3: usar los ángulos de los triángulos**

Para \(\triangle PYS\), con \(P(0,0)\), \(S(0,30)\), \(Y(x,y)\):

Los vectores son:

\[
\overrightarrow{YP} = (-x, -y), \qquad \overrightarrow{YS} = (-x, 30-y).
\]

El seno del ángulo entre ellos viene dado por:

\[
\sin(\angle PYS) = \frac{|\overrightarrow{YP} \times \overrightarrow{YS}|}{|\overrightarrow{YP}|\,|\overrightarrow{YS}|}.
\]

El producto cruz (en 2D, el determinante):

\[
\overrightarrow{YP} \times \overrightarrow{YS} = (-x)(30-y) - (-y)(-x) = -x(30-y) - xy = -30x + xy - xy = -30x.
\]

El valor absoluto es \(30x\).

Por otro lado:

\[
|\overrightarrow{YP}| = \sqrt{x^2 + y^2}, \qquad
|\overrightarrow{YS}| = \sqrt{x^2 + (30-y)^2}.
\]

Entonces:

\[
\sin(\angle PYS) = \frac{30x}{\sqrt{x^2+y^2}\,\sqrt{x^2+(30-y)^2}} = \frac{15}{17}.
\]

---

**Paso 4: análogamente para \(\triangle QYR\)**

Con \(Q(h,0)\), \(R(h,30)\), \(Y(x,y)\):

\[
\overrightarrow{YQ} = (h-x, -y), \qquad \overrightarrow{YR} = (h-x, 30-y).
\]

El producto cruz:

\[
\overrightarrow{YQ} \times \overrightarrow{YR} = (h-x)(30-y) - (-y)(h-x) = (h-x)(30-y) + y(h-x) = (h-x)\cdot 30.
\]

Así que el valor absoluto es \(30(h-x)\).

Las longitudes:

\[
|\overrightarrow{YQ}| = \sqrt{(h-x)^2 + y^2}, \qquad
|\overrightarrow{YR}| = \sqrt{(h-x)^2 + (30-y)^2}.
\]

Entonces:

\[
\sin(\angle QYR) = \frac{30(h-x)}{\sqrt{(h-x)^2+y^2}\,\sqrt{(h-x)^2+(30-y)^2}} = \frac{3}{5}.
\]

---

**Paso 5: resolver el sistema**

Tenemos de la perpendicularidad:

\[
x^2 + y^2 = xh. \tag{1}
\]

Esto implica:

\[
\sqrt{x^2 + y^2} = \sqrt{xh}.
\]

Y también:

\[
(h-x)^2 + y^2 = h^2 - 2hx + x^2 + y^2.
\]

Usando (1), \(x^2+y^2 = xh\), entonces:

\[
(h-x)^2 + y^2 = h^2 - 2hx + xh = h^2 - hx = h(h-x).
\]

Entonces:

\[
\sqrt{(h-x)^2 + y^2} = \sqrt{h(h-x)}.
\]

Además:

\[
x^2 + (30-y)^2 = x^2 + 900 - 60y + y^2 = (x^2+y^2) + 900 - 60y = xh + 900 - 60y.
\]

Y:

\[
(h-x)^2 + (30-y)^2 = (h-x)^2 + 900 - 60y + y^2.
\]

Como \((h-x)^2 + y^2 = h(h-x)\), tenemos:

\[
(h-x)^2 + (30-y)^2 = h(h-x) + 900 - 60y.
\]

---

**Paso 6: simplificar las ecuaciones de senos**

Para \(\triangle PYS\):

\[
\frac{30x}{\sqrt{xh}\,\sqrt{xh+900-60y}} = \frac{15}{17}.
\]

\[
\frac{30x}{\sqrt{xh}\,\sqrt{xh+900-60y}} = \frac{15}{17}.
\]

Elevando al cuadrado:

\[
\frac{900x^2}{xh\,(xh+900-60y)} = \frac{225}{289}.
\]

Simplificamos \(x^2/(xh) = x/h\):

\[
\frac{900 \cdot (x/h)}{xh+900-60y} = \frac{225}{289}.
\]

Multiplicamos:

\[
900 \cdot \frac{x}{h} \cdot 289 = 225\,(xh+900-60y).
\]

\[
260100 \cdot \frac{x}{h} = 225xh + 202500 - 13500y.
\]

Dividimos entre 225:

\[
1156 \cdot \frac{x}{h} = xh + 900 - 60y. \tag{2}
\]

Para \(\triangle QYR\):

\[
\frac{30(h-x)}{\sqrt{h(h-x)}\,\sqrt{h(h-x)+900-60y}} = \frac{3}{5}.
\]

Elevando al cuadrado:

\[
\frac{900(h-x)^2}{h(h-x)\bigl[h(h-x)+900-60y\bigr]} = \frac{9}{25}.
\]

Simplificamos \((h-x)^2/[h(h-x)] = (h-x)/h\):

\[
\frac{900 \cdot (h-x)/h}{h(h-x)+900-60y} = \frac{9}{25}.
\]

Multiplicamos:

\[
900 \cdot \frac{h-x}{h} \cdot 25 = 9\,[h(h-x)+900-60y].
\]

\[
22500 \cdot \frac{h-x}{h} = 9h(h-x) + 8100 - 540y.
\]

Dividimos entre 9:

\[
2500 \cdot \frac{h-x}{h} = h(h-x) + 900 - 60y. \tag{3}
\]

---

**Paso 7: restar las ecuaciones (2) y (3)**

De (2):

\[
xh + 900 - 60y = 1156\cdot\frac{x}{h}.
\]

De (3):

\[
h(h-x) + 900 - 60y = 2500\cdot\frac{h-x}{h}.
\]

Restamos (3) − (2):

\[
h(h-x) - xh = 2500\cdot\frac{h-x}{h} - 1156\cdot\frac{x}{h}.
\]

El lado izquierdo:

\[
h(h-x) - xh = h^2 - hx - xh = h^2 - 2hx.
\]

El lado derecho:

\[
\frac{2500(h-x) - 1156x}{h} = \frac{2500h - 2500x - 1156x}{h} = \frac{2500h - 3656x}{h}.
\]

Entonces:

\[
h^2 - 2hx = \frac{2500h - 3656x}{h}.
\]

Multiplicamos por \(h\):

\[
h^3 - 2h^2x = 2500h - 3656x.
\]

Reorganizamos:

\[
h^3 - 2500h = 2h^2x - 3656x = x\,(2h^2 - 3656).
\]

\[
h(h^2 - 2500) = x\,(2h^2 - 3656).
\]

Por lo tanto:

\[
x = \frac{h(h^2 - 2500)}{2h^2 - 3656} = \frac{h(h^2 - 2500)}{2(h^2 - 1828)}.
\]

---

**Paso 8: usar la ecuación de perpendicularidad y la de \(y\)**

De la condición \(x^2 + y^2 = xh\), no conocemos todavía \(y\) explícitamente, pero sí tenemos otra relación. Volvamos a la ecuación (2):

\[
xh + 900 - 60y = 1156\cdot\frac{x}{h}.
\]

Podemos despejar \(y\):

\[
60y = xh + 900 - \frac{1156x}{h}.
\]

\[
y = \frac{xh + 900 - \frac{1156x}{h}}{60}.
\]

Obviamente esto depende de \(h\).

Pero también tenemos la otra condición sobre el triángulo, que ya usamos para deducir (3). No obstante, no hemos usado que los triángulos son acutángulos de forma explícita, pero sí indirectamente al tomar cosenos positivos. Aún falta una ecuación: el valor numérico de \(h\).

---

**Paso 9: aprovechar que \(Y\) está dentro del rectángulo y las condiciones de acutángulo**

Para \(\triangle PYS\) acutángulo, el circuncentro cae dentro. La mediatriz de \(PS\) es la recta horizontal \(y=15\). El circuncentro de \(\triangle PYS\) está a distancia \(17\) de \(P\), \(S\) y \(Y\).

El lado \(PS=30\) es una cuerda del círculo circunscrito de radio \(17\). La distancia del centro a la cuerda \(PS\) es:

\[
\sqrt{17^2 - 15^2} = \sqrt{289 - 225} = \sqrt{64} = 8.
\]

Como el triángulo es acutángulo y \(Y\) está dentro del rectángulo (a la derecha de \(PS\)), el centro del círculo circunscrito está a la izquierda de \(PS\), es decir, en la recta \(y=15\) y \(x = -8\). Entonces:

\[
(x+8)^2 + (y-15)^2 = 17^2 = 289.
\]

---

**Paso 10: análogamente para \(\triangle QYR\)**

La mediatriz de \(QR\) es la recta horizontal \(y=15\) también (porque \(QR\) está a la misma altura). El lado \(QR=30\) es una cuerda del círculo de radio \(25\). La distancia del centro a la cuerda \(QR\) es:

\[
\sqrt{25^2 - 15^2} = \sqrt{625 - 225} = \sqrt{400} = 20.
\]

Como \(Y\) está dentro del rectángulo (a la izquierda de \(QR\)) y el triángulo \(\triangle QYR\) es acutángulo, el centro de su circunferencia circunscrita está a la derecha de \(QR\). Por lo tanto, tiene coordenadas \((h+20, 15)\). Entonces:

\[
(x - (h+20))^2 + (y-15)^2 = 25^2 = 625.
\]

---

**Paso 11: resolver para \(h\)**

Tenemos las dos ecuaciones:

\[
(x+8)^2 + (y-15)^2 = 289, \tag{4}
\]

\[
(x-h-20)^2 + (y-15)^2 = 625. \tag{5}
\]

Restamos (5) − (4):

\[
(x-h-20)^2 - (x+8)^2 = 336.
\]

Expandimos:

\[
[(x-h-20) - (x+8)]\,[(x-h-20) + (x+8)] = 336.
\]

\[
(-h-28)(2x - h - 12) = 336.
\]

\[
-(h+28)(2x - h - 12) = 336.
\]

\[
(h+28)(2x - h - 12) = -336. \tag{6}
\]

---

**Paso 12: usar la condición \(\angle PYQ = 90^\circ\)**

La condición de perpendicularidad es \(x^2 + y^2 = xh\).

De la ecuación (4):

\[
(x+8)^2 + (y-15)^2 = 289.
\]

Expandimos:

\[
x^2 + 16x + 64 + y^2 - 30y + 225 = 289.
\]

\[
x^2 + y^2 + 16x - 30y + 289 = 289.
\]

\[
x^2 + y^2 + 16x - 30y = 0.
\]

Usando \(x^2 + y^2 = xh\):

\[
xh + 16x - 30y = 0.
\]

\[
x(h+16) = 30y.
\]

\[
y = \frac{x(h+16)}{30}. \tag{7}
\]

---

**Paso 13: sustituir en (4)**

\[
(x+8)^2 + \left(\frac{x(h+16)}{30} - 15\right)^2 = 289.
\]

Esto da una relación entre \(x\) y \(h\). Combinando con (6), podemos resolver.

---

**Paso 14: resolver el sistema**

De (6):

\[
(h+28)(2x - h - 12) = -336.
\]

Despejamos \(2x - h - 12\):

\[
2x - h - 12 = -\frac{336}{h+28}. \tag{8}
\]

Por lo tanto:

\[
2x = h + 12 - \frac{336}{h+28}.
\]

\[
x = \frac{h + 12}{2} - \frac{168}{h+28}. \tag{9}
\]

Ahora, la perpendicularidad dio \(x^2 + y^2 = xh\), y de (4) obtuvimos \(xh + 16x - 30y=0\). Sustituyamos \(y = x(h+16)/30\) en \(x^2 + y^2 = xh\):

\[
x^2 + \frac{x^2(h+16)^2}{900} = xh.
\]

Dividimos entre \(x \neq 0\):

\[
x + \frac{x(h+16)^2}{900} = h.
\]

\[
x\left(1 + \frac{(h+16)^2}{900}\right) = h.
\]

\[
x \cdot \frac{900 + (h+16)^2}{900} = h.
\]

\[
\frac{x\,(h^2 + 32h + 256 + 900)}{900} = h.
\]

\[
x\,(h^2 + 32h + 1156) = 900h.
\]

\[
x = \frac{900h}{h^2 + 32h + 1156}. \tag{10}
\]

---

**Paso 15: igualar (9) y (10)**

\[
\frac{h+12}{2} - \frac{168}{h+28} = \frac{900h}{h^2 + 32h + 1156}.
\]

Notemos que \(h^2 + 32h + 1156 = (h+16)^2 + 900\). Además, \(h^2+32h+1156 = h^2 + 28h + 4h + 1156\), no parece factorizar directamente. Trabajemos.

Multiplicamos ambos lados por \(2(h+28)(h^2+32h+1156)\):

\[
(h+12)(h+28)(h^2+32h+1156) - 336(h^2+32h+1156) = 1800h(h+28).
\]

Observemos que:

\[
(h+12)(h+28) = h^2 + 40h + 336.
\]

Entonces:

\[
(h^2 + 40h + 336)(h^2+32h+1156) - 336(h^2+32h+1156) - 1800h(h+28) = 0.
\]

Expandiendo el producto:

\[
h^4 + 32h^3 + 1156h^2 + 40h^3 + 1280h^2 + 46240h + 336h^2 + 10752h + 388416.
\]

Sumamos términos:

- \(h^4\)
- \(72h^3\)
- \((1156+1280+336)h^2 = 2772h^2\)
- \((46240+10752)h = 56992h\)
- \(388416\)

Entonces el primer término es:

\[
h^4 + 72h^3 + 2772h^2 + 56992h + 388416.
\]

Ahora restamos el segundo término:

\[
-336h^2 - 10752h - 388416.
\]

Y el tercero:

\[
-1800h^2 - 50400h.
\]

Sumamos todo:

\[
h^4 + 72h^3 + (2772 - 336 - 1800)h^2 + (56992 - 10752 - 50400)h + (388416 - 388416).
\]

Coeficientes:

- \(h^2\): \(2772 - 336 = 2436\), menos \(1800\) = \(636\).
- \(h\): \(56992 - 10752 = 46240\), menos \(50400\) = \(-4160\).
- Constante: \(0\).

Entonces:

\[
h^4 + 72h^3 + 636h^2 - 4160h = 0.
\]

\[
h\,(h^3 + 72h^2 + 636h - 4160) = 0.
\]

Como \(h>0\), nos queda:

\[
h^3 + 72h^2 + 636h - 4160 = 0.
\]

---

**Paso 16: factorizar el polinomio cúbico**

Probemos raíces enteras. Los divisores de \(4160\) son varios. Probemos \(h=4\):

\[
4^3 + 72\cdot 16 + 636\cdot 4 - 4160 = 64 + 1152 + 2544 - 4160 = 3760 - 4160 = -400 \neq 0.
\]

Probemos \(h=5\):

\[
125 + 72\cdot 25 + 636\cdot 5 - 4160 = 125 + 1800 + 3180 - 4160 = 5105 - 4160 = 945 \neq 0.
\]

Probemos \(h=8\):

\[
512 + 72\cdot 64 + 636\cdot 8 - 4160 = 512 + 4608 + 5088 - 4160 = 10208 - 4160 = 6048 \neq 0.
\]

Probemos \(h=40\):

\[
64000 + 72\cdot 1600 + 636\cdot 40 - 4160.
\]

\[
= 64000 + 115200 + 25440 - 4160 = 204640 - 4160 = 200480 \neq 0.
\]

Quizá la raíz no sea entera, o me equivoqué en algún paso. Repasemos la deducción de los pasos 11 y 12.

---

**Paso 17: revisar la ecuación (4)**

Para \(\triangle PYS\): lado \(PS\) vertical, longitud 30. Circunradio 17. La mediatriz de \(PS\) es la recta \(y=15\). La distancia del centro a la cuerda \(PS\) es \(\sqrt{17^2 - 15^2} = 8\).

Como el triángulo es acutángulo, el centro está del lado opuesto a \(Y\) respecto de \(PS\). \(PS\) es la recta \(x=0\). \(Y\) tiene \(x>0\), así que el centro debe tener \(x<0\), concretamente \(x=-8\). Luego centro \((-8,15)\). Correcto.

Para \(\triangle QYR\): lado \(QR\) vertical en \(x=h\), longitud 30. Circunradio 25. Distancia del centro a \(QR\): \(\sqrt{25^2 - 15^2}=20\). \(Y\) tiene \(x<h\), así que el centro debe tener \(x>h\), concretamente \(x=h+20\). Centro \((h+20,15)\). Correcto.

---

**Paso 18: revisar la perpendicularidad**

Condición:

\[
x^2 + y^2 = xh.
\]

De (4):

\[
(x+8)^2 + (y-15)^2 = 289.
\]

Desarrollamos:

\[
x^2+16x+64 + y^2 - 30y + 225 = 289.
\]

\[
x^2+y^2 +16x -30y + 289 = 289.
\]

\[
x^2+y^2 +16x-30y=0.
\]

Sustituimos \(x^2+y^2=xh\):

\[
xh + 16x - 30y=0.
\]

Bien. Entonces:

\[
y = \frac{x(h+16)}{30}. \tag{7}
\]

Correcto.

---

**Paso 19: verificar la ecuación con \(x\)**

De \(x^2+y^2=xh\):

\[
x^2 + \frac{x^2(h+16)^2}{900} = xh.
\]

Dividiendo entre \(x\):

\[
x \left(1 + \frac{(h+16)^2}{900}\right) = h.
\]

\[
x \cdot \frac{(h+16)^2+900}{900} = h.
\]

\[
(h+16)^2 + 900 = h^2 + 32h + 256 + 900 = h^2+32h+1156.
\]

Bien. Entonces:

\[
x = \frac{900h}{h^2+32h+1156}. \tag{10}
\]

Correcto.

---

**Paso 20: revisar la ecuación (6)**

Restamos (5)−(4):

\[
(x-h-20)^2 - (x+8)^2 = 625-289=336.
\]

Diferencia de cuadrados:

\[
[(x-h-20)-(x+8)]\,[(x-h-20)+(x+8)] =336.
\]

\[
(-h-28)(2x-h-12)=336.
\]

\[
-(h+28)(2x-h-12)=336.
\]

\[
(h+28)(2x-h-12)=-336.
\]

Correcto.

---

**Paso 21: posible error en la expansión algebraica del paso 15**

Volvamos a la igualdad:

\[
\frac{h+12}{2} - \frac{168}{h+28} = \frac{900h}{h^2+32h+1156}.
\]

Multiplicamos todo por \(2(h+28)(h^2+32h+1156)\):

Lado izquierdo:

\[
(h+12)(h+28)(h^2+32h+1156) - 336(h^2+32h+1156).
\]

Lado derecho:

\[
1800h(h+28).
\]

Calculamos \((h+12)(h+28)\):

\[
h^2 + 40h + 336.
\]

Multiplicamos por \((h^2+32h+1156)\):

\[
h^4 + 32h^3 + 1156h^2
\]

\[
+40h^3 + 1280h^2 + 46240h
\]

\[
+336h^2 + 10752h + 388416.
\]

Suma:

\[
h^4 + 72h^3 + 2772h^2 + 56992h + 388416. \quad \checkmark
\]

Restamos \(336(h^2+32h+1156) = 336h^2 + 10752h + 388416\):

\[
h^4 + 72h^3 + 2436h^2 + 46240h.
\]

Igualamos a \(1800h(h+28) = 1800h^2 + 50400h\):

\[
h^4 + 72h^3 + 2436h^2 + 46240h = 1800h^2 + 50400h.
\]

\[
h^4 + 72h^3 + 636h^2 - 4160h = 0.
\]

Correcto.

---

**Paso 22: buscar raíces del cúbico**

\[
h^3 + 72h^2 + 636h - 4160 = 0.
\]

Intentemos \(h=4\): \(64+1152+2544-4160 = -400\).

\(h=5\): \(125+1800+3180-4160 = 945\).

Entonces hay una raíz entre 4 y 5. Probemos \(h = 4.8\):

\[
4.8^3 = 110.592,\quad 72\cdot 23.04 = 1658.88,\quad 636\cdot 4.8 = 3052.8.
\]

\[
110.592 + 1658.88 + 3052.8 - 4160 = 4822.272 - 4160 = 662.272.
\]

\(h=4.5\):

\[
91.125 + 72\cdot 20.25 + 636\cdot 4.5 - 4160.
\]

\[
=91.125 + 1458 + 2862 - 4160 = 4411.125 - 4160 = 251.125.
\]

\(h=4.4\):

\[
85.184 + 72\cdot 19.36 + 636\cdot 4.4 - 4160.
\]

\[
=85.184 + 1393.92 + 2798.4 - 4160 = 4277.504 - 4160 = 117.504.
\]

\(h=4.3\):

\[
79.507 + 72\cdot 18.49 + 636\cdot 4.3 - 4160.
\]

\[
=79.507 + 1331.28 + 2734.8 - 4160 = 4145.587 - 4160 = -14.413.
\]

Entonces la raíz real positiva está cerca de \(h \approx 4.31\).

Pero \(h = PQ\) debería ser un número razonablemente entero o simple dado el planteamiento. ¿Quizá el polinomio factoriza con una raíz \(h=2\)?

\(h=2\): \(8+288+1272-4160 = -2592\).

\(h=10\): \(1000+7200+6360-4160 = 10400\).

La raíz entre 4.3 y 4.4 no parece entera. Tal vez cometí un error conceptual en la colocación de los circuncentros.

---

**Paso 23: reconsiderar la posición de los centros**

Consideremos el triángulo \(\triangle PYS\) con \(P(0,0)\), \(S(0,30)\). El lado \(PS\) está en el eje \(y\). La mediatriz es \(y=15\). Correcto.

El centro está a distancia 8 de la recta \(x=0\). ¿Hacia qué lado? Depende de dónde esté \(Y\). Para que el triángulo \(PYS\) sea acutángulo, todos sus ángulos son menores de \(90^\circ\). Eso obliga a que el circuncentro esté dentro del triángulo. El triángulo \(PYS\) tiene vértices en \(x=0\) y \(Y\) con \(x>0\). Entonces el interior del triángulo está en \(x>0\). Por tanto, el centro debe estar en \(x>0\), no en \(x=-8\).

¡Ahí está el error! El circuncentro de un triángulo acutángulo está dentro del triángulo. Como \(Y\) está a la derecha de \(PS\), el centro del círculo de \(\triangle PYS\) debe tener \(x>0\), es decir, \(x=+8\), no \(-8\).

Corrijamos:

---

**Paso 24: corregir los centros**

Para \(\triangle PYS\), centro \(C_1 = (8,15)\), radio \(17\):

\[
(x-8)^2 + (y-15)^2 = 289. \tag{4'}
\]

Para \(\triangle QYR\), el triángulo tiene vértices \(Q(h,0)\), \(R(h,30)\) en la recta \(x=h\), y \(Y\) con \(x<h\). El interior está en \(x<h\). Por tanto, el centro debe tener \(x<h\). La mediatriz de \(QR\) es \(y=15\). La distancia del centro a \(x=h\) es 20. Como el centro debe estar dentro del triángulo, es decir, a la izquierda de \(QR\), entonces \(x = h - 20\). Así:

\[
(x - (h-20))^2 + (y-15)^2 = 625. \tag{5'}
\]

Pero espera: ¿cómo sabemos que el centro está a la izquierda de \(QR\)? El triángulo \(QYR\) es acutángulo, entonces el circuncentro está dentro. El interior del triángulo \(QYR\) está del lado de \(Y\), que tiene \(x<h\). Por tanto, el centro está en \(x<h\), es decir, \(x = h-20\).

---

**Paso 25: resolver con las correcciones**

Tenemos:

\[
(x-8)^2 + (y-15)^2 = 289, \tag{4'}
\]

\[
(x-h+20)^2 + (y-15)^2 = 625. \tag{5'}
\]

Restando (5') − (4'):

\[
(x-h+20)^2 - (x-8)^2 = 336.
\]

Diferencia de cuadrados:

\[
[(x-h+20)-(x-8)]\,[(x-h+20)+(x-8)] = 336.
\]

\[
(28-h)(2x-h+12)=336.
\]

No hay forma fácil de continuar sin saber si \(h>28\) o no. Para que el centro de \(\triangle QYR\) esté dentro, \(x=h-20\) debe ser menor que \(h\) (cierto) y mayor que 0 probablemente. Si \(h-20\) puede ser positivo o negativo, \(x\) es la coordenada del punto \(Y\).

Pero además, \(Y\) está dentro del rectángulo, luego \(0<x<h\). Para \(\triangle PYS\), el centro \((8,15)\) debe estar dentro del triángulo \(PYS\). El triángulo \(PYS\) está delimitado por la recta \(PS\) (\(x=0\)) y las rectas \(PY\) y \(SY\). El centro \((8,15)\) tiene \(x=8\), pero ¿está realmente dentro? La coordenada \(x\) del centro es 8, pero esto no garantiza que esté dentro; depende de \(Y\). Aun así, planteemos las ecuaciones y veamos.

---

**Paso 26: perpendicularidad con los nuevos centros**

De (4'):

\[
(x-8)^2 + (y-15)^2 = 289.
\]

\[
x^2 - 16x + 64 + y^2 - 30y + 225 = 289.
\]

\[
x^2+y^2 -16x -30y + 289 = 289.
\]

\[
x^2+y^2 -16x -30y =0.
\]

Con \(x^2+y^2 = xh\):

\[
xh -16x -30y = 0.
\]

\[
x(h-16) = 30y.
\]

\[
y = \frac{x(h-16)}{30}. \tag{7'}
\]

---

**Paso 27: ecuación para \(x\)**

De \(x^2+y^2=xh\):

\[
x^2 + \frac{x^2(h-16)^2}{900} = xh.
\]

Dividimos entre \(x\):

\[
x \left(1 + \frac{(h-16)^2}{900}\right) = h.
\]

\[
x \cdot \frac{(h-16)^2 + 900}{900} = h.
\]

\[
x = \frac{900h}{(h-16)^2 + 900} = \frac{900h}{h^2 -32h + 256 + 900} = \frac{900h}{h^2 -32h + 1156}. \tag{10'}
\]

---

**Paso 28: ecuación adicional de la resta**

De la resta (5')−(4'):

\[
(28-h)(2x-h+12)=336. \tag{6'}
\]

Despejamos \(2x - h+12\):

\[
2x - h + 12 = \frac{336}{28-h}.
\]

\[
2x = h - 12 + \frac{336}{28-h}.
\]

\[
x = \frac{h-12}{2} + \frac{168}{28-h}. \tag{9'}
\]

---

**Paso 29: igualar (9') y (10')**

\[
\frac{h-12}{2} + \frac{168}{28-h} = \frac{900h}{h^2 - 32h + 1156}.
\]

Multiplicamos todo por \(2(28-h)(h^2-32h+1156)\):

Lado izquierdo:

\[
(h-12)(28-h)(h^2-32h+1156) + 336(h^2-32h+1156).
\]

Lado derecho:

\[
1800h(28-h).
\]

Calculamos \((h-12)(28-h) = 28h - h^2 - 336 + 12h = -h^2 + 40h - 336\).

Multiplicamos por \((h^2-32h+1156)\):

\[
(-h^2 + 40h - 336)(h^2-32h+1156).
\]

Hagámoslo por partes.

Primero:

\[
-h^2(h^2-32h+1156) = -h^4 + 32h^3 - 1156h^2.
\]

Segundo:

\[
40h(h^2-32h+1156) = 40h^3 - 1280h^2 + 46240h.
\]

Tercero:

\[
-336(h^2-32h+1156) = -336h^2 + 10752h - 388416.
\]

Suma:

\[
-h^4 + (32+40)h^3 + (-1156-1280-336)h^2 + (46240+10752)h - 388416.
\]

\[
= -h^4 + 72h^3 - 2772h^2 + 56992h - 388416.
\]

Ahora sumamos \(336(h^2-32h+1156)\):

\[
= 336h^2 - 10752h + 388416.
\]

Total lado izquierdo:

\[
-h^4 + 72h^3 - 2436h^2 + 46240h.
\]

Lado derecho:

\[
1800h(28-h) = 50400h - 1800h^2.
\]

Igualamos:

\[
-h^4 + 72h^3 - 2436h^2 + 46240h = 50400h - 1800h^2.
\]

Llevamos todo a un lado:

\[
-h^4 + 72h^3 - 2436h^2 + 1800h^2 + 46240h - 50400h = 0.
\]

\[
-h^4 + 72h^3 - 636h^2 - 4160h = 0.
\]

Multiplicamos por \(-1\):

\[
h^4 - 72h^3 + 636h^2 + 4160h = 0.
\]

\[
h\,(h^3 - 72h^2 + 636h + 4160) = 0.
\]

Entonces:

\[
h^3 - 72h^2 + 636h + 4160 = 0.
\]

---

**Paso 30: buscar raíces enteras**

Probemos \(h=16\):

\[
4096 - 72\cdot 256 + 636\cdot 16 + 4160.
\]

\[
= 4096 - 18432 + 10176 + 4160 = 4096+10176+4160 -18432 = 18432 -18432 = 0.
\]

¡Perfecto! \(h=16\) es raíz.

---

**Paso 31: factorizar**

\[
h^3 - 72h^2 + 636h + 4160 = (h-16)(h^2 - 56h - 260).
\]

Las otras raíces:

\[
h^2 - 56h - 260 = 0.
\]

\[
h = \frac{56 \pm \sqrt{3136 + 1040}}{2} = \frac{56 \pm \sqrt{4176}}{2}.
\]

\[
\sqrt{4176} = 4\sqrt{261}, \quad \text{aprox. } 64.6.
\]

Las raíces serían \(h \approx 60.3\) y \(h \approx -4.3\). La única raíz positiva con sentido físico para el rectángulo (y que además cumpla las condiciones de acutángulo con \(Y\) dentro) parece ser \(h=16\), pero revisemos \(h \approx 60.3\) también.

---

**Paso 32: verificar \(h=16\)**

Con \(h=16\):

\[
x = \frac{900\cdot 16}{256 - 512 + 1156} = \frac{14400}{900} = 16.
\]

\[
y = \frac{x(h-16)}{30} = \frac{16 \cdot 0}{30} = 0.
\]

Pero \(y=0\) significa que \(Y\) está en el lado inferior \(PQ\), no dentro del rectángulo. Además \(\angle PYQ\) en ese caso: \(Y=P\) o algo degenerado. En efecto, con \(x=16, y=0\), \(Y=(16,0)=Q\), lo cual es degenerado.

Entonces \(h=16\) no es válida para un punto interior.

---

**Paso 33: examinar la otra raíz positiva**

La otra raíz positiva es \(h=\frac{56 + \sqrt{4176}}{2} = 28 + \sqrt{1044} = 28 + 2\sqrt{261}\).

\(\sqrt{261} \approx 16.155\), así que \(h \approx 60.31\).

Pero si \(h \approx 60.31 > 28\), entonces en la ecuación (6'):

\[
2x - h + 12 = \frac{336}{28-h}.
\]

Como \(28-h < 0\), el lado derecho es negativo. No obstante, sigamos y calculemos \(x\) e \(y\).

Con \(h = 28 + 2\sqrt{261}\):

\[
x = \frac{900h}{h^2 - 32h + 1156}.
\]

Calculemos \(h^2 - 32h + 1156\).

\[
h^2 = (28+2\sqrt{261})^2 = 784 + 112\sqrt{261} + 1044 = 1828 + 112\sqrt{261}.
\]

\[
-32h = -896 - 64\sqrt{261}.
\]

Entonces:

\[
h^2 - 32h + 1156 = 1828 + 112\sqrt{261} - 896 - 64\sqrt{261} + 1156.
\]

\[
= (1828 - 896 + 1156) + (112-64)\sqrt{261}.
\]

\[
= 2088 + 48\sqrt{261}.
\]

Entonces:

\[
x = \frac{900(28 + 2\sqrt{261})}{2088 + 48\sqrt{261}}.
\]

Simplifiquemos. Extraemos factor común \(24\) en el denominador:

\[
2088 + 48\sqrt{261} = 24(87 + 2\sqrt{261}).
\]

Y el numerador:

\[
900(28+2\sqrt{261}) = 1800(14 + \sqrt{261}).
\]

No veo una simplificación limpia inmediata. Calculemos numéricamente para ver si \(0<y<30\).

\[
h \approx 60.311.
\]

\[
h^2 - 32h + 1156 \approx 2088 + 48\cdot 16.155 \approx 2088 + 775.4 = 2863.4.
\]

\[
x \approx \frac{900 \cdot 60.311}{2863.4} \approx \frac{54280}{2863.4} \approx 18.956.
\]

\[
y = \frac{x(h-16)}{30} \approx \frac{18.956 \cdot 44.311}{30} \approx \frac{840.0}{30} \approx 28.0.
\]

Parece que \(y \approx 28 < 30\), y \(x \approx 19 < h\), así que \(Y\) está dentro del rectángulo. Esta raíz parece válida.

Sin embargo, el problema pide \(PQ\), que es \(h\). Normalmente en estos problemas se espera un valor entero. ¿Quizá hay otra interpretación o cometí un error en la posición de los centros?

---

**Paso 34: reconsiderar la posición de los centros con más cuidado**

En un triángulo acutángulo, el circuncentro está dentro del triángulo. Pero cuidado: para el triángulo \(\triangle PYS\), los vértices son \(P\) y \(S\) en la recta \(x=0\), y \(Y\) en \(x>0\). El interior del triángulo está efectivamente en \(x>0\). Por tanto, el centro debe estar en \(x>0\). Como la mediatriz de \(PS\) es \(y=15\), y la distancia al lado \(PS\) es 8, el centro podría estar en \(x=+8\) o en \(x=-8\). Para que esté dentro, debe ser \(x=+8\). Correcto.

Para \(\triangle QYR\), los vértices \(Q\) y \(R\) están en \(x=h\), y \(Y\) en \(x<h\). El interior está en \(x<h\). La mediatriz de \(QR\) es \(y=15\), la distancia al lado \(QR\) es 20. Para estar dentro, el centro debe estar en \(x=h-20\). Correcto.

Entonces la deducción parece correcta. El problema puede tener efectivamente una respuesta no entera, o quizá la clave está en que hay dos posibles posiciones y la otra da un valor entero.

---

**Paso 35: explorar la posibilidad de que ambos centros estén en lados opuestos**

Podríamos tener dos configuraciones adicionales: los centros de \(\triangle PYS\) y \(\triangle QYR\) podrían estar en posiciones que no impliquen necesariamente que el centro esté dentro. La condición de acutángulo sí obliga a que el circuncentro esté dentro. Pero hay una sutileza: la distancia del centro a la recta \(PS\) es 8, pero ¿el centro podría estar en \(x=-8\) y aun así el triángulo ser acutángulo?

Si el centro está en \(x=-8\), el ángulo \(\angle PYS\) sería obtuso, porque los tres vértices \(P, S, Y\) estarían todos en \(x\ge0\), y el centro en \(x<0\) quedaría fuera. En efecto, un triángulo con un vértice a un lado y el centro al otro lado de la base es obtuso. Como el triángulo es acutángulo, el centro debe estar en \(x=+8\).

Similarmente para el otro.

---

**Paso 36: examinar las condiciones de que ambos triángulos sean acutángulos con la raíz \(h\approx 60.31\)**

Con \(h\approx60.31\), \(x\approx19\), \(y\approx28\).

Triángulo \(PYS\): \(P(0,0), S(0,30), Y(19,28)\). ¿Es acutángulo? El centro estaría en \((8,15)\). Verifiquemos la distancia de \(Y\) al centro:

\[
(19-8)^2 + (28-15)^2 = 121 + 169 = 290 \approx 289.
\]

Casi exacto (diferencias por redondeo). El centro \((8,15)\) está dentro, bien.

Triángulo \(QYR\): \(Q(60.31,0), R(60.31,30), Y(19,28)\). El centro en \((h-20,15) \approx (40.31,15)\). Distancia de \(Y\) al centro:

\[
(19-40.31)^2 + (28-15)^2 \approx 454 + 169 = 623 \approx 625.
\]

Correcto. El centro \((40.31,15)\) está dentro del triángulo (entre \(x=19\) y \(x=60.31\)). Bien.

Y \(\angle PYQ = 90^\circ\): vectores \(YP=(-19,-28)\), \(YQ=(41.31,-28)\). Producto escalar:

\[
-19\cdot 41.31 + (-28)(-28) = -784.9 + 784 \approx -0.9 \approx 0.
\]

Correcto.

Así que la solución \(h = 28 + 2\sqrt{261}\) parece válida.

---

**Paso 37: comprobar si hay otra raíz válida entre 4 y 5 de la versión anterior**

En la versión anterior (con los centros en \(x=-8\) y \(x=h+20\)), obtuvimos una raíz \(h\approx 4.31\). Pero esa configuración corresponde a triángulos obtusos, no acutángulos, y por tanto queda descartada.

Además, el polinomio corregido \(h^3 - 72h^2 + 636h + 4160 = 0\) tiene dos raíces positivas: \(h=16\) (inválida porque \(Y=Q\)) y \(h = 28+2\sqrt{261}\) (válida).

Probemos si \(h=16\) da \(Y=Q\): con \(x=16\), \(y=0\). En efecto, \(Y=(16,0)=Q\), lo cual no está dentro. Y \(\angle PYQ = \angle PQQ\) no tiene sentido (ángulo degenerado). Entonces descartamos \(h=16\).

---

**Paso 38: verificar que no haya una raíz negativa relevante**

La tercera raíz es \(28 - 2\sqrt{261} \approx 28 - 32.31 = -4.31\), negativa. Descartada.

---

**Paso 39: ¿el problema espera un valor entero?**

El enunciado da circunradios 17 y 25, y \(QR=30\). Estos números forman ternas pitagóricas: 8-15-17 y 15-20-25. Esto sugiere fuertemente una solución elegante. Quizá la respuesta esperada sea entera, y mi deducción tiene algún error que lleva a un valor irracional.

Reconsideremos la condición de acutángulo. En realidad, para que un triángulo sea acutángulo, basta que todos sus ángulos sean agudos. En un triángulo con base \(PS=30\) y circunradio \(17\), la altura desde \(Y\) a \(PS\) y la posición horizontal del centro están relacionadas.

El centro del círculo circunscrito está en la intersección de las mediatrices. Para \(\triangle PYS\), la mediatriz de \(PS\) es \(y=15\). La mediatriz de \(PY\) o \(SY\) determina la coordenada \(x\) del centro. La condición de acutángulo no nos dice simplemente que el centro está dentro; eso es una consecuencia. Pero quizá la ambigüedad de signo no se resuelve por acutángulo de esa manera simple, pero sí parece.

Sin embargo, exploremos si la respuesta pretendida es \(PQ=40\). Veamos:

Si \(PQ=40=RS\), y \(QR=30=PS\). Rectángulo \(40\times 30\).

Para que \(\triangle PYS\) tenga circunradio 17 con lado \(PS=30\), \(\sin\angle PYS = 15/17\), \(\cos = 8/17\).

Para \(\triangle QYR\) con lado \(QR=30\), circunradio 25, \(\sin\angle QYR = 3/5\), \(\cos=4/5\).

Con \(PQ=40\), veamos si hay un \(Y\) que cumpla \(\angle PYQ=90^\circ\).

En un rectángulo \(40\times30\), si \(\angle PYQ=90^\circ\), \(Y\) está sobre el círculo de diámetro \(PQ\), que es el círculo de centro \((20,0)\) y radio 20. Pero \(Y\) debe tener \(0<y<30\).

Para el triángulo \(PYS\), con \(Y\) en ese círculo... la condición \(\sin\angle PYS = 15/17\) determina la ubicación. Probemos una combinación de ángulos que sumen 90 grados.

Alternativamente, expresemos la geometría en términos de los ángulos.

---

**Paso 40: enfoque con ángulos**

Sean \(\alpha = \angle QYP\) y \(\beta = \angle PY S\). Como \(\angle PYQ = 90^\circ\), en el punto \(Y\), las semirrectas \(YP\), \(YQ\), \(YS\), \(YR\) forman un esquema.

En realidad, \(YP\) y \(YQ\) son perpendiculares. Las semirrectas \(YS\) y \(YR\) están en direcciones que dependen de la posición de \(Y\).

Consideremos el ángulo \(\angle PYS\) (dado por su seno \(15/17\) y coseno \(8/17\)) y el ángulo \(\angle QYR\) (seno \(3/5\), coseno \(4/5\)).

Como \(PS\) y \(QR\) son lados paralelos verticales del rectángulo, y \(Y\) está dentro, los rayos \(YP\), \(YS\) van a los extremos del lado izquierdo; los rayos \(YQ\), \(YR\) van a los extremos del lado derecho.

La suma de los ángulos alrededor de \(Y\) es \(360^\circ\). Tenemos cuatro ángulos: \(\angle PYQ = 90^\circ\), \(\angle QYR\), \(\angle RYS\), \(\angle SYP\). Además, \(\angle PYS = \angle PY S\) es el ángulo entre \(YP\) y \(YS\).

Pero cuidado: \(\angle PYS\) es el ángulo en \(Y\) del triángulo \(PYS\), con rayos \(YP\) y \(YS\). Similarmente, \(\angle QYR\) es el ángulo en \(Y\) del triángulo \(QYR\).

Geométricamente, los cuatro rayos desde \(Y\) hacia los cuatro vértices del rectángulo: hacia \(P\) (abajo-izquierda), hacia \(Q\) (abajo-derecha), hacia \(R\) (arriba-derecha), hacia \(S\) (arriba-izquierda). En este orden en sentido antihorario o horario.

Supongamos que los rayos van en el orden: \(YP\), \(YQ\), \(YR\), \(YS\) (o similar). Dado que \(YP \perp YQ\), el ángulo entre \(YP\) y \(YQ\) es \(90^\circ\).

El ángulo \(\angle QYR\) es el ángulo entre \(YQ\) y \(YR\). El ángulo \(\angle PYS\) es el ángulo entre \(YP\) y \(YS\).

Si el orden cíclico es \(YP \to YQ \to YR \to YS\), entonces:

\[
\angle PYQ = 90^\circ,
\]
\[
\angle QYR = \text{dado},
\]
\[
\angle RYS = ?,
\]
\[
\angle SYP = \angle PYS = \text{dado}.
\]

La suma total es \(360^\circ\):

\[
90^\circ + \angle QYR + \angle RYS + \angle PYS = 360^\circ.
\]

\[
\angle RYS = 270^\circ - \angle QYR - \angle PYS.
\]

Pero \(\angle RYS\) no puede ser mayor que \(180^\circ\) si los rayos están en ese orden... En realidad, los ángulos \(\angle QYR\) y \(\angle PYS\) son agudos, con cosenos \(4/5\) y \(8/17\). Entonces \(\angle QYR + \angle PYS\) es, en radianes, algo menor que \(90^\circ +\) algo, veamos numéricamente:

\[
\angle QYR = \cos^{-1}(4/5) \approx 36.87^\circ.
\]

\[
\angle PYS = \cos^{-1}(8/17) \approx 61.93^\circ.
\]

Suma \(\approx 98.8^\circ\).

Entonces \(\angle RYS \approx 360 - 90 - 98.8 = 171.2^\circ\), que es menor que \(180^\circ\). Eso es consistente si el orden de los rayos alrededor de \(Y\) es \(YP, YQ, YR, YS\), yendo en sentido de las agujas del reloj o antihorario.

Esta configuración implica que \(YR\) y \(YS\) están en lados opuestos, lo cual encaja con que \(R\) y \(S\) están en la parte superior del rectángulo.

---

**Paso 41: calcular \(PQ\) a partir de los ángulos**

En el triángulo \(PYS\), conocemos \(PS=30\) y los ángulos:

\[
\angle PYS = \phi, \quad \sin\phi = 15/17, \cos\phi=8/17.
\]

Los otros ángulos de \(\triangle PYS\): sean \(\angle YPS = u\) y \(\angle YSP = v\). Entonces \(u+v+\phi = 180^\circ\).

En el triángulo \(QYR\), \(QR=30\), \(\angle QYR = \theta\), \(\sin\theta=3/5\), \(\cos\theta=4/5\), y los otros ángulos \(u'\) y \(v'\).

Relación entre los ángulos de ambos triángulos: como \(PY \perp QY\), hay una relación entre \(u\) y \(u'\).

Consideremos las rectas: en el punto \(P\), el ángulo entre \(PQ\) (horizontal) y \(PY\) es \(u\). En el punto \(Q\), el ángulo entre \(QP\) (horizontal) y \(QY\) es \(u'\).

Como \(YP \perp YQ\), y \(PQ\) es horizontal compartida, los ángulos en \(P\) y \(Q\) respecto a la horizontal están relacionados.

De hecho, si \(Y\) está por encima de \(PQ\), entonces desde \(P\), el rayo \(PY\) forma un ángulo \(u\) con la horizontal. Desde \(Q\), el rayo \(QY\) forma un ángulo \(u'\) con la horizontal (hacia la izquierda, pero medido de la manera usual).

La condición \(PY \perp QY\) se traduce en que la pendiente de \(PY\) es el recíproco negativo de la pendiente de \(QY\).

Pendiente de \(PY\): \(\tan u\). Pendiente de \(QY\): \(-\tan u'\) (porque va hacia arriba-izquierda). La perpendicularidad: \(\tan u \cdot (-\tan u') = -1\), es decir, \(\tan u \cdot \tan u' = 1\), o \(u + u' = 90^\circ\) (si ambos agudos).

Entonces \(u + u' = 90^\circ\).

---

**Paso 42: relacionar con los triángulos**

En \(\triangle PYS\), con \(PS\) vertical, los ángulos en \(P\) y \(S\) no son simplemente \(u\) y \(v\) respecto a la horizontal...

Mejor usemos coordenadas de nuevo, pero en términos de ángulos y alturas.

La altura de \(Y\) sobre la base \(PQ\) es \(y\). La distancia horizontal de \(Y\) a \(P\) es \(x\), y a \(Q\) es \(h-x\).

La condición \(\angle PYQ=90^\circ\) da \(x(h-x) = y^2\), o equivalentemente \(x^2+y^2=xh\), como ya teníamos.

---

**Paso 43: usar la fórmula del circunradio en términos de los lados**

Para \(\triangle PYS\), sus lados son:

\[
PY = \sqrt{x^2+y^2},
\]

\[
SY = \sqrt{x^2+(30-y)^2},
\]

\[
PS = 30.
\]

El circunradio \(R=17\) cumple:

\[
R = \frac{abc}{4\Delta},
\]

donde \(\Delta = \frac12 \cdot 30 \cdot x = 15x\) (base \(PS\) por altura horizontal \(x\)).

Entonces:

\[
17 = \frac{30 \cdot PY \cdot SY}{4 \cdot 15x} = \frac{PY \cdot SY}{2x}.
\]

\[
PY \cdot SY = 34x.
\]

\[
\sqrt{x^2+y^2}\,\sqrt{x^2+(30-y)^2} = 34x.
\]

Análogamente para \(\triangle QYR\):

Base \(QR=30\), altura horizontal \(h-x\), área \(\Delta = 15(h-x)\).

\[
25 = \frac{30 \cdot QY \cdot RY}{4 \cdot 15(h-x)} = \frac{QY \cdot RY}{2(h-x)}.
\]

\[
QY \cdot RY = 50(h-x).
\]

\[
\sqrt{(h-x)^2+y^2}\,\sqrt{(h-x)^2+(30-y)^2} = 50(h-x).
\]

---

**Paso 44: simplificar con la perpendicularidad**

Usamos \(x^2+y^2 = xh\), así que \(\sqrt{x^2+y^2}=\sqrt{xh}\).

También \((h-x)^2+y^2 = h(h-x)\), como vimos. Entonces:

\[
QY = \sqrt{h(h-x)}.
\]

Las ecuaciones quedan:

\[
\sqrt{xh}\,\sqrt{x^2+(30-y)^2} = 34x. \tag{A}
\]

\[
\sqrt{h(h-x)}\,\sqrt{(h-x)^2+(30-y)^2} = 50(h-x). \tag{B}
\]

---

**Paso 45: dividir por los factores**

De (A):

\[
\sqrt{x^2+(30-y)^2} = \frac{34x}{\sqrt{xh}} = 34\sqrt{\frac{x}{h}}.
\]

Elevando al cuadrado:

\[
x^2+(30-y)^2 = \frac{1156x}{h}. \tag{A'}
\]

De (B):

\[
\sqrt{(h-x)^2+(30-y)^2} = \frac{50(h-x)}{\sqrt{h(h-x)}} = 50\sqrt{\frac{h-x}{h}}.
\]

Elevando al cuadrado:

\[
(h-x)^2+(30-y)^2 = \frac{2500(h-x)}{h}. \tag{B'}
\]

---

**Paso 46: restar las ecuaciones**

Restamos (B') − (A'):

\[
(h-x)^2 - x^2 = \frac{2500(h-x)}{h} - \frac{1156x}{h}.
\]

Lado izquierdo:

\[
h^2 - 2hx + x^2 - x^2 = h^2 - 2hx = h(h-2x).
\]

Lado derecho:

\[
\frac{2500h - 2500x - 1156x}{h} = \frac{2500h - 3656x}{h}.
\]

Entonces:

\[
h(h-2x) = \frac{2500h - 3656x}{h}.
\]

\[
h^2(h-2x) = 2500h - 3656x.
\]

\[
h^3 - 2h^2x = 2500h - 3656x.
\]

Reorganizamos:

\[
h^3 - 2500h = 2h^2x - 3656x = x(2h^2 - 3656).
\]

\[
x = \frac{h(h^2-2500)}{2h^2 - 3656} = \frac{h(h^2-2500)}{2(h^2-1828)}.
\]

Este es exactamente el mismo resultado que obtuvimos en el paso 7, ¡antes de introducir la condición de acutángulo! Interesante: la condición de acutángulo nos forzó a tomar los centros dentro, pero esta deducción alternativa no usa la posición del centro, solo el circunradio y la perpendicularidad.

---

**Paso 47: otro enfoque con la ecuación de \(y\)**

De la perpendicularidad y la definición del triángulo, podemos plantear otra relación para \(y\).

Del triángulo \(PYS\), la altura de \(Y\) sobre la base \(PS\) es \(x\), y la altura del triángulo respecto a la base \(PY\) o \(SY\) podemos expresar...

Alternativamente, usemos la fórmula del área con el circunradio:

\[
R = \frac{PS}{2\sin\angle PYS} = 17.
\]

Ya sabíamos que \(\sin\angle PYS = 15/17\).

El ángulo \(\angle PYS\) es el ángulo entre vectores \(YP=(-x,-y)\) y \(YS=(-x,30-y)\). Su coseno:

\[
\cos\angle PYS = \frac{YP\cdot YS}{|YP|\,|YS|}.
\]

\[
YP\cdot YS = (-x)(-x) + (-y)(30-y) = x^2 - 30y + y^2.
\]

Usando \(x^2+y^2=xh\):

\[
YP\cdot YS = xh - 30y.
\]

El coseno debe ser \(8/17\) (porque el triángulo es acutángulo, el ángulo es agudo):

\[
\frac{xh - 30y}{\sqrt{xh}\,\sqrt{x^2+(30-y)^2}} = \frac{8}{17}.
\]

Similarmente, para \(\angle QYR\), coseno \(4/5\):

\[
\frac{h(h-x) - 30y}{\sqrt{h(h-x)}\,\sqrt{(h-x)^2+(30-y)^2}} = \frac{4}{5}.
\]

Pero quizá sea más simple usar directamente la condición de acutángulo a través del producto escalar positivo.

---

**Paso 48: usar la condición de acutángulo explícitamente**

Para que \(\triangle PYS\) sea acutángulo, los tres ángulos son agudos. El ángulo en \(Y\) ya lo tenemos agudo (coseno \(8/17>0\)). El ángulo en \(P\): el producto escalar de \(PY\) y \(PS\) debe ser positivo.

\[
\overrightarrow{PY} = (x,y), \quad \overrightarrow{PS} = (0,30).
\]

\[
\overrightarrow{PY}\cdot\overrightarrow{PS} = 30y > 0, \quad \text{siempre positivo}.
\]

El ángulo en \(S\): producto de \(\overrightarrow{SY}=(x, y-30)\) y \(\overrightarrow{SP}=(0,-30)\):

\[
\overrightarrow{SY}\cdot\overrightarrow{SP} = (y-30)(-30) = 30(30-y) > 0.
\]

Siempre positivo porque \(y<30\). Entonces, en realidad, \(\triangle PYS\) es automáticamente acutángulo siempre que \(Y\) esté dentro del rectángulo. Espera, eso no es cierto: el ángulo en \(Y\) podría ser obtuso.

El ángulo en \(Y\) de \(\triangle PYS\) es agudo si \(\cos\angle PYS > 0\), es decir, \(YP\cdot YS > 0\):

\[
YP\cdot YS = (-x)(-x) + (-y)(30-y) = x^2 - 30y + y^2.
\]

Con \(x^2+y^2 = xh\):

\[
YP\cdot YS = xh - 30y.
\]

Para que sea agudo, \(xh - 30y > 0\), es decir, \(y < \frac{xh}{30}\).

Similarmente, \(\triangle QYR\) agudo requiere \(\cos\angle QYR >0\):

\[
YQ\cdot YR = (h-x)^2 + (-y)(30-y) = (h-x)^2 - 30y + y^2.
\]

Con \((h-x)^2+y^2 = h(h-x)\):

\[
YQ\cdot YR = h(h-x) - 30y = h^2 - hx - 30y.
\]

Para agudo: \(h^2 - hx - 30y > 0\).

Entonces las condiciones de acutángulo son:

\[
xh - 30y > 0, \tag{AC1}
\]

\[
h^2 - hx - 30y > 0. \tag{AC2}
\]

---

**Paso 49: relacionar \(x\) y \(y\) con el circunradio**

Ya tenemos la relación del seno del ángulo en \(Y\):

Para \(\triangle PYS\):

\[
\sin\angle PYS = \frac{2\Delta}{PY\cdot SY} = \frac{30x}{PY\cdot SY} = \frac{15}{17}.
\]

Entonces:

\[
PY\cdot SY = 34x.
\]

Y el coseno:

\[
\cos\angle PYS = \frac{YP\cdot YS}{PY\cdot SY} = \frac{xh - 30y}{34x} = \frac{8}{17}.
\]

\[
17(xh - 30y) = 272x.
\]

\[
17xh - 510y = 272x.
\]

Para \(\triangle QYR\):

\[
\sin\angle QYR = \frac{30(h-x)}{QY\cdot RY} = \frac{3}{5}.
\]

\[
QY\cdot RY = 50(h-x).
\]

Coseno:

\[
\cos\angle QYR = \frac{YQ\cdot YR}{QY\cdot RY} = \frac{h^2 - hx - 30y}{50(h-x)} = \frac{4}{5}.
\]

\[
5(h^2 - hx - 30y) = 200(h-x).
\]

\[
5h^2 - 5hx - 150y = 200h - 200x.
\]

---

**Paso 50: resolver el sistema**

Tenemos:

\[
17xh - 510y = 272x. \tag{1}
\]

\[
5h^2 - 5hx - 150y = 200h - 200x. \tag{2}
\]

Y la perpendicularidad:

\[
x^2 + y^2 = xh. \tag{3}
\]

De (1):

\[
510y = 17xh - 272x = x(17h - 272).
\]

\[
y = \frac{x(17h - 272)}{510}. \tag{4}
\]

De (2):

\[
150y = 5h^2 - 5hx - 200h + 200x.
\]

\[
y = \frac{5h^2 - 5hx - 200h + 200x}{150}. \tag{5}
\]

Igualamos (4) y (5):

\[
\frac{x(17h-272)}{510} = \frac{5h^2 - 5hx - 200h + 200x}{150}.
\]

Multiplicamos por 510:

\[
x(17h-272) = 3.4 \cdot (5h^2 - 5hx - 200h + 200x).
\]

Mejor convertimos a fracciones exactas. \(510/150 = 17/5\). Entonces:

\[
x(17h-272) = \frac{17}{5}\bigl(5h^2 - 5hx - 200h + 200x\bigr).
\]

\[
5x(17h-272) = 17(5h^2 - 5hx - 200h + 200x).
\]

\[
85xh - 1360x = 85h^2 - 85hx - 3400h + 3400x.
\]

Llevamos todo a un lado:

\[
85xh + 85hx - 1360x - 3400x - 85h^2 + 3400h = 0.
\]

\[
170xh - 4760x - 85h^2 + 3400h = 0.
\]

Dividimos entre 85:

\[
2xh - 56x - h^2 + 40h = 0.
\]

\[
2xh - 56x = h^2 - 40h.
\]

\[
x(2h - 56) = h(h - 40).
\]

\[
x = \frac{h(h-40)}{2h-56} = \frac{h(h-40)}{2(h-28)}. \tag{6}
\]

---

**Paso 51: usar la perpendicularidad**

Sustituyamos (4) y (6) en (3).

De (4):

\[
y = \frac{x(17h-272)}{510}.
\]

Notemos que \(17h - 272 = 17(h-16)\).

Entonces (4):

\[
y = \frac{x \cdot 17(h-16)}{510} = \frac{x(h-16)}{30}.
\]

¡Esto es exactamente la ecuación (7') que ya habíamos obtenido en el paso 26! Bueno, consistente.

Además, de (6):

\[
x = \frac{h(h-40)}{2(h-28)}.
\]

Ahora sustituimos \(y = x(h-16)/30\) en \(x^2+y^2=xh\):

\[
x^2 \left(1 + \frac{(h-16)^2}{900}\right) = xh.
\]

Dividimos entre \(x\):

\[
x \cdot \frac{(h-16)^2+900}{900} = h.
\]

\[
x = \frac{900h}{(h-16)^2+900} = \frac{900h}{h^2 -32h+1156}. \tag{7}
\]

Igualamos (6) y (7):

\[
\frac{h(h-40)}{2(h-28)} = \frac{900h}{h^2-32h+1156}.
\]

Como \(h \neq 0\), dividimos entre \(h\):

\[
\frac{h-40}{2(h-28)} = \frac{900}{h^2-32h+1156}.
\]

\[
(h-40)(h^2-32h+1156) = 1800(h-28).
\]

Expandimos:

\[
h^3 - 32h^2 + 1156h - 40h^2 + 1280h - 46240 = 1800h - 50400.
\]

\[
h^3 - 72h^2 + (1156+1280)h - 46240 = 1800h - 50400.
\]

\[
h^3 - 72h^2 + 2436h - 46240 = 1800h - 50400.
\]

\[
h^3 - 72h^2 + 636h + 4160 = 0.
\]

¡Este es exactamente el mismo polinomio del paso 29! Por lo tanto, la solución \(h = 28 + 2\sqrt{261}\) es consistente. Y \(h=16\) es la otra raíz, pero con \(h=16\), de (6) obtenemos \(x = 0\), y de (4) \(y=0\), degenerado.

---

**Paso 52: confirmar la respuesta**

La única solución válida es \(h = 28 + 2\sqrt{261}\).

Verifiquemos numéricamente todos los datos con \(h = 28+2\sqrt{261}\):

\[
\sqrt{261} \approx 16.155, \quad h \approx 60.31.
\]

\[
x = \frac{h(h-40)}{2(h-28)} = \frac{60.31 \cdot 20.31}{2 \cdot 32.31} \approx \frac{1225}{64.62} \approx 18.96.
\]

\[
y = \frac{x(h-16)}{30} \approx \frac{18.96 \cdot 44.31}{30} \approx 28.0.
\]

Verifiquemos \(x^2+y^2 \approx 359 + 784 = 1143\), y \(xh \approx 18.96 \cdot 60.31 \approx 1143\). Correcto.

Triángulo \(PYS\):

\[
\sin\angle PYS = \frac{30x}{34x} = \frac{15}{17}? \quad \text{Sí, por construcción.}
\]

Triángulo \(QYR\):

\[
\sin\angle QYR = \frac{3}{5}, \quad \text{por construcción.}
\]

Condiciones de acutángulo:

\[
xh - 30y \approx 1143 - 840 = 303 > 0.
\]

\[
h^2 - hx - 30y \approx 3637 - 1143 - 840 = 1654 > 0.
\]

Ambas se cumplen.

Por lo tanto, \(PQ = h = 28 + 2\sqrt{261}\).

---

**Paso 53: verificar la raíz \(h=16\) una vez más**

Con \(h=16\), de (6):

\[
x = \frac{16(16-40)}{2(16-28)} = \frac{16(-24)}{2(-12)} = \frac{-384}{-24} = 16.
\]

\[
y = \frac{x(h-16)}{30} = \frac{16\cdot 0}{30} = 0.
\]

\(Y=(16,0)=Q\). No está dentro del rectángulo. Descartada.

---

**Paso 54: verificar la raíz negativa**

La tercera raíz es \(28 - 2\sqrt{261} \approx -4.31\), negativa, descartada.

---

**Conclusión**

La única solución válida es \(PQ = 28 + 2\sqrt{261}\).

Pero espera: revisemos si el problema quizá espera \(PQ=40\) con otra interpretación. Reconsideremos si acaso los triángulos \(\triangle PYS\) y \(\triangle QYR\) son acutángulos no solo por el ángulo en \(Y\), sino que quizá la interpretación de "acutángulo" impide que \(Y\) esté tan lejos. Aun así, con \(h\approx60.31\), \(Y\approx(19,28)\) está dentro y los triángulos son acutángulos. Todo cuadra.

Sin embargo, hay una sutileza: ¿el ángulo \(\angle PYQ=90^\circ\) con \(Y\) dentro del rectángulo siempre da \(x^2+y^2=xh\), asumiendo \(P(0,0)\) y \(Q(h,0)\). Correcto.

Vamos a dudar de la condición de que ambos triángulos son acutángulos y simplemente usar el circunradio para imponer el ángulo. Ya lo hicimos. El resultado es \(h=28+2\sqrt{261}\).

Pero el problema probablemente proviene de una competencia y debería tener una respuesta entera. Revisemos si hay un error en el paso 5, donde igualamos senos.

---

**Paso 55: revisar el paso 5 con cuidado**

Para \(\triangle PYS\):

Los lados adyacentes a \(Y\) son \(PY\) y \(SY\). El ángulo en \(Y\) es \(\angle PYS\). El seno de ese ángulo está dado por:

\[
\sin\angle PYS = \frac{|\overrightarrow{YP} \times \overrightarrow{YS}|}{|YP|\,|YS|}.
\]

\[
\overrightarrow{YP} = P - Y = (-x, -y).
\]

\[
\overrightarrow{YS} = S - Y = (-x, 30-y).
\]

Producto cruz (determinante):

\[
(-x)(30-y) - (-y)(-x) = -x(30-y) - xy = -30x + xy - xy = -30x.
\]

Valor absoluto: \(30x\). Correcto.

Entonces:

\[
\sin\angle PYS = \frac{30x}{PY\cdot SY}.
\]

Y por el circunradio:

\[
\sin\angle PYS = \frac{PS}{2R} = \frac{30}{34} = \frac{15}{17}.
\]

Igualando:

\[
\frac{30x}{PY\cdot SY} = \frac{15}{17}.
\]

\[
PY\cdot SY = \frac{30x \cdot 17}{15} = 34x.
\]

Correcto.

Para \(\triangle QYR\):

\[
\overrightarrow{YQ} = (h-x, -y), \quad \overrightarrow{YR} = (h-x, 30-y).
\]

Producto cruz:

\[
(h-x)(30-y) - (-y)(h-x) = (h-x)(30-y) + y(h-x) = 30(h-x).
\]

Correcto.

\[
\sin\angle QYR = \frac{30(h-x)}{QY\cdot RY} = \frac{QR}{2R} = \frac{30}{50} = \frac{3}{5}.
\]

\[
QY\cdot RY = \frac{30(h-x)\cdot 5}{3} = 50(h-x).
\]

Correcto.

---

**Paso 56: usar solo los senos para plantear ecuaciones**

Elevamos al cuadrado el seno y usamos la perpendicularidad.

Para \(\triangle PYS\):

\[
PY = \sqrt{x^2+y^2} = \sqrt{xh}.
\]

\[
SY = \sqrt{x^2+(30-y)^2}.
\]

Entonces:

\[
\sqrt{xh} \cdot \sqrt{x^2+(30-y)^2} = 34x.
\]

Elevando al cuadrado:

\[
xh\,[x^2+(30-y)^2] = 1156x^2.
\]

Dividimos entre \(x\) (dado \(x>0\)):

\[
h\,[x^2+(30-y)^2] = 1156x.
\]

Para \(\triangle QYR\):

\[
QY = \sqrt{(h-x)^2+y^2} = \sqrt{h(h-x)}.
\]

\[
RY = \sqrt{(h-x)^2+(30-y)^2}.
\]

\[
\sqrt{h(h-x)}\,\sqrt{(h-x)^2+(30-y)^2} = 50(h-x).
\]

Elevando al cuadrado:

\[
h(h-x)[(h-x)^2+(30-y)^2] = 2500(h-x)^2.
\]

Dividimos entre \(h-x\):

\[
h[(h-x)^2+(30-y)^2] = 2500(h-x).
\]

---

**Paso 57: simplificar usando la perpendicularidad**

De \(x^2+y^2=xh\), tenemos \(x^2 = xh - y^2\).

Entonces:

\[
x^2 + (30-y)^2 = xh - y^2 + 900 - 60y + y^2 = xh + 900 - 60y.
\]

\[
(h-x)^2 + (30-y)^2 = h^2 - 2hx + x^2 + 900 - 60y + y^2.
\]

Con \(x^2+y^2 = xh\):

\[
= h^2 - 2hx + xh + 900 - 60y = h^2 - hx + 900 - 60y.
\]

Entonces las ecuaciones (A') y (B') del paso 45 son correctas.

---

**Paso 58: otra forma de resolver: usar el ángulo de perpendicularidad**

Quizá convenga plantear las longitudes de los lados de los triángulos \(PYS\) y \(QYR\) en términos de los ángulos y después igualar la altura \(y\).

Los ángulos en \(Y\): \(\phi = \angle PYS\), \(\theta = \angle QYR\), con:

\[
\sin\phi = \frac{15}{17}, \quad \cos\phi = \frac{8}{17},
\]

\[
\sin\theta = \frac{3}{5}, \quad \cos\theta = \frac{4}{5}.
\]

Los lados del triángulo \(PYS\): \(PS=30\). Por la ley de senos:

\[
\frac{PS}{\sin\phi} = \frac{30}{15/17} = 34.
\]

Entonces:

\[
PY = 34 \sin v, \quad SY = 34 \sin u,
\]

donde \(u=\angle YPS\), \(v=\angle YSP\), y \(u+v = 180^\circ - \phi\).

Similarmente, en \(\triangle QYR\):

\[
\frac{QR}{\sin\theta} = \frac{30}{3/5} = 50.
\]

\[
QY = 50 \sin v', \quad RY = 50 \sin u',
\]

donde \(u' = \angle YQR\), \(v'=\angle YRQ\), y \(u'+v' = 180^\circ - \theta\).

---

**Paso 59: relacionar \(u\) y \(u'\) por la perpendicularidad**

En el punto \(P\), el ángulo entre \(PQ\) (horizontal) y \(PY\) es \(u\). En el punto \(Q\), el ángulo entre \(QP\) (horizontal) y \(QY\) es \(u'\). Como \(PY \perp QY\), se tiene \(u + u' = 90^\circ\) (asumiendo que \(Y\) está arriba de \(PQ\)).

Entonces \(u' = 90^\circ - u\), luego \(\sin u' = \cos u\), \(\cos u' = \sin u\).

---

**Paso 60: expresar \(PQ\) en términos de \(u\)**

La distancia horizontal de \(P\) a \(Y\) es \(x = PY \cos u = 34 \sin v \cos u\).

La distancia horizontal de \(Y\) a \(Q\) es \(h-x = QY \cos u' = 50 \sin v' \cos u'\).

Entonces:

\[
h = x + (h-x) = 34 \sin v \cos u + 50 \sin v' \sin u.
\]

Además, la altura \(y\) de \(Y\) sobre \(PQ\) es:

\[
y = PY \sin u = 34 \sin v \sin u,
\]

y también:

\[
y = QY \sin u' = 50 \sin v' \sin u' = 50 \sin v' \cos u.
\]

---

**Paso 61: relacionar \(v\) y \(v'\) con \(u\)**

En \(\triangle PYS\):

\[
u + v + \phi = 180^\circ \Rightarrow v = 180^\circ - \phi - u.
\]

\[
\sin v = \sin(\phi + u) = \sin\phi \cos u + \cos\phi \sin u = \frac{15}{17}\cos u + \frac{8}{17}\sin u.
\]

En \(\triangle QYR\):

\[
u' + v' + \theta = 180^\circ \Rightarrow v' = 180^\circ - \theta - u'.
\]

Con \(u' = 90^\circ - u\):

\[
v' = 180^\circ - \theta - (90^\circ - u) = 90^\circ - \theta + u.
\]

\[
\sin v' = \sin(90^\circ - \theta + u) = \cos(\theta - u) = \cos\theta\cos u + \sin\theta\sin u.
\]

\[
\sin v' = \frac{4}{5}\cos u + \frac{3}{5}\sin u.
\]

---

**Paso 62: igualar las expresiones de \(y\)**

De \(\triangle PYS\):

\[
y = 34 \sin v \sin u = 34 \left(\frac{15}{17}\cos u + \frac{8}{17}\sin u\right)\sin u = 30\sin u \cos u + 16 \sin^2 u.
\]

De \(\triangle QYR\):

\[
y = 50 \sin v' \cos u = 50 \left(\frac{4}{5}\cos u + \frac{3}{5}\sin u\right)\cos u = 40\cos^2 u + 30 \sin u \cos u.
\]

Igualamos:

\[
30\sin u \cos u + 16 \sin^2 u = 40\cos^2 u + 30\sin u \cos u.
\]

\[
16 \sin^2 u = 40 \cos^2 u.
\]

\[
\frac{\sin^2 u}{\cos^2 u} = \frac{40}{16} = \frac{5}{2}.
\]

\[
\tan^2 u = \frac{5}{2}.
\]

\[
\tan u = \frac{\sqrt{10}}{2} \quad (\text{positivo, pues } u \text{ es agudo}).
\]

Entonces:

\[
\sin u = \frac{\sqrt{10}}{\sqrt{10+4}} = \frac{\sqrt{10}}{\sqrt{14}}, \quad \cos u = \frac{2}{\sqrt{14}}.
\]

---

**Paso 63: calcular \(h = PQ\)**

Tenemos:

\[
h = x + (h-x) = 34 \sin v \cos u + 50 \sin v' \sin u.
\]

Sustituimos \(\sin v\) y \(\sin v'\):

\[
\sin v = \frac{15}{17}\cos u + \frac{8}{17}\sin u.
\]

\[
\sin v' = \frac{4}{5}\cos u + \frac{3}{5}\sin u.
\]

Entonces:

\[
h = 34 \left(\frac{15}{17}\cos u + \frac{8}{17}\sin u\right)\cos u + 50 \left(\frac{4}{5}\cos u + \frac{3}{5}\sin u\right)\sin u.
\]

\[
h = 30\cos^2 u + 16 \sin u \cos u + 40 \cos u \sin u + 30 \sin^2 u.
\]

\[
h = 30\cos^2 u + 16 \sin u \cos u + 40 \sin u \cos u + 30 \sin^2 u.
\]

\[
h = 30(\cos^2 u + \sin^2 u) + 56 \sin u \cos u.
\]

\[
h = 30 + 56 \sin u \cos u.
\]

Con \(\sin u = \frac{\sqrt{10}}{\sqrt{14}}\), \(\cos u = \frac{2}{\sqrt{14}}\):

\[
\sin u \cos u = \frac{2\sqrt{10}}{14} = \frac{\sqrt{10}}{7}.
\]

\[
h = 30 + 56 \cdot \frac{\sqrt{10}}{7} = 30 + 8\sqrt{10}.
\]

---

**Paso 64: ¡una respuesta diferente!**

Ahora obtenemos \(h = 30 + 8\sqrt{10} \approx 30 + 25.30 = 55.30\), que no coincide con el \(28 + 2\sqrt{261} \approx 60.31\) anterior. Hay una inconsistencia en algún razonamiento.

Esto sugiere que en algún lugar cometí un error. Comparemos ambos enfoques.

---

**Paso 65: identificar el error**

En el enfoque de ángulos, asumí \(u + u' = 90^\circ\). Verifiquemos si esto es correcto.

En el punto \(P\), el ángulo entre \(PQ\) (dirección horizontal hacia la derecha) y \(PY\) es \(u\). El vector \(PY\) va de \(P\) a \(Y\), con ángulo \(u\) sobre la horizontal.

En el punto \(Q\), el ángulo entre \(QP\) (dirección horizontal hacia la izquierda) y \(QY\) es \(u'\). El vector \(QY\) va de \(Q\) a \(Y\), apuntando hacia arriba-izquierda. El ángulo entre la dirección horizontal izquierda y \(QY\) es \(u'\).

La condición \(PY \perp QY\) significa que el ángulo entre los vectores \(PY\) (ángulo \(u\) desde la horizontal derecha) y \(QY\) (ángulo \(180^\circ - u'\) desde la horizontal derecha, ya que va hacia izquierda y arriba) es \(90^\circ\).

El ángulo entre \(PY\) (dirección con ángulo \(u\)) y \(QY\) (dirección con ángulo \(180^\circ - u'\)) es:

\[
(180^\circ - u') - u = 90^\circ \quad \text{o} \quad 270^\circ - u' - u.
\]

La diferencia aguda sería \(180^\circ - u' - u = 90^\circ\), si \(u + u' = 90^\circ\). Correcto.

Entonces \(u + u' = 90^\circ\) es correcto.

---

**Paso 66: revisar los senos de los triángulos**

En \(\triangle PYS\), los ángulos en \(P\), \(Y\), \(S\) son \(u\), \(\phi\), \(v\). Pero espera: ¿el ángulo en \(P\) del triángulo \(PYS\) es realmente \(u\)?

El ángulo en \(P\) de \(\triangle PYS\) es el ángulo entre \(PY\) y \(PS\). El vector \(PS\) apunta verticalmente hacia arriba (desde \(P\) a \(S\)). El vector \(PY\) forma un ángulo \(u\) con la horizontal, hacia arriba. Entonces el ángulo entre \(PY\) y \(PS\) (vertical) es \(90^\circ - u\), ¡no \(u\)!

¡Ahí está el error! En el paso 59, dije que el ángulo entre \(PQ\) (horizontal) y \(PY\) es \(u\), lo cual es correcto. Pero en el triángulo \(PYS\), el ángulo en \(P\) es entre \(PY\) y \(PS\) (vertical), que es \(90^\circ - u\), no \(u\).

Entonces \(u\) no es el ángulo en \(P\) del triángulo \(PYS\). Definamos correctamente.

---

**Paso 67: corregir la definición de ángulos**

Definamos:

En el punto \(P\) del triángulo \(PYS\), el ángulo \(\angle YPS = \alpha\). Entonces \(\alpha\) es el ángulo entre \(PY\) y \(PS\) (vertical). Como \(PS\) es vertical y \(PQ\) es horizontal, el ángulo entre \(PY\) y la horizontal es \(90^\circ - \alpha\).

Análogamente, en el punto \(Q\) del triángulo \(QYR\), el ángulo \(\angle YQR = \beta\). El ángulo entre \(QY\) y la horizontal (hacia la izquierda) es \(90^\circ - \beta\).

La condición \(PY \perp QY\): el ángulo entre \(PY\) (que está a \(90^\circ - \alpha\) sobre la horizontal) y \(QY\) (que está a \(90^\circ - \beta\) sobre la horizontal izquierda, es decir, en dirección \(90^\circ + (90^\circ - \beta) = 180^\circ - \beta\) desde la horizontal derecha).

Entonces el ángulo entre \(PY\) y \(QY\) es:

\[
(180^\circ - \beta) - (90^\circ - \alpha) = 90^\circ - \beta + \alpha.
\]

Para que sean perpendiculares:

\[
\alpha - \beta + 90^\circ = 90^\circ \quad \Rightarrow \quad \alpha = \beta.
\]

Entonces \(\alpha = \beta\), donde \(\alpha = \angle YPS\) y \(\beta = \angle YQR\).

---

**Paso 68: rehacer el enfoque de ángulos**

En \(\triangle PYS\), los ángulos:

\[
\alpha = \angle YPS, \quad \phi = \angle PYS, \quad v = \angle YSP.
\]

Con \(\alpha + \phi + v = 180^\circ\).

En \(\triangle QYR\), los ángulos:

\[
\beta = \angle YQR = \alpha, \quad \theta = \angle QYR, \quad v' = \angle YRQ.
\]

Con \(\alpha + \theta + v' = 180^\circ\).

---

**Paso 69: alturas y distancias horizontales**

En \(\triangle PYS\), con \(PS=30\) vertical y \(Y\) a la derecha:

La distancia horizontal de \(Y\) a \(PS\) es \(x = PY \sin \alpha\), porque el ángulo entre \(PY\) y la vertical \(PS\) es \(\alpha\), y la componente horizontal de \(PY\) es \(PY\sin\alpha\). Alternativamente, \(x = SY\sin v\).

La altura de \(Y\) sobre \(P\) es \(y = PY \cos\alpha\) (componente vertical de \(PY\)).

En \(\triangle QYR\), la distancia horizontal de \(Y\) a \(QR\) es \(h-x = QY \sin\beta = QY\sin\alpha\).

La altura de \(Y\) sobre \(Q\) es \(y = QY\cos\beta = QY\cos\alpha\).

---

**Paso 70: usar la ley de senos para las longitudes**

Para \(\triangle PYS\):

\[
\frac{PS}{\sin\phi} = \frac{30}{15/17} = 34.
\]

Entonces:

\[
PY = 34 \sin v, \quad SY = 34 \sin \alpha.
\]

Para \(\triangle QYR\):

\[
\frac{QR}{\sin\theta} = \frac{30}{3/5} = 50.
\]

\[
QY = 50 \sin v', \quad RY = 50 \sin \alpha.
\]

---

**Paso 71: expresar \(x\) y \(y\)**

De \(\triangle PYS\):

\[
x = PY \sin\alpha = 34 \sin v \sin\alpha.
\]

\[
y = PY \cos\alpha = 34 \sin v \cos\alpha.
\]

De \(\triangle QYR\):

\[
h-x = QY \sin\alpha = 50 \sin v' \sin\alpha.
\]

\[
y = QY \cos\alpha = 50 \sin v' \cos\alpha.
\]

---

**Paso 72: igualar las expresiones de \(y\)**

\[
34 \sin v \cos\alpha = 50 \sin v' \cos\alpha.
\]

Si \(\cos\alpha \neq 0\), dividimos:

\[
34 \sin v = 50 \sin v'.
\]

\[
\sin v' = \frac{34}{50} \sin v = \frac{17}{25} \sin v.
\]

---

**Paso 73: expresar \(v\) y \(v'\) en términos de \(\alpha\)**

En \(\triangle PYS\):

\[
v = 180^\circ - \alpha - \phi.
\]

\[
\sin v = \sin(\alpha + \phi) = \sin\alpha\cos\phi + \cos\alpha\sin\phi = \frac{8}{17}\sin\alpha + \frac{15}{17}\cos\alpha.
\]

En \(\triangle QYR\):

\[
v' = 180^\circ - \alpha - \theta.
\]

\[
\sin v' = \sin(\alpha + \theta) = \sin\alpha\cos\theta + \cos\alpha\sin\theta = \frac{4}{5}\sin\alpha + \frac{3}{5}\cos\alpha.
\]

---

**Paso 74: aplicar la ecuación \(34\sin v = 50\sin v'\)**

\[
34 \left(\frac{8}{17}\sin\alpha + \frac{15}{17}\cos\alpha\right) = 50 \left(\frac{4}{5}\sin\alpha + \frac{3}{5}\cos\alpha\right).
\]

\[
2(8\sin\alpha + 15\cos\alpha) = 10(4\sin\alpha + 3\cos\alpha).
\]

\[
16\sin\alpha + 30\cos\alpha = 40\sin\alpha + 30\cos\alpha.
\]

\[
16\sin\alpha = 40\sin\alpha.
\]

\[
24 \sin\alpha = 0.
\]

\[
\sin\alpha = 0.
\]

¡Esto implicaría \(\alpha = 0\), lo cual es degenerado! ¿Qué está mal?

---

**Paso 75: identificar el error en la relación de ángulos**

Repasemos la perpendicularidad. El ángulo entre \(PY\) y \(PS\) (vertical) es \(\alpha\). El ángulo entre \(PY\) y la horizontal es \(90^\circ - \alpha\) si \(PY\) apunta hacia arriba-derecha.

En el punto \(Q\), el ángulo entre \(QY\) y \(QR\) (vertical) es \(\beta\). El ángulo entre \(QY\) y la horizontal es \(90^\circ - \beta\) si \(QY\) apunta hacia arriba-izquierda.

La condición \(PY \perp QY\). Las pendientes: \(PY\) tiene pendiente \(\tan(90^\circ - \alpha) = \cot\alpha\). \(QY\) tiene pendiente \(-\tan(90^\circ - \beta) = -\cot\beta\) (porque va hacia la izquierda).

Perpendicularidad: \(\cot\alpha \cdot (-\cot\beta) = -1\), es decir \(\cot\alpha \cot\beta = 1\), o \(\tan\alpha \tan\beta = 1\), lo que da \(\alpha + \beta = 90^\circ\) si ambos agudos.

Entonces \(\alpha + \beta = 90^\circ\), no \(\alpha = \beta\).

¡Ahí está el error! La perpendicularidad da \(\alpha + \beta = 90^\circ\).

---

**Paso 76: corregir**

\(\alpha + \beta = 90^\circ\), con \(\alpha = \angle YPS\) y \(\beta = \angle YQR\).

Entonces \(\beta = 90^\circ - \alpha\).

En \(\triangle QYR\):

\[
v' = 180^\circ - \beta - \theta = 180^\circ - (90^\circ - \alpha) - \theta = 90^\circ + \alpha - \theta.
\]

\[
\sin v' = \sin(90^\circ + \alpha - \theta) = \cos(\alpha - \theta) = \cos\alpha\cos\theta + \sin\alpha\sin\theta.
\]

\[
\sin v' = \frac{4}{5}\cos\alpha + \frac{3}{5}\sin\alpha.
\]

Y en \(\triangle PYS\):

\[
v = 180^\circ - \alpha - \phi.
\]

\[
\sin v = \sin(\alpha + \phi) = \sin\alpha\cos\phi + \cos\alpha\sin\phi = \frac{8}{17}\sin\alpha + \frac{15}{17}\cos\alpha.
\]

---

**Paso 77: igualar las alturas \(y\)**

De \(\triangle PYS\): \(y = 34 \sin v \cos\alpha\).

De \(\triangle QYR\): \(y = 50 \sin v' \sin\beta = 50 \sin v' \cos\alpha\) (porque \(\beta=90^\circ-\alpha\)).

Igualamos:

\[
34 \sin v \cos\alpha = 50 \sin v' \cos\alpha.
\]

Entonces:

\[
34 \sin v = 50 \sin v'.
\]

Sustituimos:

\[
34 \left(\frac{8}{17}\sin\alpha + \frac{15}{17}\cos\alpha\right) = 50 \left(\frac{4}{5}\cos\alpha + \frac{3}{5}\sin\alpha\right).
\]

\[
2(8\sin\alpha + 15\cos\alpha) = 10(4\cos\alpha + 3\sin\alpha).
\]

\[
16\sin\alpha + 30\cos\alpha = 40\cos\alpha + 30\sin\alpha.
\]

\[
16\sin\alpha - 30\sin\alpha = 40\cos\alpha - 30\cos\alpha.
\]

\[
-14\sin\alpha = 10\cos\alpha.
\]

\[
\tan\alpha = -\frac{10}{14} = -\frac{5}{7}.
\]

Como \(\alpha\) es agudo, \(\tan\alpha >0\). ¡Contradicción!

---

**Paso 78: análisis del signo**

La ecuación da \(\tan\alpha = -5/7\), lo cual es imposible para \(\alpha\) agudo. Esto sugiere que el signo en alguna expresión trigonométrica está mal.

Revisemos \(y\) para \(\triangle PYS\). La altura de \(Y\) sobre la base \(PQ\) es \(y\), y \(PY\) forma un ángulo \(\alpha\) con la vertical \(PS\). Entonces la componente vertical de \(PY\) es \(PY \cos\alpha\), que es \(y\). Correcto, asumiendo que \(Y\) está por encima de \(P\).

Para \(\triangle QYR\), la componente vertical de \(QY\) es \(QY \cos\beta\). Pero \(\beta\) es el ángulo entre \(QY\) y la vertical \(QR\). La componente vertical de \(QY\) es \(QY\cos\beta\), que es \(y\). Correcto.

La relación \(\alpha + \beta = 90^\circ\): si \(PY\) forma ángulo \(\alpha\) con la vertical, su ángulo con la horizontal es \(90^\circ - \alpha\). Si \(QY\) forma ángulo \(\beta\) con la vertical, su ángulo con la horizontal es \(90^\circ - \beta\), pero hacia la izquierda.

El vector \(PY\) tiene dirección con ángulo \(90^\circ - \alpha\) desde el eje \(x\) positivo. El vector \(QY\) tiene dirección con ángulo \(90^\circ + \beta\) desde el eje \(x\) positivo (porque va hacia arriba-izquierda, con ángulo \(\beta\) desde la vertical).

Para que sean perpendiculares:

\[
(90^\circ + \beta) - (90^\circ - \alpha) = 90^\circ.
\]

\[
\beta + \alpha = 90^\circ.
\]

Correcto.

Entonces \(\alpha + \beta = 90^\circ\) es correcto.

Ahora, ¿qué tal la expresión de \(\sin v\)?

En \(\triangle PYS\), \(v = \angle YSP\). El ángulo en \(S\) es \(v\). La suma:

\[
\alpha + \phi + v = 180^\circ.
\]

\[
v = 180^\circ - \alpha - \phi.
\]

\[
\sin v = \sin(180^\circ - \alpha - \phi) = \sin(\alpha + \phi).
\]

Correcto.

\[
\sin(\alpha+\phi) = \sin\alpha\cos\phi + \cos\alpha\sin\phi = \frac{8}{17}\sin\alpha + \frac{15}{17}\cos\alpha.
\]

Correcto.

En \(\triangle QYR\), \(\beta + \theta + v' = 180^\circ\). Con \(\beta = 90^\circ - \alpha\):

\[
v' = 180^\circ - \beta - \theta = 180^\circ - (90^\circ - \alpha) - \theta = 90^\circ + \alpha - \theta.
\]

\[
\sin v' = \sin(90^\circ + \alpha - \theta).
\]

Ahora, \(\sin(90^\circ + x) = \cos x\), así que:

\[
\sin v' = \cos(\alpha - \theta) = \cos\alpha\cos\theta + \sin\alpha\sin\theta = \frac{4}{5}\cos\alpha + \frac{3}{5}\sin\alpha.
\]

Correcto.

¿Y \(y = 50 \sin v' \sin\beta\)? En el triángulo \(QYR\), \(QY = 50\sin v'\) por la ley de senos. La componente vertical de \(QY\) es \(QY \cos\beta\), donde \(\beta\) es el ángulo entre \(QY\) y la vertical. Entonces \(y = 50 \sin v' \cos\beta\).

A mi en el paso 76 escribí \(y = 50 \sin v' \sin\beta\), ¡error! Debe ser \(\cos\beta\), no \(\sin\beta\).

---

**Paso 79: corregir**

\(y = 50 \sin v' \cos\beta\). Como \(\beta = 90^\circ - \alpha\), \(\cos\beta = \sin\alpha\).

Entonces:

\[
y = 50 \sin v' \sin\alpha.
\]

Mientras que para \(\triangle PYS\):

\[
y = 34 \sin v \cos\alpha.
\]

Igualamos:

\[
34 \sin v \cos\alpha = 50 \sin v' \sin\alpha.
\]

Sustituimos:

\[
34 \left(\frac{8}{17}\sin\alpha + \frac{15}{17}\cos\alpha\right)\cos\alpha = 50 \left(\frac{4}{5}\cos\alpha + \frac{3}{5}\sin\alpha\right)\sin\alpha.
\]

\[
2(8\sin\alpha + 15\cos\alpha)\cos\alpha = 10(4\cos\alpha + 3\sin\alpha)\sin\alpha.
\]

\[
(16\sin\alpha + 30\cos\alpha)\cos\alpha = (40\cos\alpha + 30\sin\alpha)\sin\alpha.
\]

\[
16\sin\alpha\cos\alpha + 30\cos^2\alpha = 40\sin\alpha\cos\alpha + 30\sin^2\alpha.
\]

\[
30\cos^2\alpha - 30\sin^2\alpha = 24\sin\alpha\cos\alpha.
\]

\[
30(\cos^2\alpha - \sin^2\alpha) = 24\sin\alpha\cos\alpha.
\]

\[
30\cos 2\alpha = 12 \sin 2\alpha.
\]

\[
\frac{\sin 2\alpha}{\cos 2\alpha} = \frac{30}{12} = \frac{5}{2}.
\]

\[
\tan 2\alpha = \frac{5}{2}.
\]

---

**Paso 80: calcular \(h\)**

Tenemos:

\[
x = PY \sin\alpha = 34\sin v \sin\alpha.
\]

\[
h - x = QY \sin\beta = 50 \sin v' \sin\beta = 50 \sin v' \cos\alpha.
\]

Entonces:

\[
h = 34 \sin v \sin\alpha + 50 \sin v' \cos\alpha.
\]

Sustituimos:

\[
h = 34 \left(\frac{8}{17}\sin\alpha + \frac{15}{17}\cos\alpha\right)\sin\alpha + 50 \left(\frac{4}{5}\cos\alpha + \frac{3}{5}\sin\alpha\right)\cos\alpha.
\]

\[
h = 2(8\sin\alpha + 15\cos\alpha)\sin\alpha + 10(4\cos\alpha + 3\sin\alpha)\cos\alpha.
\]

\[
h = 16\sin^2\alpha + 30\sin\alpha\cos\alpha + 40\cos^2\alpha + 30\sin\alpha\cos\alpha.
\]

\[
h = 16\sin^2\alpha + 40\cos^2\alpha + 60\sin\alpha\cos\alpha.
\]

Usamos identidades:

\[
\sin^2\alpha = \frac{1-\cos 2\alpha}{2}, \quad \cos^2\alpha = \frac{1+\cos 2\alpha}{2}, \quad \sin\alpha\cos\alpha = \frac{\sin 2\alpha}{2}.
\]

\[
h = 16\cdot\frac{1-\cos2\alpha}{2} + 40\cdot\frac{1+\cos2\alpha}{2} + 60\cdot\frac{\sin2\alpha}{2}.
\]

\[
h = 8(1-\cos2\alpha) + 20(1+\cos2\alpha) + 30\sin2\alpha.
\]

\[
h = 8 - 8\cos2\alpha + 20 + 20\cos2\alpha + 30\sin2\alpha.
\]

\[
h = 28 + 12\cos2\alpha + 30\sin2\alpha.
\]

Usamos \(\tan 2\alpha = 5/2\):

\[
\sin2\alpha = \frac{5}{\sqrt{29}}, \quad \cos2\alpha = \frac{2}{\sqrt{29}} \quad (\text{porque } 2\alpha \text{ es agudo}).
\]

\[
h = 28 + 12\cdot\frac{2}{\sqrt{29}} + 30\cdot\frac{5}{\sqrt{29}} = 28 + \frac{24 + 150}{\sqrt{29}} = 28 + \frac{174}{\sqrt{29}}.
\]

Racionalizamos:

\[
h = 28 + \frac{174}{\sqrt{29}} \cdot \frac{\sqrt{29}}{\sqrt{29}} = 28 + \frac{174\sqrt{29}}{29} = 28 + 6\sqrt{29}.
\]

\[
h = 28 + 6\sqrt{29}.
\]

---

**Paso 81: verificar que esto coincida con el resultado anterior del enfoque de coordenadas**

El enfoque de coordenadas dio \(h = 28 + 2\sqrt{261}\). Notemos:

\[
2\sqrt{261} = 2\sqrt{9 \cdot 29} = 2 \cdot 3\sqrt{29} = 6\sqrt{29}.
\]

¡Coinciden! \(28 + 6\sqrt{29} = 28 + 2\sqrt{261}\). 

Excelente, el enfoque de ángulos confirma el resultado. La respuesta es \(PQ = 28 + 6\sqrt{29}\).

---

**Paso 82: verificación final**

Con \(h = 28 + 6\sqrt{29} \approx 28 + 32.31 = 60.31\), que coincide con el valor numérico anterior. Todo es consistente.

Además, \(h=16\) era la otra raíz, pero produce \(Y=Q\), degenerado.

---

**Conclusión**

\[
PQ = 28 + 6\sqrt{29}.
\]

Pero espera, revisemos si hay alguna solución con \(h=16\) no degenerada que no consideramos. Con \(h=16\), \(x=16\), \(y=0\), así que \(Y=Q\), fuera del interior. Descartada.

¿Y si \(Y\) está en la parte inferior pero con \(y>0\)? No, la raíz \(h=16\) da \(y=0\) exactamente.

---

**Paso 83: ¿hay otra raíz positiva?**

El polinomio \(h^3 - 72h^2 + 636h + 4160 = (h-16)(h^2 - 56h - 260)=0\). Las raíces de \(h^2 - 56h - 260=0\) son \(28 \pm \sqrt{1044} = 28 \pm 2\sqrt{261}\). La positiva es \(28 + 2\sqrt{261} = 28+6\sqrt{29}\). La negativa \(28 - 2\sqrt{261}\approx -4.31\), descartada.

Así que la única solución válida es \(h = 28 + 6\sqrt{29}\).

---

**Respuesta final**

\[
\boxed{28 + 6\sqrt{29}}
\]