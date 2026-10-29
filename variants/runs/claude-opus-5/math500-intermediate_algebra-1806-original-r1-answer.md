## Planteamiento

Escribimos $z = e^{i\theta}$.

**Primer término:** $|1+z| = |e^{i\theta/2}|\cdot|e^{-i\theta/2}+e^{i\theta/2}| = 2|\cos(\theta/2)|$.

**Segundo término:** como $|z|=1$, podemos factorizar $z$:
$$|1 - z + z^2| = |z|\cdot\left|\tfrac{1}{z} - 1 + z\right| = |\bar z + z - 1| = |2\cos\theta - 1|.$$

## Reducción a una variable

Sea $t = |\cos(\theta/2)| \in [0,1]$. Entonces $\cos\theta = 2t^2 - 1$, y
$$2\cos\theta - 1 = 4t^2 - 3.$$

Hay que maximizar
$$f(t) = 2t + |4t^2 - 3|, \qquad t\in[0,1].$$

**Caso 1: $4t^2 \le 3$**, es decir $t \le \frac{\sqrt3}{2}$.
$$f(t) = 2t + 3 - 4t^2 = -4\left(t - \tfrac14\right)^2 + \tfrac{13}{4}.$$
El máximo se alcanza en $t = \frac14$ (que cumple $\frac14 \le \frac{\sqrt3}{2}$), dando $f = \frac{13}{4}$.

**Caso 2: $4t^2 > 3$.**
$$f(t) = 2t + 4t^2 - 3,$$
creciente en $t$, así que el máximo está en $t=1$: $f(1) = 2 + 4 - 3 = 3 < \frac{13}{4}$.

## Verificación de que el valor se alcanza

Con $t = \frac14$ basta tomar $\cos(\theta/2) = \frac14$, de donde $\cos\theta = 2\cdot\frac{1}{16}-1 = -\frac78$. Ese valor es admisible, y entonces
$$|1+z| = \tfrac12, \qquad |1-z+z^2| = \left|-\tfrac74 - 1\right| = \tfrac{11}{4},$$
cuya suma es $\frac12 + \frac{11}{4} = \frac{13}{4}$.

\boxed{\dfrac{13}{4}}