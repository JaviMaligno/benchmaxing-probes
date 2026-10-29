Este es un problema clásico de ecuaciones recíprocas (palindrómicas).

**Paso 1: Reducir con la sustitución recíproca.** Como $x=0$ no es raíz, divido entre $x^2$:
$$x^2 + \frac{1}{x^2} + a\left(x + \frac{1}{x}\right) - b = 0.$$

Con $t = x + \tfrac{1}{x}$ se tiene $x^2 + \tfrac{1}{x^2} = t^2 - 2$, y la ecuación queda
$$t^2 + at - (b+2) = 0.$$

La ecuación original tiene una raíz real si y solo si existe un $t$ real con $|t| \ge 2$ que satisfaga esto (pues $x + 1/x$ toma exactamente los valores con $|t|\ge 2$).

**Paso 2: Analizar los dos casos.** Despejando: $b = t^2 + at - 2$.

- Si $t \ge 2$: $b = t^2 + at - 2 \ge 4 + 2a - 2 = 2 + 2a \ge 2 > 1$, imposible con $b \le 1$.
- Si $t \le -2$: escribo $t = -s$ con $s \ge 2$, así $b = s^2 - as - 2$. La derivada respecto a $s$ es $2s - a \ge 4 - 1 > 0$, de modo que $b$ es creciente en $s$ y su mínimo se alcanza en $s = 2$: $b_{\min} = 2 - 2a$. Como $b$ crece continuamente hasta $+\infty$, existe tal $s$ si y solo si
$$b \ge 2 - 2a.$$

**Paso 3: Calcular el área.** Dentro del cuadrado $[0,1]^2$, la región $S$ es $\{(a,b): 2a + b \ge 2\}$, un triángulo con vértices $(1,0)$, $(1,1)$ y $(\tfrac12, 1)$. Su área es
$$\frac{1}{2}\cdot \frac{1}{2} \cdot 1 = \frac{1}{4}.$$

$$\boxed{\dfrac{1}{4}}$$