## Planteamiento

Cada depósito de $25{,}000$ se hace al **final** de cada año, así que:

| Depósito | Años que genera interés | Valor al final del año 3 |
|---|---|---|
| Año 1 | 2 | $25000(1+r)^2$ |
| Año 2 | 1 | $25000(1+r)$ |
| Año 3 | 0 | $25000$ |

Condición:
$$25000\left[(1+r)^2+(1+r)+1\right] \ge 84360$$

## Resolución

Sea $x = 1+r$:
$$x^2+x+1 \ge \frac{84360}{25000} = 3.3744$$
$$x^2+x-2.3744 \ge 0$$

Discriminante: $1 + 4(2.3744) = 10.4976$, y $\sqrt{10.4976} = 3.24$.

$$x = \frac{-1+3.24}{2} = \frac{2.24}{2} = 1.12$$

Entonces $r = 0.12$, es decir **12 %**.

**Verificación:** $25000(1.2544) + 25000(1.12) + 25000 = 31360 + 28000 + 25000 = 84360$ ✓

\boxed{12}