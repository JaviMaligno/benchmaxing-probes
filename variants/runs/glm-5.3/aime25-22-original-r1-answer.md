## Planteamiento

**Factorización:** $2025 = 3^4 \cdot 5^2$.

Cada divisor de $2025$ tiene la forma $3^a \cdot 5^b$ con $0 \le a \le 4$ y $0 \le b \le 2$, así que $|A| = 5 \cdot 3 = 15$ y el total de subconjuntos de $A$ es $2^{15}$.

**Condición del MCM:** el MCM de los elementos de $B$ es $2025$ si y solo si:
- al menos un elemento tiene exponente $a = 4$, y
- al menos un elemento tiene exponente $b = 2$.

(El conjunto es automáticamente no vacío si cumple la condición.)

## Conteo por inclusión-exclusión

Cuento los subconjuntos que **fallan** cada condición:

- **Sin elementos con $a = 4$:** quedan $4 \cdot 3 = 12$ elementos → $2^{12}$ subconjuntos.
- **Sin elementos con $b = 2$:** quedan $5 \cdot 2 = 10$ elementos → $2^{10}$ subconjuntos.
- **Sin $a=4$ ni $b=2$:** quedan $4 \cdot 2 = 8$ elementos → $2^{8}$ subconjuntos.

Entonces, los subconjuntos con MCM igual a $2025$ son:

$$2^{15} - 2^{12} - 2^{10} + 2^{8} = 32768 - 4096 - 1024 + 256 = 27904$$

## Probabilidad

$$\frac{27904}{32768} = \frac{2^8 \cdot 109}{2^{15}} = \frac{109}{128}$$

Como $109$ es primo, la fracción es irreducible: $m = 109$, $n = 128$.

$$m + n = 109 + 128 = \boxed{237}$$