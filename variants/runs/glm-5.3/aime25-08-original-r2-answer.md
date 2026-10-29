## Razonamiento

Escribo $z = x + yi$.

**Primera ecuación:** $\ |z - (25+20i)| = 5$ es la circunferencia de centro $(25, 20)$ y radio $5$.

**Segunda ecuación:** $\ |z - 4 - k| = |z - 3i - k|$ dice que $z$ equidista de los puntos $A = (k+4,\, 0)$ y $B = (k,\, 3)$, es decir, $z$ está en la mediatriz del segmento $AB$.

Calculo la mediatriz con $z = x+yi$:
$$(x - k - 4)^2 + y^2 = (x - k)^2 + (y-3)^2$$
$$-8x + k^2 + 8k + 16 + k^2 \cdot 0 = k^2 - 6y + 9 + \dots$$
Simplificando: $\ -8x + 6y + 8k + 7 = 0$, es decir, la recta
$$8x - 6y = 8k + 7.$$

Esta familia de rectas (pendiente $4/3$) se desliza al variar $k$; su normal unitaria es $\tfrac{(8,-6)}{10}$.

**Condición de solución única:** una recta y una circunferencia se cortan en exactamente un punto solo si son **tangentes**, es decir, si la distancia del centro $(25,20)$ a la recta es $5$:
$$\frac{|8(25) - 6(20) - (8k+7)|}{\sqrt{8^2+6^2}} = 5 \quad\Longrightarrow\quad \frac{|200 - 120 - 8k - 7|}{10} = 5$$
$$|73 - 8k| = 50 \quad\Longrightarrow\quad k = \frac{23}{8} \ \text{ o } \ k = \frac{123}{8}.$$

**Verificación rápida:**
- $k = 23/8$: recta $x - 6y = 30 \to 4x - 3y = 15$; distancia de $(25,20)$: $\frac{|100 - 60 - 15|}{5} = 5$. ✓
- $k = 123/8$: recta $4x - 3y = 65$; distancia: $\frac{|100 - 60 - 65|}{5} = 5$. ✓

**Suma de valores:** $\ \frac{23}{8} + \frac{123}{8} = \frac{146}{8} = \frac{73}{4}$, con $\gcd(73,4)=1$, así que $m = 73$, $n = 4$.

$$m + n = 77$$

\boxed{77}