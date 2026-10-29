## Planteamiento

Ubico las celdas según el diagrama (de arriba hacia abajo):

| | | |
|---|---|---|
| $n+1$ | $1$ | $n-1$ |
| $3$ | $2n-9$ | $n$ |
| $n-3$ | $n+2$ | $2$ |

## Resolución

Sumo la primera fila:
$$(n+1) + 1 + (n-1) = 2n+1$$

Sumo la segunda fila:
$$3 + (2n-9) + n = 3n-6$$

Como ambas sumas deben ser iguales:
$$2n+1 = 3n-6 \quad\Longrightarrow\quad n = 7$$

## Verificación

Con $n=7$ el cuadrado queda:

| | | |
|---|---|---|
| $8$ | $1$ | $6$ |
| $3$ | $5$ | $7$ |
| $4$ | $9$ | $2$ |

- Filas: $8+1+6=15$, $3+5+7=15$, $4+9+2=15$
- Columnas: $8+3+4=15$, $1+5+9=15$, $6+7+2=15$
- Diagonales: $8+5+2=15$, $6+5+4=15$

Todas las sumas valen $15$, por lo que es un cuadrado mágico.

\boxed{7}