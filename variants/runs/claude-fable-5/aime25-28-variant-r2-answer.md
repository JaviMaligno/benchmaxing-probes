## Planteamiento

Escribo $y_k = \frac{a_k}{b_k}$ en términos mínimos. La recurrencia da

$$y_{k+1} = \frac{y_k^2 - y_k + 1}{3y_k} = \frac{a_k^2 - a_k b_k + b_k^2}{3 a_k b_k}.$$

**Análisis del mcd.** Como $\gcd(a_k,b_k)=1$, el numerador es coprimo con $a_k$ y con $b_k$ (pues $\gcd(a^2-ab+b^2,a)=\gcd(b^2,a)=1$). Solo queda el factor 3. Usando $a^2-ab+b^2=(a+b)^2-3ab$: si $3 \mid a_k+b_k$, entonces $3\nmid a_k b_k$ (si no, 3 dividiría a ambos), así que módulo 9 el numerador es $\equiv -3a_kb_k \not\equiv 0$, es decir, es divisible por 3 **exactamente una vez**, igual que el denominador $3a_kb_k$. Por tanto:

$$a_{k+1} = \frac{a_k^2 - a_kb_k + b_k^2}{3}, \qquad b_{k+1} = a_k b_k, \qquad \gcd(a_{k+1},b_{k+1})=1.$$

**Invariante clave.** Sea $s_k = a_k + b_k$. Entonces

$$s_{k+1} = \frac{(a_k+b_k)^2 - 3a_kb_k}{3} + a_kb_k = \frac{s_k^2}{3}.$$

Con $y_1 = \frac{19}{14}$: $s_1 = 33$, divisible por 3; y si $s_k = 3r_k$, entonces $s_{k+1}=3r_k^2$ sigue siendo divisible por 3, así que la hipótesis $3\mid s_k$ se mantiene por inducción y la fórmula vale siempre. Escribiendo $s_k = 3r_k$ obtengo $r_{k+1}=r_k^2$ con $r_1 = 11$, luego

$$s_k = 3\cdot 11^{\,2^{k-1}}.$$

*Verificación:* $y_2 = \frac{361-266+196}{798} = \frac{291}{798} = \frac{97}{266}$, y $97+266 = 363 = \frac{33^2}{3}$. ✓

Como todos los $y_k$ son positivos y las fracciones están reducidas, $m+n = s_{2025} = 3\cdot 11^{\,2^{2024}}$.

## Cálculo módulo 1000

Como $\gcd(11,1000)=1$ y $\lambda(1000)=100$, reduzco el exponente módulo 100. Para $2^{2024} \bmod 100$: módulo 4 es $0$; módulo 25, el orden de 2 es 20 y $2024 \equiv 4 \pmod{20}$, así que $2^{2024}\equiv 16 \pmod{25}$. Por el teorema chino, $2^{2024} \equiv 16 \pmod{100}$.

Entonces $11^{2^{2024}} \equiv 11^{16} \pmod{1000}$:

- $11^2 = 121$
- $11^4 = 121^2 = 14641 \equiv 641$
- $11^8 \equiv 641^2 = 410881 \equiv 881$
- $11^{16} \equiv 881^2 = 776161 \equiv 161$

Por lo tanto $m+n \equiv 3 \cdot 161 = 483 \pmod{1000}$.

$$\boxed{483}$$