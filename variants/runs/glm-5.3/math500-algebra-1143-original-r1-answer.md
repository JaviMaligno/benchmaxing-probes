# Solución paso a paso

**Paso 1: Plantear la distancia al cuadrado.**

Para un punto $(x, y)$ sobre la curva $y = \frac{1}{2}x^2 - 9$, la distancia al origen es:
$$d^2 = x^2 + y^2$$

**Paso 2: Sustituir la curva.**

$$d^2 = x^2 + \left(\frac{1}{2}x^2 - 9\right)^2$$

Hago la sustitución $u = x^2$ (con $u \geq 0$):

$$d^2 = u + \left(\frac{u}{2} - 9\right)^2 = u + \frac{u^2}{4} - 9u + 81 = \frac{u^2}{4} - 8u + 81$$

**Paso 3: Minimizar.**

Derivando respecto a $u$:

$$\frac{d(d^2)}{du} = \frac{u}{2} - 8 = 0 \quad\Longrightarrow\quad u = 16$$

(es un mínimo, pues la función es cuadrática con coeficiente positivo). Esto corresponde a $x = \pm 4$.

**Paso 4: Evaluar.**

En $u = 16$:
$$d^2 = \frac{(16)^2}{4} - 8(16) + 81 = 64 - 128 + 81 = 17$$

Verificación con el punto $(4, -1)$ (pues $y = \frac{1}{2}(16) - 9 = -1$): $d^2 = 4^2 + (-1)^2 = 16 + 1 = 17$. ✓

Por lo tanto, $a^2 = 17$.

$$\boxed{17}$$