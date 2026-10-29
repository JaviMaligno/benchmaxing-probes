## Planteamiento

Partimos de la ecuación:
$$12x^2 - xy - 6y^2 = 0$$

**Paso 1: Factorizar.**

Busco dos binomios de la forma $(3x + ay)(4x + by)$, pues $3 \cdot 4 = 12$. Necesito:
- $ab = -6$
- $3b + 4a = -1$

Con $a = 2$, $b = -3$ se cumple: $ab = -6$ y $3(-3) + 4(2) = -9 + 8 = -1$. Por lo tanto:
$$(3x + 2y)(4x - 3y) = 0$$

**Paso 2: Analizar cada factor por separado.**

*Factor 1:* $3x + 2y = 0 \Rightarrow y = -\dfrac{3x}{2}$. Para que $y$ sea entero, $x$ debe ser par: $x = 2k$, con lo cual $y = -3k$.

Las restricciones $-100 \le 2k \le 100$ y $-100 \le -3k \le 100$ dan $k \in [-50, 50] \cap [-33, 33] = [-33, 33]$, es decir, **67 pares**.

*Factor 2:* $4x - 3y = 0 \Rightarrow y = \dfrac{4x}{3}$. Para que $y$ sea entero, $x$ debe ser múltiplo de 3: $x = 3m$, con lo cual $y = 4m$.

Las restricciones $-100 \le 3m \le 100$ y $-100 \le 4m \le 100$ dan $m \in [-33, 33] \cap [-25, 25] = [-25, 25]$, es decir, **51 pares**.

**Paso 3: Corregir la intersección.**

Ambas rectas se cortan en $(0,0)$, que conté dos veces. Aplicando inclusión-exclusión:
$$67 + 51 - 1 = 117$$

## Resultado

$$\boxed{117}$$