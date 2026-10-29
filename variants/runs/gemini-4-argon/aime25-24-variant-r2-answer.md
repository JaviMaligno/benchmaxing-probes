Para hallar $n$ y $t$, analizamos primero las raíces de la función $g(x) = \sin\left(8\pi \cdot \sin(6x)\right)$ en el intervalo abierto $0 < x < 2\pi$.

**Paso 1: Encontrar el valor de $n$**

La condición $g(x) = 0$ se cumple cuando el argumento del seno exterior es un múltiplo entero de $\pi$:
$$8\pi \sin(6x) = k\pi \implies \sin(6x) = \frac{k}{8}, \quad k \in \mathbb{Z}$$

Dado que $-1 \le \sin(6x) \le 1$, el entero $k$ puede tomar cualquier valor desde $-8$ hasta $8$ inclusive ($17$ valores posibles para $k$).

Sea $u = 6x$. Como $0 < x < 2\pi$, tenemos que $0 < u < 12\pi$. Este intervalo abarca $6$ períodos completos de la función $\sin(u)$, excluyendo el extremo $u = 0$. Contamos el número de soluciones para $\sin(u) = \frac{k}{8}$ en $(0, 12\pi)$ según el valor de $k$:

1. **Para $k = 0$ ($\sin(u) = 0$):** Las soluciones son $u = m\pi$. En el intervalo abierto $(0, 12\pi)$, $m$ toma los valores $1, 2, \dots, 11$, lo que nos da **$11$ soluciones**.
2. **Para $k \in \{\pm 1, \pm 2, \pm 3, \pm 4, \pm 5, \pm 6, \pm 7\}$ ($14$ valores de $k$):** En cada uno de los $6$ períodos de longitud $2\pi$, la ecuación $\sin(u) = \frac{k}{8}$ tiene exactamente $2$ soluciones (ninguna en los múltiplos de $2\pi$). Esto aporta $14 \times 6 \times 2 =$ **$168$ soluciones**.
3. **Para $k = \pm 8$ ($\sin(u) = \pm 1$, $2$ valores de $k$):** En cada uno de los $6$ períodos, $\sin(u) = 1$ tiene $1$ solución y $\sin(u) = -1$ tiene $1$ solución. Esto aporta $2 \times 6 \times 1 =$ **$12$ soluciones**.

Sumando todos los casos, obtenemos el total de raíces $n$:
$$n = 11 + 168 + 12 = 191$$

---

**Paso 2: Encontrar el valor de $t$**

La gráfica de $y = g(x)$ es tangente al eje $x$ en aquellos puntos donde $g(x) = 0$ y simultáneamente $g'(x) = 0$. Calculamos la derivada de $g(x)$ usando la regla de la cadena:
$$g'(x) = 48\pi \cos\left(8\pi \sin(6x)\right) \cos(6x)$$

En cualquier raíz de $g(x)$, sabemos que $8\pi \sin(6x) = k\pi$, por lo que $\cos(8\pi \sin(6x)) = \cos(k\pi) = (-1)^k \neq 0$. Por lo tanto:
$$g'(x) = 0 \iff \cos(6x) = 0 \iff \sin(6x) = \pm 1$$

Esto corresponde exactamente a los casos $k = 8$ y $k = -8$ que ya contamos en el Paso 1. Por consiguiente, hay:
$$t = 12$$
valores de $x$ donde la gráfica es tangente al eje $x$.

---

**Paso 3: Calcular $n + t$**

$$n + t = 191 + 12 = 203$$

\boxed{203}