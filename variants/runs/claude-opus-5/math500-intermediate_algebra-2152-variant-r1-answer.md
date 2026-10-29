## Razonamiento

La expresión es exactamente la **interpolación de Lagrange** sobre los nodos distintos $r, s, t$ con valores $3r-1$, $3s-1$, $3t-1$.

**Paso 1.** Cada término es un polinomio de grado a lo sumo 2, así que $\deg q \le 2$.

**Paso 2.** Evaluando en los nodos: al poner $x = r$, el segundo y tercer término se anulan (contienen el factor $x-r$), y el primero vale
$$\frac{(3r-1)(r-s)(r-t)}{(r-s)(r-t)} = 3r-1.$$
Por simetría, $q(s) = 3s-1$ y $q(t) = 3t-1$.

**Paso 3.** Considérese $p(x) = 3x - 1$, que también cumple $p(r)=3r-1$, $p(s)=3s-1$, $p(t)=3t-1$. Entonces $q(x) - p(x)$ tiene grado $\le 2$ y posee tres raíces distintas $r, s, t$, por lo que es idénticamente nulo.

**Paso 4.** Así $q(x) = 3x - 1$, cuyo grado es 1 (el coeficiente $3 \ne 0$ garantiza que no degenera a constante).

\boxed{1}