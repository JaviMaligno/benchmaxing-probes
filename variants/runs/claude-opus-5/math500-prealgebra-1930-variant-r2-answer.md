## Planteamiento

**Suma de cada fila:**

- Fila 1: $(n+1) + 3 + (n-1) = 2n + 3$
- Fila 2: $5 + (2n-11) + n = 3n - 6$
- Fila 3: $(n-3) + (n+2) + 4 = 2n + 3$

Igualando la fila 1 con la fila 2:

$$2n + 3 = 3n - 6 \implies n = 9$$

## Verificación

Con $n = 9$ el cuadrado queda:

$$\begin{array}{|c|c|c|}
\hline
10 & 3 & 8 \\\hline
5 & 7 & 9 \\\hline
6 & 11 & 4 \\\hline
\end{array}$$

- Filas: $21,\ 21,\ 21$
- Columnas: $10+5+6=21$, $3+7+11=21$, $8+9+4=21$
- Diagonales: $10+7+4=21$, $8+7+6=21$

Todas las sumas valen $21$, por lo que es efectivamente un cuadrado mágico.

$\boxed{9}$