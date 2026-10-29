Para encontrar la suma de las coordenadas $y$ de todos los puntos de intersección entre la parábola $x = 66y^2$ y la gráfica de $y = g(x)$, analicemos los tramos que componen la función periódica $g(x)$.

### Paso 1: Acotar la región de intersección y analizar los vértices
Dado que $g(x) \in [-1, 1]$ para todo $x \in \mathbb{R}$, cualquier punto de intersección $(x, y)$ debe satisfacer $y \in [-1, 1]$. Como $x = 66y^2$, esto implica que $x \in [0, 66]$.

Los vértices del zigzag ocurren cuando $y = 1$ (en $x = 4k + 1$) y cuando $y = -1$ (en $x = 4k - 1$). Si la parábola pasara por alguno de estos vértices, tendríamos $x = 66(\pm 1)^2 = 66$. Como $66 \equiv 2 \pmod 4$, $x = 66$ no es de la forma $4k + 1$ ni $4k - 1$. Por lo tanto, ningún punto de intersección ocurre en los extremos de los tramos, y todos se encuentran en el interior abierto $y \in (-1, 1)$.

---

### Paso 2: Intersecciones en los tramos crecientes
Para cada $k \in \mathbb{Z}$, el tramo creciente en el intervalo $x \in [4k - 1, 4k + 1]$ está dado por $y = x - 4k$, es decir:
$$x = 4k + y, \quad y \in [-1, 1].$$

Sustituyendo en la ecuación de la parábola $x = 66y^2$, obtenemos la ecuación cuadrática:
$$f_k(y) = 66y^2 - y - 4k = 0.$$

Como $x \ge 0$, para $k < 0$ el intervalo $[4k - 1, 4k + 1]$ es completamente negativo y no hay intersecciones. Para $k \ge 0$, el vértice de la parábola $f_k(y)$ está en $y = \frac{1}{132} \in (-1, 1)$, donde $f_k$ toma un valor negativo ($-4k - \frac{1}{264} < 0$). Por tanto, el número de raíces en $[-1, 1]$ depende del signo de $f_k(y)$ en los extremos $y = -1$ y $y = 1$:
- $f_k(-1) = 67 - 4k$
- $f_k(1) = 65 - 4k$

Analizamos según el valor de $k$:
1. **Para $0 \le k \le 16$:** Se cumple que $f_k(-1) > 0$ y $f_k(1) > 0$. Por el teorema del valor intermedio, ambas raíces de $66y^2 - y - 4k = 0$ pertenecen a $(-1, 1)$. Por las relaciones de Vieta, la suma de las dos raíces para cada $k$ es $\frac{1}{66}$. Como hay $17$ valores de $k$ (desde $k = 0$ hasta $k = 16$), la suma de las coordenadas $y$ en estos tramos es:
   $$S_{\text{crec}} = 17 \cdot \frac{1}{66} = \frac{17}{66}.$$
2. **Para $k \ge 17$:** Tanto $f_k(-1) < 0$ como $f_k(1) < 0$, por lo que no hay raíces en $[-1, 1]$.

---

### Paso 3: Intersecciones en los tramos decrecientes
Para cada $k \in \mathbb{Z}$, el tramo decreciente en el intervalo $x \in [4k + 1, 4k + 3]$ está dado por $y = 2 - (x - 4k)$, es decir:
$$x = 4k + 2 - y, \quad y \in [-1, 1].$$

Sustituyendo en $x = 66y^2$, obtenemos:
$$h_k(y) = 66y^2 + y - (4k + 2) = 0.$$

Nuevamente, para $k < 0$ no hay soluciones porque $x \le 4(-1) + 3 = -1 < 0$. Para $k \ge 0$, el vértice de $h_k(y)$ está en $y = -\frac{1}{132} \in (-1, 1)$, donde $h_k$ es negativo. Evaluando en los extremos:
- $h_k(-1) = 63 - 4k$
- $h_k(1) = 65 - 4k$

Analizamos según el valor de $k$:
1. **Para $0 \le k \le 15$:** Se tiene $h_k(-1) > 0$ y $h_k(1) > 0$, por lo que ambas raíces están en $(-1, 1)$. Por las fórmulas de Vieta, la suma de las dos raíces para cada $k$ es $-\frac{1}{66}$. Como hay $16$ valores de $k$ (desde $k = 0$ hasta $k = 15$), su contribución a la suma es:
   $$S_{\text{decrec}, 1} = 16 \cdot \left(-\frac{1}{66}\right) = -\frac{16}{66}.$$
2. **Para $k = 16$:** Tenemos $h_{16}(-1) = -1 < 0$ y $h_{16}(1) = 1 > 0$. Esto significa que exactamente una raíz pertenece al intervalo $(-1, 1)$. La ecuación para $k = 16$ es:
   $$66y^2 + y - 66 = 0.$$
   Aplicando la fórmula cuadrática y tomando la raíz positiva (que es la que cae en $(-1, 1)$):
   $$y = \frac{-1 + \sqrt{1^2 - 4(66)(-66)}}{2(66)} = \frac{-1 + \sqrt{1 + 17424}}{132} = \frac{-1 + \sqrt{17425}}{132}.$$
3. **Para $k \ge 17$:** Tanto $h_k(-1) < 0$ como $h_k(1) < 0$, por lo que no hay más intersecciones.

---

### Paso 4: Suma total y simplificación
Sumando todas las contribuciones obtenidas:
$$S = \frac{17}{66} - \frac{16}{66} + \frac{-1 + \sqrt{17425}}{132} = \frac{1}{66} + \frac{-1 + \sqrt{17425}}{132} = \frac{1 + \sqrt{17425}}{132}.$$

Factorizamos $17425$ para extraer factores cuadrados:
$$17425 = 25 \times 697 = 5^2 \times 17 \times 41.$$
Como $697 = 17 \times 41$ es libre de cuadrados, tenemos $\sqrt{17425} = 5\sqrt{697}$, de modo que:
$$S = \frac{1 + 5\sqrt{697}}{132}.$$

Identificando los valores con la expresión $\frac{a + b\sqrt{c}}{d}$, tenemos $a = 1$, $b = 5$, $c = 697$ y $d = 132$, los cuales cumplen que $\gcd(1, 5, 132) = 1$ y $697$ no es divisible por el cuadrado de ningún primo.

Finalmente, calculamos $a + b + c + d$:
$$a + b + c + d = 1 + 5 + 697 + 132 = 835.$$

\boxed{835}