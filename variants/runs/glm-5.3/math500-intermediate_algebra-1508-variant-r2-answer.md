## Planteamiento

La sucesión cumple $b_{k+1} = \dfrac{-1}{1+b_k}$. Llamemos $b_1 = x$.

**Paso 1: expresar $b_3$ en función de $x$.**

$$b_2 = \frac{-1}{1+x}, \qquad b_3 = \frac{-1}{1+b_2} = \frac{-1}{1+\frac{-1}{1+x}} = \frac{-1}{\frac{x}{1+x}} = -\frac{1+x}{x}.$$

**Paso 2: usar la condición $b_3 = b_1$.**

$$x = -\frac{1+x}{x} \;\Longrightarrow\; x^2 = -(1+x) \;\Longrightarrow\; x^2 + x + 1 = 0.$$

Así $x \neq 0$ y $x^3 = 1$ (raíces cúbicas primitivas de la unidad), es decir, $x^3 - 1 = (x-1)(x^2+x+1) = 0$ y $x \neq 1$.

**Paso 3: la sucesión es constante.**

De $x^2 + x + 1 = 0$ se obtiene $1 + x = -x^2$, entonces

$$b_2 = \frac{-1}{1+x} = \frac{-1}{-x^2} = \frac{1}{x^2} = x \quad (\text{pues } x^3 = 1 \Rightarrow x^{-2} = x).$$

Por lo tanto $b_k = x$ para todo $k$; en particular $b_9 = b_3 = b_1 = x$.

**Paso 4: calcular $(b_9)^9$.**

$$(b_9)^9 = x^9 = (x^3)^3 = 1^3 = 1.$$

$$\boxed{1}$$