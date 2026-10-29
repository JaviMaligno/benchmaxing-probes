## Planteamiento

Sea $w = e^{i\theta}$ con $|w|=1$.

**Primer término:** $|1+w| = \sqrt{(1+\cos\theta)^2 + \sin^2\theta} = \sqrt{2+2\cos\theta}$.

**Segundo término:** factorizamos aprovechando $|w|=1$:
$$1 - w + w^2 = w\left(w + \tfrac{1}{w} - 1\right) = w(2\cos\theta - 1),$$
puesto que $\frac{1}{w} = \bar w$ y $w + \bar w = 2\cos\theta$. Como $|w|=1$:
$$|2 - 2w + 2w^2| = 2|2\cos\theta - 1|.$$

## Optimización

Con $x = \cos\theta \in [-1,1]$, hay que maximizar
$$f(x) = \sqrt{2+2x} + 2|2x-1|.$$

**Caso $x \ge 1/2$:** $f(x) = \sqrt{2+2x} + 4x - 2$ es creciente, así que el máximo está en $x=1$: $f(1) = 2 + 2 = 4$.

**Caso $x < 1/2$:** $f(x) = \sqrt{2+2x} + 2 - 4x$, con
$$f'(x) = \frac{1}{\sqrt{2+2x}} - 4 = 0 \iff \sqrt{2+2x} = \tfrac14 \iff x = -\tfrac{31}{32}.$$
Ahí $f' $ pasa de positiva a negativa, luego ese punto es un **mínimo local** y los candidatos son los extremos del intervalo:
$$f(-1) = 0 + 6 = 6, \qquad f(1/2) = \sqrt{3} \approx 1.73.$$

## Conclusión

El máximo es $6$, alcanzado en $x = -1$, es decir $w = -1$. Verificación directa:
$$|1 + (-1)| + |2 + 2 + 2| = 0 + 6 = 6.$$

$$\boxed{6}$$