## Planteamiento

Escribo $w = e^{i\theta}$ y simplifico cada término.

**Primer término:**
$$|1+w| = |e^{i\theta/2}|\cdot|e^{-i\theta/2} + e^{i\theta/2}| = 2|\cos(\theta/2)|$$

**Segundo término:** factorizo $w$ (válido porque $|w|=1$):
$$|2 - 2w + 2w^2| = 2|w|\left|\frac{1}{w} - 1 + w\right| = 2\,|2\cos\theta - 1|$$

usando que $w + \tfrac1w = 2\cos\theta$.

## Reducción a una variable

Tomo $\theta \in [-\pi, \pi]$, de modo que $c = \cos(\theta/2) \in [0,1]$ y $\cos\theta = 2c^2 - 1$. Entonces $2\cos\theta - 1 = 4c^2 - 3$, y la expresión queda:
$$f(c) = 2c + 2\,|4c^2 - 3|, \qquad c \in [0,1]$$

**Caso 1: $4c^2 \ge 3$**, es decir $c \in [\tfrac{\sqrt3}{2}, 1]$.
$$f(c) = 8c^2 + 2c - 6$$
Es creciente en ese intervalo, con máximo en $c=1$: $f(1) = 4$.

**Caso 2: $4c^2 < 3$**, es decir $c \in [0, \tfrac{\sqrt3}{2})$.
$$f(c) = -8c^2 + 2c + 6$$
Parábola cóncava con vértice en $c = \tfrac{2}{16} = \tfrac18$, que sí está en el intervalo:
$$f\!\left(\tfrac18\right) = -8\cdot\tfrac{1}{64} + \tfrac14 + 6 = -\tfrac18 + \tfrac14 + 6 = \tfrac{49}{8}$$

## Conclusión

El máximo global es $\tfrac{49}{8} = 6.125 > 4$, alcanzado cuando $\cos(\theta/2) = \tfrac18$, o sea $\cos\theta = 2\cdot\tfrac{1}{64} - 1 = -\tfrac{31}{32}$.

$$\boxed{\dfrac{49}{8}}$$