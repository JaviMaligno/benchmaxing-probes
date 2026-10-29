## Planteamiento

Como $2n+3$ es impar, $2n+3 \mid 2^{n!}-1$ si y solo si $d = \operatorname{ord}_{2n+3}(2)$ divide a $n!$.

**Caso 1: $2n+3$ compuesto.** Todo factor primo $q$ de $2n+3$ cumple $q \le \tfrac{2n+3}{3} < n$. Para cada potencia $q^a \,\|\, (2n+3)$, el orden de $2$ módulo $q^a$ divide a $q^{a-1}(q-1) < 2n+3 \le 203$, así que sus factores primos son $< n$ y sus potencias primas son pequeñas (p. ej., $2^7, 3^4, 5^3, 7^2, 11^2, 13^2$ como máximos posibles), todas presentes de sobra en $n!$ para $n \ge 50$. Por tanto $d \mid n!$ y **la divisibilidad siempre se cumple**.

**Caso 2: $p = 2n+3$ primo.** Entonces $d \mid p-1 = 2(n+1)$.
- Si $n+1$ es **compuesto**, todos los factores primos de $2(n+1)$ son $\le \tfrac{n+1}{2} < n$, y las potencias primas involucradas ($\le 2(n+1) \le 202$) están contenidas en $n!$. La divisibilidad se cumple.
- Si $q = n+1$ es **primo**, entonces $p = 2q+1$ y $d \in \{1, 2, q, 2q\}$. Como $p > 3$, se descarta $d = 1, 2$, luego $q \mid d$. Pero $q = n+1 > n$ es primo, así que $q \nmid n!$ y por tanto $d \nmid n!$: **la divisibilidad falla**.

## Conclusión

La divisibilidad falla exactamente cuando $n+1$ y $2n+3 = 2(n+1)+1$ son ambos primos (par de Sophie Germain). Reviso los $n \in [50,100]$ con $n+1$ primo:

| $n$ | $q = n+1$ | $p = 2q+1$ | ¿$p$ primo? |
|---|---|---|---|
| 52 | 53 | 107 | ✓ |
| 58 | 59 | 119 = 7·17 | ✗ |
| 60 | 61 | 123 = 3·41 | ✗ |
| 66 | 67 | 135 | ✗ |
| 70 | 71 | 143 = 11·13 | ✗ |
| 72 | 73 | 147 = 3·7² | ✗ |
| 78 | 79 | 159 = 3·53 | ✗ |
| 82 | 83 | 167 | ✓ |
| 88 | 89 | 179 | ✓ |
| 96 | 97 | 195 | ✗ |
| 100 | 101 | 203 = 7·29 | ✗ |

Los valores que fallan son $n = 52, 82, 88$, y su suma es $52 + 82 + 88 = 222$.

$$\boxed{222}$$