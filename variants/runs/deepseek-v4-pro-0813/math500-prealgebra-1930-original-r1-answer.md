El cuadrado mágico es de 3×3 con estas entradas:

| | | |
|---|---|---|
| $n-3$ | $3$ | $n+1$ |
| $n+2$ | $2n-9$ | $1$ |
| $2$ | $n$ | $n-1$ |

Como es un cuadrado mágico, todas las filas, columnas y diagonales principales suman lo mismo.

Calculemos una fila y una columna para igualar sus sumas.

Suma de la primera fila:
$$(n-3)+3+(n+1)=2n+1$$

Suma de la tercera fila:
$$2+n+(n-1)=2n+1$$

Ambas coinciden, así que la constante mágica es $2n+1$.

Ahora usemos una columna. Suma de la columna del medio:
$$3+(2n-9)+n=3n-6$$

La columna del medio debe sumar lo mismo que la primera fila:
$$3n-6=2n+1$$

Restamos $2n$:
$$n-6=1$$

Sumamos $6$:
$$n=7$$

Sustituimos $n=7$ en el cuadrado para comprobar:

| | | |
|---|---|---|
| $4$ | $3$ | $8$ |
| $9$ | $5$ | $1$ |
| $2$ | $7$ | $6$ |

Filas: $4+3+8=15$, $9+5+1=15$, $2+7+6=15$.  
Columnas: $4+9+2=15$, $3+5+7=15$, $8+1+6=15$.  
Diagonales: $4+5+6=15$, $8+5+2=15$.

Todo suma $15$, así que el valor es correcto.

$$\boxed{7}$$