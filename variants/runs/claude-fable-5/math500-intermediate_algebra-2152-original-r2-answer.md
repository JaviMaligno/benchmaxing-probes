Este es un problema clásico de interpolación de Lagrange.

**Paso 1: Observar la estructura.** Cada término es a lo sumo de grado 2, así que p(x) es un polinomio de grado ≤ 2.

**Paso 2: Evaluar en puntos clave.**

- En x = a: el primer término vale $\frac{(a-b)(a-c)}{(a-b)(a-c)} = 1$, y los otros dos se anulan (contienen el factor $(x-a)$). Entonces p(a) = 1.
- En x = b: solo sobrevive el segundo término, que vale $\frac{(b-a)(b-c)}{(b-a)(b-c)} = 1$. Entonces p(b) = 1.
- En x = c: análogamente, p(c) = 1.

**Paso 3: Concluir.** El polinomio p(x) − 1 tiene grado ≤ 2 pero posee tres raíces distintas (a, b, c). Un polinomio no nulo de grado ≤ 2 no puede tener tres raíces, así que p(x) − 1 ≡ 0, es decir, p(x) = 1 para todo x.

Por lo tanto, p(x) es el polinomio constante 1, cuyo grado es

\[\boxed{0}\]