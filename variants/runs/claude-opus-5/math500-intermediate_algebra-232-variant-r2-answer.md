## Planteamiento

La condición $|x+yi| \le 6$ equivale a $x^2 + y^2 \le 36$, es decir, contar los puntos de coordenadas enteras dentro del disco de radio 6 centrado en el origen.

Para cada valor de $x$ con $|x| \le 6$, cuento los enteros $y$ tales que $y^2 \le 36 - x^2$:

| $x$ | $36-x^2$ | $|y| \le \lfloor\sqrt{36-x^2}\rfloor$ | nº de $y$ | nº de $x$ | subtotal |
|---|---|---|---|---|---|
| $0$ | $36$ | $6$ | $13$ | 1 | $13$ |
| $\pm 1$ | $35$ | $5$ | $11$ | 2 | $22$ |
| $\pm 2$ | $32$ | $5$ | $11$ | 2 | $22$ |
| $\pm 3$ | $27$ | $5$ | $11$ | 2 | $22$ |
| $\pm 4$ | $20$ | $4$ | $9$ | 2 | $18$ |
| $\pm 5$ | $11$ | $3$ | $7$ | 2 | $14$ |
| $\pm 6$ | $0$ | $0$ | $1$ | 2 | $2$ |

## Suma

$$13 + 22 + 22 + 22 + 18 + 14 + 2 = 113$$

(Comprobación aproximada: el área del disco es $36\pi \approx 113.1$, consistente con el conteo.)

\boxed{113}