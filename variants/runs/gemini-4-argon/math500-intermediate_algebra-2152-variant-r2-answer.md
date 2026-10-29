Para hallar el grado del polinomio $q(x)$, analicemos sus valores en los puntos distintos $x = r$, $x = s$ y $x = t$:

1. Evaluando en $x = r$:
   \[q(r) = \frac{(3r - 1)(r - s)(r - t)}{(r - s)(r - t)} + 0 + 0 = 3r - 1.\]

2. Evaluando en $x = s$:
   \[q(s) = 0 + \frac{(3s - 1)(s - r)(s - t)}{(s - r)(s - t)} + 0 = 3s - 1.\]

3. Evaluando en $x = t$:
   \[q(t) = 0 + 0 + \frac{(3t - 1)(t - r)(t - s)}{(t - r)(t - s)} = 3t - 1.\]

Observamos que $q(x)$ es la suma de tres polinomios de grado a lo sumo $2$, por lo que el grado de $q(x)$ es como máximo $2$.

Definamos ahora el polinomio auxiliar $P(x) = q(x) - (3x - 1)$. Como tanto $q(x)$ como $3x - 1$ tienen grado a lo sumo $2$, el grado de $P(x)$ también es a lo sumo $2$. Sin embargo, al evaluar $P(x)$ en $r, s$ y $t$, obtenemos:
\[P(r) = P(s) = P(t) = 0.\]

Dado que $r, s$ y $t$ son números reales distintos, $P(x)$ tiene al menos tres raíces distintas. El único polinomio de grado menor o igual a $2$ con tres raíces distintas es el polinomio idénticamente nulo, es decir, $P(x) = 0$ para todo $x$.

Por lo tanto:
\[q(x) = 3x - 1.\]

El polinomio $q(x) = 3x - 1$ es lineal con coeficiente principal distinto de cero ($3 \neq 0$), por lo que su grado es $1$.

\boxed{1}