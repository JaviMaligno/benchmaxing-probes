## Planteamiento

Como $x=0$ no es raíz, divido entre $x^2$:

$$x^2 + \frac{1}{x^2} + a\left(x+\frac1x\right) - b = 0$$

Con la sustitución $y = x + \dfrac1x$, se tiene $x^2+\dfrac1{x^2} = y^2-2$, y la ecuación queda:

$$y^2 + ay - 2 - b = 0$$

Para que $y$ provenga de un $x$ real se necesita $|y| \ge 2$.

## Análisis de los dos casos

Despejando: $b = y^2 + ay - 2$.

**Caso $y \ge 2$:** como $a \ge 0$, resulta $b \ge 4 + 2a - 2 = 2 + 2a \ge 2 > 1$. Imposible, pues $b \le 1$.

**Caso $y \le -2$:** escribo $y = -t$ con $t \ge 2$, de modo que
$$b = f(t) = t^2 - at - 2.$$
Como $f'(t) = 2t - a \ge 4 - a > 0$ en $t\ge 2$, la función es creciente y su recorrido es $[f(2), \infty) = [2-2a, \infty)$.

Por tanto existe raíz real si y solo si
$$b \ge 2 - 2a \iff 2a + b \ge 2.$$

## Área

Dentro del cuadrado $[0,1]^2$, para cada $b \in [0,1]$ la condición da $a \in \left[1-\tfrac{b}{2},\, 1\right]$, un intervalo de longitud $\tfrac{b}{2}$ (contenido en $[0,1]$).

$$\text{Área} = \int_0^1 \frac{b}{2}\,db = \frac{1}{4}$$

Geométricamente es el triángulo de vértices $(1,0)$, $(1,1)$, $\left(\tfrac12,1\right)$, con catetos $1$ y $\tfrac12$.

\boxed{\dfrac{1}{4}}