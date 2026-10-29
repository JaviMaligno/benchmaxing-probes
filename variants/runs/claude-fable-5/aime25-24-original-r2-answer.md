**Respuesta: 149**

**Razonamiento:**

**Contando los ceros (n):** Tenemos $f(x) = 0$ cuando $7\pi \sin(5x) = k\pi$, es decir, $\sin(5x) = \frac{k}{7}$ con $k \in \{-7, \dots, 7\}$.

Para $0 < x < 2\pi$, el argumento $5x$ recorre $(0, 10\pi)$, o sea 5 períodos completos del seno.

- Para $k = \pm 1, \dots, \pm 6$ (es decir, $0 < |k/7| < 1$): cada valor da 2 soluciones por período, o sea 10 soluciones. Con 12 valores de $k$: $12 \times 10 = 120$.
- Para $k = 0$: $\sin(5x) = 0$ da $5x = m\pi$ con $m = 1, \dots, 9$ (los extremos quedan excluidos): 9 soluciones.
- Para $k = \pm 7$: $\sin(5x) = \pm 1$ da 5 soluciones cada uno: 10 soluciones.

Total: $n = 120 + 9 + 10 = 139$.

**Contando las tangencias (t):** La gráfica es tangente al eje $x$ cuando $f(x) = 0$ y $f'(x) = 0$. Como
$$f'(x) = 35\pi \cos(5x)\cos(7\pi \sin(5x)),$$
y en los ceros se cumple $7\pi\sin(5x) = k\pi$, el factor $\cos(k\pi) = \pm 1$ nunca se anula. Por tanto se necesita $\cos(5x) = 0$, lo que ocurre exactamente cuando $\sin(5x) = \pm 1$, es decir, en los 10 puntos del caso $k = \pm 7$. Así, $t = 10$.

Por lo tanto, $n + t = 139 + 10 = 149$.

$$\boxed{149}$$