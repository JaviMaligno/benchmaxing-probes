## Solución

**Paso 1: Factorizar la ecuación**

$$12x^2 - xy - 6y^2 = 0$$

Busco dos binomios $(ax+by)(cx+dy)$ con $ac=12$, $bd=-6$, $ad+bc=-1$:

$$(3x+2y)(4x-3y) = 12x^2 - 9xy + 8xy - 6y^2 = 12x^2 - xy - 6y^2 \checkmark$$

Como el producto es cero, hay dos casos: $3x+2y=0$ o $4x-3y=0$.

**Paso 2: Caso 1 — $3x+2y=0$**

Despejo $y = -\frac{3x}{2}$, así que $x$ debe ser par: escribo $x=2k$, $y=-3k$ con $k$ entero.

- $x = 2k \in [-100, 100] \Rightarrow k \in [-50, 50]$
- $y = -3k \in [-100, 100] \Rightarrow k \in [-33, 33]$

La intersección es $k \in [-33, 33]$: **67 soluciones**.

**Paso 3: Caso 2 — $4x-3y=0$**

Despejo $y = \frac{4x}{3}$, así que $x$ debe ser múltiplo de 3: escribo $x=3k$, $y=4k$ con $k$ entero.

- $x = 3k \in [-100, 100] \Rightarrow k \in [-33, 33]$
- $y = 4k \in [-100, 100] \Rightarrow k \in [-25, 25]$

La intersección es $k \in [-25, 25]$: **51 soluciones**.

**Paso 4: Verificar el solapamiento**

Un punto que cumple ambas ecuaciones: de la segunda $y = \frac{4x}{3}$; sustituyendo en la primera: $3x + \frac{8x}{3} = 0 \Rightarrow x = 0$, es decir, solo el origen $(0,0)$ está contado dos veces.

**Paso 5: Total**

$$67 + 51 - 1 = 117$$

$\boxed{117}$