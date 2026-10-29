# Resolución

**Paso 1: Plantear la función a minimizar.**

La distancia al origen de un punto $(x, y)$ es $\sqrt{x^2+y^2}$, así que basta minimizar la distancia al cuadrado, con $y=\frac{1}{\sqrt{2}}(x^2-3)$:

$$D^2 = x^2 + \frac{1}{2}(x^2-3)^2$$

**Paso 2: Sustituir $t = x^2$ (con $t \ge 0$).**

$$f(t) = t + \frac{1}{2}(t-3)^2 = t + \frac{t^2 - 6t + 9}{2} = \frac{t^2 - 4t + 9}{2}$$

**Paso 3: Minimizar la función cuadrática en $t$.**

$$f'(t) = \frac{2t-4}{2} = t - 2$$

El mínimo está en $t = 2$ (válido, pues $t \ge 0$), y el vértice de la parábola confirma que es mínimo.

**Paso 4: Evaluar.**

$$f(2) = \frac{4 - 8 + 9}{2} = \frac{5}{2}$$

Por lo tanto, la distancia mínima es:

$$D = \sqrt{\frac{5}{2}} = \frac{\sqrt{5}}{\sqrt{2}} = \frac{\sqrt{10}}{2}$$

**Paso 5: Identificar $a$ y $b$.**

Con $a = 10$ (libre de cuadrados, pues $10 = 2 \cdot 5$) y $b = 2$:

$$a + b = 10 + 2 = 12$$

$\boxed{12}$