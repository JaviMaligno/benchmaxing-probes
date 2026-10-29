## Planteamiento

- Carla gana en su tirada con probabilidad 2/6 = 1/3; falla con probabilidad 2/3.
- Dev gana en su tirada con probabilidad 2/6 = 1/3; falla con probabilidad 2/3.

Sea $P$ la probabilidad de que Carla gane, estando a punto de tirar ella.

**Ecuación recursiva:** Carla gana de inmediato (1/3), o falla (2/3) y Dev falla (2/3), volviendo a la situación inicial:

$$P = \frac{1}{3} + \frac{2}{3}\cdot\frac{2}{3}\cdot P = \frac{1}{3} + \frac{4}{9}P$$

$$\frac{5}{9}P = \frac{1}{3} \quad\Longrightarrow\quad P = \frac{9}{5}\cdot\frac{1}{3} = \frac{3}{5}$$

**Verificación por serie geométrica:** Carla gana en su $n$-ésima tirada con probabilidad $\left(\frac{4}{9}\right)^{n-1}\cdot\frac{1}{3}$, de modo que

$$P = \frac{1/3}{1 - 4/9} = \frac{1/3}{5/9} = \frac{3}{5}$$

$$\boxed{\dfrac{3}{5}}$$