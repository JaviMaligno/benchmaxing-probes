## Solución paso a paso

**Paso 1: Simplificar la congruencia.**

Como $\gcd(22, 100) = 2$ y $2 \mid 38$, podemos dividir todo entre 2:

$$11x \equiv 19 \pmod{50}$$

**Paso 2: Encontrar el inverso de 11 módulo 50.**

Como $\gcd(11, 50) = 1$, existe inverso. Probando: $11 \cdot 41 = 451 = 9 \cdot 50 + 1$, así que $11^{-1} \equiv 41 \pmod{50}$.

**Paso 3: Despejar $x$.**

$$x \equiv 19 \cdot 41 = 779 \equiv 29 \pmod{50}$$

**Paso 4: Listar las soluciones positivas.**

Las soluciones son $x \equiv 29 \pmod{50}$, es decir:

$$x = 29,\ 79,\ 129,\ \dots$$

**Verificación:** $22 \cdot 29 = 638 \equiv 38 \pmod{100}$ ✓ y $22 \cdot 79 = 1738 \equiv 38 \pmod{100}$ ✓

**Paso 5: Promediar las dos menores.**

$$\frac{29 + 79}{2} = \frac{108}{2} = 54$$

$\boxed{54}$