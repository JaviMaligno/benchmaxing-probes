Voy a resolver esto paso a paso.

**Planteamiento:** La condición $b_3 = b_1$ nos permite encontrar $b_1$.

**Calcular $b_2$ y $b_3$ en función de $b_1$:**

$$b_2 = -\frac{1}{1+b_1}, \qquad b_3 = -\frac{1}{1+b_2} = -\frac{1}{1 - \frac{1}{1+b_1}} = -\frac{1+b_1}{b_1}$$

**Imponer $b_3 = b_1$:**

$$-\frac{1+b_1}{b_1} = b_1 \;\Longrightarrow\; -(1+b_1) = b_1^2 \;\Longrightarrow\; b_1^2 + b_1 + 1 = 0$$

Las soluciones son las raíces cúbicas primitivas de la unidad, es decir, $b_1^3 = 1$ con $b_1 \neq 1$.

**La sucesión es constante:** como $b_1^2 + b_1 + 1 = 0$, se tiene $1 + b_1 = -b_1^2$, y entonces

$$b_2 = -\frac{1}{1+b_1} = \frac{1}{b_1^2} = \frac{b_1^3}{b_1^2} = b_1$$

Por lo tanto $b_n = b_1$ para todo $n$, en particular $b_9 = b_1$.

**Calcular $(b_9)^9$:**

$$(b_9)^9 = (b_1^3)^3 = 1^3 = 1$$

$$\boxed{1}$$