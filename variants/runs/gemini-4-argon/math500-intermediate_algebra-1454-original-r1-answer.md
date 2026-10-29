Para encontrar el valor mínimo de la expresión dada, primero reescribimos los términos dentro de las raíces cuadradas completando cuadrados:

1. El primer término es:
   $$\sqrt{x^2 + 400} = \sqrt{x^2 + 20^2}$$

2. El segundo término es:
   $$\sqrt{y^2 + 900} = \sqrt{30^2 + y^2}$$

3. El tercer término se puede factorizar completando el cuadrado para $x$ e $y$:
   $$x^2 + y^2 - 80x - 100y + 4100 = (x^2 - 80x + 1600) + (y^2 - 100y + 2500) = (40 - x)^2 + (50 - y)^2$$
   Por lo tanto, la tercera raíz es:
   $$\sqrt{(40 - x)^2 + (50 - y)^2}$$

Ahora podemos interpretar cada raíz cuadrada como la norma (longitud) de un vector en el plano cartesiano:
- $\vec{u} = (x, 20)$, con $\|\vec{u}\| = \sqrt{x^2 + 20^2}$
- $\vec{v} = (40 - x, 50 - y)$, con $\|\vec{v}\| = \sqrt{(40 - x)^2 + (50 - y)^2}$
- $\vec{w} = (30, y)$, con $\|\vec{w}\| = \sqrt{30^2 + y^2}$

Por la desigualdad triangular (o desigualdad de Minkowski), la suma de las longitudes de estos tres vectores es mayor o igual que la longitud de la suma de los vectores:
$$\|\vec{u}\| + \|\vec{v}\| + \|\vec{w}\| \ge \|\vec{u} + \vec{v} + \vec{w}\|$$

Calculamos la suma de los vectores:
$$\vec{u} + \vec{v} + \vec{w} = (x + (40 - x) + 30, \, 20 + (50 - y) + y) = (70, 70)$$

La longitud del vector resultante es:
$$\|(70, 70)\| = \sqrt{70^2 + 70^2} = \sqrt{9800} = 70\sqrt{2}$$

La igualdad se alcanza si y solo si los tres vectores son colineales y apuntan en la misma dirección que $(70, 70)$ (es decir, tienen pendiente $1$):
- Para $\vec{u} = (x, 20)$, necesitamos $\frac{20}{x} = 1 \implies x = 20$.
- Para $\vec{w} = (30, y)$, necesitamos $\frac{y}{30} = 1 \implies y = 30$.
- Con $x = 20$ e $y = 30$, el vector $\vec{v} = (40 - 20, 50 - 30) = (20, 20)$ también tiene pendiente $1$.

Dado que $x = 20 \in [0, 40]$ e $y = 30 \in [0, 50]$ cumplen con las restricciones del dominio, el mínimo se alcanza efectivamente en este punto.

\boxed{70\sqrt{2}}