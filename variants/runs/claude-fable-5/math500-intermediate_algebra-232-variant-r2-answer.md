Buscamos los pares de enteros $(x, y)$ con $|x+yi| = \sqrt{x^2+y^2} \le 6$, es decir, los puntos reticulares dentro del círculo $x^2 + y^2 \le 36$.

Para cada valor de $x$, cuento los $y$ enteros con $y^2 \le 36 - x^2$:

- $x = 0$: $y^2 \le 36$, así que $-6 \le y \le 6$: **13** valores.
- $x = \pm 1$: $y^2 \le 35$, $|y| \le 5$: **11** valores cada uno.
- $x = \pm 2$: $y^2 \le 32$, $|y| \le 5$: **11** valores cada uno.
- $x = \pm 3$: $y^2 \le 27$, $|y| \le 5$: **11** valores cada uno.
- $x = \pm 4$: $y^2 \le 20$, $|y| \le 4$: **9** valores cada uno.
- $x = \pm 5$: $y^2 \le 11$, $|y| \le 3$: **7** valores cada uno.
- $x = \pm 6$: $y^2 \le 0$, $y = 0$: **1** valor cada uno.

Sumando: $13 + 2(11 + 11 + 11 + 9 + 7 + 1) = 13 + 2 \cdot 50 = 113$.

$$\boxed{113}$$