Para hallar la suma de las coordenadas $y$ de los puntos de intersección entre la parábola $x = 34y^2$ y la gráfica de $y = f(x)$, analizamos la función por tramos en cada período.

### 1. Descripción de los tramos de $f(x)$
Por la definición dada y la periodicidad $f(x + 4) = f(x)$, la función $f(x)$ tiene imagen $[-1, 1]$ y, para cada entero $k \in \mathbb{Z}$, se divide en dos tramos lineales:

1. **Tramos crecientes ($U_k$):** Para $x \in [4k - 1, 4k + 1)$, tenemos
   \[y = x - 4k, \quad \text{con } y \in [-1, 1).\]
2. **Tramos decrecientes ($D_k$):** Para $x \in [4k + 1, 4k + 3)$, tenemos
   \[y = 4k + 2 - x, \quad \text{con } y \in (-1, 1].\]

Observemos que en los extremos de los intervalos donde $y = \pm 1$, la parábola toma el valor $x = 34(\pm 1)^2 = 34$, el cual no es un número impar (los extremos de los tramos ocurren en $x = 2m + 1$). Por lo tanto, ningún punto de intersección ocurre en los extremos de los tramos y la condición de pertenencia a cada tramo equivale simplemente a exigir que $y \in (-1, 1)$.

---

### 2. Intersecciones en los tramos crecientes $U_k$
Sustituyendo $x = 34y^2$ en $y = x - 4k$, obtenemos la ecuación cuadrática:
\[34y^2 - y - 4k = 0.\]
El discriminante es $\Delta = 1 + 544k$, que es no negativo si y solo si $k \ge 0$ (pues $k \in \mathbb{Z}$).

Sea $g_k(y) = 34y^2 - y - 4k$. El vértice de esta parábola está en $y = \frac{1}{68} \in (-1, 1)$, donde $g_k\left(\frac{1}{68}\right) = -\frac{1}{136} - 4k < 0$ para todo $k \ge 0$. Por tanto, sus raíces reales pertenecen al intervalo $(-1, 1)$ si y solo si la función es positiva en los extremos $y = 1$ e $y = -1$:
- $g_k(1) = 34(1)^2 - 1 - 4k = 33 - 4k > 0 \iff k \le 8$.
- $g_k(-1) = 34(-1)^2 - (-1) - 4k = 35 - 4k > 0 \iff k \le 8$.

Así, para cada $k \in \{0, 1, 2, \dots, 8\}$ (un total de $9$ valores), ambas raíces están en $(-1, 1)$, mientras que para $k \ge 9$ ninguna raíz pertenece al intervalo. Por las fórmulas de Vieta, la suma de las dos raíces para cada uno de estos $9$ valores de $k$ es $\frac{1}{34}$. La contribución total de los tramos crecientes es:
\[S_U = 9 \cdot \frac{1}{34} = \frac{9}{34}.\]

---

### 3. Intersecciones en los tramos decrecientes $D_k$
Sustituyendo $x = 34y^2$ en $y = 4k + 2 - x$, obtenemos:
\[34y^2 + y - (4k + 2) = 0.\]
El discriminante es $\Delta = 1 + 136(4k + 2)$, que es positivo para todo $k \ge 0$ (y negativo si $k \le -1$).

Sea $h_k(y) = 34y^2 + y - (4k + 2)$. Su vértice está en $y = -\frac{1}{68} \in (-1, 1)$, donde alcanza un valor negativo para $k \ge 0$. Analizamos el signo en los extremos $y = 1$ e $y = -1$:
- Para la raíz positiva: $h_k(1) = 34(1)^2 + 1 - (4k + 2) = 33 - 4k > 0 \iff k \le 8$.
- Para la raíz negativa: $h_k(-1) = 34(-1)^2 - 1 - (4k + 2) = 31 - 4k > 0 \iff k \le 7$.

Por consiguiente:
- Para $k \in \{0, 1, 2, \dots, 7\}$ ($8$ valores), ambas raíces pertenecen a $(-1, 1)$. Por las fórmulas de Vieta, la suma de cada par de raíces es $-\frac{1}{34}$, aportando en total:
  \[S_{D,1} = 8 \cdot \left(-\frac{1}{34}\right) = -\frac{8}{34}.\]
- Para $k = 8$, la ecuación es $34y^2 + y - 34 = 0$, de la cual únicamente la raíz positiva pertenece a $(-1, 1)$:
  \[y = \frac{-1 + \sqrt{1^2 - 4(34)(-34)}}{2(34)} = \frac{-1 + \sqrt{4625}}{68} = \frac{-1 + 5\sqrt{185}}{68}.\]

---

### 4. Suma total
Sumando todas las coordenadas $y$ encontradas:
\[S = \frac{9}{34} - \frac{8}{34} + \frac{-1 + 5\sqrt{185}}{68} = \frac{1}{34} + \frac{-1 + 5\sqrt{185}}{68} = \frac{2 - 1 + 5\sqrt{185}}{68} = \frac{1 + 5\sqrt{185}}{68}.\]

Esta expresión tiene la forma $\frac{a + b\sqrt{c}}{d}$ con $a = 1$, $b = 5$, $c = 185 = 5 \times 37$ (libre de cuadrados) y $d = 68$, cumpliendo $\gcd(1, 5, 68) = 1$.

Finalmente, calculamos $a + b + c + d$:
\[a + b + c + d = 1 + 5 + 185 + 68 = 259.\]

\boxed{259}