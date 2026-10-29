## Razonamiento paso a paso

**Paso 1: Calcular $a_2$ y $a_3$ en términos de $a_1$.**

Del recurrencias:
$$a_2 = \frac{1}{1 - a_1}, \qquad a_3 = \frac{1}{1 - a_2} = \frac{1}{1 - \frac{1}{1-a_1}} = \frac{1 - a_1}{(1-a_1) - 1} = \frac{a_1 - 1}{a_1}.$$

**Paso 2: Aplicar la condición $a_3 = a_1$.**

$$\frac{a_1 - 1}{a_1} = a_1 \;\Longrightarrow\; a_1 - 1 = a_1^2 \;\Longrightarrow\; a_1^2 - a_1 + 1 = 0.$$

Las raíces son $a_1 = \frac{1 \pm i\sqrt{3}}{2} = e^{\pm i\pi/3}$ (raíces sextales primitivas de la unidad). En cualquier caso, de $a_1^2 = a_1 - 1$ se deduce:
$$a_1^3 = a_1 \cdot a_1^2 = a_1(a_1 - 1) = a_1^2 - a_1 = (a_1 - 1) - a_1 = -1.$$

**Paso 3: Determinar la periodicidad de la secuencia.**

Como $a_3 = a_1$, entonces:
$$a_4 = \frac{1}{1 - a_3} = \frac{1}{1 - a_1} = a_2,$$
y por inducción la secuencia alterna: $a_1, a_2, a_1, a_2, \dots$ Es decir, todo término de índice impar es igual a $a_1$. Por lo tanto:
$$a_9 = a_1.$$

**Paso 4: Calcular $(a_9)^9$.**

$$(a_9)^9 = a_1^9 = (a_1^3)^3 = (-1)^3 = -1.$$

*(Verificación: $a_1 = e^{i\pi/3} \Rightarrow a_1^9 = e^{3i\pi} = -1$; igual con $e^{-i\pi/3}$.)*

$$\boxed{-1}$$