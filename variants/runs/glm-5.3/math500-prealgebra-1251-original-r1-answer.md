## Planteamiento

La suma de todos los ángulos interiores de un polígono convexo de $n$ lados es:
$$S = (n-2) \cdot 180^{\circ}$$

**Paso 1:** Sean $n-1$ ángulos cuya suma es $1070^{\circ}$, y el ángulo restante $x$. Entonces:
$$(n-2) \cdot 180^{\circ} = 1070^{\circ} + x$$

**Paso 2:** Como el polígono es convexo, cada ángulo interior cumple:
$$0^{\circ} < x < 180^{\circ}$$

**Paso 3:** Por lo tanto, la suma total debe estar estrictamente entre $1070^{\circ}$ y $1250^{\circ}$:
$$1070^{\circ} < (n-2) \cdot 180^{\circ} < 1250^{\circ}$$

**Paso 4:** Probamos múltiplos de $180^{\circ}$:
- Si $n-2 = 6$: suma total $= 1080^{\circ}$ → $x = 1080^{\circ} - 1070^{\circ} = 10^{\circ}$ ✓ (válido, pues $0 < 10 < 180$)
- Si $n-2 = 7$: suma total $= 1260^{\circ}$ → $x = 190^{\circ}$ ✗ (no es convexo)

**Paso 5:** Con $n-2 = 6$, obtenemos $n = 8$.

**Verificación:** Un octógono tiene suma de ángulos de $1080^{\circ}$; si siete de ellos suman $1070^{\circ}$, el octavo mide $10^{\circ}$, lo cual es consistente con un polígono convexo. ✓

$$\boxed{8}$$