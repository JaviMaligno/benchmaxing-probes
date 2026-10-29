## Planteamiento

Escribo $y_k = \dfrac{a_k}{b_k}$ en forma reducida. La recurrencia da

$$y_{k+1}=\frac{a_k^2-a_kb_k+b_k^2}{3a_kb_k}.$$

**Divisibilidad por 3.** Como $a^2-ab+b^2=(a+b)^2-3ab$, es divisible por 3 exactamente cuando $3\mid a+b$. Con $a_1=19,\ b_1=14$: $a_1+b_1=33$ ✓. Además, si $3\mid a+b$ y $\gcd(a,b)=1$, ninguno de los dos es múltiplo de 3, luego $3\nmid ab$ y la potencia de 3 es exactamente $3^1$. Por tanto

$$a_{k+1}=\frac{a_k^2-a_kb_k+b_k^2}{3},\qquad b_{k+1}=a_kb_k.$$

**Coprimalidad.** Si un primo $p$ divide a $a_{k+1}$ y a $a_kb_k$, digamos $p\mid a_k$, entonces $p\mid b_k^2$, contradiciendo $\gcd(a_k,b_k)=1$ (y $p\neq 3$ porque $3\nmid a_{k+1}$). Así la fracción siempre queda reducida y positiva: $m=a_{2025}$, $n=b_{2025}$.

## La clave: la suma

$$a_{k+1}+b_{k+1}=\frac{a_k^2-a_kb_k+b_k^2+3a_kb_k}{3}=\frac{(a_k+b_k)^2}{3}.$$

Con $s_k=a_k+b_k$ y $t_k=s_k/3$ resulta $3t_{k+1}=\frac{9t_k^2}{3}$, es decir $t_{k+1}=t_k^2$, con $t_1=33/3=11$. Luego

$$\boxed{\;}\quad s_k=3\cdot 11^{2^{k-1}},\qquad m+n=s_{2025}=3\cdot 11^{2^{2024}}.$$

(Comprobación: $y_2=\frac{97}{266}$, $s_2=363=3\cdot11^2$; $y_3=\frac{18121}{25802}$, $s_3=43923=3\cdot 11^4$ ✓.)

## Reducción módulo 1000

**Módulo 8:** $11\equiv 3$, de orden 2; el exponente $2^{2024}$ es par, así que $11^{2^{2024}}\equiv 1 \pmod 8$.

**Módulo 125:** el orden de 11 es 25 (pues $11^5\equiv 51$, $11^{25}\equiv 1$). Como $2$ tiene orden 20 módulo 25 y $2024\equiv 4\pmod{20}$, se tiene $2^{2024}\equiv 2^4=16 \pmod{25}$. Entonces
$$11^2\equiv -4,\quad 11^4\equiv 16,\quad 11^8\equiv 6,\quad 11^{16}\equiv 36 \pmod{125}.$$

**CRT:** $x\equiv 1\pmod 8$, $x\equiv 36\pmod{125}$ da $x=161$.

Por tanto $m+n\equiv 3\cdot 161=483 \pmod{1000}$.

\boxed{483}