## Planteamiento

Sea $m = n+3$, con $n = m-3$ y $m \ge 4$ (pues $n \ge 1$).

**Reducción módulo $m$:**

- $n+5 = m+2 \equiv 2 \pmod m$
- $n^2+7 = (m-3)^2 + 7 = m^2 - 6m + 16 \equiv 16 \pmod m$

Por tanto:
$$2(n+5)(n^2+7) \equiv 2 \cdot 2 \cdot 16 = 64 \pmod m$$

**Condición:** $m \mid 64$, es decir $m \in \{1,2,4,8,16,32,64\}$.

Como $m = n+3 \ge 4$, quedan $m \in \{4, 8, 16, 32, 64\}$, lo que da:
$$n = 1,\ 5,\ 13,\ 29,\ 61$$

**Verificación** (un caso): $n=13 \Rightarrow m=16$, y $2 \cdot 18 \cdot 176 = 6336 = 16 \cdot 396$ ✓

**Suma:** $1+5+13+29+61 = 109$

$\boxed{109}$