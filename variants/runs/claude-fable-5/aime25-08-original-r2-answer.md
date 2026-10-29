## Resolución

**Primera ecuación:** $|25+20i-z|=5$ describe una circunferencia de centro $(25, 20)$ y radio $5$.

**Segunda ecuación:** $|z-(4+k)| = |z-(k+3i)|$ es el conjunto de puntos equidistantes de $A=(4+k,\,0)$ y $B=(k,\,3)$, es decir, la mediatriz del segmento $AB$ (una recta, ya que $A \neq B$ siempre).

**Ecuación de la recta:** con $z = x+yi$:

$$(x-(4+k))^2 + y^2 = (x-k)^2 + (y-3)^2$$

Expandiendo:

$$-2(4+k)x + (4+k)^2 = -2kx + k^2 - 6y + 9$$

$$-8x + 16 + 8k = -6y + 9 \quad\Longrightarrow\quad 8x - 6y = 7 + 8k$$

**Condición de solución única:** la recta debe ser tangente a la circunferencia, así que la distancia del centro $(25,20)$ a la recta debe ser $5$:

$$\frac{|8(25) - 6(20) - (7+8k)|}{\sqrt{8^2+6^2}} = \frac{|200 - 120 - 7 - 8k|}{10} = \frac{|73 - 8k|}{10} = 5$$

Entonces $|73 - 8k| = 50$, lo que da:

- $73 - 8k = 50 \Rightarrow k = \frac{23}{8}$
- $73 - 8k = -50 \Rightarrow k = \frac{123}{8}$

**Suma:** $\frac{23}{8} + \frac{123}{8} = \frac{146}{8} = \frac{73}{4}$, con $m=73$, $n=4$ coprimos.

$$m+n = \boxed{77}$$