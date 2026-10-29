Analizo el dominio de $g(x)=\dfrac{1}{|x^2-x-6|+|x^2-10x+21|}$.

**Paso 1: Condición de no-definición.**

La función no está definida exactamente cuando el denominador se anula:

$$|x^2-x-6|+|x^2-10x+21| = 0$$

Como una suma de valores absolutos es no negativa, se anula si y solo si **ambos** términos se anulan simultáneamente:

$$x^2-x-6 = 0 \quad \text{y} \quad x^2-10x+21 = 0$$

**Paso 2: Resolver cada ecuación.**

- $x^2-x-6 = (x-3)(x+2) = 0 \Rightarrow x \in \{-2,\ 3\}$
- $x^2-10x+21 = (x-3)(x-7) = 0 \Rightarrow x \in \{3,\ 7\}$

**Paso 3: Intersección.**

El único valor común es $x = 3$. Comprobación con $x=3$:

- $3^2 - 3 - 6 = 0$ ✓
- $3^2 - 10(3) + 21 = 0$ ✓

El denominador es $|0|+|0| = 0$, así que $g(3)$ no existe. En cambio, con $x=-2$ o $x=7$ solo se anula uno de los dos términos y el otro queda estrictamente positivo, por lo que $g$ sí está definida ahí.

$\boxed{3}$