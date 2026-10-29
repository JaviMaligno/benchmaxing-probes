# Resolución

**Paso 1: Interpretar cada ecuación geométricamente.**

Escribamos $z = x + yi$.

La primera ecuación $|20+15i-z| = 13$ es una **circunferencia** de centro $C = (20, 15)$ y radio $r = 13$.

La segunda ecuación $|z-12-k| = |z-5i-k|$ dice que $z$ equidista de los puntos $A = (12+k,\ 0)$ y $B = (k,\ 5)$, es decir, $z$ está en la **mediatriz** del segmento $AB$ (que siempre está bien definida, pues $A \neq B$).

**Paso 2: Hallar la ecuación de la mediatriz.**

Elevando al cuadrado con $z = x+yi$:

$$(x-12-k)^2 + y^2 = (x-k)^2 + (y-5)^2$$

Expandiendo y cancelando $(x-k)^2 + y^2$ de ambos lados:

$$-24(x-k) + 144 = -10y + 25$$

$$24x - 10y = 24k + 119$$

Es una **familia de rectas paralelas** (pendiente $\tfrac{24}{10} = \tfrac{12}{5}$) parametrizada por $k$.

**Paso 3: Condición de solución única.**

El sistema tiene exactamente una solución cuando la recta es **tangente** a la circunferencia, es decir, cuando la distancia del centro $C = (20,15)$ a la recta $24x - 10y - (24k+119) = 0$ es igual al radio $13$:

$$\frac{|24(20) - 10(15) - 119 - 24k|}{\sqrt{24^2 + 10^2}} = 13$$

Como $\sqrt{576+100} = \sqrt{676} = 26$:

$$|480 - 150 - 119 - 24k| = 338 \quad\Longrightarrow\quad |211 - 24k| = 338$$

**Paso 4: Resolver para $k$.**

$$24k = 211 \pm 338$$

$$k = \frac{549}{24} = \frac{183}{8} \qquad \text{o} \qquad k = \frac{-127}{24}$$

Ambos valores producen tangencia (por ambos lados de la familia de rectas paralelas), así que ambos son válidos.

**Paso 5: Sumar los valores.**

$$\frac{183}{8} - \frac{127}{24} = \frac{549 - 127}{24} = \frac{422}{24} = \frac{211}{12}$$

Como $211$ es primo, $\gcd(211, 12) = 1$, así que $m = 211$, $n = 12$ y:

$$m + n = \boxed{223}$$