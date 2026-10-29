## Razonamiento

**Sustitución.** Sea $m = n+3$, es decir $n = m-3$. Entonces:

- $n+5 = m+2$
- $n^2+7 = (m-3)^2+7 = m^2-6m+16$

**Reducción módulo $m$.** El producto queda:

$$2(n+5)(n^2+7) = 2(m+2)(m^2-6m+16) \equiv 2\cdot 2\cdot 16 = 64 \pmod{m}$$

Por lo tanto, la condición $n+3 \mid 2(n+5)(n^2+7)$ es equivalente a $m \mid 64$.

**Divisores admisibles.** Como $n \geq 1$, se tiene $m = n+3 \geq 4$. Los divisores de $64$ que cumplen esto son:

$$m \in \{4,\ 8,\ 16,\ 32,\ 64\} \quad\Longrightarrow\quad n \in \{1,\ 5,\ 13,\ 29,\ 61\}$$

**Verificación** (un par de casos):
- $n=1$: $4 \mid 2\cdot 6\cdot 8 = 96$, y $96/4 = 24$ ✓
- $n=13$: $16 \mid 2\cdot 18\cdot 176 = 6336$, y $6336/16 = 396$ ✓
- $n=61$: $64 \mid 2\cdot 66\cdot 3728 = 492096$, y $492096/64 = 7689$ ✓

**Suma.** $1+5+13+29+61 = 109$

$$\boxed{109}$$