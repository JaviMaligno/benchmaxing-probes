## Solución

**Paso 1: Encontrar los ceros.**

$f(x) = \sin(7\pi \cdot \sin(5x)) = 0$ requiere que $7\pi \sin(5x) = k\pi$ con $k$ entero, es decir:
$$\sin(5x) = \frac{k}{7}, \quad -7 \le k \le 7.$$

Como $5x$ recorre un intervalo de longitud $10\pi$ (cinco períodos completos), contamos soluciones en $(0, 2\pi)$ según el valor de $k$:

- **$k = \pm 7$:** $\sin(5x) = \pm 1$ da exactamente $5$ soluciones cada uno ($10$ en total).
- **$k = 0$:** $\sin(5x) = 0$ da $5x = m\pi$ con $m = 1,\dots,9$, es decir $9$ soluciones.
- **$k = \pm 1, \dots, \pm 6$** (12 valores): cada $\sin(5x) = c$ con $|c| < 1$, $c \ne 0$ da $10$ soluciones, es decir $12 \times 10 = 120$.

$$n = 10 + 9 + 120 = 139.$$

**Paso 2: Encontrar los puntos de tangencia.**

Derivamos con la regla de la cadena:
$$f'(x) = 35\pi \cos(5x)\cos(7\pi \sin 5x).$$

Queremos $f(x) = 0$ **y** $f'(x) = 0$ simultáneamente. En un cero sabemos que $7\sin(5x) = k$ (entero), así que:

- $\cos(7\pi \sin 5x) = \cos(k\pi) = \pm 1 \ne 0$: este factor nunca se anula en un cero.
- Por lo tanto necesitamos $\cos(5x) = 0$, es decir $\sin(5x) = \pm 1$, que corresponde a $k = \pm 7$.

Esos son exactamente los $10$ puntos del caso $k = \pm 7$ (en ellos $\sin(5x)$ tiene un máximo o mínimo local, la gráfica toca el eje sin cruzarlo). Comprobación: no hay otros candidatos, pues $\cos(7\pi\sin 5x) = 0$ exigiría $7\sin(5x) = \text{entero} + \tfrac12$, incompatible con $f(x) = 0$.

$$t = 10.$$

**Paso 3: Resultado.**

$$n + t = 139 + 10 = \boxed{149}$$