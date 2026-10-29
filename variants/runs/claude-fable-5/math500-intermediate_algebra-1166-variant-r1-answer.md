## Resolución

**Paso 1: Reducir variables.** Sea $s = x + y$. Para $s$ fijo, el numerador $(s+z)[4s^2 + (s+z)^2]$ no depende de cómo se reparte $s$ entre $x$ e $y$, mientras que el denominador contiene $xy$, que por AM-GM se maximiza cuando $x = y = s/2$, dando $xy \le s^2/4$. Por tanto conviene tomar $x = y$, y la expresión queda acotada inferiormente por

$$\frac{(s+z)\left[4s^2 + (s+z)^2\right]}{\frac{s^2}{4}\,z} = \frac{4(s+z)\left[4s^2 + (s+z)^2\right]}{s^2 z}.$$

**Paso 2: Homogeneidad.** La expresión es homogénea de grado 0, así que fijamos $t = z/s$:

$$g(t) = \frac{4(1+t)\left[4 + (1+t)^2\right]}{t} = \frac{4\left[(1+t)^3 + 4(1+t)\right]}{t}.$$

Expandiendo $(1+t)^3 + 4(1+t) = t^3 + 3t^2 + 7t + 5$, obtenemos

$$g(t) = 4\left(t^2 + 3t + 7 + \frac{5}{t}\right).$$

**Paso 3: Minimizar.** Derivando:

$$g'(t) = 4\left(2t + 3 - \frac{5}{t^2}\right) = 0 \;\Longrightarrow\; 2t^3 + 3t^2 - 5 = 0.$$

Se factoriza como $(t-1)(2t^2 + 5t + 5) = 0$, cuya única raíz positiva es $t = 1$ (el factor cuadrático no tiene raíces reales). Como $g(t) \to \infty$ cuando $t \to 0^+$ y $t \to \infty$, se trata de un mínimo.

**Paso 4: Evaluar.**

$$g(1) = 4(1 + 3 + 7 + 5) = 64.$$

**Verificación:** con $x = y = 1$, $z = 2$: $x+y+z = 4$, $2x+2y = 4$, y la expresión vale $\dfrac{4(16+16)}{1\cdot 1\cdot 2} = \dfrac{128}{2} = 64$. ✓

$$\boxed{64}$$