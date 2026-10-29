## Planteamiento

**Paso 1: Ecuación de la parábola rotada.**

Un punto $(x,y)$ está en la imagen rotada si y solo si, al rotarlo $60^\circ$ en sentido *horario* (la rotación inversa), cae en la parábola original $y = x^2 - 4$. La rotación de $-60^\circ$ es

$$(x,y) \mapsto \left(\frac{x+\sqrt{3}\,y}{2},\ \frac{y-\sqrt{3}\,x}{2}\right),$$

de modo que la imagen rotada satisface

$$\frac{y-\sqrt{3}\,x}{2} = \left(\frac{x+\sqrt{3}\,y}{2}\right)^{\!2} - 4
\quad\Longleftrightarrow\quad
x^2 + 2\sqrt{3}\,xy + 3y^2 + 2\sqrt{3}\,x - 2y - 16 = 0. \tag{1}$$

**Paso 2: Intersecciones.**

Sustituyendo $y = x^2-4$ en (1):

$$3x^4 + 2\sqrt{3}\,x^3 - 25x^2 - 6\sqrt{3}\,x + 40 = 0.$$

Buscando factores cuadráticos con coeficientes en $\mathbb{Q}(\sqrt{3})$, la cuártica se factoriza (se verifica por expansión directa):

$$(x^2 + \sqrt{3}\,x - 4)(3x^2 - \sqrt{3}\,x - 10) = 0.$$

*Observación geométrica:* como la parábola es simétrica respecto al eje $y$, rotarla $60^\circ$ equivale a reflejarla respecto a la recta $y = -\sqrt{3}\,x$; los puntos de la parábola sobre esa recta satisfacen $x^2-4 = -\sqrt{3}x$, o sea el primer factor — de ahí su aparición.

**Paso 3: La raíz del cuarto cuadrante.**

En la parábola original, el cuarto cuadrante exige $x>0$ y $y = x^2-4 < 0$, es decir $0 < x < 2$. Las cuatro raíces son:

- $x^2+\sqrt{3}x-4=0 \Rightarrow x = \frac{-\sqrt{3}\pm\sqrt{19}}{2} \approx 1.313,\ -3.045$
- $3x^2-\sqrt{3}x-10=0 \Rightarrow x = \frac{\sqrt{3}\pm\sqrt{123}}{6} \approx 2.137,\ -1.560$

La única en $(0,2)$ es $x = \dfrac{\sqrt{19}-\sqrt{3}}{2}$, que da el único punto de intersección en el cuarto cuadrante.

**Paso 4: La coordenada $y$.**

Del propio factor, $y = x^2-4 = -\sqrt{3}\,x$, así que

$$y = -\sqrt{3}\cdot\frac{\sqrt{19}-\sqrt{3}}{2} = \frac{3-\sqrt{57}}{2} \approx -2.275.$$

**Paso 5: Respuesta.**

Con $a = 3$, $b = 57$, $c = 2$ (donde $\gcd(3,2)=1$ y $57 = 3\cdot 19$ es libre de cuadrados):

$$a+b+c = 3+57+2 = \boxed{62}$$