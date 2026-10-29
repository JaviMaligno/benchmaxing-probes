Resolvamos la congruencia paso a paso:

**1. Simplificar la congruencia.** Como $\gcd(14, 100) = 2$ y $2 \mid 46$, hay solución, y podemos dividir todo entre 2:
$$7u \equiv 23 \pmod{50}$$

**2. Hallar el inverso de 7 módulo 50.** Buscamos $x$ tal que $7x \equiv 1 \pmod{50}$. Como $7 \cdot 43 = 301 = 6 \cdot 50 + 1$, el inverso es $43$.

**3. Despejar $u$.**
$$u \equiv 43 \cdot 23 = 989 \equiv 989 - 19\cdot 50 = 39 \pmod{50}$$

**4. Las dos soluciones positivas más pequeñas.** Son $u = 39$ y $u = 39 + 50 = 89$. (Verificación: $14 \cdot 39 = 546 \equiv 46 \pmod{100}$ ✓, y $14 \cdot 89 = 1246 \equiv 46 \pmod{100}$ ✓.)

**5. Promedio:**
$$\frac{39 + 89}{2} = 64$$

$$\boxed{64}$$