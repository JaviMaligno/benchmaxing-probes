**Planteamiento.** Los puntos de intersección satisfacen $y = f(34y^2)$. Como $f$ toma valores en $[-1,1]$, se cumple $y^2 \le 1$, es decir $x = 34y^2 \le 34$, lo que garantiza un número finito de soluciones. Además $x \ge 0$, así que solo importan las ramas con $x \in [0, 34]$.

**Ramas crecientes:** para $x \in [4k-1,\ 4k+1)$, vale $f(x) = x - 4k$. La ecuación $y = 34y^2 - 4k$ da
$$34y^2 - y - 4k = 0 \quad\Rightarrow\quad y = \frac{1 \pm \sqrt{1+544k}}{68}.$$
La condición de rama equivale a $y \in [-1, 1)$. Se cumple para ambas raíces exactamente cuando $k = 0, 1, \dots, 8$ (con $k \ge 9$ la raíz positiva ya supera $1$, y para $k \le -1$ no hay $x \ge 0$). Son $9$ valores de $k$, dos raíces cada uno, y la suma de raíces de cada ecuación es $\frac{1}{34}$:
$$S_1 = 9 \cdot \frac{1}{34} = \frac{18}{68}.$$

**Ramas decrecientes:** para $x \in [4k+1,\ 4k+3)$, vale $f(x) = 4k + 2 - x$. La ecuación $y = 4k + 2 - 34y^2$ da
$$34y^2 + y - 4k - 2 = 0 \quad\Rightarrow\quad y = \frac{-1 \pm \sqrt{544k + 273}}{68}.$$
Ahora la condición de rama equivale a $y \in (-1, 1]$. La raíz positiva es válida para $k = 0,\dots,8$, pero la negativa solo para $k \le 7$ (con $k = 8$: $\sqrt{4625} > 67$, luego $y_- < -1$). La suma de ambas raíces es $-\frac{1}{34}$, así que:
$$S_2 = 8\cdot\left(-\frac{1}{34}\right) + \frac{-1 + \sqrt{4625}}{68} = \frac{-16 + 5\sqrt{185} - 1}{68} = \frac{5\sqrt{185} - 17}{68},$$
usando que $\sqrt{4625} = \sqrt{25 \cdot 185} = 5\sqrt{185}$.

**Suma total.**
$$S_1 + S_2 = \frac{18}{68} + \frac{5\sqrt{185} - 17}{68} = \frac{1 + 5\sqrt{185}}{68}.$$

Esto da $a = 1$, $b = 5$, $c = 185$ (libre de cuadrados, pues $185 = 5 \cdot 37$) y $d = 68$, con $\gcd(1, 5, 68) = 1$. Por lo tanto:
$$a + b + c + d = 1 + 5 + 185 + 68 = \boxed{259}$$