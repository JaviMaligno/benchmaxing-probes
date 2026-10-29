## Resolución

**Paso 1: Verificar la solubilidad.**
$\gcd(14, 100) = 2$, y $2 \mid 46$, así que la congruencia tiene solución (exactamente 2 clases módulo 100).

**Paso 2: Dividir todo entre 2.**
$$14u \equiv 46 \pmod{100} \iff 7u \equiv 23 \pmod{50}$$

**Paso 3: Invertir 7 módulo 50.**
Como $7 \cdot 43 = 301 = 6\cdot 50 + 1$, el inverso es $43$.

**Paso 4: Despejar.**
$$u \equiv 43 \cdot 23 = 989 \equiv 989 - 19\cdot 50 = 39 \pmod{50}$$

**Paso 5: Las dos soluciones positivas más pequeñas.**
$u = 39$ y $u = 89$.

Comprobación: $14 \cdot 39 = 546 \equiv 46$, y $14 \cdot 89 = 1246 \equiv 46 \pmod{100}$. ✓

**Paso 6: Promedio.**
$$\frac{39 + 89}{2} = \frac{128}{2} = 64$$

\boxed{64}