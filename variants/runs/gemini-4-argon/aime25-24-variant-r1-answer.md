Para encontrar los valores de $n$ y $t$, primero determinamos las soluciones de la ecuación $g(x) = 0$ en el intervalo abierto $0 < x < 2\pi$.

La función dada es:
$$g(x) = \sin\left(8\pi \cdot \sin(6x)\right)$$

### Paso 1: Encontrar $n$ (el número de raíces en $0 < x < 2\pi$)
Para que $g(x) = 0$, el argumento de la función seno exterior debe ser un múltiplo entero de $\pi$:
$$8\pi \cdot \sin(6x) = k\pi, \quad k \in \mathbb{Z}$$
$$\sin(6x) = \frac{k}{8}$$

Dado que $-1 \le \sin(6x) \le 1$, el entero $k$ puede tomar cualquier valor desde $-8$ hasta $8$ inclusive (es decir, $17$ valores posibles para $k$).

Sea $u = 6x$. Como $x \in (0, 2\pi)$, la variable $u$ recorre el intervalo abierto $(0, 12\pi)$, lo que corresponde exactamente a $6$ períodos completos de la función $\sin(u)$ sin incluir los extremos $0$ y $12\pi$. Contamos las soluciones para $u \in (0, 12\pi)$ según el valor de $k$:

1. **Para $k = 0$:** $\sin(u) = 0$.
   Las soluciones en $(0, 12\pi)$ son $u = \pi, 2\pi, \dots, 11\pi$. Hay **$11$ soluciones**.

2. **Para $k \in \{\pm 1, \pm 2, \pm 3, \pm 4, \pm 5, \pm 6, \pm 7\}$:** $\sin(u) = \frac{k}{8} \in (-1, 0) \cup (0, 1)$.
   Para cada uno de estos $14$ valores de $k$, la ecuación $\sin(u) = \frac{k}{8}$ tiene $2$ soluciones por cada período de longitud $2\pi$. Como hay $6$ períodos, hay $2 \times 6 = 12$ soluciones para cada valor de $k$.
   En total, esto aporta $14 \times 12 =$ **$168$ soluciones**.

3. **Para $k = 8$ y $k = -8$:** $\sin(u) = 1$ y $\sin(u) = -1$.
   Cada una de estas dos ecuaciones tiene $1$ única solución por cada período de $2\pi$. En $6$ períodos, hay $6$ soluciones para $k = 8$ y $6$ soluciones para $k = -8$.
   En total, esto aporta $6 + 6 =$ **$12$ soluciones**.

Sumando todas las soluciones obtenemos $n$:
$$n = 11 + 168 + 12 = 191$$

---

### Paso 2: Encontrar $t$ (el número de puntos de tangencia con el eje $x$)
La gráfica de $y = g(x)$ es tangente al eje $x$ en una raíz $x_0$ si y solo si $g(x_0) = 0$ y además $g'(x_0) = 0$.

Calculamos la derivada de $g(x)$ usando la regla de la cadena:
$$g'(x) = \cos\left(8\pi \cdot \sin(6x)\right) \cdot 48\pi \cos(6x)$$

Si $g(x_0) = 0$, entonces $8\pi \cdot \sin(6x_0) = k\pi$, por lo que $\cos\left(8\pi \cdot \sin(6x_0)\right) = \cos(k\pi) = (-1)^k \neq 0$.
Por lo tanto, para que $g'(x_0) = 0$ en una raíz, es necesario y suficiente que:
$$\cos(6x_0) = 0 \iff \sin(6x_0) = \pm 1$$

Esto corresponde exactamente a las soluciones obtenidas cuando $k = 8$ y $k = -8$. Como vimos en el Paso 1, existen exactamente $12$ de estos valores en el intervalo $(0, 2\pi)$. Por lo tanto:
$$t = 12$$

---

### Paso 3: Calcular $n + t$
$$n + t = 191 + 12 = 203$$

\boxed{203}