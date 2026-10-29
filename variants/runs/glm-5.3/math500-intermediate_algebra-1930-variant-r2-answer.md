## Solución

**Paso 1: Explotar la simetría del polinomio.**

Los coeficientes son palindrómicos: $1,\ 2p,\ -q,\ 2p,\ 1$. Como el término constante es $1$, nunca $x=0$; dividiendo entre $x^2$:

$$x^2 + 2px - q + \frac{2p}{x} + \frac{1}{x^2} = 0.$$

**Paso 2: Sustitución $t = x + \frac1x$.**

Con $t = x + \frac1x$ tenemos $x^2 + \frac{1}{x^2} = t^2 - 2$, y una raíz real $x$ existe si y solo si existe $t$ real con $|t| \ge 2$ que satisfaga

$$t^2 + 2pt - (q+2) = 0. \tag{$\ast$}$$

**Paso 3: Analizar las dos ramas de $t$.**

Sea $g(t) = t^2 + 2pt$ (parábola con vértice en $t=-p \in [-1,0]$).

- **Rama $t \ge 2$:** $g$ es creciente ahí, con mínimo $g(2) = 4 + 4p \ge 4$. Pero $q \le 1 \Rightarrow q + 2 \le 3 < 4$. Nunca hay solución en esta rama.

- **Rama $t \le -2$:** $g'(t) = 2(t+p) \le -2 < 0$, así que $g$ es decreciente, con mínimo $g(-2) = 4 - 4p$ y $g \to +\infty$ cuando $t \to -\infty$. Su recorrido es $[4-4p, \infty)$.

Por lo tanto, $(\ast)$ tiene solución con $t \le -2$ si y solo si

$$q + 2 \ge 4 - 4p \iff q \ge 2 - 4p.$$

(Esto corresponde exactamente a que $x=-1$ sea raíz: $P(-1) = 2 - 4p - q$, la frontera de la región.)

**Paso 4: Describir $T$ y calcular su área.**

$$T = \{(p,q) \in [0,1]^2 : q \ge 2 - 4p\}.$$

La recta $q = 2 - 4p$ corta $q = 1$ en $p = \tfrac14$ y corta $q = 0$ en $p = \tfrac12$. Entonces:

- Para $p \in [\tfrac12, 1]$: todo $q \in [0,1]$ cumple la condición $\Rightarrow$ área $= \tfrac12$.
- Para $p \in [\tfrac14, \tfrac12]$: altura $1 - (2-4p) = 4p - 1$:
$$\int_{1/4}^{1/2} (4p - 1)\, dp = \left[2p^2 - p\right]_{1/4}^{1/2} = 0 - \left(-\tfrac18\right) = \tfrac18.$$

**Verificación:** con $p = \tfrac12$, $q = 0$ (punto frontera): $x^4 + x^3 + x + 1 = (x+1)(x^3+1)$, que tiene raíz $x = -1$ ✓. Con $p=0$, $q=1$: $x^4 - x^2 + 1 = 0$ no tiene raíces reales, y en efecto $1 < 2 - 0$ ✓.

Área total: $\tfrac12 + \tfrac18 = \tfrac58$.

$$\boxed{\dfrac{5}{8}}$$