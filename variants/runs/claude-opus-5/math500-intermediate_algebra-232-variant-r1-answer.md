## Planteamiento

La condición $|x+yi| \le 6$ equivale a $\sqrt{x^2+y^2} \le 6$, es decir:

$$x^2 + y^2 \le 36$$

Hay que contar los puntos de la retícula entera dentro del disco de radio 6. Recorro cada valor de $x$ y cuento los $y$ válidos: $|y| \le \sqrt{36-x^2}$, lo que da $2\lfloor\sqrt{36-x^2}\rfloor + 1$ valores.

| $x$ | $36-x^2$ | $\lfloor\sqrt{\cdot}\rfloor$ | nº de $y$ |
|---|---|---|---|
| $0$ | 36 | 6 | 13 |
| $\pm 1$ | 35 | 5 | 11 |
| $\pm 2$ | 32 | 5 | 11 |
| $\pm 3$ | 27 | 5 | 11 |
| $\pm 4$ | 20 | 4 | 9 |
| $\pm 5$ | 11 | 3 | 7 |
| $\pm 6$ | 0 | 0 | 1 |

## Suma

Para los valores positivos de $x$ (que se duplican por simetría):

$$11+11+11+9+7+1 = 50$$

Total:

$$13 + 2\cdot 50 = 113$$

\boxed{113}