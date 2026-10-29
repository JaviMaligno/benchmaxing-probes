## Razonamiento

**Paso 1: Calcular $b_3$ en términos de $b_1$.**

$$b_2 = -\frac{1}{1+b_1}$$

$$b_3 = -\frac{1}{1+b_2} = -\frac{1}{1 - \frac{1}{1+b_1}} = -\frac{1}{\frac{(1+b_1)-1}{1+b_1}} = -\frac{1+b_1}{b_1}$$

**Paso 2: Imponer la condición $b_3 = b_1$.**

$$-\frac{1+b_1}{b_1} = b_1 \quad\Longrightarrow\quad -(1+b_1) = b_1^2 \quad\Longrightarrow\quad b_1^2 + b_1 + 1 = 0$$

**Paso 3: Usar la periodicidad.**

Como $b_3 = b_1$ y la recurrencia es la misma en cada paso, la sucesión es periódica de periodo 2:
$$b_1 = b_3 = b_5 = b_7 = b_9$$

Por lo tanto $b_9 = b_1$.

**Paso 4: Calcular $b_1^9$.**

De $b_1^2 + b_1 + 1 = 0$, multiplicando por $(b_1 - 1)$ se obtiene $b_1^3 - 1 = 0$, es decir $b_1^3 = 1$ (y $b_1 \neq 1$, pues $b_1$ es una raíz cúbica primitiva de la unidad).

$$b_9^9 = b_1^9 = (b_1^3)^3 = 1^3 = 1$$

\boxed{1}