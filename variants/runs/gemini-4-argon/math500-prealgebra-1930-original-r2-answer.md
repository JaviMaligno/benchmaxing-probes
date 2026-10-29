Para encontrar el valor de $n$, primero organizamos las expresiones de las casillas del cuadrado mágico según sus coordenadas en la cuadrícula de $3 \times 3$:

* **Fila superior:** $(n+1)$, $1$, $(n-1)$
* **Fila central:** $3$, $(2n-9)$, $n$
* **Fila inferior:** $(n-3)$, $(n+2)$, $2$

En un cuadrado mágico, la suma de los elementos de cada fila, columna y diagonal principal es la misma. 

Calculamos la suma de la fila superior:
$$(n + 1) + 1 + (n - 1) = 2n + 1$$

Calculamos la suma de la fila central:
$$3 + (2n - 9) + n = 3n - 6$$

Igualamos las sumas de ambas filas para hallar $n$:
$$2n + 1 = 3n - 6$$
$$1 + 6 = 3n - 2n$$
$$n = 7$$

*(Verificación: Si $n = 7$, la suma mágica es $2(7) + 1 = 15$, formando el cuadrado mágico estándar con filas $8, 1, 6$; $3, 5, 7$ y $4, 9, 2$, donde todas las filas, columnas y diagonales suman $15$).*

\boxed{7}