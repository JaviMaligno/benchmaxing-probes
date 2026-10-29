## Razonamiento paso a paso

**1. Definir la variable:**
Sea $n$ el número de monedas en cada una de las 7 bolsas originales. El total inicial es $7n$.

**2. Tras encontrar la bolsa de 53 monedas:**
El total pasa a ser $7n + 53$, y debe repartirse equitativamente entre 8 bolsas. Por tanto:
$$7n + 53 \equiv 0 \pmod{8}$$

**3. Resolver la congruencia:**
Como $53 = 6 \times 8 + 5$, tenemos $53 \equiv 5 \pmod{8}$, así que:
$$7n \equiv -5 \equiv 3 \pmod{8}$$
El inverso de 7 módulo 8 es 7 (pues $7 \times 7 = 49 \equiv 1 \pmod{8}$), luego:
$$n \equiv 3 \times 7 \equiv 21 \equiv 5 \pmod{8}$$
Es decir, $n \in \{5, 13, 21, 29, 37, \dots\}$.

**4. Condición de más de 200 monedas:**
$$7n + 53 > 200 \implies 7n > 147 \implies n > 21$$

**5. Encontrar el menor $n$ válido:**
- $n = 21$ no cumple $n > 21$ (daría $7 \times 21 + 53 = 200$, que no es mayor que 200).
- $n = 29$ sí cumple: $7 \times 29 + 53 = 203 + 53 = 256$, y $256 / 8 = 32$ monedas por bolsa, con $256 > 200$. ✓

**6. Monedas antes de encontrar la bolsa:**
$$7n = 7 \times 29 = 203$$

$$\boxed{203}$$