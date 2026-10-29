## Razonamiento

La condición $|a+bi| \le 5$ equivale a $a^2 + b^2 \le 25$, es decir, contar los puntos de la retícula entera dentro del disco de radio 5.

Para cada valor de $a$ (que debe cumplir $|a| \le 5$), contamos los enteros $b$ con $b^2 \le 25 - a^2$:

| $a$ | $25-a^2$ | cota para $b$ | nº de valores |
|---|---|---|---|
| $0$ | $25$ | $|b|\le 5$ | $11$ |
| $\pm 1$ | $24$ | $|b|\le 4$ | $9$ cada uno → $18$ |
| $\pm 2$ | $21$ | $|b|\le 4$ | $9$ cada uno → $18$ |
| $\pm 3$ | $16$ | $|b|\le 4$ | $9$ cada uno → $18$ |
| $\pm 4$ | $9$ | $|b|\le 3$ | $7$ cada uno → $14$ |
| $\pm 5$ | $0$ | $b=0$ | $1$ cada uno → $2$ |

Suma total: $11 + 18 + 18 + 18 + 14 + 2 = 81$.

\boxed{81}