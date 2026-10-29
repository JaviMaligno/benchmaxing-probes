## Planteamiento

Sea $P$ la probabilidad de que Carla gane, estando a punto de tirar ella.

**Probabilidades por tirada:**
- Carla gana con un 5 o 6: $\frac{2}{6} = \frac{1}{3}$; no gana con probabilidad $\frac{2}{3}$.
- Dev gana con un 1 o 2: $\frac{2}{6} = \frac{1}{3}$; no gana con probabilidad $\frac{2}{3}$.

**Ecuación recursiva:**

Carla gana si acierta de inmediato, o si ambos fallan y la situación se repite idénticamente:

$$P = \frac{1}{3} + \frac{2}{3}\cdot\frac{2}{3}\cdot P$$

$$P = \frac{1}{3} + \frac{4}{9}P \quad\Longrightarrow\quad \frac{5}{9}P = \frac{1}{3} \quad\Longrightarrow\quad P = \frac{3}{5}$$

**Verificación por serie:** Carla gana en su ronda $k$-ésima con probabilidad $\left(\frac{4}{9}\right)^{k-1}\cdot\frac{1}{3}$, de modo que

$$P = \frac{1}{3}\sum_{k=0}^{\infty}\left(\frac{4}{9}\right)^{k} = \frac{1}{3}\cdot\frac{1}{1-\frac49} = \frac{1}{3}\cdot\frac{9}{5} = \frac{3}{5}$$

La ventaja de tirar primero es lo que rompe la simetría: ambos tienen la misma probabilidad por tirada, pero Carla gana el 60 % de las partidas.

$$\boxed{\dfrac{3}{5}}$$