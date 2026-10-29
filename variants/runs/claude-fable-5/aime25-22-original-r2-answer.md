Factorizamos: $2025 = 3^4 \cdot 5^2$, así que $A$ tiene $5 \cdot 3 = 15$ divisores, y hay $2^{15} = 32768$ subconjuntos posibles de $A$.

**Condición para lcm = 2025:** el subconjunto $B$ debe contener al menos un divisor divisible por $3^4$ y al menos uno divisible por $5^2$ (eso garantiza automáticamente que sea no vacío).

- Divisores con $3^4$: son $3^4 \cdot 5^j$ con $j \in \{0,1,2\}$, es decir **3 divisores**.
- Divisores con $5^2$: son $3^i \cdot 5^2$ con $i \in \{0,\dots,4\}$, es decir **5 divisores**.
- La unión de ambos conjuntos tiene $3 + 5 - 1 = 7$ divisores (el común es $2025$).

**Inclusión-exclusión** sobre los subconjuntos que fallan alguna condición:

$$2^{15} - 2^{12} - 2^{10} + 2^{8} = 32768 - 4096 - 1024 + 256 = 27904.$$

La probabilidad es

$$\frac{27904}{32768} = \frac{109}{128},$$

con $\gcd(109, 128) = 1$. Por lo tanto $m + n = 109 + 128 = 237$.

$$\boxed{237}$$