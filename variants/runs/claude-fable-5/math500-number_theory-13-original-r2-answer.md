Resolvamos la congruencia $14u \equiv 46 \pmod{100}$.

**Paso 1: Simplificar.** Como $\gcd(14, 100) = 2$ y $2 \mid 46$, hay soluciones. Dividimos todo entre 2:
$$7u \equiv 23 \pmod{50}$$

**Paso 2: Hallar el inverso de 7 módulo 50.** Buscamos $x$ tal que $7x \equiv 1 \pmod{50}$. Probando: $7 \cdot 43 = 301 = 6 \cdot 50 + 1$, así que el inverso es $43$.

**Paso 3: Despejar $u$.**
$$u \equiv 43 \cdot 23 = 989 \equiv 989 - 950 = 39 \pmod{50}$$

**Paso 4: Las dos soluciones positivas más pequeñas.** Son $u = 39$ y $u = 89$ (ambas verifican: $14 \cdot 39 = 546 \equiv 46$, y $14 \cdot 89 = 1246 \equiv 46 \pmod{100}$).

**Promedio:** $\dfrac{39 + 89}{2} = 64$.

$$\boxed{64}$$