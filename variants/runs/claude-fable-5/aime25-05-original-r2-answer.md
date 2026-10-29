## Solución

**Divisibilidad por 22 = 2 × 11.**

**Condición de divisibilidad por 11:** la suma de dígitos en posiciones impares menos la de posiciones pares debe ser múltiplo de 11. La suma total de los dígitos 1–8 es 36. Si $S_p$ es la suma en posiciones pares, necesitamos $36 - 2S_p \equiv 0 \pmod{11}$, es decir $2S_p \equiv 3 \pmod{11}$, lo que da $S_p \equiv 7 \pmod{11}$. Como $S_p$ es la suma de 4 dígitos distintos de 1–8, está entre 10 y 26, así que $S_p = 18$ (y por tanto ambas mitades suman 18).

**Subconjuntos de 4 dígitos que suman 18:**
$$\{1,2,7,8\},\{1,3,6,8\},\{1,4,5,8\},\{1,4,6,7\},\{2,3,5,8\},\{2,3,6,7\},\{2,4,5,7\},\{3,4,5,6\}$$
Son 8 subconjuntos, y **cada uno contiene exactamente 2 dígitos pares** (se verifica caso por caso).

**Condición de divisibilidad por 2:** el último dígito (posición 8, que es posición par) debe ser par.

**Conteo por cada subconjunto** asignado a las posiciones pares:
- Posición 8: 2 opciones (los 2 dígitos pares del subconjunto).
- Posiciones 2, 4, 6: $3! = 6$ formas con los restantes.
- Posiciones impares: $4! = 24$ formas.

Total por subconjunto: $2 \cdot 6 \cdot 24 = 288$.

Entonces $N = 8 \cdot 288 = 2304$, y la diferencia pedida es $2304 - 2025 = 279$.

$$\boxed{279}$$