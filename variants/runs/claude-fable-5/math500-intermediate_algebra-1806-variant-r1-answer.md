Voy a resolver este problema de optimización en el círculo unitario.

**Planteamiento.** Sea $w = e^{i\theta}$. Entonces:
- $|1 + w| = 2\left|\cos\frac{\theta}{2}\right|$.
- Para el segundo término, factorizo $w$: $1 - w + w^2 = w\left(w + \frac{1}{w} - 1\right) = w(2\cos\theta - 1)$, de modo que $|2 - 2w + 2w^2| = 2|2\cos\theta - 1|$.

**Reducción a una variable.** Sea $t = \left|\cos\frac{\theta}{2}\right| \in [0,1]$. Como $\cos\theta = 2\cos^2\frac{\theta}{2} - 1 = 2t^2 - 1$, se tiene $2\cos\theta - 1 = 4t^2 - 3$. La expresión queda:
$$f(t) = 2t + 2\,|4t^2 - 3|.$$

**Caso 1: $t^2 \le \frac{3}{4}$.** Entonces $f(t) = 2t + 6 - 8t^2$, parábola con máximo en $f'(t) = 2 - 16t = 0$, es decir $t = \frac{1}{8}$ (válido, pues $\frac{1}{64} < \frac34$):
$$f\left(\tfrac{1}{8}\right) = \tfrac{1}{4} + 6 - \tfrac{1}{8} = \tfrac{49}{8}.$$

**Caso 2: $t^2 \ge \frac{3}{4}$.** Entonces $f(t) = 2t + 8t^2 - 6$, creciente en $[\frac{\sqrt3}{2}, 1]$, con máximo en $t = 1$: $f(1) = 2 + 8 - 6 = 4 < \frac{49}{8}$.

El máximo global es $\frac{49}{8}$, alcanzado cuando $\cos\frac{\theta}{2} = \frac18$ (tal $\theta$ existe).

$$\boxed{\dfrac{49}{8}}$$