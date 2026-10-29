## Planteamiento

Sean $a,b$ uniformes e independientes en $(0,4)$: el espacio muestral es el cuadrado $(0,4)^2$, de área $16$.

Existe triángulo con lados $2, a, b$ si y solo si se cumplen las tres desigualdades triangulares:
- $a + b > 2$
- $a + 2 > b \iff b - a < 2$
- $b + 2 > a \iff a - b < 2$

Es decir: $a+b > 2$ y $|a-b| < 2$.

## Cálculo del área

**Condición $|a-b| < 2$:** el complemento $|a-b| \ge 2$ son dos triángulos rectángulos dentro del cuadrado:
- $a - b \ge 2$: vértices $(2,0), (4,0), (4,2)$, área $\tfrac{1}{2}\cdot 2\cdot 2 = 2$
- $b - a \ge 2$: por simetría, área $2$

Luego el área con $|a-b| < 2$ es $16 - 4 = 12$.

**Condición $a+b > 2$:** hay que quitar de esos $12$ la parte con $a+b \le 2$. La región $a+b\le 2$ es el triángulo de vértices $(0,0),(2,0),(0,2)$, de área $2$. Dentro de ella, $|a-b|\ge 2$ exigiría por ejemplo $a\ge 2$ y $b\le 0$, que tiene medida nula. Así que toda esa región de área $2$ ya estaba contada.

Área favorable:
$$12 - 2 = 10$$

## Probabilidad

$$P = \frac{10}{16} = \frac{5}{8}$$

\boxed{\dfrac{5}{8}}