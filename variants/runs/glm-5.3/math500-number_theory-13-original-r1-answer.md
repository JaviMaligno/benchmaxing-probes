## Solución

**Paso 1: Simplificar la congruencia.**
Como $\gcd(14, 100) = 2$ y $2 \mid 46$, la congruencia tiene soluciones. Dividimos todo entre 2 (incluido el módulo):

$$14u \equiv 46 \pmod{100} \;\Longleftrightarrow\; 7u \equiv 23 \pmod{50}$$

**Paso 2: Encontrar el inverso de 7 módulo 50.**
Buscamos $x$ tal que $7x \equiv 1 \pmod{50}$. Probando: $7 \cdot 43 = 301 = 6 \cdot 50 + 1$, así que $7^{-1} \equiv 43 \pmod{50}$.

**Paso 3: Despejar $u$.**
Multiplicamos ambos lados por 43:

$$u \equiv 23 \cdot 43 \equiv 989 \pmod{50}$$

Como $989 = 19 \cdot 50 + 39$, tenemos $u \equiv 39 \pmod{50}$.

**Paso 4: Hallar las dos soluciones positivas más pequeñas.**
Son $u = 39$ y $u = 89$ (pues $39 + 50 = 89$).

*Verificación:*
- $14 \cdot 39 = 546 \equiv 46 \pmod{100}$ ✓
- $14 \cdot 89 = 1246 \equiv 46 \pmod{100}$ ✓

**Paso 5: Calcular el promedio.**

$$\frac{39 + 89}{2} = \frac{128}{2} = 64$$

$$\boxed{64}$$