## Planteamiento

El día en que la piel se vuelve rosa es el primer día en que el total alcanza 10 o más. Ese total es 10 (si cae justo en 10) o 11 (si salta de 9 a 11 comiendo 2 camarones). Pinky no se enferma ese día exactamente cuando el total alcanzado es 10, es decir, cuando alguna suma parcial vale exactamente 10.

## Cálculo

Sea $p_n$ la probabilidad de que las sumas parciales pasen por $n$. Para llegar a $n$ hay que venir de $n-1$ (comiendo 1) o de $n-2$ (comiendo 2), cada caso con probabilidad $1/2$:

$$p_n = \tfrac{1}{2}p_{n-1} + \tfrac{1}{2}p_{n-2}, \qquad p_0 = 1,\; p_1 = \tfrac12$$

La solución de esta recurrencia (raíces $1$ y $-1/2$) es:

$$p_n = \frac{2}{3} + \frac{1}{3}\left(-\frac{1}{2}\right)^n$$

Para $n = 10$:

$$p_{10} = \frac{2}{3} + \frac{1}{3}\cdot\frac{1}{1024} = \frac{2048 + 1}{3072} = \frac{2049}{3072} = \frac{683}{1024}$$

\boxed{\dfrac{683}{1024}}