# Solución

**Planteamiento.** Sea $m = 2n+3$ (impar, con $123 \le m \le 243$). Como $\gcd(2,m)=1$, tenemos
$$m \mid 2^{n!}-1 \iff \operatorname{ord}_m(2) \mid n!,$$
donde $\operatorname{ord}_m(2)$ es el orden multiplicativo de 2 módulo $m$.

**Paso 1: el orden es pequeño.** Como $\operatorname{ord}_m(2) \mid \lambda(m) \mid \phi(m) \le m-1$, el orden es a lo sumo $242$.

**Paso 2: cuándo divide $n!$.** Para $n \ge 60$, el factorial $n!$ contiene potencias primas pequeñas de sobra: la multiplicidad de $2$ es $\ge 56$, la de $3$ es $\ge 28$, la de $5$ es $\ge 14$, la de $7$ es $\ge 9$, etc. Como todo entero $\le 242$ tiene a lo sumo $2^7$, $3^4$, $5^3$, $7^2$, $11^2$, o $13^2$ en su factorización, se concluye:

$$\operatorname{ord}_m(2) \nmid n! \iff \operatorname{ord}_m(2) \text{ tiene un factor primo } q > n.$$

**Paso 3: el factor primo grande fuerza estructura.** Supongamos que $q > n$ divide a $\operatorname{ord}_m(2)$. Entonces $q$ divide a $\operatorname{ord}_{p^a}(2) \mid p^{a-1}(p-1)$ para alguna potencia prima $p^a \| m$.
- Si $q = p$, entonces $a \ge 2$, así que $p \le \sqrt{243} < 16 \le n$: contradicción.
- Entonces $q \mid p-1$, con lo cual $p \ge q+1 \ge n+2 > n$. Pero $p \mid m = 2n+3$; si $m$ fuera compuesto, su factor primo $p$ cumpliría $p \le m/3 < n$ para $n \ge 4$: contradicción.

Por lo tanto $m = p$ es primo, y $q \mid m-1 = 2(n+1)$ con $q > n$ primo impar fuerza $q = n+1$.

**Paso 4: la condición es automática.** Si $m = 2(n+1)+1 = 2q+1$ es primo con $q = n+1$ primo, entonces $\operatorname{ord}_m(2) \mid 2q$ y $\operatorname{ord}_m(2) \notin \{1,2\}$ (pues $m>3$), así que $\operatorname{ord}_m(2) \in \{q,\, 2q\}$ y **siempre** contiene el factor $q > n$, que no divide a $n!$. 

**Conclusión:** $2n+3 \nmid 2^{n!}-1$ si y solo si $n+1$ y $2n+3 = 2(n+1)+1$ son ambos primos.

**Paso 5: enumeración.** Los primos $n+1 \in [61, 121]$ dan candidatos $n \in \{60, 66, 70, 72, 78, 82, 88, 96, 100, 102, 106, 108, 112\}$. Comprobando $2n+3$:
- $123, 135, 143, 147, 159, 195, 203, 207, 215, 219$ son compuestos.
- $167$ (para $n=82$), $179$ (para $n=88$), $227$ (para $n=112$) son primos. ✓

**Verificación directa de los tres casos:**
- $n=82$: $\operatorname{ord}_{167}(2) = 83$ (pues $167 \equiv 7 \pmod 8$, así que 2 es residuo cuadrático y $2^{83}\equiv 1$), y $83 \nmid 82!$.
- $n=88$: $179 \equiv 3 \pmod 8$, así que $2^{89} \equiv -1 \pmod{179}$ y $\operatorname{ord}_{179}(2) = 178 = 2\cdot 89$, con $89 \nmid 88!$.
- $n=112$: $227 \equiv 3 \pmod 8$, así que $\operatorname{ord}_{227}(2) = 226 = 2 \cdot 113$, con $113 \nmid 112!$.

Los enteros pedidos son $n \in \{82, 88, 112\}$, y su suma es
$$82 + 88 + 112 = 282.$$

\boxed{282}