**Planteamiento.** Sea $w = e^{i\theta}$. Usamos la factorización
$$1 + w^3 = (1+w)(1 - w + w^2),$$
de modo que
$$|2 - 2w + 2w^2| = 2|1 - w + w^2| = \frac{2|1+w^3|}{|1+w|}.$$

**Cambio de variable.** Sea $t = |1+w| = 2|\cos(\theta/2)| \in [0,2]$. Con $x = \cos(\theta/2)$, tenemos $t = 2|x|$ y, usando $\cos(3\alpha) = 4\cos^3\alpha - 3\cos\alpha$:
$$|1+w^3| = 2|\cos(3\theta/2)| = 2|x|\,|4x^2-3| = t\,|t^2-3|.$$

Entonces la expresión (con continuidad en $t=0$, donde $w=-1$ y vale $0+6$) queda como función de una variable:
$$f(t) = t + 2|t^2 - 3|, \qquad t \in [0,2].$$

**Caso 1: $t \in [0,\sqrt3]$.** Aquí $f(t) = t + 2(3-t^2) = 6 + t - 2t^2$. Es una parábola cóncava con vértice en $t = \tfrac14$, donde
$$f(1/4) = 6 + \frac14 - \frac18 = \frac{49}{8}.$$

**Caso 2: $t \in [\sqrt3, 2]$.** Aquí $f(t) = 2t^2 + t - 6$, que es creciente, con máximo $f(2) = 4$.

**Comparación.** $\frac{49}{8} > 6 > 4$, así que el máximo global es $\frac{49}{8}$, alcanzado cuando $|1+w| = \frac14$ (por ejemplo, $w = e^{i\theta}$ con $\cos(\theta/2) = \pm\frac18$).

$$\boxed{\dfrac{49}{8}}$$