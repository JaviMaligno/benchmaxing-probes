## Resolución

Sea $w = e^{i\theta}$, con $c = \cos\theta \in [-1, 1]$.

**Primer término.** $|1+w| = \sqrt{(1+\cos\theta)^2 + \sin^2\theta} = \sqrt{2+2c}$.

**Segundo término.** Calculemos $|1 - w + w^2|^2$ con $w = e^{i\theta}$:

$$|1-w+w^2|^2 = (1-\cos\theta+\cos 2\theta)^2 + (\sin 2\theta - \sin\theta)^2.$$

Al expandir, los cuadrados suman $3$, y los productos cruzados dan $-2\cos\theta + 2\cos 2\theta - 2\cos(2\theta - \theta)$, de modo que:

$$|1-w+w^2|^2 = 3 - 4\cos\theta + 2\cos 2\theta = 3 - 4c + 2(2c^2 - 1) = (1-2c)^2.$$

Por lo tanto $|2 - 2w + 2w^2| = 2|1 - 2c|$.

**Optimización.** Hay que maximizar
$$f(c) = \sqrt{2+2c} + 2|1-2c|, \qquad c \in [-1, 1].$$

- **Caso $c \ge \tfrac12$:** $f(c) = \sqrt{2+2c} + 4c - 2$ es creciente; su máximo es $f(1) = 2 + 2 = 4$.
- **Caso $c \le \tfrac12$:** $f(c) = \sqrt{2+2c} + 2 - 4c$. Derivando: $f'(c) = \dfrac{1}{\sqrt{2+2c}} - 4 = 0 \Rightarrow \sqrt{2+2c} = \tfrac14 \Rightarrow c = -\tfrac{31}{32}$.

Como $f' > 0$ para $c < -\tfrac{31}{32}$ y $f' < 0$ después, ahí hay un máximo:

$$f\left(-\tfrac{31}{32}\right) = \sqrt{\tfrac{1}{16}} + 2 + \tfrac{31}{8} = \tfrac14 + 2 + \tfrac{31}{8} = \tfrac{2 + 16 + 31}{8} = \tfrac{49}{8}.$$

Comparando con los extremos ($f(-1) = 6$, $f(1) = 4$), el máximo global es $\tfrac{49}{8} = 6.125$.

$$\boxed{\dfrac{49}{8}}$$