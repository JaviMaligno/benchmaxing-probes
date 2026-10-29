Para hallar el grado del polinomio $q(x)$, podemos observar su estructura utilizando la fórmula de interpolación de Lagrange.

Cada uno de los tres sumandos que componen $q(x)$ es un polinomio de grado $2$ en $x$, por lo que el grado de $q(x)$ es a lo sumo $2$.

Evaluemos $q(x)$ en los tres números reales distintos $x = r$, $x = s$ y $x = t$:

1. Para $x = r$, el segundo y tercer término se anulan debido al factor $(x - r)$, y obtenemos:
   \[q(r) = \frac{(3r - 1)(r - s)(r - t)}{(r - s)(r - t)} + 0 + 0 = 3r - 1.\]

2. Para $x = s$, el primer y tercer término se anulan debido al factor $(x - s)$, y obtenemos:
   \[q(s) = 0 + \frac{(3s - 1)(s - r)(s - t)}{(s - r)(s - t)} + 0 = 3s - 1.\]

3. Para $x = t$, el primer y segundo término se anulan debido al factor $(x - t)$, y obtenemos:
   \[q(t) = 0 + 0 + \frac{(3t - 1)(t - r)(t - s)}{(t - r)(t - s)} = 3t - 1.\]

Consideremos ahora el polinomio lineal $p(x) = 3x - 1$. Vemos que $p(x)$ toma exactamente los mismos valores que $q(x)$ en $x = r, s, t$:
\[p(r) = 3r - 1 = q(r), \quad p(s) = 3s - 1 = q(s), \quad p(t) = 3t - 1 = q(t).\]

Definamos el polinomio diferencia $d(x) = q(x) - p(x)$. Como $q(x)$ tiene grado a lo sumo $2$ y $p(x)$ tiene grado $1$, $d(x)$ tiene grado a lo sumo $2$. Sin embargo, $d(x)$ tiene al menos tres raíces distintas ($r$, $s$ y $t$). El único polinomio de grado menor o igual a $2$ con tres raíces distintas es el polinomio idénticamente nulo, por lo que $d(x) = 0$ para todo $x$.

Por lo tanto,
\[q(x) = 3x - 1,\]
el cual es un polinomio de grado $1$.

\boxed{1}