## Solución

**Reformulación.** Escribo la recursión como
$$y_{k+1}=\frac{y_k^2-y_k+1}{3y_k}.$$
Si $y_k=\frac{m_k}{n_k}$ en términos mínimos ($\gcd(m_k,n_k)=1$), entonces
$$y_{k+1}=\frac{m_k^2-m_kn_k+n_k^2}{3m_kn_k}.$$
Un primo $p$ que divida a $m_kn_k$ y a $m_k^2-m_kn_k+n_k^2$ tendría que dividir a $m_k$ y $n_k$ a la vez (o viceversa), lo que es imposible; es decir, **el único factor común posible es 3**.

**La suma $m_k+n_k$.** Observo la identidad clave:
$$\left(m_k^2-m_kn_k+n_k^2\right)+3m_kn_k=(m_k+n_k)^2.$$
Es decir: numerador $+$ denominador $=(m_k+n_k)^2$.

**Patrín módulo 3.** Afirmo que $m_k\equiv 1$ y $n_k\equiv 2 \pmod 3$ para todo $k$. Es cierto para $k=1$ pues $19\equiv 1$, $14\equiv 2$. Si $m\equiv 1$, $n\equiv 2 \pmod 3$, escribiendo $m=1+3s$, $n=2+3t$:
$$m^2-mn+n^2\equiv 3 \pmod 9,$$
de modo que $\frac{m^2-mn+n^2}{3}\equiv 1\pmod 3$ y $mn\equiv 2\pmod 3$. Por el análisis de arriba, no hay más factores comunes, así que
$$m_{k+1}=\frac{m_k^2-m_kn_k+n_k^2}{3},\qquad n_{k+1}=m_kn_k,$$
con $m_{k+1}\equiv 1$, $n_{k+1}\equiv 2 \pmod 3$: el patrón continúa. ✓

**Conclusión sobre $s_k=m_k+n_k$:** 
$$s_{k+1}=m_{k+1}+n_{k+1}=\frac{(m_k+n_k)^2}{3}=\frac{s_k^2}{3}.$$
Con $s_1=19+14=33$, escribiendo $s_k=3t_k$: $t_{k+1}=t_k^2$, $t_1=11$, así que
$$s_k=m_k+n_k=3\cdot 11^{2^{k-1}}.$$
Verificación: $s_2=97+266=363=3\cdot 11^2$ ✓, $s_3=18121+25802=43923=3\cdot 11^4$ ✓.

**Cálculo final.** Necesito $s_{2025}=3\cdot 11^{2^{2024}}\pmod{1000}$.

El orden multiplicativo de $11$ módulo $1000$: módulo $8$ es $2$ ($11\equiv3$, $3^2\equiv1$); módulo $125$ es $25$ (pues $11^2\equiv-4$, $11^4\equiv16$, $11^8\equiv6$, $11^{16}\equiv36$, y $11^{25}\equiv 76\cdot 51\equiv 1 \pmod{125}$). Por lo tanto el orden es $\mathrm{mcm}(2,25)=50$.

Reduzco el exponente: $2^{2024}\pmod{50}$. Potencias de $2$ módulo $50$ tienen periodo $20$ desde $n\ge1$, y $2024\equiv 4\pmod{20}$, así que $2^{2024}\equiv 2^4=16\pmod{50}$.

Entonces
$$11^{2^{2024}}\equiv 11^{16}\pmod{1000}.$$
Calculo $11^{16}\pmod{1000}$ por cuadrados sucesivos: $11^2=121$, $11^4\equiv 641$, $11^8\equiv 881$, $11^{16}\equiv 881^2=776161\equiv \mathbf{161}$. (Verifico por CRT: $161\equiv 36\pmod{125}$ y $161\equiv 1\pmod 8$, que coinciden con $11^{16}$ módulo $125$ y $8$ ✓.)

Por lo tanto:
$$m+n=3\cdot 11^{2^{2024}}\equiv 3\cdot 161=483 \pmod{1000}.$$