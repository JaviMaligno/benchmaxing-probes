Voy a resolver este problema de teoría de números y verificar el resultado numéricamente con un script rápido.

**Planteamiento:** $D = \gcd_{n>2024} Q(n)$, y $v_p(D) = \min_n v_p(Q(n))$ para cada primo $p$, calculado independientemente por CRT.

**Qué primos aportan:** Si $p \equiv 1 \pmod 3$, los cubos no cubren todos los residuos mod $p$, así que eligiendo $n$ como no-cubo se obtiene $v_p = 0$. Si $p > 45$, hay clases mod $p$ sin ningún $k \in [1,45]$, también $v_p = 0$. Quedan $p \in \{2, 3, 5, 11, 17, 23, 29, 41\}$ (el 3 y los $p \equiv 2 \pmod 3$ hasta 45), donde cubicar es biyección mod $p$.

**Cálculo por primo:** Para clase $c \not\equiv 0$ (con $p \neq 3$), $v_p(k^3 - k'^3) = v_p(k-k')$, y los $N_c$ valores de $k$ en la clase son consecutivos en $j$; el mínimo es $N_c + v_p(N_c!)$. Para la clase $0$, eligiendo $v_p(n) = 1$ se logra exactamente $N_0$. Para $p=3$, $v_3(k^3-k'^3) = v_3(k-k')+1$, pero eligiendo $n \equiv 4 \pmod 9$ (clase 1) o $v_3(n)=1$ (clase 0) cada factor vale exactamente 1, dando 15.

| $p$ | mínimo |
|---|---|
| 2 | clase par: 22 (clase impar daría $23 + v_2(23!) = 42$) |
| 3 | 15 |
| 5 | clase 0: 9 (clase no nula: $9 + v_5(9!) = 10$) |
| 11 | 4 |
| 17 | 2 |
| 23, 29, 41 | 1 cada uno |

Verifico con un cálculo directo del gcd:

**Bash: Verificación numérica del gcd y su factorización**

```bash
cd /tmp && python3 -I -c "
from math import gcd
def Q(n):
    p=1
    for k in range(1,46): p*=n-k**3
    return p
g=0
for n in range(2025,2425): g=gcd(g,abs(Q(n)))
# factorizar g
m=0; x=g; d=2; fac={}
while d*d<=x:
    while x%d==0: fac[d]=fac.get(d,0)+1; x//=d; m+=1
    d+=1
if x>1: fac[x]=fac.get(x,0)+1; m+=1
print(fac); print('m =', m)
"
```

```
{2: 22, 3: 15, 5: 9, 11: 4, 17: 2, 23: 1, 29: 1, 41: 1}
m = 55
```

La verificación numérica coincide exactamente con el análisis: $D = 2^{22} \cdot 3^{15} \cdot 5^{9} \cdot 11^{4} \cdot 17^{2} \cdot 23 \cdot 29 \cdot 41$ (el gcd sobre 400 valores de $n$ ya se estabiliza en este valor, y el argumento constructivo por residuos muestra que cada exponente es alcanzado como mínimo).

Sumando los exponentes: $22 + 15 + 9 + 4 + 2 + 1 + 1 + 1 = 55$.

$$\boxed{55}$$