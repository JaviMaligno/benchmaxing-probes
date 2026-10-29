# Resolución

**Paso 1: Interpretar la primera ecuación geométricamente.**

Sea $z = x + iy$. La ecuación $|20+15i-z| = 13$ describe un círculo con centro $C = (20, 15)$ y radio $r = 13$.

**Paso 2: Interpretar la segunda ecuación.**

Como $k$ es real, $z - 12 - k = z - (12+k)$ corresponde al punto $(12+k,\, 0)$, y $z - 5i - k = z - (k+5i)$ corresponde al punto $(k,\, 5)$. La ecuación

$$|z-12-k| = |z-5i-k|$$

es el **mediador** (perpendicular bisector) de los puntos $A = (12+k, 0)$ y $B = (k, 5)$.

**Paso 3: Encontrar la ecuación de la recta.**

Expandiendo $(x-12-k)^2 + y^2 = (x-k)^2 + (y-5)^2$:

$$-24x + 24k + 119 + 10y = 0 \quad\Longrightarrow\quad 24x - 10y = 24k + 119.$$

Es una familia de rectas **paralelas** con vector normal $(24, -10)$.

**Paso 4: Condición de solución única.**

El sistema tiene exactamente una solución cuando la recta es **tangente** al círculo, es decir, cuando la distancia del centro $(20,15)$ a la recta es $13$:

$$\frac{|24(20) - 10(15) - 24k - 119|}{\sqrt{24^2 + 10^2}} = \frac{|211 - 24k|}{26} = 13.$$

Entonces $|211 - 24k| = 338$, lo que da:

$$211 - 24k = 338 \implies k = -\frac{127}{24}, \qquad 211 - 24k = -338 \implies k = \frac{549}{24} = \frac{183}{8}.$$

**Verificación:** para $k = -\tfrac{127}{24}$, la recta es $12x - 5y = -4$ y la distancia al centro es $\tfrac{|240 - 75 + 4|}{13} = 13$ ✓. Para $k = \tfrac{183}{8}$, la recta es $12x - 5y = 334$ y la distancia es $\tfrac{|240 - 75 - 334|}{13} = 13$ ✓.

**Paso 5: Suma de los valores de $k$.**

$$-\frac{127}{24} + \frac{183}{8} = -\frac{127}{24} + \frac{549}{24} = \frac{422}{24} = \frac{211}{12}.$$

Como $211$ es primo, la fracción es irreducible: $m = 211$, $n = 12$.

$$m + n = \boxed{223}$$