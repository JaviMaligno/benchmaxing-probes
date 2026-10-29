## Planteamiento

Sea $(x, y)$ un punto de la gráfica, con $y = \tfrac{1}{2}x^2 - 9$. La distancia al origen cumple:

$$d^2 = x^2 + y^2 = x^2 + \left(\tfrac{1}{2}x^2 - 9\right)^2$$

## Sustitución

Tomando $u = x^2$ (con $u \ge 0$):

$$d^2 = u + \left(\tfrac{u}{2} - 9\right)^2 = u + \frac{u^2}{4} - 9u + 81 = \frac{u^2}{4} - 8u + 81$$

## Minimización

Es una parábola en $u$ con vértice en:

$$\frac{d}{du}\left(\frac{u^2}{4} - 8u + 81\right) = \frac{u}{2} - 8 = 0 \implies u = 16$$

Como $u = 16 \ge 0$, el valor es admisible (corresponde a $x = \pm 4$, $y = -1$).

## Valor mínimo

$$d^2 = \frac{256}{4} - 8(16) + 81 = 64 - 128 + 81 = 17$$

Por lo tanto $a = \sqrt{17}$ y $a^2 = 17$.

\boxed{17}