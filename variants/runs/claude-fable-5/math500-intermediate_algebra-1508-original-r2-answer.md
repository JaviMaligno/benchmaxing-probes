La recursión es $a_{i+1} = f(a_i)$ con $f(x) = \dfrac{1}{1-x}$.

**Paso 1: La condición $a_3 = a_1$ fuerza un punto fijo.**

Calculemos $f(f(x))$:
$$f(f(x)) = \frac{1}{1 - \frac{1}{1-x}} = \frac{1-x}{(1-x) - 1} = \frac{1-x}{-x} = \frac{x-1}{x}.$$

La condición $a_3 = a_1$ dice $f(f(a_1)) = a_1$, es decir:
$$\frac{a_1 - 1}{a_1} = a_1 \quad\Longrightarrow\quad a_1 - 1 = a_1^2 \quad\Longrightarrow\quad a_1^2 - a_1 + 1 = 0.$$

Las soluciones son complejas:
$$a_1 = \frac{1 \pm i\sqrt{3}}{2} = e^{\pm i\pi/3},$$
que son raíces sextas primitivas de la unidad (satisfacen $a_1^6 = 1$, con $a_1^3 = -1$).

**Paso 2: Toda la sucesión es constante.**

Nótese que $a_1^2 = a_1 - 1$, entonces:
$$f(a_1) = \frac{1}{1-a_1} = \frac{1}{-a_1^2} = \frac{-a_1}{a_1^3} = \frac{-a_1}{-1} = a_1.$$

Así que $a_1$ es punto fijo de $f$, y por lo tanto $a_n = a_1$ para todo $n$; en particular $a_9 = a_1$.

**Paso 3: Calcular $(a_9)^9$.**

Como $a_1^3 = -1$:
$$(a_9)^9 = a_1^9 = (a_1^3)^3 = (-1)^3 = -1.$$

(Ambas raíces dan el mismo resultado.)

$$\boxed{-1}$$