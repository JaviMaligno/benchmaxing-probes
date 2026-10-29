## Planteamiento

Sean $c > v > s \ge 1$ con $c+v+s=9$.

**Particiones válidas:**
- $(7,1,1)$: no vale, pues $v = s$.
- $(6,2,1)$ ✓
- $(5,3,1)$ ✓
- $(5,2,2)$: no vale, $v = s$.
- $(4,3,2)$ ✓

**Conteo multinomial para cada caso:**

$$\binom{9}{6,2,1}=\frac{9!}{6!\,2!\,1!}=252$$

$$\binom{9}{5,3,1}=\frac{9!}{5!\,3!\,1!}=504$$

$$\binom{9}{4,3,2}=\frac{9!}{4!\,3!\,2!}=1260$$

**Total:** $N = 252 + 504 + 1260 = 2016$

Resto al dividir entre $1000$: $16$.

\boxed{16}