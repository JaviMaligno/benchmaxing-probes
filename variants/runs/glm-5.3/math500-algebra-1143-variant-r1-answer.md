# Solución paso a paso

**Planteamiento.** Buscamos el punto $(x, y)$ de la parábola $y = \frac{1}{4}x^2 - 6$ que minimiza la distancia al origen. Como la distancia es $\sqrt{x^2 + y^2}$, es equivalente minimizar el cuadrado de la distancia:

$$f(x) = x^2 + y^2 = x^2 + \left(\frac{x^2}{4} - 6\right)^2$$

**Derivada y puntos críticos.** Derivamos respecto a $x$:

$$f'(x) = 2x + 2\left(\frac{x^2}{4} - 6\right)\cdot\frac{x}{2} = 2x + x\left(\frac{x^2}{4} - 6\right) = x\left(\frac{x^2}{4} - 4\right)$$

Igualando a cero: $x = 0$ o $x^2 = 16$, es decir, $x = \pm 4$.

**Evaluación de los candidatos.**

- En $x = 0$: $y = -6$, entonces $f(0) = 0 + 36 = 36$.
- En $x = \pm 4$: $y = \frac{16}{4} - 6 = -2$, entonces $f(\pm 4) = 16 + 4 = 20$.

**Verificación de que es mínimo.** Con $f''(x) = \frac{3x^2}{4} - 4$, tenemos $f''(\pm 4) = 8 > 0$, así que $x = \pm 4$ son mínimos locales. Como $f(x) \to \infty$ cuando $|x| \to \infty$, el valor $f = 20$ es el mínimo global.

Por lo tanto, $b^2 = 20$.

$$\boxed{20}$$