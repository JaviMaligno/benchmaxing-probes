## Resolución

**Paso 1: Encontrar los ceros de $f$.**

$f(x) = \sin(7\pi \sin(5x)) = 0$ cuando $7\pi \sin(5x) = k\pi$, es decir, $\sin(5x) = \frac{k}{7}$ con $k$ entero. Como $-1 \le \sin(5x) \le 1$, tenemos $k \in \{-7, -6, \dots, 6, 7\}$.

**Paso 2: Contar soluciones.** Con $0 < x < 2\pi$, el argumento $u = 5x$ recorre $(0, 10\pi)$, que son 5 períodos completos de la función seno.

- **$k = 0$:** $\sin(u) = 0$ con $u \in (0, 10\pi)$ da $u = \pi, 2\pi, \dots, 9\pi$: **9 soluciones**.
- **$k = \pm 7$:** $\sin(u) = \pm 1$ da 1 solución por período: $5 + 5 = $ **10 soluciones**.
- **$k = \pm 1, \dots, \pm 6$ (12 valores):** $\sin(u) = k/7$ con $0 < |k/7| < 1$ da 2 soluciones por período, o sea 10 cada uno: $12 \times 10 = $ **120 soluciones**.

Total: $n = 9 + 10 + 120 = 139$.

**Paso 3: Tangencia con el eje $x$.** Se requiere además $f'(x) = 0$. Derivando:
$$f'(x) = 35\pi \cos(5x)\cos(7\pi \sin(5x)).$$
En un cero de $f$, $7\pi\sin(5x) = k\pi$, así que $\cos(7\pi\sin(5x)) = \pm 1 \neq 0$. Por lo tanto necesitamos $\cos(5x) = 0$, lo que implica $\sin(5x) = \pm 1$, es decir, exactamente los casos $k = \pm 7$. Esos son los 10 puntos encontrados arriba (y en ellos $f$ efectivamente toca el eje sin cruzarlo, pues $\sin(5x)$ alcanza un extremo): $t = 10$.

**Paso 4:** $n + t = 139 + 10 = 149$.

$$\boxed{149}$$