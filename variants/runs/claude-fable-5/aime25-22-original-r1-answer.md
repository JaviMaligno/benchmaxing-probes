Este es un problema de conteo con divisores. Lo resuelvo paso a paso:

**Factorización:** $2025 = 3^4 \cdot 5^2$, así que $A$ tiene $(4+1)(2+1) = 15$ divisores, y hay $2^{15} = 32768$ subconjuntos de $A$.

**Condición sobre el lcm:** El lcm de un subconjunto es $2025$ si y solo si el subconjunto contiene al menos un divisor con exponente $3^4$ y al menos un divisor con exponente $5^2$ (puede ser el mismo elemento).

- Divisores con $3^4$: son $81, 405, 2025$ → **3 divisores**.
- Divisores con $5^2$: son $25, 75, 225, 675, 2025$ → **5 divisores**.
- Divisores con $3^4$ **o** $5^2$: $3 + 5 - 1 = 7$ divisores.

**Inclusión-exclusión:** Cuento los subconjuntos que contienen al menos uno de cada tipo:

$$2^{15} - 2^{12} - 2^{10} + 2^{8} = 32768 - 4096 - 1024 + 256 = 27904$$

(Aquí $2^{12}$ cuenta los subconjuntos que evitan los 3 divisores con $3^4$, $2^{10}$ los que evitan los 5 divisores con $5^2$, y $2^8$ los que evitan los 7.) El conjunto vacío queda automáticamente excluido, pues aparece con coeficiente $1 - 1 - 1 + 1 = 0$.

**Probabilidad:**

$$\frac{27904}{32768} = \frac{27904/256}{32768/256} = \frac{109}{128}$$

Como $109$ es impar (de hecho, primo), la fracción está en forma irreducible. Entonces $m + n = 109 + 128 = 237$.

$$\boxed{237}$$