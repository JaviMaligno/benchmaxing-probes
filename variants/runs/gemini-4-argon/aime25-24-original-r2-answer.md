Para encontrar los valores de $n$ y $t$, analizamos paso a paso la ecuación $f(x) = 0$ y su condición de tangencia en el intervalo $0 < x < 2\pi$.

### Paso 1: Encontrar $n$ (número de raíces de $f(x) = 0$)
Tenemos la función:
$$f(x) = \sin\left(7\pi \cdot \sin(5x)\right)$$

Para que $f(x) = 0$, el argumento del seno exterior debe ser un múltiplo entero de $\pi$:
$$7\pi \cdot \sin(5x) = k\pi \quad \text{para algún } k \in \mathbb{Z}$$
$$\sin(5x) = \frac{k}{7}$$

Dado que $-1 \le \sin(5x) \le 1$, el entero $k$ puede tomar cualquier valor en el conjunto $\{-7, -6, -5, \dots, 5, 6, 7\}$, lo que nos da $15$ posibles valores para $k$.

Hacemos el cambio de variable $u = 5x$. Como $0 < x < 2\pi$, el intervalo para $u$ es:
$$0 < u < 10\pi$$
Este intervalo abarca exactamente $5$ períodos completos de la función $\sin(u)$ (excluyendo los extremos $0$ y $10\pi$). Contamos las soluciones de $\sin(u) = \frac{k}{7}$ según el valor de $k$:

1. **Caso $k = 7$ ($\sin(u) = 1$):** En cada período de longitud $2\pi$ hay exactamente $1$ solución. En $5$ períodos hay $5 \times 1 = 5$ soluciones.
2. **Caso $k = -7$ ($\sin(u) = -1$):** En cada período de longitud $2\pi$ hay exactamente $1$ solución. En $5$ períodos hay $5 \times 1 = 5$ soluciones.
3. **Caso $k = 0$ ($\sin(u) = 0$):** Las soluciones son de la forma $u = m\pi$ con $m \in \mathbb{Z}$. En el intervalo abierto $(0, 10\pi)$, $m$ toma los valores $1, 2, \dots, 9$, lo que da $9$ soluciones.
4. **Caso $k \in \{\pm 1, \pm 2, \pm 3, \pm 4, \pm 5, \pm 6\}$ ($12$ valores de $k$):** Para cada uno de estos valores, $-1 < \frac{k}{7} < 1$ y $\frac{k}{7} \neq 0$, por lo que la ecuación $\sin(u) = \frac{k}{7}$ tiene $2$ soluciones en cada uno de los $5$ períodos (es decir, $10$ soluciones por cada valor de $k$). En total hay $12 \times 10 = 120$ soluciones.

Como distintos valores de $k$ producen conjuntos disjuntos de soluciones, sumamos todos los casos para obtener $n$:
$$n = 5 + 5 + 9 + 120 = 139$$

---

### Paso 2: Encontrar $t$ (puntos de tangencia con el eje $x$)
La gráfica de $y = f(x)$ es tangente al eje $x$ en una raíz $x_0$ si además se cumple que $f'(x_0) = 0$. Calculamos la derivada de $f(x)$ usando la regla de la cadena:
$$f'(x) = 35\pi \cos(5x) \cos\left(7\pi \cdot \sin(5x)\right)$$

En cualquiera de las $n$ raíces donde $f(x) = 0$, sabemos que $7\pi \cdot \sin(5x) = k\pi$, por lo que:
$$\cos\left(7\pi \cdot \sin(5x)\right) = \cos(k\pi) = (-1)^k \neq 0$$

Por lo tanto, en una raíz de $f(x)$, tenemos que $f'(x) = 0$ si y solo si:
$$\cos(5x) = 0 \iff \sin(5x) = \pm 1 \iff k = \pm 7$$

(Además, en estos puntos la segunda derivada es no nula, por lo que son extremos locales donde la curva toca el eje $x$ sin cruzarlo).

Del Paso 1, sabemos que para $k = 7$ hay $5$ soluciones y para $k = -7$ hay $5$ soluciones. Así:
$$t = 5 + 5 = 10$$

---

### Paso 3: Calcular $n + t$
$$n + t = 139 + 10 = 149$$

\boxed{149}