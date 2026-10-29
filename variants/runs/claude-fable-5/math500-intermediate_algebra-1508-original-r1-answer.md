Este es un problema de matemáticas, lo resuelvo directamente.

**Paso 1: Calcular $a_2$ y $a_3$ en términos de $a_1$.**

$$a_2 = \frac{1}{1-a_1}, \qquad a_3 = \frac{1}{1-a_2} = \frac{1}{1-\frac{1}{1-a_1}} = \frac{1-a_1}{(1-a_1)-1} = \frac{a_1-1}{a_1}.$$

**Paso 2: Imponer la condición $a_3 = a_1$.**

$$\frac{a_1-1}{a_1} = a_1 \;\Longrightarrow\; a_1 - 1 = a_1^2 \;\Longrightarrow\; a_1^2 - a_1 + 1 = 0.$$

**Paso 3: Usar esa relación para hallar potencias de $a_1$.**

De $a_1^2 = a_1 - 1$ se sigue:
$$a_1^3 = a_1 \cdot a_1^2 = a_1(a_1-1) = a_1^2 - a_1 = (a_1-1) - a_1 = -1.$$

**Paso 4: Identificar $a_9$.**

Como $a_3 = a_1$, la sucesión es periódica con período 3, así que $a_9 = a_6 = a_3 = a_1$. Por lo tanto:

$$(a_9)^9 = a_1^9 = (a_1^3)^3 = (-1)^3 = -1.$$

$$\boxed{-1}$$