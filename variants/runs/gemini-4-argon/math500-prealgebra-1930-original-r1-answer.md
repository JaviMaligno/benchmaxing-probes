Para hallar el valor de $n$, primero organizamos las expresiones de la cuadrícula de $3 \times 3$ a partir de sus coordenadas en el diagrama:

* **Fila superior:** $(n+1)$, $1$, $(n-1)$
* **Fila central:** $3$, $(2n-9)$, $n$
* **Fila inferior:** $(n-3)$, $(n+2)$, $2$

Como se trata de un cuadrado mágico, la suma de los números de cada fila, columna y diagonal principal debe ser la misma.

1. **Calculamos la suma de la fila superior:**
   $$(n + 1) + 1 + (n - 1) = 2n + 1$$

2. **Calculamos la suma de la fila central:**
   $$3 + (2n - 9) + n = 3n - 6$$

3. **Igualamos ambas sumas para despejar $n$:**
   $$2n + 1 = 3n - 6$$
   $$1 + 6 = 3n - 2n$$
   $$n = 7$$

Comprobamos que con $n = 7$ la suma mágica es $2(7) + 1 = 15$ en todas las direcciones (por ejemplo, la diagonal de abajo a la izquierda hacia arriba a la derecha suma $(7-3) + (14-9) + (7-1) = 4 + 5 + 6 = 15$).

\boxed{7}