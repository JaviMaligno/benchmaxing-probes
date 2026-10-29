## Razonamiento

El polinomio $p(x)$ es exactamente la interpolación de Lagrange sobre los nodos distintos $a$, $b$, $c$.

**Paso 1: evaluar en los nodos.**

En $x = a$: el primer término vale $\frac{(a-b)(a-c)}{(a-b)(a-c)} = 1$, y los otros dos contienen el factor $(x-a)$, que se anula. Luego $p(a) = 1$.

Por simetría, $p(b) = 1$ y $p(c) = 1$.

**Paso 2: comparar con el polinomio constante.**

Cada sumando es un polinomio de grado a lo más $2$, así que $\deg p \le 2$. Consideremos
$$q(x) = p(x) - 1,$$
que también tiene grado a lo más $2$. Pero $q(a) = q(b) = q(c) = 0$, es decir, $q$ tiene tres raíces distintas. Un polinomio no nulo de grado $\le 2$ tiene a lo más $2$ raíces, de modo que necesariamente $q \equiv 0$.

**Paso 3: conclusión.**

Por tanto $p(x) = 1$ para todo $x$, un polinomio constante no nulo, cuyo grado es $0$.

$$\boxed{0}$$