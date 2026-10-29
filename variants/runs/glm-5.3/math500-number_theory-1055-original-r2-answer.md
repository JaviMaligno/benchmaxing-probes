# Resolución paso a paso

**Planteamiento:**
- Tengo 7 bolsas con $n$ monedas cada una → total antes: $7n$ monedas.
- Encuentro una bolsa de 53 monedas → total después: $7n + 53$ monedas en 8 bolsas.
- Para poder redistribuir equitativamente en 8 bolsas, necesito que $7n + 53$ sea divisible entre 8.
- Además, tengo más de 200 monedas.

**Condición de divisibilidad:**

$$7n + 53 \equiv 0 \pmod{8}$$

Como $7 \equiv -1 \pmod{8}$ y $53 \equiv 5 \pmod{8}$:

$$-n + 5 \equiv 0 \pmod{8} \implies n \equiv 5 \pmod{8}$$

**Candidatos:** $n \in \{5, 13, 21, 29, \dots\}$

**Verificación de la condición de más de 200 monedas:**

| $n$ | Total antes ($7n$) | Total después ($7n+53$) | ¿Divisible entre 8? | ¿>200? |
|-----|--------------------|------------------------|---------------------|--------|
| 5   | 35                 | 88                     | Sí (11 c/u)         | No ✗   |
| 13  | 91                 | 144                    | Sí (18 c/u)         | No ✗   |
| 21  | 147                | 200                    | Sí (25 c/u)         | No ✗ (200 no es *más* que 200) |
| 29  | 203                | **256**                | **Sí (32 c/u)**     | **Sí ✓** |

**Comprobación final con $n = 29$:**
- Antes: $7 \times 29 = 203$ monedas.
- Después: $203 + 53 = 256$ monedas.
- Redistribución: $256 / 8 = 32$ monedas por bolsa ✓
- $256 > 200$ ✓

**Conclusión:** El menor número de monedas posible antes de encontrar la bolsa es:

$$\boxed{203}$$