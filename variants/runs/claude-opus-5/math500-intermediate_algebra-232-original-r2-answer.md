## Razonamiento

La condición $|a+bi| \le 5$ equivale a $a^2 + b^2 \le 25$, es decir, contar los puntos de coordenadas enteras en el disco cerrado de radio 5.

Para cada valor de $a$ (que debe cumplir $|a| \le 5$), contamos los enteros $b$ con $b^2 \le 25 - a^2$:

| $a$ | $25 - a^2$ | $|b| \le$ | número de $b$ |
|---|---|---|---|
| $0$ | $25$ | $5$ | $11$ |
| $\pm 1$ | $24$ | $4$ | $9$ cada uno |
| $\pm 2$ | $21$ | $4$ | $9$ cada uno |
| $\pm 3$ | $16$ | $4$ | $9$ cada uno |
| $\pm 4$ | $9$ | $3$ | $7$ cada uno |
| $\pm 5$ | $0$ | $0$ | $1$ cada uno |

Suma total:

$$11 + 2(9) + 2(9) + 2(9) + 2(7) + 2(1) = 11 + 18 + 18 + 18 + 14 + 2 = 81$$

\boxed{81}