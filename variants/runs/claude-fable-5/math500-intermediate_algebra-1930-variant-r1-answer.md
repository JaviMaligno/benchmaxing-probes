## Resolución

**Paso 1: Simetría recíproca.** El polinomio es palindrómico, y $x=0$ no es raíz. Dividiendo entre $x^2$:

$$x^2 + \frac{1}{x^2} + 2p\left(x + \frac{1}{x}\right) - q = 0.$$

Con la sustitución $t = x + \tfrac1x$ (que satisface $x^2 + \tfrac1{x^2} = t^2 - 2$), la ecuación se convierte en

$$t^2 + 2pt - (q+2) = 0.$$

Una $x$ real existe si y solo si existe $t$ real con $|t| \ge 2$ (rango de $x + 1/x$ sobre los reales).

**Paso 2: Rango de $q$.** Despejando, $q = f(t) = t^2 + 2pt - 2$. El vértice de $f$ está en $t = -p \in [-1,0]$, es decir, dentro de $(-2,2)$. Por lo tanto:

- En $t \ge 2$: $f$ es creciente, con mínimo $f(2) = 2 + 4p$.
- En $t \le -2$: $f$ es decreciente hacia la izquierda, con mínimo $f(-2) = 2 - 4p$.

El conjunto de valores alcanzables es $[2-4p,\infty) \cup [2+4p,\infty) = [2-4p, \infty)$.

**Paso 3: Condición sobre $(p,q)$.** La ecuación tiene raíz real si y solo si

$$q \ge 2 - 4p, \qquad \text{es decir, } 4p + q \ge 2.$$

**Paso 4: Área dentro del cuadrado unitario.** La recta $q = 2 - 4p$ cruza el cuadrado en $(1/4, 1)$ y $(1/2, 0)$. La región excluida ($4p + q < 2$) consta de:

- Para $p \in [0, \tfrac14]$: toda la columna, área $\tfrac14$.
- Para $p \in [\tfrac14, \tfrac12]$: $\displaystyle\int_{1/4}^{1/2} (2-4p)\,dp = \left[2p - 2p^2\right]_{1/4}^{1/2} = \tfrac12 - \tfrac38 = \tfrac18$.

Área excluida: $\tfrac14 + \tfrac18 = \tfrac38$, de modo que

$$\text{Área}(T) = 1 - \frac38 = \frac58.$$

$$\boxed{\dfrac{5}{8}}$$