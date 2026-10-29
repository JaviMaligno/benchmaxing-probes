# Solución

**Paso 1: Evaluar $q(x)$ en los nodos $r$, $s$, $t$.**

En $x = r$, los factores $(x - r)$ hacen que el segundo y el tercer término se anulen. El primer término queda:

$$q(r) = \frac{(3r-1)(r-s)(r-t)}{(r-s)(r-t)} = 3r - 1.$$

Análogamente:

$$q(s) = 3s - 1, \qquad q(t) = 3t - 1.$$

**Paso 2: Reconocer la interpolación de Lagrange.**

La estructura de $q(x)$ es exactamente la de la forma de interpolación de Lagrange para los puntos $(r, 3r-1)$, $(s, 3s-1)$, $(t, 3t-1)$. Como $r, s, t$ son distintos, los denominadores no se anulan, y $q$ es el único polinomio de grado a lo más $2$ que pasa por esos tres puntos.

**Paso 3: Identificar el polinomio interpolador.**

El polinomio lineal $p(x) = 3x - 1$ satisface $p(r) = 3r - 1$, $p(s) = 3s - 1$, $p(t) = 3t - 1$; es decir, coincide con $q$ en los tres nodos. Por la unicidad de la interpolación (tres puntos distintos determinan un único polinomio de grado $\le 2$), se concluye que

$$q(x) = 3x - 1$$

idénticamente. Su coeficiente principal es $3 \neq 0$, así que el grado de $q$ es $1$.

\boxed{1}