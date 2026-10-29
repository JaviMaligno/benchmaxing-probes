## Planteamiento

Igualamos la suma de la primera fila con la de la segunda fila.

**Primera fila:** $(n+1) + 3 + (n-1) = 2n + 3$

**Segunda fila:** $5 + (2n-11) + n = 3n - 6$

Como ambas sumas deben coincidir:

$$2n + 3 = 3n - 6 \implies n = 9$$

## Verificación

Sustituyendo $n = 9$, el cuadrado queda:

$$\begin{array}{ccc} 10 & 3 & 8 \\ 5 & 7 & 9 \\ 6 & 11 & 4 \end{array}$$

- Filas: $10+3+8 = 21$, $5+7+9 = 21$, $6+11+4 = 21$
- Columnas: $10+5+6 = 21$, $3+7+11 = 21$, $8+9+4 = 21$
- Diagonales: $10+7+4 = 21$, $8+7+6 = 21$

Todas las sumas valen 21, por lo que efectivamente es un cuadrado mágico.

\boxed{9}