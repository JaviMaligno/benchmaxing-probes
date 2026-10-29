## Razonamiento paso a paso

**Planteamiento.** Sea $n$ el número de monedas en cada una de las 7 bolsas originales. Antes de encontrar la nueva bolsa tienes $7n$ monedas. Después tienes $7n + 53$ monedas en total.

**Condición 1: reparto exacto en 8 bolsas.**
$$7n + 53 \equiv 0 \pmod{8}$$
Como $7 \equiv -1 \pmod 8$ y $53 \equiv 5 \pmod 8$:
$$-n + 5 \equiv 0 \pmod 8 \implies n \equiv 5 \pmod 8$$
Entonces $n \in \{5, 13, 21, 29, 37, \dots\}$

**Condición 2: más de 200 monedas en total.**
$$7n + 53 > 200 \implies 7n > 147 \implies n \geq 22$$

**Combinando ambas condiciones.** El menor valor de $n$ que es $\geq 22$ y además $\equiv 5 \pmod 8$ es $n = 29$.

- Nota: $n = 21$ da un total de $147 + 53 = 200$, que **no** es más de 200, así que se descarta.

**Verificación con $n = 29$:**
$$7 \cdot 29 + 53 = 203 + 53 = 256 = 8 \cdot 32 \checkmark \quad \text{y} \quad 256 > 200 \checkmark$$

Por tanto, el total antes de encontrar la bolsa era $7 \cdot 29 = 203$ monedas.

\boxed{203}