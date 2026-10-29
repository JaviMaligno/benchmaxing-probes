## Resolución

**Paso 1: Expresar $b_3$ en función de $b_1$.**

$$b_2 = -\frac{1}{1+b_1}, \qquad b_3 = -\frac{1}{1+b_2} = -\frac{1}{1 - \frac{1}{1+b_1}} = -\frac{1+b_1}{(1+b_1)-1} = -\frac{1+b_1}{b_1}.$$

**Paso 2: Imponer la condición $b_3 = b_1$.**

$$-\frac{1+b_1}{b_1} = b_1 \;\Longrightarrow\; -(1+b_1) = b_1^2 \;\Longrightarrow\; b_1^2 + b_1 + 1 = 0.$$

Multiplicando por $(b_1 - 1)$: $b_1^3 - 1 = 0$, es decir, $b_1^3 = 1$ (con $b_1 \neq 1$; $b_1$ es una raíz cúbica primitiva de la unidad).

**Paso 3: Ubicar $b_9$.**

Como $b_3 = b_1$, la recurrencia es determinista, así que la sucesión tiene período 2: $b_1, b_2, b_1, b_2, \dots$ Los índices impares valen $b_1$, de modo que $b_9 = b_1$.

**Paso 4: Calcular la potencia.**

$$(b_9)^9 = b_1^9 = (b_1^3)^3 = 1^3 = 1.$$

$$\boxed{1}$$