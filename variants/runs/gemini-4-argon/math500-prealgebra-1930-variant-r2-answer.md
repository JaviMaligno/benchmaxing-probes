Para hallar el valor de $n$, utilizamos la propiedad de un cuadrado mágico por la cual la suma de los números en cada fila, columna y diagonal principal es siempre la misma.

1. Calculamos la suma de la fila superior:
$$(n + 1) + 3 + (n - 1) = 2n + 3$$

2. Calculamos la suma de la fila central:
$$5 + (2n - 11) + n = 3n - 6$$

3. Igualamos las sumas de ambas filas para despejar $n$:
$$2n + 3 = 3n - 6$$
$$3 + 6 = 3n - 2n$$
$$n = 9$$

4. Verificamos el resultado sustituyendo $n = 9$ en el cuadrado:
- Fila superior: $10, 3, 8 \rightarrow 10 + 3 + 8 = 21$
- Fila central: $5, 7, 9 \rightarrow 5 + 7 + 9 = 21$
- Fila inferior: $6, 11, 4 \rightarrow 6 + 11 + 4 = 21$
- Columnas: $10+5+6=21$, $3+7+11=21$, $8+9+4=21$
- Diagonales: $10+7+4=21$, $8+7+6=21$

\boxed{9}