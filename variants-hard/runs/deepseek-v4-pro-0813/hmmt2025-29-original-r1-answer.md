Voy a resolver el problema paso a paso.

Sea el rectángulo $ABCD$ con $BC=24$. Como es un rectángulo, $AD = BC = 24$ y $AB=CD$. Denotemos $AB = L$ (lo que buscamos).

Pongamos coordenadas:
- $A=(0,0)$
- $B=(L,0)$
- $C=(L,24)$
- $D=(0,24)$

Sea $X=(x,y)$ con $0<x<L$ y $0<y<24$.

La condición $\angle AXB = 90^\circ$ significa que $(A-X)\cdot(B-X)=0$:
$$(-x,-y)\cdot(L-x,-y)=0$$
$$-x(L-x)+y^2=0$$
$$y^2=x(L-x) \quad (1)$$

Ahora, los circunradios de los triángulos $\triangle AXD$ y $\triangle BXC$.

**Triángulo $AXD$:** vértices $A=(0,0)$, $X=(x,y)$, $D=(0,24)$.

El circuncírculo pasa por $(0,0)$ y $(0,24)$, ambos sobre el eje $y$. Si el centro es $(h,k)$, entonces:
$$h^2+k^2 = h^2+(k-24)^2 \implies k^2=(k-24)^2 \implies k=12.$$

Además pasa por $X=(x,y)$:
$$(x-h)^2+(y-12)^2 = h^2+144.$$

El radio es $13$, así que $h^2+144=169$, luego $h^2=25$, $h=\pm 5$.

Desarrollando la ecuación del punto $X$:
$$(x-h)^2+(y-12)^2 = h^2+144$$
$$x^2-2hx+h^2 + y^2-24y+144 = h^2+144$$
$$x^2+y^2-2hx-24y+144 = 144$$
$$x^2+y^2-2hx-24y=0 \quad (2)$$

**Triángulo $BXC$:** vértices $B=(L,0)$, $X=(x,y)$, $C=(L,24)$.

El circuncírculo pasa por $(L,0)$ y $(L,24)$, ambos sobre la recta vertical $x=L$. Si el centro es $(p,q)$, entonces:
$$(L-p)^2+q^2 = (L-p)^2+(q-24)^2 \implies q=12.$$

Pasa por $X=(x,y)$:
$$(x-p)^2+(y-12)^2 = (L-p)^2+144.$$

El radio es $15$, así que $(L-p)^2+144=225$, luego $(L-p)^2=81$, $L-p=\pm 9$.

Desarrollando la ecuación del punto $X$:
$$(x-p)^2+(y-12)^2 = (L-p)^2+144$$
$$x^2-2px+p^2+y^2-24y+144 = (L-p)^2+144$$
$$x^2+y^2-2px-24y+p^2 = (L-p)^2$$
$$x^2+y^2-2px-24y+p^2 = L^2-2Lp+p^2$$
$$x^2+y^2-2px-24y = L^2-2Lp \quad (3)$$

Ahora sustituimos $y^2=x(L-x)$ de (1).

**De (2):**
$$x^2 + x(L-x) - 2hx - 24y = 0$$
$$xL - 2hx - 24y = 0$$
$$x(L-2h) = 24y \quad (4)$$

**De (3):**
$$x^2 + x(L-x) - 2px - 24y = L^2 - 2Lp$$
$$xL - 2px - 24y = L^2 - 2Lp$$
$$x(L-2p) - 24y = L^2-2Lp = L(L-2p)$$
$$(L-2p)(x-L) = 24y$$
$$(L-2p)(x-L) = 24y \quad (5)$$

Tenemos dos ecuaciones (4) y (5):
$$24y = x(L-2h) \quad \text{con } h=\pm 5$$
$$24y = (L-2p)(x-L) \quad \text{con } L-p=\pm 9$$

Recordemos que $p = L \mp 9$. Es decir:
- Si $L-p=9$, entonces $p=L-9$, luego $L-2p = L-2L+18 = 18-L$.
- Si $L-p=-9$, entonces $p=L+9$, luego $L-2p = L-2L-18 = -(L+18)$.

Y $h=\pm 5$, así que $L-2h = L\mp 10$.

Los triángulos son agudos. Analicemos las condiciones de acutángulo.

**Triángulo $AXD$ acutángulo:** 
- Lado $AD=24$ vertical. El ángulo en $X$, $\angle AXD$, es agudo ⟺ $X$ está fuera del círculo de diámetro $AD$ (el que tiene radio 12 centrado en $(0,12)$). Como el circuncírculo real tiene radio 13, y necesitamos que el ángulo opuesto a $AD$ sea agudo (es decir, $\cos \angle AXD >0$).

El ángulo en el vértice $X$ es agudo si y solo si $X$ está fuera del círculo de diámetro $AD$:
$$x^2+(y-12)^2 > 144$$

De la ecuación (2), el circuncírculo tiene centro $(h,12)$, radio 13, y $X$ está sobre él. La distancia de $X$ al centro $(0,12)$ del círculo de diámetro:
$$x^2+(y-12)^2 = h^2 + 2hx \quad \text{?}$$

Veamos: de (2), $x^2+y^2-2hx-24y=0$. Entonces:
$$x^2+(y-12)^2 = x^2+y^2-24y+144 = 2hx + 144.$$

Entonces la condición $\angle AXD < 90^\circ$ es:
$$2hx+144 > 144 \iff 2hx>0 \iff hx>0.$$

Como $x>0$, necesitamos $h>0$, es decir $h=5$.

Además, los ángulos en $A$ y $D$ deben ser agudos. 

El ángulo en $A$, $\angle DAX$, es agudo. En el triángulo $AXD$, el ángulo en $A$ es entre $AD$ (vector $(0,24)$) y $AX$ (vector $(x,y)$). Es agudo ⟺ $(0,24)\cdot(x,y)>0 \iff y>0$. Cierto.

El ángulo en $D$, $\angle ADX$, es entre $DA=(0,-24)$ y $DX=(x,y-24)$. Es agudo ⟺ $(0,-24)\cdot(x,y-24)>0 \iff -24(y-24)>0 \iff y<24$. Cierto.

Así que para $\triangle AXD$ acutángulo necesitamos $h=5$.

Recapitulando duda sobre si $h$ podría ser negativo... Con $h=5$, $x^2+(y-12)^2 = 2\cdot 5\cdot x + 144 = 10x+144 > 144$, así ángulo en $X$ agudo. Bien.

**Triángulo $BXC$ acutángulo:**
- Ángulo en $X$, $\angle BXC$, agudo ⟺ $X$ fuera del círculo de diámetro $BC$ (centro $(L,12)$, radio 12):
$$(x-L)^2+(y-12)^2>144.$$

De (3), $x^2+y^2-2px-24y+p^2 = (L-p)^2$... mejor despejemos:
$$x^2+y^2-2px-24y = L^2-2Lp.$$

Entonces:
$$(x-L)^2+(y-12)^2 = x^2-2Lx+L^2 + y^2 -24y+144$$
$$= (x^2+y^2-24y) -2Lx + L^2+144.$$

De (3): $x^2+y^2-24y = 2px + L^2-2Lp$.

Sustituyendo:
$$= 2px + L^2-2Lp -2Lx + L^2+144 - L^2$$
Espera, con cuidado:
$$(x-L)^2+(y-12)^2 = 2px + L^2 - 2Lp - 2Lx + L^2 + 144 - L^2 + L^2$$
Me estoy liando. Rehagamos directamente:

$$(x-L)^2+(y-12)^2 = x^2-2Lx+L^2+y^2-24y+144$$
$$= (x^2+y^2-24y) - 2Lx + L^2+144.$$

Y de (3) tenemos $x^2+y^2-24y = 2px + L^2 - 2Lp$. Entonces:
$$= 2px + L^2-2Lp - 2Lx + L^2 + 144$$
$$= 2x(p-L) + 2L^2 - 2Lp + 144$$
$$= 2x(p-L) + 2L(L-p) + 144$$
$$= -2x(L-p) + 2L(L-p)+144$$
$$= 2(L-p)(L-x)+144.$$

La condición $\angle BXC<90^\circ$ es:
$$2(L-p)(L-x)+144 > 144 \iff (L-p)(L-x)>0.$$

Como $x<L$, tenemos $L-x>0$, luego necesitamos $L-p>0$, es decir $L-p=9$ (la opción positiva), lo que da $p=L-9$.

Entonces: $h=5$ y $L-p=9$, $p=L-9$.

Por lo tanto de (4): $24y = x(L-10)$.
Y de (5): $24y = (L-2p)(x-L) = (L-2(L-9))(x-L) = (18-L)(x-L)$.

Igualamos:
$$x(L-10) = (18-L)(x-L). \quad (6)$$

Además tenemos (1): $y^2 = x(L-x)$, y de (4): $y = \frac{x(L-10)}{24}$.

Sustituimos $y$ en (1):
$$\left(\frac{x(L-10)}{24}\right)^2 = x(L-x).$$

Si $x>0$:
$$\frac{x(L-10)^2}{576} = L-x$$
$$x\left[\frac{(L-10)^2}{576}+1\right] = L$$
$$x = \frac{L}{\frac{(L-10)^2}{576}+1} = \frac{576L}{(L-10)^2+576}. \quad (7)$$

Ahora usemos (6). Desarrollemos (6):
$$x(L-10) = (18-L)x - (18-L)L$$
$$x(L-10) - x(18-L) = -(18-L)L$$
$$x[(L-10)-(18-L)] = -L(18-L)$$
$$x(2L-28) = L(L-18)$$
$$x = \frac{L(L-18)}{2L-28} = \frac{L(L-18)}{2(L-14)}. \quad (8)$$

Igualamos (7) y (8):
$$\frac{576L}{(L-10)^2+576} = \frac{L(L-18)}{2(L-14)}.$$

Como $L>0$, cancelamos $L$:
$$\frac{576}{(L-10)^2+576} = \frac{L-18}{2(L-14)}.$$

Multiplicamos en cruz:
$$576 \cdot 2(L-14) = (L-18)[(L-10)^2+576].$$

Desarrollemos el lado derecho. Primero $(L-10)^2 = L^2-20L+100$. Más 576: $L^2-20L+676$.

Lado izquierdo: $1152(L-14) = 1152L - 16128$.

Lado derecho: $(L-18)(L^2-20L+676) = L^3 -20L^2+676L -18L^2+360L - 12168$
$$= L^3 -38L^2 + 1036L - 12168.$$

Igualamos:
$$1152L - 16128 = L^3 -38L^2 + 1036L - 12168$$
$$0 = L^3 -38L^2 + 1036L - 1152L - 12168 + 16128$$
$$0 = L^3 -38L^2 -116L + 3960.$$

Debemos resolver:
$$L^3 -38L^2 -116L + 3960 = 0.$$

Probemos raíces racionales. Divisores de 3960... Probemos valores razonables. Dado que $X$ está dentro y las condiciones, $L$ debe ser razonable.

Probemos $L=20$: $8000 - 38\cdot400 - 2320 + 3960 = 8000 - 15200 - 2320 + 3960 = 8000-15200=-7200; -7200-2320=-9520; -9520+3960=-5560$. No.

$L=22$: $10648 - 38\cdot484 - 2552 + 3960 = 10648 - 18392 - 2552 + 3960 = 10648-18392=-7744; -7744-2552=-10296; -10296+3960=-6336$. No.

$L=30$: $27000 - 38\cdot900 - 3480 + 3960 = 27000 - 34200 - 3480+3960 = 27000-34200=-7200; -7200-3480=-10680; -10680+3960=-6720$. No.

$L=18$: $5832 -38\cdot324 -2088+3960 = 5832-12312-2088+3960 = 5832-12312=-6480; -6480-2088=-8568; -8568+3960=-4608$. No.

Probemos $L=36$: $46656 - 38\cdot1296 - 4176 + 3960 = 46656 - 49248 - 4176+3960 = 46656-49248=-2592; -2592-4176=-6768; -6768+3960=-2808$. No.

$L=40$: $64000 -38\cdot1600 -4640 +3960 = 64000-60800=3200; 3200-4640=-1440; -1440+3960=2520$. No.

$L=38$: $54872 -38\cdot1444 -4408 +3960 = 54872 - 54872 - 4408+3960 = -448$. No.

$L=39$: $59319 -38\cdot1521 -4524+3960 = 59319 - 57798 -4524+3960 = 1521-4524+3960 = 957$. No.

$L=38$ y $39$ dan signos opuestos, pero no da exacto. Probemos fracciones o factorización.

Intentemos factorizar. Probemos $L=44$: $85184 - 38\cdot1936 - 5104+3960 = 85184 - 73568 - 5104+3960 = 11616 - 5104 + 3960 = 10472$. No.

Hmm, probemos divisor. Probemos $L=20$ no, $L=45$: $91125 - 38\cdot2025 -5220+3960 = 91125-76950=14175; 14175-5220=8955; 8955+3960=12915$.

Probemos $L=15$: $3375 - 38\cdot225 -1740+3960 = 3375-8550=-5175; -5175-1740=-6915; -6915+3960=-2955$. No.

Probemos $L=30$ no dio. $L=33$: $35937 - 38\cdot1089 -3828+3960 = 35937 - 41382 -3828+3960 = -5445-3828+3960 = -5313$. No.

$L=34$: $39304 - 38\cdot1156 -3944+3960 = 39304-43928=-4624; -4624-3944=-8568; -8568+3960=-4608$.

$L=36$: dieron -2808.

$L=37$: $50653 - 38\cdot1369 -4292+3960 = 50653 - 52022 -4292+3960 = -1369-4292+3960 = -1701$.

$L=38$: -448. $L=39$: 957. Así que hay una raíz entre 38 y 39, quizás no entera.

Probemos factores de 3960: $2,3,4,5,6,8,9,10,11,12,15,18,20,22,24,30,...$

Probemos $L=20$: no. $L=24$: $13824 - 38\cdot576 -2784+3960 = 13824-21888=-8064; -8064-2784=-10848; +3960=-6888$. No.

$L=25$: $15625 - 38\cdot625 - 2900+3960 = 15625-23750=-8125; -8125-2900=-11025; +3960=-7065$.

$L=27$: $19683 - 38\cdot729 - 3132 +3960 = 19683 - 27702 -3132+3960 = -8019 -3132 + 3960 = -7191$.

$L=28$: $21952 - 38\cdot784 - 3248+3960 = 21952-29792=-7840; -7840-3248=-11088; +3960=-7128$.

$L=36$: -2808.

Parece que no hay raíz entera. Revisemos cuentas.

Quizá cometí un error de signos o de planteamiento. Repasemos.

Coordenadas: $A=(0,0), B=(L,0), C=(L,24), D=(0,24)$. $X=(x,y)$.

$\angle AXB=90°$: vectores $A-X = (-x,-y)$, $B-X=(L-x,-y)$. Producto punto: $-x(L-x)+y^2=0 \Rightarrow y^2=x(L-x)$. Correcto.

Circunradio de $AXD$ = 13. Vértices $A,D$ en $x=0$, separados 24. El centro está en la mediatriz de $AD$: $y=12$, y a distancia $\sqrt{13^2-12^2}=5$ del segmento, o sea $x$-coordenada del centro $\pm5$. Entonces centro $(h,12)$ con $h=\pm5$. 

El punto $X$ está sobre el circuncírculo: $(x-h)^2+(y-12)^2=169$.

Además, como $A$ y $D$ están en el círculo, $(0-h)^2+(0-12)^2=169$ da $h^2+144=169$, $h^2=25$. Correcto.

Ahora, ¿cuál es la condición de acutángulo correcta? Un triángulo es acutángulo si todos los ángulos < 90°. 

Ángulo en $X$ opuesto al lado $AD$. Por la ley del coseno, el ángulo en $X$ es agudo ⟺ $AD^2 < AX^2 + XD^2$... En términos de círculo de diámetro $AD$: el ángulo $\angle AXD$ es agudo ⟺ $X$ fuera del círculo con diámetro $AD$. Sí, correcto.

Entonces necesitamos $(x-0)^2+(y-12)^2>144$. De $(x-h)^2+(y-12)^2=169$:

$(x-h)^2 = x^2-2hx+h^2$. Entonces:
$$x^2+(y-12)^2 = (x-h)^2+(y-12)^2+2hx-h^2 = 169+2hx-25 = 144+2hx.$$

Así que la condición $x^2+(y-12)^2>144$ es $144+2hx>144 \Rightarrow 2hx>0\Rightarrow hx>0$. Como $x>0$, $h>0$, $h=5$. Correcto.

Ángulo en $A$: entre $AD$ (hacia arriba, vector $(0,24)$, o sea desde A a D) y $AX$ (vector $(x,y)$ de A a X). Es agudo ⟺ $X$ está en el mismo semiplano... no, mejor: el ángulo $\angle DAX$ con vértice en A, rayos $AD$ y $AX$. El producto punto $AD \cdot AX = (0,24)\cdot (x,y)=24y>0$ ya que $y>0$. Correcto, agudo.

Ángulo en $D$: rayos $DA=(0,-24)$ y $DX=(x,y-24)$. Producto punto $= -24(y-24)>0 \Leftrightarrow y<24$. Cierto.

Entonces $AXD$ acutángulo ⟺ $h=5$. Correcto.

Circunradio $BXC=15$: vértices $B=(L,0), C=(L,24)$ separados 24. Centro en mediatriz $y=12$, y a distancia de la recta $x=L$: $\sqrt{15^2-12^2}=\sqrt{225-144}=\sqrt{81}=9$. Entonces centro $(p,12)$ con $p=L\pm9$.

El punto $X$ está en el circuncírculo: $(x-p)^2+(y-12)^2=225$.

Condición ángulo en $X$ opuesto a $BC$: agudo ⟺ $X$ fuera del círculo de diámetro $BC$: $(x-L)^2+(y-12)^2>144$.

Calculemos $(x-L)^2+(y-12)^2$ usando $(x-p)^2+(y-12)^2=225$.

$(x-L)^2 = (x-p)^2 - (x-p)^2 + (x-L)^2$... mejor directamente:
$(x-L)^2 = [(x-p)+(p-L)]^2 = (x-p)^2 + 2(x-p)(p-L)+(p-L)^2$.

Entonces:
$$(x-L)^2+(y-12)^2 = (x-p)^2+(y-12)^2 + 2(x-p)(p-L)+(p-L)^2$$
$$= 225 + 2(x-p)(p-L)+(L-p)^2.$$

$p-L = \pm9$, $(p-L)^2=81$. Entonces:
$$= 306 + 2(x-p)(p-L).$$

Condición $>144$:
$$306 + 2(x-p)(p-L) > 144 \Rightarrow 2(x-p)(p-L) > -162 \Rightarrow (x-p)(p-L) > -81.$$

Hmm, esto no simplifica tan directo. Veamos con la otra aproximación.

Mejor usar la expresión que derivamos antes. Rehagamos de forma limpia:

Queremos la condición sobre $(x-L)^2+(y-12)^2$ a partir de la ecuación del circuncírculo de $BXC$.

Circuncírculo $BXC$: centro $(p,12)$, radio 15. Ecuación:
$$(x-p)^2+(y-12)^2=225.$$

El círculo de diámetro $BC$ tiene centro $(L,12)$ y radio 12.

El ángulo $\angle BXC$ es agudo ⟺ $X$ está fuera del círculo de diámetro $BC$ ⟺ $(x-L)^2+(y-12)^2>144$.

De la ecuación del circuncírculo:
$$(x-p)^2+(y-12)^2=225.$$

Escribamos $(x-L)^2+(y-12)^2$ en términos:

Usando la diferencia de cuadrados:
$$(x-p)^2 - (x-L)^2 = [(x-p)-(x-L)][(x-p)+(x-L)] = (L-p)(2x-p-L).$$

Entonces:
$$(x-L)^2+(y-12)^2 = 225 - (L-p)(2x-p-L).$$

Condición $>144$:
$$225 - (L-p)(2x-p-L) > 144$$
$$(L-p)(2x-p-L) < 81.$$

Con $L-p = \pm9$:
- Si $L-p=9$: $9(2x-p-L)<81 \Rightarrow 2x-p-L<9$, es decir $x < \frac{p+L+9}{2}$.
- Si $L-p=-9$: $-9(2x-p-L)<81 \Rightarrow 2x-p-L>-9$.

Hmm, esto no es simplemente elegir signo. Puede que ambos signos sean posibles, y deba verificar cuál da triángulo acutángulo para TODOS los ángulos, no solo el de $X$.

Además ángulos en $B$ y $C$ de $\triangle BXC$:

Ángulo en $B$: rayos $BC=(0,24)$ y $BX=(x-L,y)$. Producto punto $=24y>0$, agudo. Cierto.

Ángulo en $C$: rayos $CB=(0,-24)$ y $CX=(x-L,y-24)$. Producto $= -24(y-24)>0\Leftrightarrow y<24$. Cierto.

Entonces los ángulos en $B$ y $C$ son agudos automáticamente. Solo el ángulo en $X$ es el restrictivo.

Por lo tanto, $\triangle BXC$ acutángulo ⟺ $(x-L)^2+(y-12)^2>144$. Y esto nos da una desigualdad, no necesariamente fija el signo de $L-p$.

Necesito reconsiderar. Tal vez ambas opciones para $p$ sean válidas en principio, y tendremos que ver cuál produce un $X$ dentro del rectángulo y consistente.

Volvamos a las ecuaciones.

Tenemos:
- (1): $y^2=x(L-x)$.
- Para $AXD$ con $h=5$: el circuncírculo está centrado en $(5,12)$, radio 13:
$$(x-5)^2+(y-12)^2=169. \quad (2')$$
- Para $BXC$: centro $(p,12)$ con $p=L\pm9$, radio 15:
$$(x-p)^2+(y-12)^2=225. \quad (3')$$

Aquí $p=L+9$ o $p=L-9$.

Desarrollemos (2'):
$$x^2-10x+25+y^2-24y+144=169$$
$$x^2+y^2-10x-24y+169=169$$
$$x^2+y^2-10x-24y=0. \quad (2a)$$

Desarrollamos (3'):
$$x^2-2px+p^2+y^2-24y+144=225$$
$$x^2+y^2-2px-24y+p^2=81$$
$$x^2+y^2-2px-24y = 81-p^2. \quad (3a)$$

Sustituimos $y^2=x(L-x)$ en ambas.

De (2a): $x^2+x(L-x)-10x-24y=0\Rightarrow xL-10x-24y=0\Rightarrow x(L-10)=24y$. (4) como antes.

De (3a): $x^2+x(L-x)-2px-24y=81-p^2\Rightarrow xL-2px-24y=81-p^2\Rightarrow x(L-2p)-24y=81-p^2$. (5')

De (4): $24y=x(L-10)$.

Sustituimos en (5'):
$$x(L-2p)-x(L-10)=81-p^2$$
$$x[(L-2p)-(L-10)] = 81-p^2$$
$$x(10-2p)=81-p^2$$
$$x = \frac{81-p^2}{10-2p}. \quad (8')$$

Y de (4) con (1):
$$y=\frac{x(L-10)}{24},\quad y^2=x(L-x)\Rightarrow \frac{x^2(L-10)^2}{576}=x(L-x).$$
Si $x>0$: $x(L-10)^2/576 = L-x$, luego:
$$x=\frac{576L}{(L-10)^2+576}. \quad (7)$$

Igualamos (7) y (8') para cada caso de $p$.

**Caso 1: $p=L+9$.**
Entonces $81-p^2 = 81-(L+9)^2 = 81 - L^2 -18L -81 = -L^2-18L = -L(L+18)$.
Y $10-2p = 10-2L-18 = -2L-8 = -2(L+4)$.
Entonces:
$$x = \frac{-L(L+18)}{-2(L+4)} = \frac{L(L+18)}{2(L+4)}. \quad (8'_1)$$

Igualamos con (7):
$$\frac{576L}{(L-10)^2+576} = \frac{L(L+18)}{2(L+4)}.$$

Cancelamos $L>0$:
$$\frac{576}{(L-10)^2+576} = \frac{L+18}{2(L+4)}.$$

Multiplicamos en cruz:
$$576\cdot 2(L+4) = (L+18)[(L-10)^2+576]$$
$$1152(L+4) = (L+18)(L^2-20L+676).$$

Lado derecho: $(L+18)(L^2-20L+676) = L^3 -20L^2+676L + 18L^2 -360L + 12168$
$$= L^3 -2L^2 +316L +12168.$$

Lado izquierdo: $1152L+4608$.

Igualamos:
$$L^3 -2L^2 +316L +12168 = 1152L+4608$$
$$L^3 -2L^2 -836L +7560 = 0.$$

Probemos raíces. $L=20$: $8000 - 800 - 16720 + 7560 = -1960$. 
$L=18$: $5832 -648 -15048 +7560 = -2304$. 
$L=22$: $10648 -968 -18392 +7560 = -1152$. 
$L=24$: $13824 -1152 -20064 +7560 = 168$. 

Ah, entre 22 y 24. $L=23$: $12167 - 1058 - 19228 + 7560 = -559$.

$L=23.5$: $12977.875 - 1104.5 - 19646 + 7560$. Calculemos: $23.5^3 = 12977.875$. $2\cdot 23.5^2 = 1104.5$. $836\cdot 23.5 = 19646$. Entonces $12977.875 - 1104.5 - 19646 + 7560 = -212.625$.

$L=24$: dio 168. Entonces raíz entre 23.5 y 24. $L\approx 23.7$.

Probemos $L=23.7$: $23.7^2=561.69$, $23.7^3=13312.053$ (calculemos: $561.69\cdot23.7=13312.053$). $2\cdot561.69=1123.38$. $836\cdot23.7=19813.2$. Suma: $13312.053 - 1123.38 - 19813.2 + 7560 = -64.527$.

$L=23.8$: $23.8^2=566.44$, $23.8^3 = 566.44\cdot 23.8 = 13481.272$. $2\cdot566.44=1132.88$. $836\cdot23.8=19896.8$. Suma: $13481.272 - 1132.88 - 19896.8 + 7560 = 11.592$.

Entonces raíz $\approx 23.78$. No parece entero. Hmm.

Probemos factores enteros de 7560. Divisores: ..., $18, 20, 21, 24, 27, 28, 30, 35, ...$

Probemos $L=21$: $9261 -882 -17556 + 7560 = -1617$.

$L=24$: 168. $L=26$: $17576 - 1352 - 21736 + 7560 = 2048$. 

$L=28$: $21952 - 1568 - 23408 + 7560 = 4536$. 

$L=30$: $27000 - 1800 - 25080 + 7560 = 7680$.

$L=36$: $46656 -2592 -30096 +7560 = 21528$.

No hay raíz entera evidente. Probemos divisor $L=14$: $2744 - 392 - 11704 + 7560 = -1792$. $L=15$: $3375-450-12540+7560=-2055$. $L=16$: $4096-512-13376+7560=-2232$. $L=17$: $4913-578-14212+7560=-2317$. $L=18$: -2304. $L=19$: $6859-722-15884+7560=-2187$. $L=20$: $-1960$. $L=21$: -1617. $L=22$: -1152. $L=23$: -559. $L=24$: 168. 

Ninguno entero. Probemos $L=21$: no. Quizás la raíz no sea entera, o cometí otro error.

Probemos el **Caso 2: $p=L-9$.**

Entonces $81-p^2 = 81-(L-9)^2 = 81 -(L^2-18L+81) = -L^2+18L = L(18-L)$.
Y $10-2p = 10 -2L+18 = 28-2L = 2(14-L)$.
Entonces:
$$x = \frac{L(18-L)}{2(14-L)}. \quad (8'_2)$$

Observa que esto es exactamente la ecuación (8) que tenía antes (con $18-L$ y $14-L$). Correcto.

Igualamos con (7):
$$\frac{576L}{(L-10)^2+576} = \frac{L(18-L)}{2(14-L)}.$$

Cancelamos $L$:
$$\frac{576}{(L-10)^2+576} = \frac{18-L}{2(14-L)}.$$

Multiplicamos en cruz:
$$576\cdot 2(14-L) = (18-L)[(L-10)^2+576].$$

Esto es lo mismo que antes (ecuación con raíz entre 38 y 39).

Entonces tenemos dos casos con raíces no enteras: $\approx 23.78$ y $\approx 38.35$. Pero el problema probablemente tiene respuesta entera. He debido cometer un error en la condición de acutángulo (la condición del ángulo en $X$ no necesariamente excluye un signo).

Reexaminemos qué significa que el triángulo sea acutángulo respecto al círculo de diámetro BC. En realidad, la condición del ángulo en $X$ opuesto al lado $BC$ está bien, pero hay una condición adicional sobre los ángulos en B y C, que ya vimos se satisfacen automáticamente dado que $0<y<24$. Sin embargo, ¡eso depende de que X esté dentro del rectángulo! Como X está dentro, confirmado.

Entonces la condición de acutángulo para BXC es solo $\angle BXC<90°$, que da $(x-L)^2+(y-12)^2>144$.

Calculemos esta cantidad de manera explícita en cada caso y veamos qué valores de x,y resultan.

Alternativamente, podríamos darnos cuenta de que la condición del ángulo en X es equivalente a si el circuncírculo tiene radio mayor... Hmm.

Vamos a pensarlo de otra forma. En el triángulo AXD, el lado AD=24 y circuncírculo radio 13. El ángulo en X opuesto a AD. Usando la ley de senos, el ángulo en X, $\sin(\angle AXD) = \frac{AD}{2R} = \frac{24}{26}=\frac{12}{13}$. Así $\angle AXD \approx 67.4°$ (agudo) o $\approx 112.6°$ (obtuso). Como el triángulo es acutángulo, $\angle AXD$ es el ángulo agudo: $\cos\angle AXD = \frac{5}{13}$.

Espera, $\sin = 12/13$, así que $\cos = \pm 5/13$. Agudo significa $\cos >0$, $\cos = 5/13$.

Esto se relaciona con $h$: el centro está a $h=5$ de la recta AD. Si $h=5$ (centro a la derecha de AD, dentro del rectángulo), entonces el círculo de diámetro AD (radio 12 centrado en $(0,12)$) y el circuncírculo (centro $(5,12)$, radio 13) se intersectan... Veamos dónde queda X.

De hecho, para el triángulo AXD, los posibles puntos X son los puntos del circuncírculo que están "arriba" o "abajo"... Las intersecciones del circuncírculo con el interior.

Hmm, déjame reconsiderar si $h=5$ o $h=-5$ desde la condición de acutángulo.

Para el triángulo AXD con vértices A y D fijos, el conjunto de puntos X que forman triángulos acutángulos con A y D:

Un triángulo acutángulo requiere que X esté en la franja entre las rectas perpendiculares a AD por A y D (para ángulos en A y D agudos), y fuera del semicírculo de diámetro AD (para ángulo en X agudo).

Las rectas perpendiculares a AD por A y D son rectas horizontales $y=0$ y $y=24$. Para ángulos en A y D agudos, X debe estar entre estas rectas: $0<y<24$. De acuerdo.

Para el ángulo en X agudo, X debe estar fuera del círculo con diámetro AD. Correcto.

Entonces, con $R=13$, el circuncírculo está centrado en $(\pm5, 12)$, radio 13. 

El círculo con diámetro AD tiene centro $(0,12)$, radio 12. La distancia entre centros es 5. Como $5+12=17>13$ y $13-12=1<5$, los círculos se intersectan en dos puntos. El circuncírculo se extiende fuera del círculo de diámetro en la parte de la derecha (cuando $h=5$) o izquierda (cuando $h=-5$).

Para $X$ dentro del rectángulo ($0<x<L$), si $h=-5$, el circuncírculo está centrado en $(-5,12)$, radio 13. Las intersecciones con el rectángulo... la coordenada x mínima sería $-5-13=-18$, máxima $-5+13=8$. Entonces $x\le 8$. Para X dentro con $0<x<L$, necesitamos $L>8$ (probable) y $x<8$.

Con $h=-5$, el circuncírculo está casi todo a la izquierda de $x=0$, con solo una porción pequeña a la derecha (x de 0 a 8). Y la región donde $\angle AXD>90°$ (dentro del círculo de diámetro) es donde $x^2+(y-12)^2<144$. Para $h=-5$ y puntos con $x>0$ cerca de 0, es muy posible que estén dentro del círculo de diámetro, lo que daría ángulo obtuso.

Entonces la condición de acutángulo distingue: con $h=5$, para todo punto del circuncírculo con $x>0$, ¿está fuera del círculo de diámetro? Revisemos.

Para $h=5$: $(x-5)^2+(y-12)^2=169$. Entonces $x^2+(y-12)^2 = 169 -25 +10x = 144+10x>144$ para $x>0$. Así que todo punto con $x>0$ está fuera del círculo de diámetro, ángulo en X agudo. Bien.

Para $h=-5$: $x^2+(y-12)^2 = 144 -10x$. Para $x>0$, esto es $<144$, así que $X$ está dentro del círculo de diámetro, ángulo en X obtuso. Entonces no es acutángulo.

Por lo tanto, efectivamente $h=5$ es necesaria para acutángulo. Correcto.

Similar para BXC: el circuncírculo con centro $(p,12)$, $p=L\pm9$, radio 15.

El círculo de diámetro BC tiene centro $(L,12)$, radio 12. Para el ángulo en X agudo, X fuera de este círculo: $(x-L)^2+(y-12)^2>144$.

Para $p=L+9$: $(x-p)^2 = (x-L-9)^2$. Entonces:
$(x-L)^2+(y-12)^2 = (x-p)^2+(y-12)^2 - (x-p)^2 + (x-L)^2$
... calculemos directamente:

$(x-p)^2+(y-12)^2=225$.
$(x-L)^2 = (x-p+9)^2 = (x-p)^2 + 18(x-p)+81$.
Como $p=L+9$, $x-p = x-L-9$. Y $(x-L)^2 = (x-p)^2 + 18(x-p)+81$? Revisemos: $x-L = x-p+9$. $(x-L)^2=(x-p+9)^2=(x-p)^2+18(x-p)+81$. Correcto.

Entonces:
$(x-L)^2+(y-12)^2 = 225 + 18(x-p)+81 = 306+18(x-p).$

Necesitamos $>144$:
$$306+18(x-p)>144 \Rightarrow 18(x-p)>-162 \Rightarrow x-p>-9.$$
Como $p=L+9$, $x-p=x-L-9>-9 \Rightarrow x>L$. ¡Imposible porque $x<L$!

Por lo tanto, el caso $p=L+9$ NO puede dar triángulo acutángulo: para $x<L$, $x-p=x-L-9<-9$, luego $x-p<-9$, así $306+18(x-p)<306-162=144$, el ángulo en X es obtuso. Entonces $p=L+9$ se descarta.

Para $p=L-9$: $x-p = x-L+9$. 
$(x-L)^2 = (x-p-9)^2 = (x-p)^2 -18(x-p)+81$.
$(x-L)^2+(y-12)^2 = 225 - 18(x-p)+81 = 306-18(x-p)$.

Necesitamos $>144$:
$$306-18(x-p)>144 \Rightarrow 18(x-p)<162 \Rightarrow x-p<9.$$
Con $p=L-9$: $x-p=x-L+9$. Entonces $x-L+9<9 \Rightarrow x<L$. ¡Cierto siempre!

Entonces para $p=L-9$, todo punto con $x<L$ da ángulo agudo en X. Y esto es consistente con X dentro del rectángulo.

Por lo tanto, solo el caso $p=L-9$ es válido (junto con $h=5$), como deduje inicialmente. La ecuación resultante es:

$$L^3 - 38L^2 - 116L + 3960 = 0.$$

Debo encontrar la raíz. Como es un problema de competencia, $L$ debería ser entero. Revisemos si factoricé bien o si hay error en el desarrollo.

Retomemos: Caso $p=L-9$, $h=5$.

Ecuaciones:
(4): $x(L-10)=24y$.
(5'): con $p=L-9$: 
$x(L-2p)-24y=81-p^2$.
$L-2p = L-2L+18 = 18-L$.
$81-p^2=81-(L-9)^2=81-L^2+18L-81 = 18L-L^2 = L(18-L)$.
Entonces:
$$x(18-L) - 24y = L(18-L).$$

Pero de (4), $24y=x(L-10)$. Sustituimos:
$$x(18-L) - x(L-10) = L(18-L)$$
$$x[(18-L)-(L-10)] = L(18-L)$$
$$x(28-2L) = L(18-L)$$
$$x = \frac{L(18-L)}{28-2L} = \frac{L(18-L)}{2(14-L)}.$$

Esto da $x = \frac{L(18-L)}{2(14-L)}$.

Ahora, ¿$x>0$? $L>0$. Necesitamos $18-L$ y $14-L$ mismo signo. Si $L<14$: ambos positivos, $x>0$. Si $14<L<18$: $x<0$, inválido. Si $L>18$: numerador negativo, denominador negativo, $x>0$. Entonces $L<14$ o $L>18$.

Ahora, $x<L$:
Para $L<14$: $\frac{L(18-L)}{2(14-L)} < L \Rightarrow \frac{18-L}{2(14-L)} < 1 \Rightarrow 18-L < 28-2L \Rightarrow -L < 10-2L \Rightarrow L < 10$. Hmm, para $L<14$, $x<L$ requiere $L<10$.

Para $L>18$: denominador $2(14-L)<0$. Desigualdad $\frac{L(18-L)}{2(14-L)}<L$. Dividimos por $L>0$: $\frac{18-L}{2(14-L)}<1$. Como $18-L<0$ y $14-L<0$, el lado izquierdo es positivo. $\frac{18-L}{2(14-L)} = \frac{L-18}{2(L-14)}$. ¿Menor que 1? $\frac{L-18}{2(L-14)}<1 \Rightarrow L-18 < 2L-28 \Rightarrow 10 < L$. Cierto siempre para $L>18$. Entonces $x<L$ se cumple para $L>18$.

Por lo tanto, $L>18$. La raíz de la cúbica entre 38 y 39 es consistente.

Ahora resolvamos la cúbica:
$$L^3 -38L^2 -116L + 3960 = 0.$$

Busquemos raíces racionales. Los divisores de 3960: $2^3\cdot 3^2\cdot5\cdot11$. Probemos $L=20$: $8000 - 15200 - 2320 + 3960 = -5560$. No.

$L=24$: $13824 - 21888 - 2784 + 3960 = -6888$. No.

$L=30$: $27000 - 34200 - 3480 + 3960 = -6720$. No.

$L=36$: $46656 - 49248 - 4176 + 3960 = -2808$.

$L=40$: $64000 - 60800 - 4640 + 3960 = 2520$.

$L=44$: $85184 - 73568 - 5104 + 3960 = 10472$.

$L=50$: $125000 - 95000 - 5800 + 3960 = 28160$.

$L=60$: $216000 - 136800 - 6960 + 3960 = 76200$.

$L=45$: $91125 - 76950 - 5220 + 3960 = 12915$.

$L=38$: $54872 - 54872 - 4408 + 3960 = -448$.

$L=39$: $59319 - 57798 - 4524 + 3960 = 957$.

$L=38.5$: $38.5^3=57066.625$. $38\cdot38.5^2=38\cdot1482.25=56325.5$. $116\cdot38.5=4466$. Suma: $57066.625 - 56325.5 - 4466 + 3960 = 235.125$.

Hmm, $L=38$: -448, $L=38.5$: 235. Raíz ≈ 38.3.

Probemos $L=38.3$: $38.3^3 = 56191.787$ (calculemos: $38.3^2=1466.89$, $\times 38.3 = 56191.687$... es tedioso). No es entero.

Revisemos si de verdad es la cúbica correcta. Quizá el error está en la derivación de (7) usando (1), o en la condición (1).

Repasemos la condición $\angle AXB=90°$ con más cuidado. Vectores desde X:
$\overrightarrow{XA}=A-X=(-x,-y)$.
$\overrightarrow{XB}=B-X=(L-x,-y)$.

Producto punto: $(-x)(L-x)+(-y)(-y) = -x(L-x)+y^2 = y^2 - xL + x^2$. Como $y^2 - x(L-x) = y^2 - xL + x^2$. La condición es:
$$y^2 - xL + x^2 = 0 \Rightarrow x^2 - xL + y^2 =0 \Rightarrow x^2+y^2 = xL.$$

Hmm, ¡he estado usando $y^2 = x(L-x)$ que es $y^2=xL-x^2$, lo mismo que $x^2+y^2=xL$. Correcto.

Vamos a ver: $x^2+y^2=xL \Rightarrow x^2+y^2-xL=0$. Despejando $y^2=xL-x^2=x(L-x)$. Correcto.

Ahora, puede que la cúbica se factorice. Intentemos factorizar:
$$L^3 -38L^2 -116L + 3960.$$

Probemos $L=36$: -2808. $L=40$: 2520. 

Probemos $L=35$: $42875 - 38\cdot1225 - 4060 + 3960 = 42875 - 46550 - 4060+3960 = -3775$.

$L=33$: $35937 - 41382 - 3828+3960 = -5313$.

$L=32$: $32768 - 38912 - 3712+3960 = -5896$.

$L=34$: -4608.

$L=44$: 10472.

$L=42$: $74088 - 67032 - 4872+3960 = 6144$.

$L=41$: $68921 - 63878 - 4756+3960 = 4247$.

$L=40$: 2520.

$L=39$: 957.

$L=38$: -448.

Entonces raíz entre 38 y 39, específicamente ≈38.32. No es entero.

Esto sugiere un error en el planteamiento. Reconsideremos la condición de acutángulo del triángulo AXD más rigurosamente.

Un triángulo es acutángulo si los tres ángulos son menores a 90°. 

En el triángulo AXD:
- Ángulo en A: entre los lados AD y AX.
- Ángulo en D: entre DA y DX.
- Ángulo en X: entre XA y XD.

Ya analicé. Ángulo en A agudo ⟺ $y>0$. Ángulo en D agudo ⟺ $y<24$. Ángulo en X agudo ⟺ $X$ fuera del círculo de diámetro AD.

¿Es correcto que fuera del círculo ⟺ agudo? El teorema de Tales dice: el ángulo subtendido por un diámetro es 90° para puntos sobre el círculo. Para puntos dentro del círculo, el ángulo es >90° (obtuso); para puntos fuera, <90° (agudo). Esto se mantiene para el ángulo que mira al diámetro AD. Correcto.

Ahora, el problema dice "triangles AXD and BXC are both acute". Quizá "acute" se refiere a que los ángulos en $X$ son agudos, no todo el triángulo. Pero dice "triangles are acute", que significa triángulos acutángulos (todos los ángulos agudos). Sin embargo, los ángulos en A, D, B, C son automáticamente agudos ya que $X$ está dentro. Así que el único requisito adicional es el ángulo en X agudo. Eso ya lo cumplimos.

Quizá me perdí una posibilidad: el circuncírculo de AXD con centro en $h=-5$ podría dar ángulo en X agudo para puntos en un arco particular.

Revisemos $h=-5$: $(x+5)^2+(y-12)^2=169$. Con $x>0$, obtuvimos $x^2+(y-12)^2=144-10x<144$ para $x>0$. Así que todos los puntos con $x>0$ están dentro del círculo de diámetro, dando ángulo obtuso. Entonces $h=-5$ realmente se descarta si $x>0$. Correcto.

Para $p=L+9$: $(x-L-9)^2+(y-12)^2=225$. Con $x<L$, obtuvimos $(x-L)^2+(y-12)^2=306+18(x-L-9) = 306 + 18x -18L -162 = 144 +18(x-L)$. Como $x<L$, esto es $<144$, ángulo obtuso. Entonces $p=L+9$ se descarta. Correcto.

Entonces el caso es único y la cúbica es correcta. Sin embargo la raíz no es entera. Quizá el problema espera un valor específico no entero, o quizá hay otra interpretación de "acute": solo el ángulo en X es agudo. Pero ya.

Déjame revisar si la condición de que los triángulos comparten X y son acutángulos impone algo más sutil: quizá el ángulo en X de AXD y el ángulo en X de BXC deben sumar con el ángulo recto AXB para completar... Total, $\angle AXD + \angle BXC + 90° = 360°$ si X está rodeado; o podrían sumar 180°-90°=90°... Veamos.

Alrededor de X: rayos XA, XB, XC, XD. En un rectángulo ABCD, los puntos están ordenados A, B, C, D. Desde el interior X, los rayos hacia los vértices están en orden: XA, XB, XC, XD (en sentido horario o antihorario). El ángulo AXB forma el ángulo entre XA y XB. Los ángulos AXD y BXC... El ángulo AXD está entre XA y XD, pasando por... depende del orden.

Si el orden es XA, XB, XC, XD (por ejemplo), entonces $\angle AXB$ (de XA a XB), $\angle BXC$ (de XB a XC), $\angle CXD$ (de XC a XD), $\angle DXA$ (de XD a XA) suman 360°.

$\angle AXD = \angle DX A$... El ángulo AXD es el ángulo en X entre XA y XD. En el orden XA,XB,XC,XD, el ángulo entre XA y XD puede ser el ángulo que pasa por XB, XC (el ángulo mayor) o el directo (menor). El ángulo interno del triángulo AXD es el menor entre las direcciones XA y XD.

Dado $\angle AXB=90°$, si el orden es XA, XB, XC, XD, entonces $\angle AXD$ (el menor entre XA y XD) pasa por XB y XC. Hmm, no es directo.

Puede que esta restricción imponga relaciones adicionales. No la he usado. Vamos a ver si hay una ecuación adicional que determine L de forma única y más simple.

Alternativamente, volvamos a plantear el problema de manera puramente geométrica.

Dado que $\angle AXB=90°$, $X$ está sobre el círculo de diámetro AB. También está sobre el circuncírculo de AXD (radio 13) y el circuncírculo de BXC (radio 15).

Sean:
- Circuncírculo de AXD: pasa por A, D y X, radio 13.
- Circuncírculo de BXC: pasa por B, C y X, radio 15.
- Círculo de diámetro AB: pasa por A, B y X (con ángulo recto en X), y su centro está en el punto medio de AB, radio $L/2$.

Tenemos múltiples círculos. Podemos usar las coordenadas ya establecidas; es lo más directo.

Revisemos las cuentas de nuevo, quizá hay un error aritmético en la cúbica.

Partimos de:
Circuncírculo AXD: centro $(5,12)$, radio 13. Ecuación:
$$(x-5)^2+(y-12)^2=169. \quad (A)$$

Circuncírculo BXC: centro $(L-9,12)$, radio 15. Ecuación:
$$(x-L+9)^2+(y-12)^2=225. \quad (B)$$

Condición $\angle AXB=90°$:
$$x^2+y^2=xL. \quad (C)$$

Ahora, ¿podemos sacar L sin despejar x,y de manera tan enrevesada? Restemos ecuaciones.

Expandamos (A):
$$x^2-10x+25+y^2-24y+144=169 \Rightarrow x^2+y^2-10x-24y+169=169$$
$$x^2+y^2-10x-24y=0. \quad (A')$$

Expandamos (B):
$$x^2-2(L-9)x+(L-9)^2+y^2-24y+144=225$$
$$x^2+y^2-2(L-9)x-24y+(L-9)^2+144=225$$
$$x^2+y^2-2(L-9)x-24y+(L-9)^2=81. \quad (B')$$

Sustituimos (C) $x^2+y^2=xL$ en (A'):
$$xL-10x-24y=0 \Rightarrow x(L-10)=24y. \quad (1)$$

Sustituimos en (B'):
$$xL-2(L-9)x-24y+(L-9)^2=81$$
$$xL-2xL+18x-24y+L^2-18L+81=81$$
$$-xL+18x-24y+L^2-18L=0. \quad (2)$$

De (1): $24y=x(L-10)$. Sustituimos en (2):
$$-xL+18x-x(L-10)+L^2-18L=0$$
$$-xL+18x-xL+10x+L^2-18L=0$$
$$-2xL+28x+L^2-18L=0$$
$$x(28-2L)+L^2-18L=0$$
$$x(28-2L)=L(18-L)$$
$$x=\frac{L(18-L)}{28-2L}.$$

Esto coincide con la expresión anterior ($x=\frac{L(18-L)}{2(14-L)}$). Correcto.

Ahora usamos (C) junto con (1) para obtener otra relación. De (1), $y=\frac{x(L-10)}{24}$.

Sustituimos en (C): $x^2+y^2=xL$.
$$x^2+\frac{x^2(L-10)^2}{576}=xL$$
Si $x>0$:
$$x\left(1+\frac{(L-10)^2}{576}\right)=L$$
$$x = \frac{576L}{(L-10)^2+576}. \quad (3)$$

Esto es correcto.

Igualamos (2) y (3):
$$\frac{L(18-L)}{28-2L} = \frac{576L}{(L-10)^2+576}.$$

Cancelamos L:
$$\frac{18-L}{28-2L} = \frac{576}{(L-10)^2+576}.$$

Multiplicamos en cruz:
$$(18-L)[(L-10)^2+576] = 576(28-2L).$$

Desarrollamos el lado izquierdo:
$(18-L)(L^2-20L+100+576) = (18-L)(L^2-20L+676)$.

Lado derecho: $576\cdot 28 - 1152L = 16128 - 1152L$.

Lado izquierdo: $18(L^2-20L+676) - L(L^2-20L+676)$
$= 18L^2 -360L + 12168 - L^3 +20L^2 -676L$
$= -L^3 + 38L^2 -1036L + 12168$.

Igualamos:
$$-L^3 + 38L^2 -1036L + 12168 = 16128 - 1152L$$
$$-L^3 +38L^2 -1036L +1152L +12168 -16128 =0$$
$$-L^3+38L^2+116L -3960=0$$
Multiplicando por $-1$:
$$L^3 -38L^2 -116L +3960=0.$$

Correcto, es la cúbica. Ahora, ¿es posible que factoricemos de otra manera? Probemos con $L=44$, $42$, $46$, $48$, $52$, $54$, $55$, $60$, $66$, $72$, $88$, etc.

Probemos $L=44$: $85184 - 38\cdot1936 -5104 +3960 = 85184-73568=11616; 11616-5104=6512; +3960=10472$. No.

$L=48$: $110592 - 38\cdot2304 -5568+3960 = 110592 -87552 -5568+3960 = 23040-5568=17472; +3960=21432$. No.

$L=52$: $140608 - 38\cdot2704 -6032+3960 = 140608 -102752 -6032+3960 = 37856-6032=31824; +3960=35784$. No.

$L=56$: $175616 - 38\cdot3136 -6496+3960 = 175616 -119168 -6496+3960 = 56448-6496=49952;+3960=53912$.

$L=60$: 76200.

$L=66$: $287496 - 38\cdot4356 -7656+3960 = 287496 -165528 -7656+3960 = 121968-7656=114312;+3960=118272$.

$L=72$: $373248 - 38\cdot5184 -8352+3960 = 373248 -196992 -8352+3960 = 176256-8352=167904;+3960=171864$.

Todo positivo para $L\geq 40$? $L=40$: 2520 (positivo). $L=39$: 957. $L=38$: -448. Entonces única raíz entre 38 y 39, y las otras raíces... la cúbica debe tener 3 raíces reales o 1. Veamos comportamiento: para $L\to\infty$, principal $L^3$ domina $\to +\infty$. Para $L\to -\infty$, $\to -\infty$. Derivada: $3L^2-76L-116$. Raíces de la derivada: $L=(76\pm\sqrt{5776+1392})/6 = (76\pm\sqrt{7168})/6 \approx (76\pm84.66)/6$, entonces $L\approx -1.44$ y $L\approx 26.78$.

En $L=26.78$ la cúbica tiene un mínimo local. Evaluemos: $L\approx26.78$: 
$26.78^3 = 19202$ (aprox). $38\cdot26.78^2 = 38\cdot717.17=27252$. $116\cdot26.78=3106$. Suma: $19202 -27252 -3106+3960 = -7196$. Entonces el mínimo local es negativo, y solo hay una raíz real (la de ~38.33). Bien.

Entonces la única raíz real es $\approx38.327$. Pero parece extraño para una competencia. Quizá el valor esperado sea este. Revisemos si hay una manera de obtener una expresión exacta más simple.

Podemos intentar factorizar la cúbica. Probemos raíces racionales más sistemáticamente.

$3960 = 2^3 \cdot 3^2 \cdot 5 \cdot 11$. Divisores enteros positivos: 1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 15, 18, 20, 22, 24, 30, 33, 36, 40, 44, 45, 55, 60, 66, 72, 88, 90, 99, 110, 120, 132, 165, 180, 198, 220, 264, 330, 360, 396, 440, 495, 660, 792, 990, 1320, 1980, 3960.

Evaluemos $P(L)=L^3-38L^2-116L+3960$ en algunos más:

$P(33) = 35937 - 41382 -3828+3960 = -5313$.
$P(36) = -2808$.
$P(40) = 2520$.
$P(44) = 10472$.
$P(45) = 91125 -76950 -5220 +3960 = 12915$.
$P(48)=21432$.
$P(55) = 166375 - 38\cdot3025 -6380+3960 = 166375 -114950 -6380 +3960 = 51425-6380=45045;+3960=49005$.
$P(60)=76200$.
$P(66)=118272$.
$P(72)=171864$.
$P(88)=681472 - 38\cdot7744 -10208+3960 = 681472 -294272 -10208+3960 = 387200-10208=376992;+3960=380952$.
$P(90)=729000 -38\cdot8100 -10440+3960 = 729000 -307800 -10440+3960 = 421200-10440=410760;+3960=414720$.
$P(99)=970299 -38\cdot9801 -11484+3960 = 970299 -372438 -11484+3960 = 597861-11484=586377;+3960=590337$.
$P(110)=1331000 -38\cdot12100 -12760+3960 = 1331000 -459800 -12760+3960 = 871200-12760=858440;+3960=862400$.
$P(120)=1728000 -38\cdot14400 -13920+3960 = 1728000-547200-13920+3960 = 1180800-13920=1166880;+3960=1170840$.
$P(132)=...$ obviamente grande.
$P(165), P(180),...$

Todos los divisores grandes dan positivo. Los pequeños dan negativo. Parece que no hay raíz entera.

Probemos divisores negativos: $P(-1)=-1-38+116+3960=4037$. $P(-2)=-8-152+232+3960=4032$. $P(-3)=-27-342+348+3960=3939$. $P(-4)=-64-608+464+3960=3752$. $P(-5)=-125-950+580+3960=3465$. $P(-6)=-216-1368+696+3960=3072$. $P(-8)=-512-2432+928+3960=1944$. $P(-9)=-729-3078+1044+3960=1197$. $P(-10)=-1000-3800+1160+3960=320$. $P(-11)=-1331-4598+1276+3960=-693$. No hay raíz entera negativa tampoco.

Entonces la cúbica es irreducible sobre los racionales y la respuesta no es un entero. Hmm.

Quizá cometí un error en la asignación de $AD$ y $BC$. Releamos: "Let ABCD be a rectangle with BC=24". En un rectángulo nombrado ABCD, normalmente ABCD está en orden, con AB horizontal y BC vertical; pero quizá BC=24 es el lado horizontal? No, en un rectángulo ABCD el orden canónico es A, B, C, D consecutivos, con AB y CD paralelos, BC y DA paralelos. Si BC=24, entonces AD=24 también. AB=CD es el otro lado. Eso usé.

Podría el rectángulo estar orientado con BC horizontal? No importa, la geometría es simétrica.

Reexaminemos si la elección del signo de $h$ y $p$ está correcta. Hay otra sutileza: para el triángulo AXD, el circuncírculo pasa por A y D, que están en la misma vertical. El centro está en $y=12$. La distancia al centro desde la recta AD: $\sqrt{13^2-12^2}=5$, por lo que la coordenada x de centro es $\pm5$, es decir $h=5$ o $h=-5$.

Para que el ángulo en X sea agudo (X fuera del círculo de diámetro AD), necesitamos que X esté al lado opuesto de la recta AD respecto al círculo de diámetro... En realidad, el circuncírculo y el círculo de diámetro comparten A y D; el resto del circuncírculo se extiende en ambas direcciones transversales. Para $X$ dentro del rectángulo (a la derecha de AD), y con $h=-5$, el circuncírculo en la zona $x>0$ está dentro del círculo de diámetro (ya que $144-10x<144$), así ángulo obtuso. Correcto. Con $h=5$, zona $x>0$ fuera, ángulo agudo. Correcto.

Para BXC, $p=L+9$ o $p=L-9$. Para $X$ a la izquierda de BC ($x<L$). Con $p=L+9$, el circuncírculo en la zona $x<L$ está dentro del círculo de diámetro BC (ángulo obtuso). Con $p=L-9$, zona $x<L$ está fuera (ángulo agudo). Correcto.

Así que la configuración es única: $h=5$, $p=L-9$, dando la cúbica.

Quizá el problema NO requiere que todo el triángulo sea acutángulo, sino solo que los ángulos en X sean agudos... pero eso es lo mismo aquí. O quizá "acute" incluye solo los ángulos en X, que es lo que restringimos.

Déjame verificar numéricamente si hay solución con una cúbica distinta si considero una combinación diferente ($h=-5$ o $p=L+9$) y un triángulo con un ángulo obtuso... No, el problema dice agudo.

Quizá interpreté mal qué es un "triángulo acutángulo" con respecto al circuncírculo: Para que un triángulo sea acutángulo, el circuncírculo tiene centro en el interior. En el triángulo AXD, el lado más grande es AD=24 (si X está dentro) — no necesariamente. Hmm. En un triángulo acutángulo, el cuadrado de cada lado es menor que la suma de cuadrados de los otros dos. Específicamente, para el triángulo AXD ser acutángulo:

- $\angle AXD <90° \Leftrightarrow AD^2 < AX^2 + XD^2$.
- $\angle XAD<90° \Leftrightarrow XD^2 < AX^2+AD^2$ (siempre cierto si X cercano).
- $\angle ADX<90° \Leftrightarrow AX^2 < AD^2 + XD^2$.

Las condiciones de ángulo en A y D se verifican automáticamente dadas las posiciones, pero la condición del ángulo en X es la que elegimos correctamente.

Sin embargo, hay una condición adicional para acutángulo relacionada con X: $AD$ debe ser el lado, y el circuncírculo... No.

Vamos a comprobar numéricamente la solución con la cúbica para ver si las condiciones de acutángulo se cumplen y si $X$ está dentro.

Raíz $L \approx 38.327$.

Calculemos $x$, $y$:
$x = \frac{576L}{(L-10)^2+576}$. Con $L=38.327$: $L-10=28.327$. $(28.327)^2 \approx 802.42$. Más 576: 1378.42. $576L = 576\cdot 38.327 = 22076.35$. $x = 22076.35/1378.42 = 16.016$.

$y = \frac{x(L-10)}{24} = \frac{16.016 \cdot 28.327}{24} = \frac{453.68}{24}=18.90$.

Verifiquemos que $X=(16.0, 18.9)$ está dentro del rectángulo $0<x<38.3$, $0<y<24$. Sí.

Verificamos ángulo AXB: $x^2+y^2 = 256.5+357.2=613.7$. $xL=16.016\cdot38.327=613.9$. Bien.

Verificamos circuncírculo AXD (centro $(5,12)$, radio 13): $(16.016-5)^2+(18.9-12)^2 = 11.016^2+6.9^2 = 121.35+47.61=168.96 \approx 169$. Bien.

Circuncírculo BXC (centro $(L-9,12)=(29.327,12)$, radio 15): $(16.016-29.327)^2+(18.9-12)^2 = 13.311^2+6.9^2=177.18+47.61=224.79 \approx 225$. Bien.

Ángulo en X de AXD: $x^2+(y-12)^2 = 256.5+47.61=304.1>144$, agudo. Bien.
Ángulo en X de BXC: $(x-L)^2+(y-12)^2 = (16.016-38.327)^2+47.61 = 22.311^2+47.61=497.8+47.61=545.4>144$, agudo. Bien.

Todos los ángulos de ambos triángulos:
- AXD: ángulos en A, D, X agudos (verificado).
- BXC: ángulos en B, C, X agudos.

Entonces la solución es $L \approx 38.327$.

Pero el problema debe tener una respuesta más limpia. Déjame reconsiderar si $AB$ es en realidad el otro lado. Si $BC=24$ y el rectángulo es ABCD, $AB$ es uno de los lados. Calculé $AB=L$.

Quizá hice la correspondencia de los circuncírculos incorrectamente: "triangles AXD and BXC have circumradii 13 and 15". El triángulo AXD tiene radio 13, BXC radio 15, o al revés? El problema dice "have circumradii 13 and 15, respectively", lo que significa AXD→13, BXC→15. Correcto.

Revisemos si existe una solución más elegante usando trigonometría. Tal vez el valor de L es racional, no entero. Calculemos la raíz más exactamente.

Resolvamos la cúbica numéricamente con más precisión.

$P(L)=L^3-38L^2-116L+3960$.

Sabemos $P(38)=-448$, $P(38.5)=235.125$ (calculado). Interpolando: raíz ≈ 38 + 448/(448+235.125)*0.5 ≈ 38 + 448/683.125*0.5 ≈ 38 + 0.3279 ≈ 38.328.

Refinemos con Newton. $P'(L)=3L^2-76L-116$.

En $L=38.3$: 
$38.3^2 = 1466.89$.
$38.3^3 = 1466.89 \cdot 38.3 = 1466.89\cdot38 + 1466.89\cdot0.3 = 55741.82 + 440.067 = 56181.887$.
$38\cdot38.3^2 = 38\cdot1466.89 = 55741.82$.
$116\cdot38.3 = 4442.8$.
$P(38.3) = 56181.887 - 55741.82 - 4442.8 + 3960 = (56181.887-55741.82)=440.067; 440.067-4442.8=-4002.733; +3960=-42.733$.

$P'(38.3) = 3\cdot1466.89 -76\cdot38.3 -116 = 4400.67 - 2910.8 -116 = 1373.87$.

Corrección: $L = 38.3 - (-42.733)/1373.87 = 38.3 + 0.0311 = 38.3311$.

$P(38.331)$: calculemos para refinar.
$38.331^2 = (38.3+0.031)^2 = 1466.89 + 2\cdot38.3\cdot0.031 + 0.031^2 = 1466.89 + 2.3746 + 0.000961 = 1469.2656$.
$38.331^3 = 38.331 \cdot 1469.2656$. Mejor usar $38.3^3$ y derivada: $38.331^3 = 38.3^3 + 3\cdot38.3^2\cdot0.031 + 3\cdot38.3\cdot0.031^2 + 0.031^3 = 56181.887 + 3\cdot1466.89\cdot0.031 + 3\cdot38.3\cdot0.000961 + 0.0000298 = 56181.887 + 136.4208 + 0.1104 + 0.00003 = 56318.4182$.
$38\cdot38.331^2 = 38\cdot1469.2656 = 55832.0928$.
$116\cdot38.331 = 4446.396$.
$P(38.331) = 56318.4182 - 55832.0928 - 4446.396 + 3960 = (56318.4182-55832.0928)=486.3254; 486.3254-4446.396=-3960.0706; +3960=-0.0706$.

$P'(38.331) = 3\cdot1469.2656 - 76\cdot38.331 -116 = 4407.7968 - 2913.156 -116 = 1378.6408$.

Corrección: $L=38.331 + 0.0706/1378.64 = 38.33105$.

Entonces $L \approx 38.33105$. El valor exacto es la raíz de esa cúbica, que no es un número racional simple. Sin embargo, quizá la respuesta esperada sea un entero y el error esté en otro lugar. Revisemos una vez más si el problema pudo significar que los ángulos en X son agudos, o existe otra simetría.

Releamos: "Point X lies inside the rectangle such that ∠AXB=90°. Given that triangles AXD and BXC are both acute and have circumradii 13 and 15 ...". 

Sí, "triangles ... are both acute" = triángulos acutángulos. Correcto.

Quizá hay un error de signo en la condición de acutángulo del caso $p$. Reexaminemos la condición ángulo en X para BXC.

Triángulo BXC, vértices B=(L,0), X=(x,y), C=(L,24). Lado BC=24 vertical. Circuncírculo radio 15, centro en $(p,12)$ con $p=L\pm9$.

Ángulo en X, opuesto al lado BC. Es agudo ⟺ $BC^2 < BX^2 + CX^2$.

$BX^2 = (x-L)^2+y^2$.
$CX^2 = (x-L)^2+(y-24)^2$.
$BC^2 = 576$.

Condición: $576 < (x-L)^2+y^2 + (x-L)^2+(y-24)^2 = 2(x-L)^2 + y^2 + (y-24)^2$.

$y^2+(y-24)^2 = y^2+y^2-48y+576 = 2y^2-48y+576$.

Entonces:
$$576 < 2(x-L)^2 + 2y^2 -48y +576$$
$$2(x-L)^2 + 2y^2 -48y >0$$
$$(x-L)^2 + y^2 -24y>0.$$

¿Coincide con $(x-L)^2+(y-12)^2>144$? Desarrollemos: $(x-L)^2+(y-12)^2 = (x-L)^2 + y^2 -24y +144$. La condición $>144$ equivale a $(x-L)^2+y^2-24y>0$. ¡Sí, coincide! Correcto.

Entonces la condición de acutángulo es correcta.

Hmm, quizá en el problema original la respuesta es simplemente la raíz de la cúbica y se espera un valor entero si la cúbica fuera $L^3-38L^2-116L+3960=0$ con raíz $L=44$? No, $P(44)=10472$.

Probemos si la cúbica tiene una raíz entera que no probé. Probemos $L=66$: 118272. Probemos $L=22$: -1152... ya.

Probemos $L=20$: -5560, $L=21$: -1617, $L=22$: -1152, $L=23$: -559, $L=24$: 168, $L=25$: -7065?? Espera, $L=25$: $15625 - 38\cdot625 -2900+3960 = 15625 - 23750 -2900+3960 = -7065$. 

¿Por qué $P(24)=168$ y $P(25)=-7065$? Revisemos $P(24)$:
$24^3=13824$. $38\cdot24^2 = 38\cdot576 = 21888$. $116\cdot24=2784$.
$P(24) = 13824 - 21888 -2784 +3960 = 13824-21888 = -8064; -8064-2784 = -10848; +3960 = -6888$.

Antes dije $P(24)=168$, pero es -6888. Error de cálculo previo. Recorrijamos los valores:

- $P(20) = 8000 - 15200 -2320 +3960 = -5560$.
- $P(21) = 9261 - 38\cdot441 -2436 +3960 = 9261 - 16758 -2436 +3960 = 9261-16758=-7497; -7497-2436=-9933; +3960=-5973$.
- $P(22) = 10648 - 38\cdot484 -2552+3960 = 10648 -18392 -2552+3960 = 10648-18392=-7744; -7744-2552=-10296; +3960=-6336$.
- $P(23) = 12167 - 38\cdot529 -2668+3960 = 12167 -20102 -2668+3960 = 12167-20102=-7935; -7935-2668=-10603; +3960=-6643$.
- $P(24) = 13824 -21888 -2784+3960 = -6888$.
- $P(25) = 15625 -23750 -2900+3960 = -7065$.
- $P(26) = 17576 - 38\cdot676 -3016+3960 = 17576 -25688 -3016+3960 = 17576-25688=-8112; -8112-3016=-11128; +3960=-7168$.
- $P(27) = 19683 - 38\cdot729 -3132+3960 = 19683 -27702 -3132+3960 = 19683-27702=-8019; -8019-3132=-11151; +3960=-7191$.
- $P(28) = 21952 - 38\cdot784 -3248+3960 = 21952 -29792 -3248 +3960 = 21952-29792=-7840; -7840-3248=-11088; +3960=-7128$.
- $P(30) = 27000 -34200 -3480+3960 = -6720$.
- $P(32) = 32768 -38912 -3712+3960 = -5896$.
- $P(33) = 35937 - 41382 -3828+3960 = -5313$.
- $P(34) = 39304 - 38\cdot1156 -3944+3960 = 39304 -43928 -3944+3960 = 39304-43928=-4624; -4624-3944=-8568; +3960=-4608$.
- $P(35) = 42875 -46550 -4060+3960 = -3775$.
- $P(36) = 46656 -49248 -4176 +3960 = -2808$.
- $P(37) = 50653 - 38\cdot1369 -4292+3960 = 50653 -52022 -4292+3960 = 50653-52022=-1369; -1369-4292=-5661; +3960=-1701$.
- $P(38) = 54872 - 54872 -4408+3960 = -448$.
- $P(39) = 59319 - 57798 -4524+3960 = 1521 -4524+3960 = 957$.
- $P(40) = 64000 -60800 -4640+3960 = 2520$.

Entonces la única raíz real positiva está entre 38 y 39, ≈38.33.

Probemos si la cúbica se puede escribir como $(L-a)(L^2+bL+c)$ con $a$ entero... no hay raíz entera.

Quizá el problema realmente tiene como respuesta $L=44$ u otro entero y hay un error de signo en alguna parte. Revisemos la condición de acutángulo del ángulo en X una vez más.

Para el triángulo AXD, el ángulo en X es agudo ⟺ $AD^2 < AX^2 + XD^2$ (el lado opuesto al ángulo en X es AD). 

$AD=24$, $AD^2=576$.
$AX^2 = x^2+y^2$.
$XD^2 = x^2+(y-24)^2$.

Condición: $576 < x^2+y^2 + x^2+(y-24)^2 = 2x^2+2y^2-48y+576$.
$$576 < 2x^2+2y^2-48y+576 \Rightarrow 2x^2+2y^2-48y>0 \Rightarrow x^2+y^2-24y>0.$$

Y con la condición $\angle AXB=90°$: $x^2+y^2=xL$. Entonces:
$$x^2+y^2-24y = xL-24y >0 \Rightarrow xL>24y$$

Pero de (1), $x(L-10)=24y$, lo que implica $xL -10x =24y$, es decir $xL = 24y+10x > 24y$ (ya que $x>0$). Entonces esta condición se cumple automáticamente y no impone nada extra.

Ahora circum radio de AXD: 13. Esto lo usamos para obtener (A).

Volvamos a la ecuación (A): $(x-5)^2+(y-12)^2=169$. ¿Y si el centro es $h=-5$? Entonces (A) sería $(x+5)^2+(y-12)^2=169$. Con $x^2+y^2=xL$, desarrollemos:

$$x^2+10x+25+y^2-24y+144=169 \Rightarrow x^2+y^2+10x-24y=0.$$
Con $x^2+y^2=xL$:
$$xL+10x-24y=0 \Rightarrow x(L+10)=24y.$$

Este es el caso $h=-5$. Como determinamos, para $h=-5$ y $x>0$, el ángulo en X es obtuso. Así que no es válido.

Para BXC con $p=L+9$: $(x-L-9)^2+(y-12)^2=225$. Ya vimos que da obtuso; no válido.

Por lo tanto, la configuración válida es única y da $L \approx 38.331$.

Sin embargo, consideremos: ¿puede el triángulo AXD ser acutángulo con $h=-5$ si el ángulo "en X" en realidad mira el lado AD pero el ángulo interno del triángulo AXD podría ser el suplementario? No, el ángulo en X es único y está entre los rayos XA y XD. Hemos usado correctamente la condición.

Espera, hay un detalle importante: el punto X dentro del rectángulo con $\angle AXB=90°$ restringe a X a estar sobre el círculo de diámetro AB, que es el semicírculo superior (dentro del rectángulo). Los puntos del círculo de diámetro AB son: centro $(L/2,0)$, radio $L/2$. Ecuación:
$$(x-L/2)^2 + y^2 = (L/2)^2 \Rightarrow x^2 -xL + L^2/4 + y^2 = L^2/4 \Rightarrow x^2+y^2=xL.$$
Correcto.

Ahora, para que X esté dentro del rectángulo, también $0<y<24$. En el círculo de diámetro AB, $y^2=x(L-x)\le L^2/4$, con máximo en $x=L/2$. Para que $y$ alcance al menos cierto valor... No añade restricción directa.

Podríamos considerar la otra orientación: quizá $BC=24$ significa que el rectángulo tiene lados $AB$ y $BC$ con $AB=BC=24$? No, "rectangle with BC=24" no implica cuadrado.

Revisemos si quizá la condición de acutángulo debería ser $\angle AXD$ agudo ⟺ $X$ está DENTRO del círculo de diámetro AD, al revés. Repasemos el teorema de Tales.

El teorema de Tales: si X está sobre el círculo con diámetro AD, $\angle AXD = 90°$.

Considera puntos en el semicírculo opuesto... Tomemos A=(0,0), D=(0,24). Círculo de diámetro AD: centro (0,12), radio 12. El punto (12,12) está sobre el círculo. El ángulo $\angle AXD$ con X=(12,12): vectores XA=(-12,-12), XD=(-12,12). Producto punto: $144-144=0$, ángulo 90°. Correcto.

El punto (24,12) está fuera del círculo (distancia 24>12). Vectores XA=(-24,-12), XD=(-24,12). Producto punto: $576-144=432>0$, ángulo agudo (<90°). Correcto: fuera → agudo.

El punto (0,12) es el centro, dentro. Vectores XA=(0,-12), XD=(0,12). Producto punto: $-144<0$, ángulo obtuso. Correcto: dentro → obtuso.

Entonces la condición está bien: fuera del círculo ⟺ ángulo agudo. Confirmado.

Revisemos la condición $\angle AXB=90°$: X sobre el círculo de diámetro AB. El punto X está "arriba" del segmento AB, con $y>0$. Correcto.

Entonces el planteamiento es consistente y la solución es la raíz de la cúbica.

Ahora, quizá el problema espera una respuesta entera y el número 13 o 15 está en otro lugar, o la respuesta es un valor como $L = 44$ con una configuración distinta de signos. Probemos todas las combinaciones de signos y veamos si alguna da raíz entera, aunque viole acutángulo... solo por curiosidad.

Combinación 1: $h=5$, $p=L+9$. ($p=L+9$ no da acutángulo). Las ecuaciones: (A) con $h=5$ y (B) con $p=L+9$.

De (A'): $x^2+y^2-10x-24y=0$. Con (C): $xL-10x-24y=0 \Rightarrow x(L-10)=24y$. (1)

De (B) con $p=L+9$: $(x-L-9)^2+(y-12)^2=225$. Expandimos:
$$x^2-2(L+9)x+(L+9)^2+y^2-24y+144=225$$
$$x^2+y^2-2(L+9)x-24y+(L+9)^2=81.$$
Con (C) $x^2+y^2=xL$:
$$xL-2(L+9)x-24y+(L+9)^2=81$$
$$xL-2xL-18x-24y+L^2+18L+81=81$$
$$-xL-18x-24y+L^2+18L=0.$$
Usando (1): $24y=x(L-10)$:
$$-xL-18x-x(L-10)+L^2+18L=0$$
$$-xL-18x-xL+10x+L^2+18L=0$$
$$-2xL-8x+L^2+18L=0$$
$$x(2L+8)=L^2+18L$$
$$x = \frac{L(L+18)}{2L+8} = \frac{L(L+18)}{2(L+4)}.$$

De (3): $x = \frac{576L}{(L-10)^2+576}$.

Igualamos:
$$\frac{L(L+18)}{2(L+4)} = \frac{576L}{(L-10)^2+576}.$$
Cancelamos L:
$$\frac{L+18}{2(L+4)} = \frac{576}{(L-10)^2+576}.$$
Multiplicamos en cruz:
$$(L+18)[(L-10)^2+576] = 1152(L+4).$$
$(L-10)^2+576 = L^2-20L+676$.
Lado izquierdo: $(L+18)(L^2-20L+676) = L^3 -20L^2+676L +18L^2 -360L +12168 = L^3 -2L^2+316L+12168$.
Lado derecho: $1152L+4608$.
$$L^3-2L^2+316L+12168 = 1152L+4608$$
$$L^3-2L^2-836L+7560=0.$$

Como antes, raíz ≈23.78.

Combinación 2: $h=-5$, $p=L-9$. (h=-5 no da acutángulo).
(A) con $h=-5$: $x^2+y^2+10x-24y=0$. Con (C): $xL+10x-24y=0\Rightarrow x(L+10)=24y$. (1')

(B) con $p=L-9$: $(x-L+9)^2+(y-12)^2=225$. Ya expandimos como (B') con $p=L-9$:
$$x^2+y^2-2(L-9)x-24y+(L-9)^2=81.$$
Con (C): $xL-2(L-9)x-24y+(L-9)^2=81$
$$xL-2xL+18x-24y+L^2-18L+81=81$$
$$-xL+18x-24y+L^2-18L=0.$$
Con (1'): $24y=x(L+10)$:
$$-xL+18x-x(L+10)+L^2-18L=0$$
$$-xL+18x-xL-10x+L^2-18L=0$$
$$-2xL+8x+L^2-18L=0$$
$$x(8-2L)=L(18-L)$$
$$x = \frac{L(18-L)}{8-2L} = \frac{L(18-L)}{2(4-L)}.$$

De (3): $x = \frac{576L}{(L-10)^2+576}$ (esto usa (C), que no depende de signos).

Igualamos:
$$\frac{18-L}{2(4-L)} = \frac{576}{(L-10)^2+576}.$$
Multiplicamos en cruz:
$$(18-L)[(L-10)^2+576] = 1152(4-L).$$
Lado izquierdo: $(18-L)(L^2-20L+676) = -L^3+38L^2-1036L+12168$.
Lado derecho: $4608-1152L$.
$$-L^3+38L^2-1036L+12168 = 4608-1152L$$
$$-L^3+38L^2+116L+7560=0$$
$$L^3-38L^2-116L-7560=0.$$

Probemos raíces: $L=45$: $91125-76950-5220-7560=1395$. $L=44$: $85184-73568-5104-7560=-1048$. Entonces raíz entre 44 y 45, ≈44.3. No entero.

Combinación 3: $h=-5$, $p=L+9$. (ambos no acutángulos).
(A) $h=-5$: $x(L+10)=24y$.
(B) $p=L+9$: $-xL-18x-24y+L^2+18L=0$.
Sustituimos $24y=x(L+10)$:
$$-xL-18x-x(L+10)+L^2+18L=0$$
$$-xL-18x-xL-10x+L^2+18L=0$$
$$-2xL-28x+L^2+18L=0$$
$$x(2L+28)=L^2+18L$$
$$x=\frac{L(L+18)}{2(L+14)}.$$

Igualamos con (3):
$$\frac{L+18}{2(L+14)} = \frac{576}{(L-10)^2+576}.$$
$$(L+18)(L^2-20L+676) = 1152(L+14)$$
$$L^3-2L^2+316L+12168 = 1152L+16128$$
$$L^3-2L^2-836L-3960=0.$$

Probemos raíces: $L=30$: $27000-1800-25080-3960=-3840$. $L=36$: $46656-2592-30096-3960=10008$. Raíz entre 30 y 36. $L=33$: $35937-2178-27588-3960=2211$. $L=32$: $32768-2048-26752-3960=8$. $L=31$: $29791-1922-25916-3960=-2007$. Raíz entre 32 y 33. $L=32$: 8, $L=32.1$... Probemos $L=32$: 8, $L=33$: 2211. Raíz ≈32.003. No entero.

Ninguna combinación da raíz entera. Interesante. Por lo tanto, la respuesta es la raíz de la cúbica del caso acutángulo, $L \approx 38.331$.

Sin embargo, puede que el problema realmente provenga de una competencia y la respuesta sea un entero. Quizá cometí un error conceptual en la relación entre el circuncírculo de BXC y la condición de acutángulo.

Repensemos: para un triángulo con circuncírculo de radio R, si es acutángulo, entonces el centro del circuncírculo está dentro del triángulo. Ahora, para el triángulo BXC, ¿dónde está su circuncírculo y centro?

El circuncírculo de BXC pasa por B(L,0) y C(L,24) en la vertical x=L, y por X(x,y) con x<L (a la izquierda). El centro está en (p,12), con p=L±9.

Para que el triángulo BXC sea acutángulo, el centro debe estar dentro del triángulo. El triángulo BXC tiene vértices B(L,0), C(L,24) (en la derecha) y X(x,y) (a la izquierda). El interior del triángulo está en el lado izquierdo de la vertical BC (x<L). Entonces el centro debe tener $p<L$. Esto requiere $p=L-9$, no $p=L+9$. Esto confirma $p=L-9$.

Además, para que el centro $(L-9,12)$ esté dentro del triángulo BXC, debe estar dentro del triángulo formado por B, C, X. El interior del triángulo BXC (con B y C en la derecha, X a la izquierda) es la región x<L, y entre algunas líneas. El centro $(L-9,12)$ está a x=L-9<L, bien.

Similar para AXD: centro (5,12) con 5>0, que está a la derecha de AD (x=0). El interior del triángulo AXD (con A y D a la izquierda en x=0, X a la derecha) es x>0, así que el centro (5,12) con x=5>0 está dentro. Confirma $h=5$. Correcto.

La condición del centro dentro del triángulo es equivalente al triángulo acutángulo. Todo bien.

Así que la respuesta es la raíz ≈38.331. Dado que el problema dice "compute AB", quizá la respuesta sea este número extraño, y no hay más.

Pero hmm, déjame revisar si quizá $AB=44$ es la respuesta si la condición fuera "have circumradii 13 and 15" y "both acute" refiriéndose a los ángulos en A y B... No, "triangles AXD and BXC are both acute" es claro.

Espera, quizá cometí un error en la cúbica del caso correcto: revisemos una vez más la combinación $h=5$, $p=L-9$ de manera directa con las ecuaciones de los circuncírculos sin expandir, usando la distancia.

Círculo AXD (centro $(5,12)$, radio 13): $(x-5)^2+(y-12)^2=169$. (A)
Círculo BXC (centro $(L-9,12)$, radio 15): $(x-L+9)^2+(y-12)^2=225$. (B)

Círculo diámetro AB (centro $(L/2,0)$, radio $L/2$): $(x-L/2)^2+y^2=(L/2)^2 \Rightarrow x^2+y^2=xL$. (C)

Estas son las tres ecuaciones. Con (C) podemos simplificar.

De (A): $x^2-10x+25+y^2-24y+144=169 \Rightarrow x^2+y^2-10x-24y=0 \Rightarrow xL-10x-24y=0 \Rightarrow x(L-10)=24y$. ✓

De (B): $(x-L+9)^2 = x^2-2(L-9)x+(L-9)^2 = x^2-2xL+18x+(L-9)^2$.
$(y-12)^2 = y^2-24y+144$.
Suma: $x^2+y^2-2xL+18x-24y+(L-9)^2+144 = 225$.
Con $x^2+y^2=xL$: $xL-2xL+18x-24y+(L-9)^2+144=225$
$-xL+18x-24y+(L-9)^2+144=225$
$-xL+18x-24y+(L-9)^2=81$
$-xL+18x-24y+L^2-18L+81=81$
$-xL+18x-24y+L^2-18L=0$
$-xL+18x-24y+L^2-18L=0$. ✓

Sustituimos $24y=x(L-10)$:
$-xL+18x-x(L-10)+L^2-18L=0$
$-xL+18x-xL+10x+L^2-18L=0$
$-2xL+28x+L^2-18L=0$
$x(28-2L)=18L-L^2=L(18-L)$
$x=\frac{L(18-L)}{28-2L}=\frac{L(18-L)}{2(14-L)}$. ✓

De (C) con (1): $x^2+y^2=xL$. $24y=x(L-10)\Rightarrow y=\frac{x(L-10)}{24}$.
$x^2 + \frac{x^2(L-10)^2}{576}=xL$.
Dividimos por x>0: $x\left(1+\frac{(L-10)^2}{576}\right)=L$.
$x\cdot \frac{576+(L-10)^2}{576}=L \Rightarrow x = \frac{576L}{576+(L-10)^2}$. ✓

Igualamos: $\frac{L(18-L)}{2(14-L)} = \frac{576L}{576+(L-10)^2}$.
Cancelamos L: $\frac{18-L}{2(14-L)}=\frac{576}{576+(L-10)^2}$.

En cruz: $(18-L)[576+(L-10)^2] = 1152(14-L)$.
$(L-10)^2 = L^2-20L+100$. Más 576: $L^2-20L+676$.
$(18-L)(L^2-20L+676) = 1152\cdot14 -1152L$.
$18(L^2-20L+676) - L(L^2-20L+676) = 16128 -1152L$.
$18L^2-360L+12168 - (L^3-20L^2+676L) = 16128 -1152L$.
$18L^2-360L+12168 -L^3+20L^2-676L = 16128-1152L$.
$-L^3+38L^2-1036L+12168 = 16128-1152L$.
$-L^3+38L^2-1036L+1152L+12168-16128=0$.
$-L^3+38L^2+116L-3960=0$.
$L^3-38L^2-116L+3960=0$. ✓

Todo correcto.

Ahora, quizá el problema realmente tiene esta respuesta, y la raíz exacta se puede simplificar. Intentemos factorizar la cúbica usando el método de Cardano o hiperbólico para ver si la raíz tiene una forma cerrada "bonita".

Cúbica: $L^3-38L^2-116L+3960=0$.

Hagamos $L = t + \frac{38}{3}$ para eliminar el término cuadrático.

$L = t + 38/3$.

$\left(t+\frac{38}{3}\right)^3 = t^3+3t^2\frac{38}{3}+3t\frac{1444}{9}+\frac{54872}{27} = t^3+38t^2+\frac{4332}{9}t+\frac{54872}{27}$. Espera, calculemos con calma.

Cabezal: $(t+a)^3 = t^3 + 3at^2 + 3a^2t + a^3$, con $a=38/3$.

$3a^2 = 3\cdot \frac{1444}{9} = \frac{1444}{3}$.
$a^3 = \frac{54872}{27}$.

Entonces $L^3 = t^3 + 38t^2 + \frac{1444}{3}t + \frac{54872}{27}$.

$38L^2 = 38\left(t+\frac{38}{3}\right)^2 = 38\left(t^2 + \frac{76}{3}t + \frac{1444}{9}\right) = 38t^2 + \frac{2888}{3}t + \frac{54872}{9}$.

$116L = 116t + 116\cdot\frac{38}{3} = 116t+\frac{4408}{3}$.

Sustituimos en $L^3-38L^2-116L+3960$:

$t^3 + 38t^2+\frac{1444}{3}t+\frac{54872}{27} - \left(38t^2+\frac{2888}{3}t+\frac{54872}{9}\right) -116t -\frac{4408}{3} +3960$.

Combinamos:
- $t^3$
- términos $t^2$: $38t^2-38t^2=0$.
- términos $t$: $\frac{1444}{3}t - \frac{2888}{3}t -116t = \frac{1444-2888}{3}t -116t = -\frac{1444}{3}t -116t = -\frac{1444}{3}t - \frac{348}{3}t = -\frac{1792}{3}t$.
- constante: $\frac{54872}{27} - \frac{54872}{9} - \frac{4408}{3} +3960$.

Calculemos la constante. $\frac{54872}{27} - \frac{54872}{9} = \frac{54872}{27} - \frac{164616}{27} = -\frac{109744}{27}$.

$-\frac{4408}{3} = -\frac{4408}{3}$. Convertimos a denominador 27: $-\frac{4408}{3} = -\frac{4408\cdot9}{27} = -\frac{39672}{27}$.

$3960 = \frac{3960\cdot27}{27} = \frac{106920}{27}$.

Suma: $-\frac{109744}{27}-\frac{39672}{27}+\frac{106920}{27} = \frac{-109744-39672+106920}{27} = \frac{-149416+106920}{27} = \frac{-42496}{27}$.

Entonces la cúbica en $t$:
$$t^3 - \frac{1792}{3}t - \frac{42496}{27} = 0.$$

Multiplicamos por 27:
$$27t^3 - 16128t - 42496 = 0.$$
Simple: $27t^3 = 16128t + 42496$.

Dividimos por 27: $t^3 = \frac{16128}{27}t + \frac{42496}{27} = \frac{1792}{3}t + \frac{42496}{27}$.

La forma $t^3 - 3pt - 2q =0$ con $3p = 1792/3$, $p=1792/9$, $2q = 42496/27$, $q = 21248/27$.

Discriminante: $q^2-p^3 = \left(\frac{21248}{27}\right)^2 - \left(\frac{1792}{9}\right)^3$. Si es positivo, una raíz real con Cardano.

$q^2 = \frac{21248^2}{27^2}$. $21248^2 = ?$ Quizás factoricemos: $1792 = 2^8\cdot7$? Veamos: $1792 = 256\cdot7 = 2^8\cdot7$. $21248 = ?$ $21248/7 ≈ 3035.4...$ Hmm, $21248 = 2^7\cdot166$? $21248/128 = 166$, $166=2\cdot83$. Entonces $21248 = 2^8\cdot83$? Revisemos: $2^8=256$, $256\cdot83 = 21248$. Sí, $21248 = 2^8\cdot83 = 256\cdot83$.

$1792 = 256\cdot7$. Entonces $p = \frac{256\cdot7}{9}$. $p^3 = \frac{256^3\cdot7^3}{729}$.

$q = \frac{256\cdot83}{27}$.

$q^2 = \frac{256^2 \cdot 83^2}{729}$.

$p^3 = \frac{256^3 \cdot 7^3}{729} = \frac{256^3\cdot343}{729}$.

$q^2 - p^3 = \frac{256^2(83^2 - 256\cdot343)}{729} = \frac{256^2(6889 - 87808)}{729} = \frac{256^2(-80919)}{729}<0$.

El discriminante es negativo, así que hay 3 raíces reales, y la solución se expresa con coseno. Interesante: $q^2-p^3<0$, así que 3 raíces reales, y la raíz deseada es la mayor.

Entonces:
$$t = 2\sqrt{\frac{p}{3}}\cos\left(\frac{1}{3}\arccos\left(\frac{q}{\sqrt{p^3}}\right)-\frac{2\pi k}{3}\right)$$ con $k=0,1,2$.

$\sqrt{p^3} = \frac{256\sqrt{256\cdot343}}{\sqrt{729}} = \frac{256\cdot\sqrt{87808}}{27}$. Esto no da un valor "bonito". El coseno de algo con arccos de un número complejo (porque $q/\sqrt{p^3}$ es un número real con $|q|/\sqrt{p^3}=\frac{21248/27}{\sqrt{87808}\cdot256/27} = \frac{21248}{256\sqrt{87808}} = \frac{83}{\sqrt{87808}} \approx \frac{83}{296.32} \approx 0.28$, menor a 1, así que ángulo real). Es válido pero no bonito.

Entonces la respuesta es un número algebraico de grado 3, no un entero. Esto es inusual para un problema de competencia. Quizá el problema tiene una errata, o quizá se espera que la respuesta sea $\frac{38}{3} + \frac{64}{3}\cos(...)$... No.

Alternativamente, quizá el problema original tiene números distintos que dan una raíz entera. Por ejemplo, si el problema fuera con $BC=24$, radios 13 y 15, quizá hay otra interpretación donde $AB=44$. Revisemos si con $AB=44$ se satisfacen las condiciones con alguna elección de signos, aunque no acutángulo... no importa.

Espera, la condición del centro dentro del triángulo para que sea acutángulo es necesario y suficiente. Para AXD, centro dentro del triángulo AXD. El centro (5,12) debe estar dentro del triángulo con vértices A(0,0), X(x,y), D(0,24). Para que (5,12) esté dentro, debe estar en el semiplano derecho de la recta AX y en el semiplano... En realidad, el centro (5,12) con x=5>0. ¿Está dentro del triángulo AXD? El triángulo AXD tiene A y D en x=0, X en (x,y) con x>0, y>0. El interior es la región delimitada por AD (el eje y), y las rectas AX y DX. El centro (5,12) podría estar dentro o fuera dependiendo de X.

De hecho, el triángulo acutángulo requiere TODOS los ángulos agudos, y el centro del circuncírculo está dentro del triángulo. Ya concluimos que la condición del ángulo en X es la única restrictiva, pero revisemos el centro dentro del triángulo AXD en nuestro caso numérico.

Con $L\approx38.33$, $x\approx16.0$, $y\approx18.9$, $X=(16,18.9)$.

Triángulo AXD: A=(0,0), X=(16,18.9), D=(0,24). El centro del circuncírculo es (5,12). ¿Está (5,12) dentro del triángulo AXD?

El triángulo AXD tiene vértices A(0,0), X(16,18.9), D(0,24). La recta AX pasa por (0,0) y (16,18.9): pendiente 18.9/16 ≈1.18, así $y=1.18x$. La recta DX pasa por (16,18.9) y (0,24): pendiente $(24-18.9)/(0-16)=5.1/(-16)=-0.319$, así $y = 24 -0.319x$.

El interior del triángulo: puntos con $x>0$, por encima de la recta AX y por debajo de la recta DX. Es decir, $y \ge 1.18x$ y $y \le 24-0.319x$ (aproximadamente, con la orientación correcta).

Evaluemos el centro (5,12): $1.18\cdot5=5.9$; $12 \ge 5.9$ ✓. $24-0.319\cdot5 = 24-1.59=22.4$; $12\le22.4$ ✓. Entonces (5,12) está dentro. Acutángulo ✓.

Para BXC: B=(L,0)=(38.33,0), C=(38.33,24), X=(16,18.9). Centro (L-9,12)=(29.33,12). El interior del triángulo BXC es la región x<L, entre rectas BX y CX. Recta BX: pasa por (38.33,0) y (16,18.9): pendiente $(18.9-0)/(16-38.33)=18.9/(-22.33)=-0.846$, así $y=-0.846(x-38.33)$. Recta CX: pasa por (38.33,24) y (16,18.9): pendiente $(18.9-24)/(16-38.33)=(-5.1)/(-22.33)=0.228$, así $y=24+0.228(x-38.33)$.

El interior es $x<38.33$, por encima de la recta BX y por debajo de la recta CX. Evaluemos (29.33,12): $x<38.33$ ✓. Recta BX en x=29.33: $y=-0.846(29.33-38.33)=-0.846(-9)=7.61$. $12\ge7.61$ ✓. Recta CX en x=29.33: $y=24+0.228(29.33-38.33)=24+0.228(-9)=24-2.05=21.95$. $12\le21.95$ ✓. Dentro ✓. Acutángulo ✓.

Todo correcto. Entonces la respuesta es la raíz ≈38.331.

Déjame reconsiderar si quizá se espera un valor entero y el problema original tiene algún detalle distinto, como "circumradii 13 and 15" refiriéndose a los circuncírculos de los triángulos que forman el rectángulo entero, o algo así.

Releamos el problema: "Given that triangles AXD and BXC are both acute and have circumradii 13 and 15, respectively". 

Hmm, quizá la condición "both acute" es superflua o se refiere a algo más. En cualquier caso, con los datos dados, la solución es única y es la raíz de la cúbica.

Ahora, ¿cuál es el valor numérico más preciso? Calculé $L\approx38.33105$. Hmm, espera, verifiquemos $P(38.331)$ más exactamente, y hagamos una iteración más de Newton.

Recapitulemos cálculos exactos para $L=38.331$:

$38.331^2$: calculemos precisamente.
$38.331^2 = (38 + 0.331)^2 = 1444 + 2\cdot38\cdot0.331 + 0.331^2 = 1444 + 25.156 + 0.109561 = 1469.265561$.

$38.331^3 = 38.331 \cdot 1469.265561$.
$38.331 \cdot 1469.265561 = 38\cdot1469.265561 + 0.331\cdot1469.265561 = 55832.091318 + 486.326900 = 56318.418218$.

$38\cdot38.331^2 = 38\cdot1469.265561 = 55832.091318$.

$116\cdot38.331 = 4446.396$.

$P(38.331) = 56318.418218 - 55832.091318 - 4446.396 + 3960 = 56318.418218 - 55832.091318 = 486.326900; 486.326900 - 4446.396 = -3960.069100; -3960.069100 + 3960 = -0.069100$.

$P'(38.331) = 3\cdot1469.265561 - 76\cdot38.331 - 116 = 4407.796683 - 2913.156 -116 = 1378.640683$.

Corrección de Newton: $\Delta = -P/P' = 0.069100/1378.640683 = 0.00005012$.

$L = 38.33105012$.

$P(38.33105) \approx 0$.

Entonces $AB \approx 38.33105$.

Para verificar, recalculamos $x$, $y$ con $L=38.33105012$:

$(L-10)^2 = 28.33105012^2 = 802.648... $ calculemos: $28.33105012^2 = (28.3+0.03105012)^2 = 800.89 + 2\cdot28.3\cdot0.03105012 + 0.03105012^2 = 800.89 + 1.7574368 + 0.0009641 = 802.6484009$.

$(L-10)^2+576 = 1378.6484009$.

$576L = 576\cdot38.33105012 = 22078.68484...$ calculemos: $38.33105012\cdot576 = 38.33105012\cdot500 + 38.33105012\cdot76 = 19165.52506 + 2913.15980... = 22078.68486$.

$x = 22078.68486/1378.6484 = 16.01460...$ Hmm, $1378.6484\cdot16 = 22058.3744$. Diferencia: 20.3105. $20.3105/1378.6484 = 0.01473$. Entonces $x\approx16.0147$.

$y = \frac{x(L-10)}{24} = \frac{16.0147\cdot28.33105}{24} = \frac{453.681}{24}=18.9034$.

Verificamos (C): $x^2+y^2 = 16.0147^2+18.9034^2 = 256.47+357.34=613.81$. $xL = 16.0147\cdot38.33105 = 613.83$. ✓

Verificamos (A): $(x-5)^2+(y-12)^2 = 11.0147^2+6.9034^2=121.32+47.66=168.98 \approx169$. Bien, hay un pequeño error de redondeo porque x,y recalculados con L aproximado; está bien.

Todo consistente.

Entonces la respuesta $AB = L \approx 38.331$. 

Sin embargo, dado que el problema probablemente espera un valor entero, revisemos si quizá se debe a un error en la lectura: "BC=24" y "circumradii 13 and 15". Podría ser que los circuncírculos de AXD y BXC tienen radios 13 y 15, sí.

Quizá el problema de origen es de Art of Problem Solving o AIME, y la respuesta es un entero entre 0 y 999. Si es AIME, la respuesta debe ser entero. Tal vez la intención era que $\angle AXB=90°$ y que los triángulos tengan radios, y haya una respuesta entera si los radios son 13 y 15 y BC=24.

Probemos a resolver el sistema sin la condición de acutángulo, para ver si hay una solución con L entero.

Si no hubiera la condición de acutángulo, podríamos mezclar signos. Las cuatro combinaciones dadas arriba dieron raíces no enteras excepto quizá alguna cercana. Pero probemos todas las combinaciones de signos de $h=\pm5$ y $L-p=\pm9$ (equivalentemente $p=L\mp9$), y veamos cuál da L entero.

- $h=+5, p=L-9$: raíz ≈38.33. P(38)=-448, P(39)=957.
- $h=+5, p=L+9$: raíz ≈23.78.
- $h=-5, p=L-9$: raíz ≈44.3? 
- $h=-5, p=L+9$: raíz ≈32.003.

Ninguna entera.

Ahora, quizá la condición de acutángulo, tal como la aplicamos, es correcta, y la respuesta es que la cúbica se factoriza sobre los racionales si elegimos L correctamente. Intentemos con L=38.331 en la cúbica... P(38.331)≈0. No entero.

Revisemos si la condición de acutángulo de BXC podría admitir $p=L+9$ si $x>L$... pero X está dentro del rectángulo, $x<L$ siempre. Correcto.

Hmm, déjame probar a sustituir L=44 en las ecuaciones originales para ver si todo se cumple y quizá cometí un error en la condición de acutángulo.

Con L=44, h=5, p=L-9=35. 
Circuncírculo AXD: $(x-5)^2+(y-12)^2=169$.
Circuncírculo BXC: $(x-35)^2+(y-12)^2=225$.
Círculo diámetro AB: $x^2+y^2=44x$.

De (A) + (C): $x(44-10)=24y \Rightarrow 34x=24y \Rightarrow y = \frac{17}{12}x$.
De (B) + (C): $x(18-44) = 44(18-44)$... revisemos: $L=44$, $18-L=-26$, $14-L=-30$. $x = \frac{44(-26)}{2(-30)} = \frac{-1144}{-60} = 19.0667$. 

Entonces $x = \frac{44\cdot26}{60} = \frac{1144}{60} = \frac{286}{15} \approx 19.0667$.

$y = \frac{17}{12}x = \frac{17}{12}\cdot\frac{286}{15} = \frac{17\cdot286}{180} = \frac{4862}{180} = \frac{2431}{90}\approx27.011$.

¡$y\approx27.0 >24$! Entonces X está fuera del rectángulo ($y>24$). Por lo tanto L=44 no es válido porque X queda fuera. Interesante. Con L=38.33, $y\approx18.9<24$ ✓.

Entonces la restricción $y<24$ es crucial y quizá determina L exactamente. Con L=38.331, y≈18.9<24, bien. Para L>38.331, ¿y crece? Veamos. De $y=\frac{x(L-10)}{24}$ y con L creciente, x también cambia.

La cúbica tiene una única raíz, y para esa raíz, todas las condiciones se cumplen. La respuesta es $L\approx38.331$.

En realidad, consideré la cúbica como única restricción; junto con las condiciones de acutángulo e interior, obtenemos la raíz. No hay otra restricción que fuerce L entero.

Quizá el problema es una prueba donde se espera que la respuesta sea una fracción o se deje indicada. Hmm.

Espera, repasemos la condición $y>0$ y $y<24$. Con la raíz ≈38.33, y≈18.9. Bien. Además, para el triángulo BXC, los ángulos en B y C agudos requieren $y>0$ y $y<24$, ✓.

Todo cuadra.

Reexaminemos la expresión para la combinación correcta una vez más para ver si podemos obtener una ecuación cuadrática o lineal adicional que simplifique.

Tenemos:
- $x(L-10)=24y$
- $x=\frac{L(18-L)}{2(14-L)}$
- $x=\frac{576L}{(L-10)^2+576}$
- $x^2+y^2=xL$ (equivalente a (1) y la expresión de x).

De estas, igualamos la 2 y la 3 para obtener la cúbica. Es correcto.

Alternativamente, podríamos usar $x^2+y^2=xL$ con $y=\frac{x(L-10)}{24}$:
$$x^2 + \frac{x^2(L-10)^2}{576} = xL \Rightarrow x = \frac{576L}{576+(L-10)^2}.$$
Correcto.

Y también tenemos la relación con el circuncírculo BXC, que da $x=\frac{L(18-L)}{2(14-L)}$.

Parece correcto.

Dado el análisis, la respuesta es la raíz de $L^3-38L^2-116L+3960=0$, cuyo valor numérico es aproximadamente $38.33$. 

A menos que el problema sea de una competencia tipo AIME (respuesta entera), quizá haya una errata. Pero si se pide "compute AB" sin especificar que sea entero, la respuesta exacta es la raíz de esa cúbica. Para dar una respuesta final, puedo presentar la raíz aproximada o la expresión exacta.

Sin embargo, quizá me equivoqué en un signo en la condición de acutángulo y el caso correcto sea otro con L entero. Revisemos el caso $h=-5$, $p=L+9$ (combinación 3) dio $P(L)=L^3-2L^2-836L-3960=0$, con raíz entre 32 y 33. P(32)=8, P(33)=2211. No entero.

El caso $h=-5$, $p=L-9$ (combinación 2) dio raíz entre 44 y 45. P(44)=-1048, P(45)=1395. No entero.

El caso $h=5$, $p=L+9$ (combinación 1) dio raíz entre 23 y 24. No entero.

El caso $h=5$, $p=L-9$ (correcto, acutángulo) dio raíz entre 38 y 39. No entero.

Hmm, quizá hay un error en la correspondencia de los radios: quizá el triángulo AXD tiene circunradio 15 y BXC tiene 13. Releamos: "circumradii 13 and 15, respectively" → AXD=13, BXC=15. Pero probemos al revés por curiosidad.

Si AXD tiene radio 15, BXC radio 13:

- AXD: centro $(h,12)$, $h^2+144=225 \Rightarrow h^2=81 \Rightarrow h=\pm9$.
- BXC: centro $(p,12)$, $(L-p)^2+144=169 \Rightarrow (L-p)^2=25 \Rightarrow L-p=\pm5$.

Acutángulo: para AXD, necesitamos h>0 (centro a la derecha), h=9. Para BXC, necesitamos L-p>0, L-p=5, p=L-5.

Ecuaciones correspondientes:

De (A) con h=9: $x^2+y^2-18x-24y=0 \Rightarrow x(L-18)=24y$. (1)

De (B) con p=L-5: $x(L-2p)-24y = (L-p)^2 - p^2 + ...$ mejor directamente:
$(x-p)^2+(y-12)^2=169$ con $p=L-5$. Expandimos:
$x^2-2(L-5)x+(L-5)^2+y^2-24y+144=169$
$x^2+y^2-2(L-5)x-24y+(L-5)^2+144=169$
$(L-5)^2 = L^2-10L+25$. +144 = $L^2-10L+169$.
Entonces: $x^2+y^2-2(L-5)x-24y+L^2-10L+169=169$
$x^2+y^2-2(L-5)x-24y+L^2-10L=0$.
Con $x^2+y^2=xL$: $xL-2(L-5)x-24y+L^2-10L=0$
$xL-2xL+10x-24y+L^2-10L=0$
$-xL+10x-24y+L^2-10L=0$. (2)

De (1): $24y=x(L-18)$.
Sustituimos en (2):
$-xL+10x-x(L-18)+L^2-10L=0$
$-xL+10x-xL+18x+L^2-10L=0$
$-2xL+28x+L^2-10L=0$
$x(28-2L)=10L-L^2=L(10-L)$
$x=\frac{L(10-L)}{28-2L}=\frac{L(10-L)}{2(14-L)}$.

De (C) con (1): $y=\frac{x(L-18)}{24}$.
$x^2+y^2=xL$:
$x^2 + \frac{x^2(L-18)^2}{576}=xL$
$x\left(1+\frac{(L-18)^2}{576}\right)=L$
$x = \frac{576L}{576+(L-18)^2}$.

Igualamos:
$$\frac{L(10-L)}{2(14-L)} = \frac{576L}{576+(L-18)^2}$$
Cancelamos L:
$$\frac{10-L}{2(14-L)} = \frac{576}{576+(L-18)^2}$$
En cruz: $(10-L)[576+(L-18)^2] = 1152(14-L)$.
$(L-18)^2 = L^2-36L+324$. Más 576: $L^2-36L+900$.
$(10-L)(L^2-36L+900) = 1152\cdot14 -1152L = 16128-1152L$.
$10(L^2-36L+900Sea $L=AB$. Ubicamos el rectángulo como
$A=(0,0)$, $B=(L,0)$, $C=(L,24)$, $D=(0,24)$ y $X=(x,y)$.

Por ley de senos:

- En $\triangle AXD$, con circunradio $13$ y lado $AD=24$:
$$
\frac{24}{\sin\angle AXD}=26 \implies \sin\angle AXD=\frac{12}{13},\quad \cos\angle AXD=\frac{5}{13}.
$$

- En $\triangle BXC$, con circunradio $15$ y lado $BC=24$:
$$
\frac{24}{\sin\angle BXC}=30 \implies \sin\angle BXC=\frac45,\quad \cos\angle BXC=\frac35.
$$

Sea $\delta=\angle DAX$ y sea $\zeta=\angle CBX$. Como $\angle AXB=90^\circ$ y las rectas verticales del rectángulo son paralelas, se tiene
$$
\delta+\zeta=90^\circ.
$$

En $\triangle AXD$, si $\varepsilon=\angle ADX$, entonces
$$
\sin\varepsilon=\sin(\angle AXD+\delta)
=\frac{12}{13}\cos\delta+\frac5{13}\sin\delta.
$$
Además $AX=26\sin\varepsilon$, por lo que
$$
x=26\sin\varepsilon\sin\delta,\qquad y=26\sin\varepsilon\cos\delta.
$$

En $\triangle BXC$, sea $\eta=\angle BCX$. Como $\zeta=90^\circ-\delta$,
$$
\eta=90^\circ-\angle BXC+\delta.
$$
Entonces
$$
\sin\eta=\sin(\delta+90^\circ-\angle BXC)
=\frac45\sin\delta+\frac35\cos\delta,
$$
y $BX=30\sin\eta$. Así
$$
L-x=30\sin\eta\sin\zeta,\qquad y=30\sin\eta\cos\zeta.
$$

Igualando las dos expresiones para $y$:
$$
26\sin\varepsilon\cos\delta=30\sin\eta\cos\zeta.
$$
Como $\cos\zeta=\sin\delta$ y $\sin\zeta=\cos\delta$, se obtiene
$$
24\cos^2\delta+10\sin\delta\cos\delta
=24\sin^2\delta+18\sin\delta\cos\delta.
$$
Simplificando, con $t=\tan\delta$:
$$
3t^2+t-3=0.
$$
La raíz positiva es
$$
t=\frac{-1+\sqrt{37}}6.
$$

Ahora,
$$
L=x+(L-x)=26\sin\varepsilon\sin\delta+30\sin\eta\sin\zeta.
$$
Sustituyendo y usando las mismas relaciones,
$$
L=\frac{48t+10t^2+18}{1+t^2}.
$$
Con $t^2=\dfrac{3-t}{3}$:
$$
L=\frac{2(67t+42)}{6-t}.
$$
Sustituyendo $t=\dfrac{-1+\sqrt{37}}6$:
$$
L=\frac{2(185+67\sqrt{37})}{37-\sqrt{37}}
=14+4\sqrt{37}.
$$

Por lo tanto,
$$
\boxed{14+4\sqrt{37}}
$$