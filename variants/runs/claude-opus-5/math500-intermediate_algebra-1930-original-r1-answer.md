## Planteamiento

Como $x=0$ no es raíz, divido entre $x^2$:

$$x^2 + \frac{1}{x^2} + a\left(x+\frac1x\right) - b = 0$$

Con $y = x + \dfrac{1}{x}$ se tiene $x^2+\dfrac1{x^2} = y^2-2$, luego

$$y^2 + ay - 2 - b = 0.$$

Para que $y$ provenga de un $x$ real se requiere $|y| \ge 2$.

## Análisis de los dos casos

Despejando: $b = y^2 + ay - 2$.

**Caso $y \ge 2$:** $b = y^2+ay-2 \ge 4 + 2a - 2 = 2+2a \ge 2 > 1$, imposible porque $b \le 1$.

**Caso $y \le -2$:** escribo $y=-t$ con $t \ge 2$, y entonces $b = t^2 - at - 2$. Esta parábola en $t$ tiene vértice en $t = a/2 \le 1/2 < 2$, así que es creciente en $[2,\infty)$. Su recorrido es $[\,2-2a,\ \infty)$.

Por tanto existe raíz real si y solo si

$$b \ge 2-2a.$$

## Cálculo del área

Dentro del cuadrado $0\le a,b\le 1$, la condición $b\ge 2-2a$ exige $2-2a\le 1$, es decir $a \ge \tfrac12$. Para cada $a\in[\tfrac12,1]$ la longitud admisible de $b$ es $1-(2-2a)=2a-1$:

$$\int_{1/2}^{1} (2a-1)\,da = \Big[a^2-a\Big]_{1/2}^{1} = 0 - \left(-\tfrac14\right) = \tfrac14.$$

Es el triángulo de vértices $(\tfrac12,1)$, $(1,0)$, $(1,1)$, de área $\tfrac12\cdot\tfrac12\cdot 1 = \tfrac14$.

\boxed{\dfrac{1}{4}}