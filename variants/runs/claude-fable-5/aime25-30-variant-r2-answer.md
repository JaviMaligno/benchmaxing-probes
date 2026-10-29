## Planteamiento

Para $x>0$, $g(x)\to+\infty$ cuando $x\to 0^+$ y cuando $x\to\infty$. Que el mínimo valor $m$ se alcance en exactamente dos puntos positivos $x_1, x_2$ equivale a que

$$(x-8)(x-50)(x-72)(x-k) - mx \;=\; (x^2 - ux + v)^2,$$

donde $u = x_1+x_2 > 0$ y $v = x_1 x_2 > 0$ (ambos puntos de tangencia positivos y distintos).

## Comparación de coeficientes

Con $P(x) = x^4 - e_1x^3 + e_2x^2 - e_3x + e_4$, donde

- $e_1 = 130 + k$
- $e_2 = 4576 + 130k$
- $e_3 = 28800 + 4576k$
- $e_4 = 28800k$,

igualando con $(x^2-ux+v)^2 = x^4 - 2ux^3 + (u^2+2v)x^2 - 2uvx + v^2$:

1. $u = \dfrac{130+k}{2}$
2. $v = \dfrac{e_2 - u^2}{2} = \dfrac{-k^2 + 260k + 1404}{8}$
3. $2uv = e_3 + m$ (esto solo determina $m$)
4. $v^2 = 28800k$

Como $v>0$, de (2) y (4):

$$-k^2 + 260k + 1404 = 960\sqrt{2k}.$$

## Resolución

Con $t = \sqrt{k}$:

$$t^4 - 260t^2 + 960\sqrt{2}\,t - 1404 = 0.$$

Buscando una factorización $(t^2 + at + b)(t^2 - at + c)$ con $a = \alpha\sqrt2$, la condición sobre $\beta = \alpha^2$ es

$$\beta^3 - 260\beta^2 + 18304\beta - 230400 = 0,$$

que tiene la raíz $\beta = 16$, es decir $a = 4\sqrt2$, $b = -234$, $c = 6$:

$$\left(t^2 + 4\sqrt2\,t - 234\right)\left(t^2 - 4\sqrt2\,t + 6\right) = 0.$$

Las raíces positivas son $t = 9\sqrt2,\; 3\sqrt2,\; \sqrt2$, lo que da

$$k = 162,\quad 18,\quad 2.$$

## Verificación

Para cada valor: $-k^2+260k+1404 > 0$ (así $v>0$), $u^2 - 4v > 0$ (dos puntos distintos) y $m = 2uv - e_3 < 0$. Por ejemplo, con $k=18$: $u=74$, $v=720$, $u^2-4v = 2596 > 0$ y $m = -4608 < 0$. Los tres valores cumplen todas las condiciones, y son exactamente tres, como pide el enunciado.

$$2 + 18 + 162 = \boxed{182}$$