Sea $z = x + yi$. La primera ecuación es un círculo con centro $(20, 15)$ y radio $13$.

La segunda ecuación es la mediatriz del segmento entre los puntos $(12+k, 0)$ y $(k, 5)$:

$$|z-(12+k)|^2 = |z-(k+5i)|^2$$

$$(x-12-k)^2 + y^2 = (x-k)^2 + (y-5)^2$$

Expandiendo y simplificando:

$$-24x + 144 + 24k = -10y + 25$$

$$24x - 10y - 119 - 24k = 0$$

Para que el sistema tenga exactamente una solución, esta recta debe ser tangente al círculo. La distancia del centro $(20,15)$ a la recta debe ser igual a $13$:

$$\frac{|24(20) - 10(15) - 119 - 24k|}{\sqrt{24^2 + 10^2}} = 13$$

$$\frac{|480 - 150 - 119 - 24k|}{26} = 13$$

$$|211 - 24k| = 338$$

Esto da dos casos:

- $211 - 24k = 338 \Rightarrow k = -\frac{127}{24}$
- $211 - 24k = -338 \Rightarrow k = \frac{549}{24}$

La suma de los valores de $k$ es:

$$-\frac{127}{24} + \frac{549}{24} = \frac{422}{24} = \frac{211}{12}$$

Como $211$ es primo y no divide a $12$, la fracción está en términos mínimos. Por lo tanto $m = 211$, $n = 12$.

$$m + n = 211 + 12 = \boxed{223}$$