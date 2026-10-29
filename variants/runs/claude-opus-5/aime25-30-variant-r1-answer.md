## Planteamiento

Si el mínimo $M$ se alcanza exactamente en dos puntos $x_1,x_2>0$, entonces $g(x)-M\ge 0$ en $x>0$ con ceros dobles en $x_1,x_2$. Multiplicando por $x$:

$$(x-8)(x-50)(x-72)(x-k) - Mx = (x^2-sx+p)^2,\qquad s=x_1+x_2,\ p=x_1x_2.$$

Comparando coeficientes (con $a+b+c=130$, $\sum ab = 4576$, $abc=28800$):

- $x^3$: $2s = 130+k \Rightarrow s=\dfrac{130+k}{2}$
- $x^2$: $s^2+2p = 4576+130k \Rightarrow p=\dfrac{-k^2+260k+1404}{8}$
- $x^0$: $p^2 = 28800k$
- el coeficiente de $x$ solo fija $M$ (no impone condición)

## Ecuación en $k$

$$(k^2-260k-1404)^2 = 1843200\,k$$
$$k^4-520k^3+64792k^2-1113120k+1971216=0$$

Factorizando: $(k-2)(k-18)(k^2-500k+54756)=0$, con $k^2-500k+54756=0 \Rightarrow k=\frac{500\pm176}{2}$.

Raíces: $k=2,\ 18,\ 162,\ 338$.

## Filtrado

Hace falta $p=x_1x_2>0$ (y $s^2>4p$) para que ambos puntos sean positivos y distintos:

| $k$ | $p$ | $s$ | $s^2-4p$ | válido |
|---|---|---|---|---|
| 2 | 240 | 66 | 3396 | sí |
| 18 | 720 | 74 | 2596 | sí |
| 162 | 2160 | 146 | 12676 | sí |
| 338 | $-3120$ | 234 | — | no |

Para $k=338$ se tiene $p<0$: una de las raíces es negativa, así que en $x>0$ el mínimo se alcanzaría en un solo punto. En los otros tres casos $g(x)=\frac{(x^2-sx+p)^2}{x}+M\ge M$, con igualdad exactamente en dos puntos positivos.

$$2+18+162=182$$

\boxed{182}