Planteo el problema paso a paso.

**Encontrar n (ceros de g):**

$g(x) = \sin(8\pi \sin(6x)) = 0$ cuando $8\pi \sin(6x) = k\pi$, es decir, $\sin(6x) = \frac{k}{8}$ con $k$ entero y $|k| \le 8$.

Sea $u = 6x$. Como $0 < x < 2\pi$, entonces $u \in (0, 12\pi)$, que abarca 6 períodos completos del seno.

- **k = 0:** $\sin u = 0$ da $u = m\pi$ con $m = 1, \dots, 11$ (se excluyen los extremos): **11 soluciones**.
- **k = ±8:** $\sin u = \pm 1$ ocurre una vez por período: $6 + 6 = $ **12 soluciones**.
- **0 < |k| < 8** (es decir, $k = \pm1, \dots, \pm7$, 14 valores): cada ecuación $\sin u = k/8$ tiene 2 soluciones por período, o sea $12$ cada una: $14 \times 12 = $ **168 soluciones**.

Total: $n = 11 + 12 + 168 = 191$.

**Encontrar t (tangencias al eje x):**

La gráfica es tangente al eje x cuando $g(x) = 0$ y $g'(x) = 0$. Derivando:
$$g'(x) = \cos(8\pi \sin(6x)) \cdot 8\pi \cdot 6\cos(6x)$$

En los ceros, $\sin(6x) = k/8$, así que $\cos(8\pi \sin(6x)) = \cos(k\pi) = \pm 1 \neq 0$. Por lo tanto $g'(x) = 0$ exige $\cos(6x) = 0$, lo que implica $\sin(6x) = \pm 1$, es decir, $k = \pm 8$.

Esos son exactamente los 12 ceros contados arriba, y en ellos la función efectivamente toca el eje sin cruzarlo (son extremos de $\sin(6x)$). Así, $t = 12$.

**Resultado:**
$$n + t = 191 + 12 = 203$$

$$\boxed{203}$$