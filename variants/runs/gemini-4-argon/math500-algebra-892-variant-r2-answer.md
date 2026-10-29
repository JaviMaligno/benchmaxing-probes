Para que la gráfica de $y = g(x)$ interseque a toda recta horizontal al menos una vez, el recorrido (imagen) de la función $g(x)$ debe ser todo el conjunto de los números reales, $\mathbb{R}$.

Analicemos los casos según el signo de $b$:

1. **Si $b = 0$:**
   La función es $g(x) = 0$ para todo $x \in \mathbb{R}$, cuyo recorrido es únicamente $\{0\} \neq \mathbb{R}$.

2. **Si $b > 0$:**
   - Para el tramo $x < b$: Como $b > 0$, la función lineal $g(x) = bx + 6b$ es estrictamente creciente. Por lo tanto, cuando $x$ toma valores en $(-\infty, b)$, el recorrido de este tramo es el intervalo abierto $(-\infty, b^2 + 6b)$.
   - Para el tramo $x \geq b$: Como $x \geq b > 0$ y $b > 0$, la función cuadrática $g(x) = bx^2$ es estrictamente creciente en $[b, \infty)$. Por lo tanto, el recorrido de este tramo es el intervalo cerrado $[b^3, \infty)$.

   Para que la unión de ambos intervalos, $(-\infty, b^2 + 6b) \cup [b^3, \infty)$, cubra todo $\mathbb{R}$ sin dejar ningún hueco, es necesario y suficiente que:
   \[ b^3 \leq b^2 + 6b \]

   Dado que $b > 0$, podemos dividir ambos lados de la desigualdad entre $b$:
   \[ b^2 \leq b + 6 \implies b^2 - b - 6 \leq 0 \implies (b - 3)(b + 2) \leq 0 \]

   Como estamos en el caso $b > 0$, esto se cumple para $0 < b \leq 3$.

(Los valores con $b < 0$ son menores que los obtenidos en el caso $b > 0$, por lo que no pueden superar a $3$).

Por lo tanto, el mayor valor posible de $b$ es $3$.

\boxed{3}