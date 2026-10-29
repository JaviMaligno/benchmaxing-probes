Para hallar el valor mínimo de la expresión dada, primero reescribimos los términos dentro de las raíces cuadradas completando cuadrados en el tercer término:

1. Notamos que $225 = 15^2$ y $400 = 20^2$.
2. Para el tercer radical, agrupamos los términos con $a$ y con $b$:
   \[a^2 + b^2 - 70a - 80b + 2825 = (a^2 - 70a + 1225) + (b^2 - 80b + 1600) = (35 - a)^2 + (40 - b)^2\]
   ya que $1225 + 1600 = 2825$.

Sustituyendo esto en la expresión original, obtenemos:
\[E = \sqrt{a^2 + 15^2} + \sqrt{20^2 + b^2} + \sqrt{(35 - a)^2 + (40 - b)^2}\]

Podemos interpretar cada término como la norma (longitud) de un vector en $\mathbb{R}^2$:
- $\vec{v}_1 = (a, 15)$, con $\|\vec{v}_1\| = \sqrt{a^2 + 15^2}$
- $\vec{v}_2 = (20, b)$, con $\|\vec{v}_2\| = \sqrt{20^2 + b^2}$
- $\vec{v}_3 = (35 - a, 40 - b)$, con $\|\vec{v}_3\| = \sqrt{(35 - a)^2 + (40 - b)^2}$

Por la desigualdad triangular (o desigualdad de Minkowski), la suma de las longitudes de los vectores es mayor o igual que la longitud de la suma de los vectores:
\[E = \|\vec{v}_1\| + \|\vec{v}_2\| + \|\vec{v}_3\| \ge \|\vec{v}_1 + \vec{v}_2 + \vec{v}_3\|\]

Calculamos la suma de los tres vectores:
\[\vec{v}_1 + \vec{v}_2 + \vec{v}_3 = (a + 20 + 35 - a, 15 + b + 40 - b) = (55, 55)\]

Por lo tanto:
\[E \ge \sqrt{55^2 + 55^2} = 55\sqrt{2}\]

La igualdad se alcanza cuando los tres vectores tienen la misma dirección que el vector resultante $(55, 55)$, es decir, son múltiplos positivos de $(1, 1)$:
- Para $\vec{v}_1 = (a, 15)$, se requiere $a = 15$ (que cumple $0 \le 15 \le 35$).
- Para $\vec{v}_2 = (20, b)$, se requiere $b = 20$ (que cumple $0 \le 20 \le 40$).
- Con estos valores, $\vec{v}_3 = (35 - 15, 40 - 20) = (20, 20)$, que también es paralelo y del mismo sentido que $(1, 1)$.

Así, el valor mínimo se alcanza efectivamente en $a = 15$ y $b = 20$.

\boxed{55\sqrt{2}}