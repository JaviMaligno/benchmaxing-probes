

Resolvamos la congruencia $22x \equiv 38 \pmod{100}$.

**Paso 1: Verificar existencia de soluciones.**
$\gcd(22,100)=2$, y como $2 \mid 38$, existen exactamente $2$ soluciones módulo $100$.

**Paso 2: Simplificar.**
Dividiendo entre $2$:
$$11x \equiv 19 \pmod{50}$$

**Paso 3: Hallar el inverso de $11$ módulo $50$.**
Como $11 \cdot 41 = 451 = 9\cdot 50 + 1$, se tiene $11^{-1} \equiv 41 \pmod{50}$.

**Paso 4: Despejar $x$.**
$$x \equiv 19 \cdot 41 = 779 \equiv 29 \pmod{50}$$

**Paso 5: Soluciones módulo $100$.**
$$x \equiv 29 \quad \text{o} \quad x \equiv 79 \pmod{100}$$

Verificación: $22\cdot 29 = 638 \equiv 38 \pmod{100}$ ✓, y $22\cdot 79 = 1738 \equiv 38 \pmod{100}$ ✓.

Las dos menores soluciones enteras positivas son $29$ y $79$, cuyo promedio es:
$$\frac{29+79}{2} = 54$$

$$\boxed{54}$$