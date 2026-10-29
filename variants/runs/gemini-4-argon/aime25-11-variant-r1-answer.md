Para hallar la suma de las coordenadas $y$ de todos los puntos de intersección entre la parábola $x = 66y^2$ y la gráfica de $y = g(x)$, analizamos las ramas crecientes y decrecientes de la función periódica $g(x)$.

Como el rango de $g(x)$ es $[-1, 1]$, cualquier punto de intersección $(x, y)$ debe cumplir $y \in [-1, 1]$, lo que implica que $x = 66y^2 \in [0, 66]$.

En cada período $[4k - 1, 4k + 3)$ con $k \in \mathbb{Z}$, la gráfica de $y = g(x)$ consta de dos segmentos:

1. **Ramas crecientes:** En el intervalo $x \in [4k - 1, 4k + 1)$, tenemos $y = x - 4k$, es decir, $x = 4k + y$ con $y \in [-1, 1)$.
   Sustituyendo en la ecuación de la parábola $x = 66y^2$, obtenemos:
   \[66y^2 - y - 4k = 0\]
   Sea $f_k(y) = 66y^2 - y - 4k$. El vértice de esta parábola está en $y = \frac{1}{132} \in (-1, 1)$, donde $f_k\left(\frac{1}{132}\right) = -4k - \frac{1}{264}$.
   - Para $k < 0$, $f_k(y) > 0$ para todo $y \in \mathbb{R}$, por lo que no hay intersecciones reales.
   - Evaluando en los extremos del intervalo $y \in [-1, 1]$:
     \[f_k(-1) = 67 - 4k, \qquad f_k(1) = 65 - 4k\]
   - Para $k = 0, 1, 2, \dots, 16$, tanto $f_k(-1) > 0$ como $f_k(1) > 0$, mientras que en el vértice $f_k\left(\frac{1}{132}\right) < 0$. Por lo tanto, ambas raíces de la ecuación cuadrática pertenecen a $(-1, 1)$.
   - Para $k \ge 17$, se tiene $f_k(-1) < 0$ y $f_k(1) < 0$, por lo que ninguna raíz cae en $[-1, 1]$.

   Por las fórmulas de Vieta, para cada $k \in \{0, 1, \dots, 16\}$ (un total de $17$ ramas), la suma de las dos raíces es $\frac{1}{66}$. Así, la contribución total de las ramas crecientes es:
   \[S_1 = 17 \cdot \frac{1}{66} = \frac{17}{66}\]

2. **Ramas decrecientes:** En el intervalo $x \in [4k + 1, 4k + 3)$, tenemos $y = 2 - (x - 4k)$, es decir, $x = 4k + 2 - y$ con $y \in (-1, 1]$.
   Sustituyendo en $x = 66y^2$, obtenemos:
   \[66y^2 + y - (4k + 2) = 0\]
   Sea $h_k(y) = 66y^2 + y - (4k + 2)$. Su vértice está en $y = -\frac{1}{132} \in (-1, 1)$.
   - Para $k < 0$, $h_k(y) > 0$ para todo $y \in \mathbb{R}$, por lo que no hay raíces reales.
   - Evaluando en los extremos $y = -1$ y $y = 1$:
     \[h_k(-1) = 63 - 4k, \qquad h_k(1) = 65 - 4k\]
   - Para $k = 0, 1, 2, \dots, 15$ (un total de $16$ ramas), se cumple $h_k(-1) > 0$ y $h_k(1) > 0$, por lo que ambas raíces están en $(-1, 1)$. Por las fórmulas de Vieta, la suma de las dos raíces en cada una de estas ramas es $-\frac{1}{66}$, aportando en total:
     \[S_2 = 16 \cdot \left(-\frac{1}{66}\right) = -\frac{16}{66}\]
   - Para $k = 16$, la ecuación es $66y^2 + y - 66 = 0$. Como $h_{16}(-1) = -1 < 0$ y $h_{16}(1) = 1 > 0$, exactamente una raíz se encuentra en $[-1, 1]$. Resolviendo la ecuación cuadrática:
     \[y = \frac{-1 \pm \sqrt{1 - 4(66)(-66)}}{132} = \frac{-1 \pm \sqrt{17425}}{132}\]
     Dado que $132 < \sqrt{17425} < 133$, la raíz que pertenece a $[-1, 1]$ es la positiva:
     \[y_{16} = \frac{-1 + \sqrt{17425}}{132}\]
   - Para $k \ge 17$, tanto $h_k(-1) < 0$ como $h_k(1) < 0$, por lo que no hay más intersecciones en $[-1, 1]$.

Sumando todas las contribuciones obtenemos la suma total de las coordenadas $y$:
\[S = S_1 + S_2 + y_{16} = \frac{17}{66} - \frac{16}{66} + \frac{-1 + \sqrt{17425}}{132} = \frac{1}{66} + \frac{-1 + \sqrt{17425}}{132} = \frac{1 + \sqrt{17425}}{132}\]

Simplificamos el radical factorizando $17425$:
\[17425 = 25 \times 697 = 5^2 \times 17 \times 41 \implies \sqrt{17425} = 5\sqrt{697}\]

Por lo tanto, la suma es:
\[S = \frac{1 + 5\sqrt{697}}{132}\]

Identificando $a = 1$, $b = 5$, $c = 697$ (libre de cuadrados) y $d = 132$, con $\gcd(1, 5, 132) = 1$, calculamos:
\[a + b + c + d = 1 + 5 + 697 + 132 = 835\]

\boxed{835}