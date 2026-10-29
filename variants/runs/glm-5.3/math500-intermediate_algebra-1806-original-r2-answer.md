## Razonamiento

**Paso 1: Parametrizar.** Como $|z|=1$, escribimos $z = e^{i\theta}$ y sea $c = \cos\theta \in [-1,1]$.

**Paso 2: Simplificar cada término.**

Primer término:
$$|1+z|^2 = (1+\cos\theta)^2 + \operatorname{sen}^2\theta = 2 + 2\cos\theta \implies |1+z| = \sqrt{2+2c}.$$

Segundo término: usando $|z|=1$ y que $z^{-1} = \bar z$,
$$z^2 - z + 1 = z\left(z + z^{-1} - 1\right) = z\,(2\cos\theta - 1),$$
ya que $z + z^{-1} = 2\cos\theta$. Entonces
$$|1 - z + z^2| = |z|\,|2\cos\theta - 1| = |2c-1|.$$

**Paso 3: Maximizar.** La expresión es $F(c) = \sqrt{2+2c} + |2c-1|$, con $c \in [-1,1]$.

*Casos $c \ge \tfrac12$:* $F(c) = \sqrt{2+2c} + 2c - 1$, con derivada $\frac{1}{\sqrt{2+2c}} + 2 > 0$; es creciente, y $F(1) = 2 + 1 = 3$.

*Casos $c \le \tfrac12$:* $F(c) = \sqrt{2+2c} + 1 - 2c$. La derivada $\frac{1}{\sqrt{2+2c}} - 2$ se anula cuando $\sqrt{2+2c} = \tfrac12$, es decir, $c = -\tfrac78$.

En ese punto:
$$F\!\left(-\tfrac78\right) = \sqrt{\tfrac14} + 1 + \tfrac74 = \tfrac12 + 1 + \tfrac74 = \tfrac{13}{4}.$$

En los extremos: $F(-1) = 0 + 3 = 3$ y $F(\tfrac12) = \sqrt3$, ambos menores que $\tfrac{13}{4}$.

**Paso 4: Conclusión.** El máximo es $\tfrac{13}{4}$, alcanzado por ejemplo en $z = e^{i\theta}$ con $\cos\theta = -\tfrac78$ (verificación: $|1+z| = \tfrac12$ y $|1-z+z^2| = \tfrac{11}{4}$).

$$\boxed{\dfrac{13}{4}}$$