## Razonamiento paso a paso

**Paso 1: Expresar $a_3$ en función de $a_1$.**

$$a_2 = \frac{1}{1-a_1}, \qquad a_3 = \frac{1}{1-a_2} = \frac{1}{1-\frac{1}{1-a_1}} = \frac{1-a_1}{(1-a_1)-1} = \frac{a_1-1}{a_1} = 1 - \frac{1}{a_1}.$$

**Paso 2: Imponer la condición $a_3 = a_1$.**

$$1 - \frac{1}{a_1} = a_1 \;\Longrightarrow\; a_1 - 1 = a_1^2 \;\Longrightarrow\; a_1^2 - a_1 + 1 = 0.$$

**Paso 3: Consecuencia sobre la sucesión.**

De la ecuación: $a_1(1-a_1) = 1$, es decir $a_1 = \frac{1}{1-a_1}$, o sea que $a_1$ es un punto fijo de la transformación $f(x) = \frac{1}{1-x}$. Por tanto la sucesión es constante: $a_9 = a_1$.

(Alternativamente: $f^3(x) = x$ para todo $x$, así que la sucesión tiene periodo 3 y $a_9 = a_6 = a_3 = a_1$.)

**Paso 4: Potencias de $a_1$.**

De $a_1^2 = a_1 - 1$:
$$a_1^3 = a_1\cdot a_1^2 = a_1(a_1 - 1) = a_1^2 - a_1 = (a_1 - 1) - a_1 = -1.$$

(Equivale a $a_1 = \frac{1 \pm i\sqrt{3}}{2} = e^{\pm i\pi/3}$, una raíz sexta primitiva de la unidad.)

**Paso 5: Calcular $(a_9)^9$.**

$$(a_9)^9 = a_1^9 = (a_1^3)^3 = (-1)^3 = -1.$$

$$\boxed{-1}$$