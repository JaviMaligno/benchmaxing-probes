**Factorización y conteo de divisores.** $675 = 3^3 \cdot 5^2$, así que $S$ tiene $(3+1)(2+1) = 12$ divisores, y hay $2^{12} = 4096$ subconjuntos posibles.

**Condición para que el lcm sea 675.** El lcm de $T$ es $675$ si y solo si $T$ contiene al menos un divisor con exponente de 3 igual a 3, y al menos un divisor con exponente de 5 igual a 2. (Tal $T$ es automáticamente no vacío.)

- Divisores con $3^3$: son $3^3 \cdot 5^b$ con $b = 0,1,2$, es decir **3 divisores** (conjunto $A$).
- Divisores con $5^2$: son $3^a \cdot 5^2$ con $a = 0,1,2,3$, es decir **4 divisores** (conjunto $B$).
- Intersección $A \cap B$: solo $675$, es decir **1 divisor**, así que $|A \cup B| = 6$.

**Inclusión-exclusión.** Contamos los subconjuntos que tocan tanto $A$ como $B$:

$$2^{12} - 2^{12-3} - 2^{12-4} + 2^{12-6} = 4096 - 512 - 256 + 64 = 3392.$$

**Probabilidad.**

$$\frac{3392}{4096} = \frac{53}{64},$$

con $\gcd(53, 64) = 1$. Entonces $m + n = 53 + 64 = 117$.

$$\boxed{117}$$