## Planteamiento

Buscamos los puntos donde $x = 66y^2$ corta a $y = g(x)$. Como $g$ toma valores en $[-1, 1]$, se cumple $y \in [-1,1]$ y por tanto $x = 66y^2 \in [0, 66]$.

Por periodicidad, el gráfico de $g$ consiste en:
- **Segmentos ascendentes:** $y = x - 4k$ para $x \in [4k-1,\, 4k+1)$, es decir $y \in [-1, 1)$.
- **Segmentos descendentes:** $y = 4k+2 - x$ para $x \in [4k+1,\, 4k+3)$, es decir $y \in (-1, 1]$.

## Caso 1: segmentos ascendentes

Sustituyendo $x = 66y^2$: 
$$66y^2 - y - 4k = 0, \qquad y = \frac{1 \pm \sqrt{1 + 1056k}}{132}.$$

Ambas raíces deben estar en $[-1, 1)$:
- Raíz positiva $< 1$: $\sqrt{1+1056k} < 131 \Rightarrow k \le 16$.
- Raíz negativa $> -1$: $\sqrt{1+1056k} < 133 \Rightarrow k \le 16$.

Para $k = 0, 1, \dots, 16$ ambas raíces son válidas, y por Vieta cada par suma $\tfrac{1}{66}$:
$$S_1 = 17 \cdot \frac{1}{66} = \frac{17}{66}.$$

## Caso 2: segmentos descendentes

Sustituyendo:
$$66y^2 + y - (4k+2) = 0, \qquad y = \frac{-1 \pm \sqrt{1056k + 529}}{132}.$$

Condiciones con $y \in (-1, 1]$:
- Raíz positiva $\le 1$: $\sqrt{1056k+529} \le 133 \Rightarrow k \le 16$.
- Raíz negativa $> -1$: $\sqrt{1056k+529} < 131 \Rightarrow 1056k < 16632 \Rightarrow k \le 15$.

Para $k = 0, \dots, 15$ ambas raíces valen, sumando $-\tfrac{1}{66}$ cada par:
$$16 \cdot \left(-\frac{1}{66}\right) = -\frac{16}{66}.$$

Para $k = 16$ solo sobrevive la raíz positiva:
$$\sqrt{1056\cdot 16 + 529} = \sqrt{17425} = \sqrt{25 \cdot 17 \cdot 41} = 5\sqrt{697},$$
$$y = \frac{-1 + 5\sqrt{697}}{132} \approx 0.9924 \le 1 \ \checkmark \quad (x \approx 65.01 \in [65, 67),\ x \le 66\ \checkmark).$$

La raíz negativa daría $y \approx -1.008 < -1$, inválida.

## Suma total

$$S = \frac{17}{66} - \frac{16}{66} + \frac{-1 + 5\sqrt{697}}{132} = \frac{2}{132} + \frac{-1 + 5\sqrt{697}}{132} = \frac{1 + 5\sqrt{697}}{132}.$$

Aquí $a = 1$, $b = 5$, $c = 697 = 17\cdot 41$ (libre de cuadrados), $d = 132$, con $\gcd(1,5,132) = 1$.

$$a + b + c + d = 1 + 5 + 697 + 132 = \boxed{835}$$