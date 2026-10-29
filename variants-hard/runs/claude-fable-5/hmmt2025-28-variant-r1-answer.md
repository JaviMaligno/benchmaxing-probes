Planteo coordenadas con el centro de la circunferencia en el origen y los lados paralelos horizontales.

**Configuración.** Por simetría del trapecio isósceles, el eje vertical de simetría pasa por el centro. Sea:
- $P = (-3, h)$, $Q = (3, h)$, con $9 + h^2 = 49$, es decir $h^2 = 40$.
- $S = (-r, k)$, $R = (r, k)$, con $r^2 + k^2 = 49$ y $r > 3$ (pues $RS > PQ$).

Como $S$ está entre $T$ y $R$ y $ST = 3$, el punto $T$ está a la izquierda de $S$: $T = (-r-3, k)$.

**Punto $N$.** El punto medio de $\overline{PT}$ es
$$N = \left(\frac{-3 + (-r-3)}{2}, \frac{h+k}{2}\right) = \left(-\frac{r+6}{2}, \frac{h+k}{2}\right).$$

**Condición de que $N$ esté en la circunferencia.**
$$\left(\frac{r+6}{2}\right)^2 + \left(\frac{h+k}{2}\right)^2 = 49 \;\Longrightarrow\; (r+6)^2 + (h+k)^2 = 196.$$

Expandiendo y usando $r^2 + k^2 = 49$ y $h^2 = 40$:
$$r^2 + 12r + 36 + h^2 + 2hk + k^2 = 196 \;\Longrightarrow\; 125 + 12r + 2hk = 196 \;\Longrightarrow\; 12r + 2hk = 71.$$

**Cálculo de $NS$.** Con $S = (-r, k)$:
$$NS^2 = \left(-r + \frac{r+6}{2}\right)^2 + \left(k - \frac{h+k}{2}\right)^2 = \frac{(6-r)^2 + (k-h)^2}{4}.$$

Expandiendo el numerador:
$$(6-r)^2 + (k-h)^2 = 36 - 12r + r^2 + k^2 + h^2 - 2hk = 36 - 12r + 49 + 40 - 2hk = 125 - (12r + 2hk).$$

Sustituyendo $12r + 2hk = 71$:
$$NS^2 = \frac{125 - 71}{4} = \frac{54}{4} = \frac{27}{2} \;\Longrightarrow\; NS = \sqrt{\frac{27}{2}} = \frac{3\sqrt{6}}{2}.$$

$$\boxed{\dfrac{3\sqrt{6}}{2}}$$