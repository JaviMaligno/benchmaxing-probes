Para que exista un triángulo con lados $1$, $x$ e $y$, se deben cumplir las tres desigualdades triangulares:

$$x + y > 1, \qquad x + 1 > y, \qquad y + 1 > x$$

**Espacio muestral:** $(x,y)$ se elige uniformemente en el cuadrado $(0,3)\times(0,3)$, que tiene área $3 \cdot 3 = 9$.

**Regiones desfavorables** (donde falla alguna desigualdad):

1. **$x + y \le 1$:** es el triángulo de vértices $(0,0)$, $(1,0)$, $(0,1)$, con área
$$\frac{1}{2}\cdot 1 \cdot 1 = \frac{1}{2}.$$

2. **$y \ge x + 1$:** dentro del cuadrado es el triángulo de vértices $(0,1)$, $(0,3)$, $(2,3)$, con área
$$\frac{1}{2}\cdot 2 \cdot 2 = 2.$$

3. **$x \ge y + 1$:** por simetría con la anterior, también tiene área $2$.

Estas tres regiones no se superponen entre sí (solo se tocan, a lo sumo, en puntos o segmentos de área cero), de modo que el área desfavorable total es

$$\frac{1}{2} + 2 + 2 = \frac{9}{2}.$$

Por tanto, el área favorable es

$$9 - \frac{9}{2} = \frac{9}{2},$$

y la probabilidad pedida es

$$\frac{9/2}{9} = \frac{1}{2}.$$

$$\boxed{\dfrac{1}{2}}$$