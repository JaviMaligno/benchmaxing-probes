Para hallar la suma de las coordenadas $y$ de los puntos de intersección entre la parábola $x = 34y^2$ y la función periódica $f(x)$, analicemos los tramos que componen la gráfica de $f(x)$.

### Paso 1: Caracterización de los segmentos de $f(x)$
Por la definición de $f(x)$ y su periodicidad $f(x + 4) = f(x)$, para cada número entero $k$, la gráfica de $f(x)$ consta de dos tipos de segmentos sobre un período de longitud $4$:

1. **Segmentos con pendiente $+1$:** Para $x \in [4k - 1, 4k + 1]$, tenemos
   \[y = x - 4k \iff x = 4k + y, \quad \text{con } y \in [-1, 1].\]

2. **Segmentos con pendiente $-1$:** Para $x \in [4k + 1, 4k + 3]$, tenemos
   \[y = 4k + 2 - x \iff x = 4k + 2 - y, \quad \text{con } y \in [-1, 1].\]

Observemos que en los extremos de los intervalos, donde $y = \pm 1$, la coordenada $x$ en la gráfica de $f(x)$ es siempre un número impar, mientras que en la parábola $x = 34(\pm 1)^2 = 34$ es par. Por lo tanto, la parábola nunca interseca a $f(x)$ en los vértices $(y = \pm 1)$, lo que garantiza que todas las intersecciones ocurren en el interior de los segmentos y ninguna se cuenta dos veces.

Además, como $x = 34y^2 \ge 0$ y $y \in [-1, 1]$, ningún segmento con $k < 0$ puede intersecar a la parábola (pues para $k \le -1$, $x \le -1 < 0$).

---

### Paso 2: Intersecciones en los segmentos de pendiente $+1$
Sustituyendo $x = 4k + y$ en $x = 34y^2$, obtenemos la ecuación cuadrática:
\[g_k(y) = 34y^2 - y - 4k = 0.\]

Para $k = 0$, la ecuación es $34y^2 - y = 0$, cuyas soluciones son $y = 0$ e $y = \frac{1}{34}$. Ambas pertenecen al intervalo $[-1, 1]$ y su suma es $\frac{1}{34}$.

Para $k \ge 1$, la parábola $g_k(y)$ abre hacia arriba y $g_k(0) = -4k < 0$, por lo que tiene una raíz positiva $y_+$ y una raíz negativa $y_-$. Estas raíces pertenecen al intervalo $[-1, 1]$ si y solo si $g_k(1) \ge 0$ y $g_k(-1) \ge 0$:
- $g_k(1) = 34(1)^2 - 1 - 4k = 33 - 4k \ge 0 \iff k \le 8$.
- $g_k(-1) = 34(-1)^2 - (-1) - 4k = 35 - 4k \ge 0 \iff k \le 8$.

Para $k \ge 9$, ninguna de las raíces está en $[-1, 1]$. Así, para cada $k \in \{0, 1, 2, \dots, 8\}$ (un total de $9$ valores), ambas raíces están en $[-1, 1]$. Por las relaciones de Vieta, la suma de las dos raíces para cada $k$ es $\frac{1}{34}$.

La contribución total de estos segmentos a la suma de las coordenadas $y$ es:
\[S_1 = 9 \times \frac{1}{34} = \frac{9}{34} = \frac{18}{68}.\]

---

### Paso 3: Intersecciones en los segmentos de pendiente $-1$
Sustituyendo $x = 4k + 2 - y$ en $x = 34y^2$, obtenemos la ecuación cuadrática:
\[h_k(y) = 34y^2 + y - (4k + 2) = 0.\]

Para $k \ge 0$, dado que $h_k(0) = -(4k + 2) < 0$, la ecuación tiene una raíz positiva $y_+$ y una raíz negativa $y_-$. Analizamos cuándo caen en $[-1, 1]$:
- Para la raíz positiva ($y_+ \le 1$): $h_k(1) = 34(1)^2 + 1 - (4k + 2) = 33 - 4k \ge 0 \iff k \le 8$.
- Para la raíz negativa ($y_- \ge -1$): $h_k(-1) = 34(-1)^2 - 1 - (4k + 2) = 31 - 4k \ge 0 \iff k \le 7$.

Por lo tanto:
1. Para $k \in \{0, 1, 2, \dots, 7\}$ (un total de $8$ valores), **ambas** raíces están en $[-1, 1]$. Por las relaciones de Vieta, la suma de las dos raíces para cada uno de estos valores de $k$ es $-\frac{1}{34}$. Su contribución conjunta es:
   \[S_{2,\text{pares}} = 8 \times \left(-\frac{1}{34}\right) = -\frac{8}{34} = -\frac{16}{68}.\]

2. Para $k = 8$, solo la raíz positiva $y_+$ está en $[-1, 1]$. La ecuación para $k = 8$ es:
   \[34y^2 + y - 34 = 0.\]
   Aplicando la fórmula general para la raíz positiva:
   \[y_+ = \frac{-1 + \sqrt{1^2 - 4(34)(-34)}}{2(34)} = \frac{-1 + \sqrt{1 + 4624}}{68} = \frac{-1 + \sqrt{4625}}{68}.\]
   Como $4625 = 25 \times 185$, donde $185 = 5 \times 37$ es libre de cuadrados, simplificamos:
   \[y_+ = \frac{-1 + 5\sqrt{185}}{68}.\]

3. Para $k \ge 9$, ninguna raíz pertenece a $[-1, 1]$.

---

### Paso 4: Suma total
Sumando todas las contribuciones obtenidas:
\[S = S_1 + S_{2,\text{pares}} + y_+ = \frac{18}{68} - \frac{16}{68} + \frac{-1 + 5\sqrt{185}}{68} = \frac{1 + 5\sqrt{185}}{68}.\]

Esta expresión tiene la forma $\frac{a + b\sqrt{c}}{d}$ con $a = 1$, $b = 5$, $c = 185$ y $d = 68$. Se cumple que $\gcd(1, 5, 68) = 1$ y $185$ no es divisible por el cuadrado de ningún primo.

Finalmente, calculamos $a + b + c + d$:
\[a + b + c + d = 1 + 5 + 185 + 68 = 259.\]

\boxed{259}