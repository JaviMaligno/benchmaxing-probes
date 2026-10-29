Queremos contar los pares de enteros $(x, y)$ con $|x + yi| = \sqrt{x^2 + y^2} \le 6$, es decir, los puntos de la retícula entera dentro del círculo $x^2 + y^2 \le 36$.

Para cada valor de $x$, el número de valores válidos de $y$ es $2\lfloor\sqrt{36 - x^2}\rfloor + 1$:

- $x = 0$: $\sqrt{36} = 6$, hay $2(6)+1 = 13$ valores.
- $x = \pm 1$: $\sqrt{35} \approx 5.9$, hay $2(5)+1 = 11$ valores cada uno.
- $x = \pm 2$: $\sqrt{32} \approx 5.66$, hay $11$ valores cada uno.
- $x = \pm 3$: $\sqrt{27} \approx 5.2$, hay $11$ valores cada uno.
- $x = \pm 4$: $\sqrt{20} \approx 4.47$, hay $2(4)+1 = 9$ valores cada uno.
- $x = \pm 5$: $\sqrt{11} \approx 3.32$, hay $2(3)+1 = 7$ valores cada uno.
- $x = \pm 6$: $\sqrt{0} = 0$, hay $1$ valor cada uno.

Sumando: $13 + 2(11 + 11 + 11 + 9 + 7 + 1) = 13 + 2(50) = 13 + 100 = 113$.

$$\boxed{113}$$