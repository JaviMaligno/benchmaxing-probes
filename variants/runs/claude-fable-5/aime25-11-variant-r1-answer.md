## Planteamiento

La parábola $x = 66y^2$ solo corta a la gráfica donde $|y| \le 1$ (pues $g$ oscila entre $-1$ y $1$), así que $x \in [0, 66]$. La gráfica de $g$ consta de dos familias de segmentos:

- **Ascendentes:** $y = x - 4k$ para $x \in [4k-1,\, 4k+1)$, es decir $y \in [-1, 1)$.
- **Descendentes:** $y = (4k+2) - x$ para $x \in [4k+1,\, 4k+3)$, es decir $y \in (-1, 1]$.

## Segmentos ascendentes

Sustituyendo $x = 66y^2$: $\;66y^2 - y - 4k = 0$, con raíces $y = \dfrac{1 \pm \sqrt{1 + 1056k}}{132}$. La condición $x \in [4k-1, 4k+1)$ equivale a $y \in [-1, 1)$:

- $y_+ < 1 \iff \sqrt{1+1056k} < 131 \iff k \le 16$.
- $y_- \ge -1 \iff \sqrt{1+1056k} \le 133 \iff k \le 16$.

Para $k = 0, 1, \dots, 16$ ambas raíces son válidas, y cada par suma $\frac{1}{66}$ (Vieta). Aporte total: $\dfrac{17}{66}$.

## Segmentos descendentes

Sustituyendo: $\;66y^2 + y - (4k+2) = 0$, con raíces $y = \dfrac{-1 \pm \sqrt{1056k + 529}}{132}$. La condición equivale a $y \in (-1, 1]$:

- $y_+ \le 1 \iff \sqrt{1056k+529} \le 133 \iff k \le 16$.
- $y_- > -1 \iff \sqrt{1056k+529} < 131 \iff k \le 15$.

Para $k = 0, \dots, 15$ ambas raíces valen y cada par suma $-\frac{1}{66}$: aporte $-\dfrac{16}{66}$.

Para $k = 16$ solo sobrevive la raíz positiva:
$$y_+ = \frac{-1 + \sqrt{1056 \cdot 16 + 529}}{132} = \frac{-1 + \sqrt{17425}}{132} = \frac{-1 + 5\sqrt{697}}{132},$$
pues $17425 = 25 \cdot 697$ y $697 = 17 \cdot 41$ es libre de cuadrados. (Se verifica que $x = 66 - y_+ \in [65, 66] \subset [65, 67)$.)

## Suma total

$$\frac{17}{66} - \frac{16}{66} + \frac{-1 + 5\sqrt{697}}{132} = \frac{2}{132} + \frac{-1 + 5\sqrt{697}}{132} = \frac{1 + 5\sqrt{697}}{132}.$$

Así $a = 1$, $b = 5$, $c = 697$, $d = 132$, con $\gcd(1,5,132) = 1$ y $697$ libre de cuadrados.

$$a + b + c + d = 1 + 5 + 697 + 132 = \boxed{835}$$