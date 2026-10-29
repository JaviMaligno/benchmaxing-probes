# Resolución paso a paso

**Paso 1: Plantear la fórmula de la suma de ángulos interiores.**

Para un polígono convexo de $n$ lados, la suma de todos los ángulos interiores es:
$$(n-2)\cdot 180^{\circ}$$

**Paso 2: Incorporar el dato del problema.**

Sea $x$ el ángulo que se omite. Entonces:
$$(n-2)\cdot 180^{\circ} = 1070^{\circ} + x$$

Como el polígono es convexo, cada ángulo interior cumple $0^{\circ} < x < 180^{\circ}$.

**Paso 3: Acotar la suma total.**

$$1070^{\circ} < (n-2)\cdot 180^{\circ} < 1070^{\circ} + 180^{\circ} = 1250^{\circ}$$

Dividiendo entre $180^{\circ}$:

$$5.94\ldots < n-2 < 6.94\ldots$$

El único entero posible es $n-2 = 6$, es decir, $n = 8$.

**Paso 4: Verificar.**

Con $n = 8$, la suma total es $6 \cdot 180^{\circ} = 1080^{\circ}$. El ángulo omitido sería $x = 1080^{\circ} - 1070^{\circ} = 10^{\circ}$, que es válido (mayor que $0^{\circ}$ y menor que $180^{\circ}$). ✓

\boxed{8}