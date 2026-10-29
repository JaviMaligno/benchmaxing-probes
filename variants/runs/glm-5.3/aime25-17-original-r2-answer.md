# Resolución

**Planteamiento.** Buscamos todos los enteros positivos $n$ tales que
$$
(n+2) \mid 3(n+3)(n^2+9).
$$

**Sustitución clave.** Sea $m = n+2$. Entonces:
- $n + 3 = m + 1 \equiv 1 \pmod{m}$
- $n^2 + 9 = (m-2)^2 + 9 = m^2 - 4m + 13 \equiv 13 \pmod{m}$

**Reducción módulo $m$.** Entonces:
$$
3(n+3)(n^2+9) \equiv 3 \cdot 1 \cdot 13 = 39 \pmod{m}.
$$

Por lo tanto, $m \mid 39$. Como $n \geq 1$, tenemos $m = n+2 \geq 3$. Los divisores de $39$ son $1, 3, 13, 39$, así que los valores válidos de $m$ son:
$$
m \in \{3, 13, 39\}.
$$

**Valores de $n$:**
- $m = 3 \Rightarrow n = 1$
- $m = 13 \Rightarrow n = 11$
- $m = 39 \Rightarrow n = 37$

**Verificación rápida:**
- $n=1$: $(n+2)=3 \mid 3\cdot 4 \cdot 10 = 120$ ✓
- $n=11$: $13 \mid 3\cdot 14\cdot 130 = 5460$ ✓
- $n=37$: $39 \mid 3\cdot 40\cdot 1378 = 165360$ ✓

**Suma.**
$$
1 + 11 + 37 = 49.
$$

$$\boxed{49}$$