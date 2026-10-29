## Resolución

Sean $r$ y $s$ las raíces de la ecuación (posiblemente iguales). La condición exige que la aplicación $c \mapsto c^2 - 2$ envíe cada raíz al conjunto de raíces $\{r, s\}$. Analizo los casos posibles.

**Caso 1: ambas raíces son fijas**, es decir $r^2 - 2 = r$ y $s^2 - 2 = s$.

La ecuación $t^2 - t - 2 = 0$ tiene soluciones $t = 2$ y $t = -1$. Las elecciones posibles de $\{r, s\}$ son:
- $\{2, 2\}$: $x^2 - 4x + 4 = 0$
- $\{-1, -1\}$: $x^2 + 2x + 1 = 0$
- $\{2, -1\}$: $x^2 - x - 2 = 0$

Esto da **3 ecuaciones**.

**Caso 2: las raíces se intercambian**, es decir $r^2 - 2 = s$ y $s^2 - 2 = r$ con $r \neq s$.

Restando: $r^2 - s^2 = s - r$, o sea $(r-s)(r+s) = -(r-s)$, de donde $r + s = -1$. Sustituyendo $s = -1 - r$ en $r^2 - 2 = s$ se obtiene $r^2 + r - 1 = 0$, cuyas dos raíces $\frac{-1 \pm \sqrt{5}}{2}$ son precisamente $r$ y $s$. Esto da la ecuación $x^2 + x - 1 = 0$: **1 ecuación**.

**Caso 3: una raíz es fija y la otra se envía a ella**, es decir $r^2 - 2 = r$ (así $r \in \{2, -1\}$) y $s^2 - 2 = r$ con $s \neq r$.

- Si $r = 2$: $s^2 = 4 \Rightarrow s = -2$. Verificación: $(-2)^2 - 2 = 2$ ✓ y $2$ es fijo ✓. Raíces $\{2, -2\}$: $x^2 - 4 = 0$.
- Si $r = -1$: $s^2 = 1 \Rightarrow s = 1$. Verificación: $1^2 - 2 = -1$ ✓ y $(-1)^2 - 2 = -1$ ✓. Raíces $\{1, -1\}$: $x^2 - 1 = 0$.

Esto da **2 ecuaciones** más (el caso simétrico, con $s$ fija, produce los mismos conjuntos de raíces).

**Total:** las seis ecuaciones $x^2 - 4x + 4$, $x^2 + 2x + 1$, $x^2 - x - 2$, $x^2 + x - 1$, $x^2 - 4$ y $x^2 - 1$ son todas distintas, y los casos agotan todas las formas en que $c \mapsto c^2 - 2$ puede actuar sobre el conjunto de raíces.

$$\boxed{6}$$