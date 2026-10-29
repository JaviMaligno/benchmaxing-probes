Sea $z = e^{i\theta}$, de modo que $z + \bar z = 2\cos\theta =: 2c$ y $z\bar z = 1$.

**Paso 1: simplificar cada módulo.**

$$|1+z|^2 = (1+z)(1+\bar z) = 2 + 2c \quad\Rightarrow\quad |1+z| = \sqrt{2+2c}.$$

Para el segundo término, expandiendo $(1-z+z^2)(1-\bar z+\bar z^2)$ y usando $z^2+\bar z^2 = 4c^2-2$:

$$|1-z+z^2|^2 = 3 - 2(z+\bar z) + (z^2+\bar z^2) = 3 - 4c + 4c^2 - 2 = (2c-1)^2,$$

así que $|1-z+z^2| = |2c-1|$.

**Paso 2: optimizar.** Sea $u = \sqrt{2+2c}$, con $u \in [0,2]$ y $c = \frac{u^2-2}{2}$, de donde $2c-1 = u^2-3$. Queremos maximizar

$$f(u) = u + |u^2 - 3|.$$

- Si $u^2 \le 3$: $f(u) = 3 + u - u^2$, parábola con máximo en $u = \tfrac12$, que da $3 + \tfrac14 = \tfrac{13}{4}$.
- Si $u^2 \ge 3$: $f(u) = u^2 + u - 3$, creciente, con máximo en $u = 2$, que da $4 + 2 - 3 = 3 < \tfrac{13}{4}$.

El máximo se alcanza con $u = \tfrac12$, es decir $\cos\theta = -\tfrac78$, que es un valor válido.

$$\boxed{\dfrac{13}{4}}$$