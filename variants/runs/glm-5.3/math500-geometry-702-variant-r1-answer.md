## Planteamiento

Sitúo $O$ en el origen: $C=(0,-c)$ al sur, $D=(d,0)$ al este, con $d,c>0$, y $H=(0,0,h)$ a altura $h$.

**Paso 1: hallar $c$, $d$, $h$.**

$$c^2+h^2=145^2,\qquad d^2+h^2=125^2,\qquad c^2+d^2=180^2$$

Sumando las dos primeras y usando la tercera:
$$c^2+d^2+2h^2=145^2+125^2 \;\Rightarrow\; 32400+2h^2=36650 \;\Rightarrow\; h^2=2125$$

Entonces:
$$c^2=145^2-2125=18900,\qquad d^2=125^2-2125=13500$$

**Paso 2: reformular el ahorro.**

El ahorro es $HC+HD-HP=270-HP$, así que hay que **minimizar** $HP$ con $P$ en el segmento $CD$. Si $P=(x,-y)$ con $x,y\ge 0$, entonces $HP=\sqrt{x^2+y^2+h^2}$, y minimizar $HP$ equivale a minimizar $x^2+y^2$ sujeto a que $P$ esté en la recta $CD$:

$$\frac{x}{d}+\frac{y}{c}=1,\qquad x,y\ge 0$$

**Paso 3: punto más cercano al origen en la recta.**

Es el pie de la perpendicular desde el origen a la recta $CD$. Con multiplicadores de Lagrange (o minimizando $x^2+y^2+\lambda\left(\frac{x}{d}+\frac{y}{c}-1\right)$):

$$x=\frac{c^2d}{c^2+d^2},\qquad y=\frac{cd^2}{c^2+d^2}$$

Comprobación de que está en el segmento: $\frac{x}{d}=\frac{c^2}{c^2+d^2}=\frac{18900}{32400}=\frac{7}{12}$ y $\frac{y}{c}=\frac{13500}{32400}=\frac{5}{12}$, positivos y con suma $1$; el punto es interior. ✓

**Paso 4: calcular $HP$.**

$$x^2+y^2=\frac{c^2d^2}{c^2+d^2}=\frac{18900\cdot 13500}{32400}=7875$$

(Equivalentemente, es el cuadrado de la distancia del origen a la recta: $\left(\frac{cd}{180}\right)^2=7875$.)

$$HP=\sqrt{7875+2125}=\sqrt{10000}=100 \text{ m}$$

**Paso 5: ahorro máximo.**

$$270-100=170$$

## Verificación

Con $x=\frac{35\sqrt{15}}{2}\approx 67.7\le d\approx 116.2$ y $y=\frac{25\sqrt{21}}{2}\approx 57.3\le c\approx 137.5$, el punto óptimo $P$ está efectivamente dentro del segmento $CD$, así que el mínimo se alcanza y la solución es válida.

\boxed{170\text{ m}}