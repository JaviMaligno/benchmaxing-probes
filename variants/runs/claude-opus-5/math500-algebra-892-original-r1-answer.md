## Planteamiento

Para que la gráfica corte **toda** recta horizontal, el recorrido (rango) de $f$ debe ser todo $\mathbb{R}$.

Supongamos $a>0$ (necesario para que la parábola abra hacia arriba y cubra valores grandes; conviene buscar el máximo ahí).

**Rama cuadrática ($x \ge a$):** como $a>0$, se tiene $x \ge a > 0$, luego $x^2 \ge a^2$ y por tanto
$$ax^2 \ge a^3.$$
Su recorrido es $[a^3, \infty)$.

**Rama lineal ($x < a$):** $ax+2a$ es creciente (pues $a>0$), con valor límite en $x=a$ igual a $a^2+2a$ (no alcanzado). Su recorrido es
$$(-\infty,\, a^2+2a).$$

## Condición de cobertura

La unión $(-\infty,\,a^2+2a)\cup[a^3,\infty)$ es $\mathbb{R}$ si y solo si no queda hueco:
$$a^3 \le a^2 + 2a.$$

Dividiendo por $a>0$:
$$a^2 - a - 2 \le 0 \quad\Longleftrightarrow\quad (a-2)(a+1)\le 0 \quad\Longleftrightarrow\quad -1 \le a \le 2.$$

Con $a>0$ queda $0 < a \le 2$, así que el máximo candidato es $a=2$.

**Verificación con $a=2$:** la parábola $2x^2$ en $x\ge 2$ da $[8,\infty)$, y la recta $2x+4$ en $x<2$ da $(-\infty,8)$. La unión es exactamente $\mathbb{R}$. ✓

\boxed{2}