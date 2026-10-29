## Planteamiento

Si $g$ alcanza su valor mínimo $m$ en exactamente dos puntos positivos $x_1, x_2$, entonces $g(x) - m \ge 0$ para todo $x > 0$ con igualdad solo en esos dos puntos. Como

$$g(x) - m = \frac{(x-8)(x-50)(x-72)(x-k) - mx}{x},$$

el polinomio de grado 4 del numerador debe tener raíces dobles en $x_1$ y $x_2$:

$$(x-8)(x-50)(x-72)(x-k) - mx = (x^2 - px + q)^2,\qquad p = x_1+x_2,\ q = x_1x_2.$$

## Igualando coeficientes

Con $a+b+c = 130$, $ab+ac+bc = 4576$, $abc = 28800$ (para $a,b,c = 8,50,72$):

- **Coeficiente de $x^3$:** $2p = 130 + k$
- **Término constante:** $q^2 = 28800\,k \Rightarrow q = \sqrt{28800k}$
- **Coeficiente de $x^2$:** $p^2 + 2q = 4576 + 130k$

(El coeficiente de $x$ solo determina $m$, no impone restricción.)

Sustituyendo $p$ y $q$ en la tercera ecuación y multiplicando por 4:

$$k^2 + 260k + 16900 + 8\sqrt{28800k} = 18304 + 520k$$
$$k^2 - 260k - 1404 = -960\sqrt{2k}.$$

## Resolviendo

Con la sustitución $k = 2v^2$ (con $v > 0$) la ecuación se vuelve polinómica:

$$4v^4 - 520v^2 + 1920v - 1404 = 0 \quad\Longrightarrow\quad v^4 - 130v^2 + 480v - 351 = 0.$$

Factorizando (se verifican las raíces $v=3$ y $v=1$):

$$(v-1)(v-3)(v^2 + 4v - 117) = 0 \quad\Longrightarrow\quad v \in \{1,\ 3,\ 9,\ -13\}.$$

Descartando $v = -13$, quedan $v = 1, 3, 9$, es decir:

$$k = 2v^2 \in \{2,\ 18,\ 162\}.$$

**Verificación:** en los tres casos $q = \sqrt{28800k}$ es entero ($240, 720, 2160$), se cumple $p^2 > 4q$ (raíces $x_1 \ne x_2$ reales y positivas), y $m = 2pq - S_3 < 0$, de modo que el mínimo se alcanza exactamente en dos puntos positivos. Por ejemplo, con $k=18$: $p = 74$, $q = 720$, y $p^2 + 2q = 6916 = 4576 + 130\cdot 18$ ✓.

La suma pedida es $2 + 18 + 162 = 182$.

$$\boxed{182}$$