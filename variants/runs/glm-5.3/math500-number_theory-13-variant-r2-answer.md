## Resolución paso a paso

**Paso 1: Simplificar la congruencia.**
Como gcd(22, 100) = 2, y 2 divide a 38, podemos dividir todo entre 2:
$$11x \equiv 19 \pmod{50}$$

**Paso 2: Encontrar el inverso de 11 módulo 50.**
Buscamos $y$ tal que $11y \equiv 1 \pmod{50}$. Probando: $11 \cdot 41 = 451 = 9(50) + 1$, así que $11^{-1} \equiv 41 \pmod{50}$.

**Paso 3: Despejar $x$.**
$$x \equiv 19 \cdot 41 \equiv 779 \equiv 29 \pmod{50}$$

**Paso 4: Volver al módulo 100.**
Las soluciones módulo 100 son $x \equiv 29$ y $x \equiv 79 \pmod{100}$.

**Verificación:**
- $22 \cdot 29 = 638 = 6(100) + 38$ ✓
- $22 \cdot 79 = 1738 = 17(100) + 38$ ✓

**Paso 5: Promedio de las dos soluciones positivas más pequeñas.**
Las soluciones positivas más pequeñas son $29$ y $79$:
$$\frac{29 + 79}{2} = 54$$

$$\boxed{54}$$