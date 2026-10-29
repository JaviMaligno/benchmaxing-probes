Para que la gráfica de $y = g(x)$ interseque a cada recta horizontal al menos una vez, el rango (o imagen) de la función $g(x)$ debe ser todo el conjunto de los números reales, $\mathbb{R} = (-\infty, \infty)$.

Analicemos el rango de $g(x)$ según el signo de $b$:

1. **Caso $b = 0$:**
   Si $b = 0$, entonces $g(x) = 0$ para todo $x \in \mathbb{R}$. Su rango es $\{0\}$, por lo que no cumple la condición.

2. **Caso $b > 0$:**
   - Para $x < b$, la función $g(x) = bx + 6b$ es lineal y estrictamente creciente (ya que $b > 0$). Por lo tanto, su rango en el intervalo $(-\infty, b)$ es $(-\infty, b^2 + 6b)$.
   - Para $x \geq b$, como $b > 0$, la función $g(x) = bx^2$ es estrictamente creciente en $[b, \infty)$. Su rango en este intervalo es $[b^3, \infty)$.

   Para que la unión de ambos rangos, $(-\infty, b^2 + 6b) \cup [b^3, \infty)$, cubra todo $\mathbb{R}$, es necesario y suficiente que:
   \[ b^3 \leq b^2 + 6b \]
   Como $b > 0$, podemos dividir ambos lados de la desigualdad entre $b$:
   \[ b^2 \leq b + 6 \implies b^2 - b - 6 \leq 0 \implies (b - 3)(b + 2) \leq 0 \]
   Considerando que $b > 0$, esto nos da el intervalo $0 < b \leq 3$.

3. **Caso $b < 0$:**
   Cualquier valor en este caso es menor que los valores positivos obtenidos en el caso anterior (en particular, menor que $3$).

Por lo tanto, el mayor valor posible de $b$ es $3$.

\boxed{3}