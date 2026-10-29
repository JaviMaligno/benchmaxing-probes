Para hallar los valores de $n$ y $t$, analizamos paso a paso la ecuación $f(x) = 0$ en el intervalo $0 < x < 2\pi$.

### Paso 1: Encontrar el número de raíces $n$
Tenemos la ecuación:
$$f(x) = \sin\left(7\pi \cdot \sin(5x)\right) = 0$$

Sabemos que $\sin(\theta) = 0$ si y solo si $\theta = k\pi$ para algún número entero $k \in \mathbb{Z}$. Por lo tanto:
$$7\pi \cdot \sin(5x) = k\pi \iff \sin(5x) = \frac{k}{7}$$

Como $-1 \le \sin(5x) \le 1$, el entero $k$ puede tomar cualquier valor en el conjunto $\{-7, -6, -5, \dots, 5, 6, 7\}$ (un total de $15$ valores posibles).

Sea $u = 5x$. Como $x \in (0, 2\pi)$, la variable $u$ varía en el intervalo abierto $(0, 10\pi)$, el cual abarca $5$ periodos completos de longitud $2\pi$ (excluyendo los extremos $0$ y $10\pi$). Contemos las soluciones para $u \in (0, 10\pi)$ según el valor de $k$:

1. **Para $k = 0$:** $\sin(u) = 0$. Las soluciones en $(0, 10\pi)$ son $u = \pi, 2\pi, 3\pi, \dots, 9\pi$, lo que nos da **$9$ soluciones**.
2. **Para $k \in \{1, 2, 3, 4, 5, 6\}$:** Para cada uno de estos $6$ valores de $k$, se cumple $0 < \frac{k}{7} < 1$. En cada uno de los $5$ periodos de longitud $2\pi$, la ecuación $\sin(u) = \frac{k}{7}$ tiene exactamente $2$ soluciones. Esto aporta $6 \times 5 \times 2 = \mathbf{60}$ **soluciones**.
3. **Para $k \in \{-6, -5, -4, -3, -2, -1\}$:** De manera análoga, para cada uno de estos $6$ valores se tiene $-1 < \frac{k}{7} < 0$, lo que produce $2$ soluciones por cada uno de los $5$ periodos. Esto aporta $6 \times 5 \times 2 = \mathbf{60}$ **soluciones**.
4. **Para $k = 7$:** $\sin(u) = 1$. En cada periodo de longitud $2\pi$ hay exactamente $1$ solución ($u = \frac{\pi}{2} + 2m\pi$). En los $5$ periodos tenemos **$5$ soluciones**.
5. **Para $k = -7$:** $\sin(u) = -1$. En cada periodo de longitud $2\pi$ hay exactamente $1$ solución ($u = \frac{3\pi}{2} + 2m\pi$). En los $5$ periodos tenemos **$5$ soluciones**.

Sumando todos los casos, el número total de soluciones es:
$$n = 9 + 60 + 60 + 5 + 5 = 139$$

---

### Paso 2: Encontrar el número de puntos de tangencia $t$
La gráfica de $y = f(x)$ es tangente al eje $x$ en $x_0$ si $f(x_0) = 0$ y además su derivada se anula, es decir, $f'(x_0) = 0$. Calculamos la derivada usando la regla de la cadena:
$$f'(x) = 35\pi \cos(5x) \cos\left(7\pi \cdot \sin(5x)\right)$$

En cualquiera de las $n$ raíces donde $7\pi \cdot \sin(5x) = k\pi$, tenemos que:
$$\cos\left(7\pi \cdot \sin(5x)\right) = \cos(k\pi) = (-1)^k \neq 0$$

Por consiguiente, en una raíz de $f(x)$, se cumple que:
$$f'(x) = 0 \iff \cos(5x) = 0 \iff \sin(5x) = \pm 1$$

Esto corresponde exactamente a los casos $k = 7$ y $k = -7$ (además, en estos puntos $f''(x) \neq 0$, por lo que son extremos locales donde la gráfica toca el eje $x$ sin cruzarlo).

Sumando las soluciones correspondientes a $k = 7$ y $k = -7$, obtenemos:
$$t = 5 + 5 = 10$$

---

### Paso 3: Calcular $n + t$
$$n + t = 139 + 10 = 149$$

\boxed{149}