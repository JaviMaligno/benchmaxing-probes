## Planteamiento

Los puntos $(x,y)$ se eligen uniformemente en el cuadrado $(0,3)\times(0,3)$, de área total $9$.

La desigualdad triangular para lados $1, x, y$ exige:
- $x + y > 1$
- $x + 1 > y \iff y - x < 1$
- $y + 1 > x \iff x - y < 1$

Es decir: $x+y>1$ y $|x-y|<1$.

## Área del complemento

Calculo las tres regiones "malas":

**1) $x+y \le 1$:** triángulo de vértices $(0,0), (1,0), (0,1)$, área $= \tfrac12$.

**2) $y \ge x+1$:** triángulo de vértices $(0,1), (0,3), (2,3)$, área $= \tfrac{2\cdot 2}{2} = 2$.

**3) $x \ge y+1$:** por simetría, área $= 2$.

Estas regiones son esencialmente disjuntas: si $y \ge x+1$ y $x+y \le 1$, entonces $2x+1 \le 1$, o sea $x \le 0$, lo que solo da un conjunto de medida nula (análogo para el caso 3).

Área mala $= \tfrac12 + 2 + 2 = \tfrac92$.

## Probabilidad

Área favorable $= 9 - \tfrac92 = \tfrac92$, luego

$$P = \frac{9/2}{9} = \frac12$$

\boxed{\dfrac{1}{2}}