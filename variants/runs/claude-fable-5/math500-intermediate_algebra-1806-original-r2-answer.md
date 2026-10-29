Sea $z = e^{i\theta}$. Calculo cada término:

**Primer término:** $|1+z| = |e^{i\theta/2}||e^{-i\theta/2} + e^{i\theta/2}| = 2|\cos(\theta/2)|$.

**Segundo término:** como $|z|=1$, multiplico por $|\bar z| = 1$:
$$|1 - z + z^2| = |\bar z - 1 + z| = |2\cos\theta - 1|.$$

Sea $c = |\cos(\theta/2)| \in [0,1]$. Usando $\cos\theta = 2\cos^2(\theta/2) - 1$, tenemos $2\cos\theta - 1 = 4c^2 - 3$. Entonces hay que maximizar:
$$g(c) = 2c + |4c^2 - 3|, \quad c \in [0,1].$$

**Caso 1:** $4c^2 \ge 3$, es decir $c \ge \tfrac{\sqrt3}{2}$. Entonces $g(c) = 4c^2 + 2c - 3$, creciente, con máximo en $c=1$: $g(1) = 4 + 2 - 3 = 3$.

**Caso 2:** $c < \tfrac{\sqrt3}{2}$. Entonces $g(c) = 3 + 2c - 4c^2$, parábola con vértice en $c = \tfrac14$:
$$g\!\left(\tfrac14\right) = 3 + \tfrac12 - \tfrac14 = \tfrac{13}{4}.$$

Como $\tfrac{13}{4} > 3$, el máximo es $\tfrac{13}{4}$, alcanzado cuando $\cos(\theta/2) = \tfrac14$ (ese valor de $\theta$ existe, así que el máximo se alcanza).

$$\boxed{\dfrac{13}{4}}$$