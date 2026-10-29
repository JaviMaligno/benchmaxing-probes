## Razonamiento

La expresión es exactamente la **interpolación de Lagrange** sobre los nodos $r, s, t$, con valores $3r-1$, $3s-1$, $3t-1$.

Es decir, $q$ interpola la función $f(x) = 3x - 1$ en esos tres puntos distintos:
- $q(r) = 3r - 1$ (los otros dos términos se anulan en $x=r$),
- $q(s) = 3s - 1$,
- $q(t) = 3t - 1$.

Cada sumando tiene grado a lo sumo 2, así que $\deg q \le 2$.

Consideremos $p(x) = q(x) - (3x - 1)$. Entonces $p$ tiene grado a lo sumo 2 y se anula en los tres valores distintos $r, s, t$. Un polinomio no nulo de grado $\le 2$ no puede tener tres raíces distintas, por lo tanto $p \equiv 0$.

Luego
$$q(x) = 3x - 1,$$
que es un polinomio de grado 1 (el coeficiente $3 \neq 0$, independientemente de $r, s, t$).

$\boxed{1}$