## Planteamiento

Sea $m = 2n+3$ (impar, con $103 \le m \le 203$). Como $\gcd(2,m)=1$, se tiene
$$m \mid 2^{n!}-1 \iff \operatorname{ord}_m(2) \mid n!.$$

**Paso 1: el orden es menor que $m$.** Siempre $\operatorname{ord}_m(2) \le \lambda(m) < m = 2n+3 \le 203$. Para que $\operatorname{ord}_m(2) \nmid n!$ hace falta una potencia de primo $q^e \mid \operatorname{ord}_m(2)$ con $q^e \nmid n!$. Como $q^e < 203$ y $n \ge 50$, las potencias pequeñas sobran en $n!$ (p. ej. $v_2(50!)=47$, $v_3(50!)=22$). Por tanto el único obstáculo posible es un primo $q \mid \operatorname{ord}_m(2)$ con $q > n$.

**Paso 2: $m$ debe ser primo.** Si $q > n$ divide $\lambda(m)$, entonces algún primo $p_i \mid m$ cumple $p_i \equiv 1 \pmod q$, luego $p_i \ge q+1 > n+1$. Si $m$ tuviera otro factor $\ge 3$, sería $m \ge 3(n+2) > 2n+3$, imposible. Así $m = 2n+3$ es primo.

**Paso 3: condición final.** Con $p = 2n+3$ primo, $\operatorname{ord}_p(2) \mid p-1 = 2(n+1)$. Un primo $q > n$ que divida $2(n+1)$ obliga a $q = n+1$, es decir $n+1$ primo. En ese caso los divisores de $2(n+1)$ son $1, 2, n+1, 2n+2$; como $\operatorname{ord}_p(2) \ne 1,2$ (si no $p \mid 3$), necesariamente $(n+1) \mid \operatorname{ord}_p(2)$, y $n+1 \nmid n!$ al ser primo.

Conclusión: $2n+3 \nmid 2^{n!}-1 \iff$ **$n+1$ y $2n+3$ son ambos primos**.

## Búsqueda en $50 \le n \le 100$

$n+1$ primo da $n \in \{52, 58, 60, 66, 70, 72, 78, 82, 88, 96, 100\}$. Ahora $2n+3$:

| $n$ | $2n+3$ | |
|---|---|---|
| 52 | 107 | primo ✓ |
| 58 | 119 $=7\cdot17$ | ✗ |
| 60 | 123 $=3\cdot41$ | ✗ |
| 66 | 135 | ✗ |
| 70 | 143 $=11\cdot13$ | ✗ |
| 72 | 147 | ✗ |
| 78 | 159 $=3\cdot53$ | ✗ |
| 82 | 167 | primo ✓ |
| 88 | 179 | primo ✓ |
| 96 | 195 | ✗ |
| 100 | 203 $=7\cdot29$ | ✗ |

Verificación de $n=52$: $p=107$, $p-1=2\cdot53$; como $107 \equiv 3 \pmod 8$, el 2 no es resto cuadrático, así $\operatorname{ord}=106$ y $53 \nmid 52!$.

Suma: $52+82+88 = 222$.

\boxed{222}