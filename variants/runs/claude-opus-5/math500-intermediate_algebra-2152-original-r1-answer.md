## Razonamiento

El polinomio $p(x)$ es exactamente la interpolación de Lagrange sobre los nodos $a$, $b$, $c$.

**Grado a priori:** cada término es un producto de dos factores lineales dividido por una constante, así que $p(x)$ es, como máximo, de grado 2.

**Evaluación en los nodos:**

- En $x = a$: el primer término da $\frac{(a-b)(a-c)}{(a-b)(a-c)} = 1$, y los otros dos se anulan porque contienen el factor $(x-a)$. Luego $p(a) = 1$.
- En $x = b$: análogamente, solo sobrevive el segundo término, que vale $1$. Luego $p(b) = 1$.
- En $x = c$: solo sobrevive el tercero, que vale $1$. Luego $p(c) = 1$.

**Conclusión:** consideremos $q(x) = p(x) - 1$. Es un polinomio de grado a lo sumo 2 que tiene tres raíces distintas: $a$, $b$ y $c$ (son distintas por hipótesis). Un polinomio no nulo de grado $\le 2$ no puede tener tres raíces distintas, así que $q(x) \equiv 0$, es decir,
$$p(x) = 1 \quad \text{para todo } x.$$

El polinomio constante $1$ tiene grado $0$.

\boxed{0}