Este es un problema clásico de interpolación de Lagrange.

**Paso 1: Acotar el grado.** Cada uno de los tres sumandos es un polinomio cuadrático, así que $p(x)$ tiene grado a lo sumo 2.

**Paso 2: Evaluar en los puntos clave.**

- En $x = a$: el primer término vale $\frac{(a-b)(a-c)}{(a-b)(a-c)} = 1$, y los otros dos se anulan (contienen el factor $x - a$). Así, $p(a) = 1$.
- Por simetría, $p(b) = 1$ y $p(c) = 1$.

**Paso 3: Concluir.** El polinomio $q(x) = p(x) - 1$ tiene grado a lo sumo 2, pero se anula en tres puntos distintos $a, b, c$. Un polinomio no nulo de grado $\le 2$ tiene a lo sumo 2 raíces, de modo que $q(x) \equiv 0$, es decir, $p(x) = 1$ para todo $x$.

Como $p(x)$ es la constante 1, su grado es

$$\boxed{0}$$