## Planteamiento

Escribo la recurrencia como $y_{k+1}=\dfrac{y_k^2-y_k+1}{3y_k}$ y hago el cambio de variable que lleva los puntos fijos $y=\tfrac12$ y $y=-1$ a $0$ e $\infty$:

$$p_k=\frac{2y_k-1}{y_k+1},\qquad y_k=\frac{1+p_k}{2-p_k}.$$

Usando
$$y_{k+1}-\tfrac12=\frac{(2y_k-1)(y_k-2)}{6y_k},\qquad y_{k+1}+1=\frac{(y_k+1)^2}{3y_k},$$
se obtiene una recurrencia limpia:
$$\boxed{p_{k+1}=p_k^2-p_k}\ \text{(sin caja: }p_{k+1}=p_k(p_k-1)).$$

## Iteración

Con $y_1=\frac{19}{14}$: $p_1=\frac{38/14-1}{33/14}=\frac{24}{33}=\frac{8}{11}$.

Si $p_k=\dfrac{c_k}{11^{e_k}}$ con $e_k=2^{k-1}$ y $\gcd(c_k,11)=1$, entonces
$$p_{k+1}=\frac{c_k(c_k-11^{e_k})}{11^{2e_k}},$$
es decir $c_{k+1}=c_k(c_k-11^{e_k})$ y $e_{k+1}=2e_k$. Así $e_k=2^{k-1}$ siempre, y $11\nmid c_k$.

## La clave: la suma numerador + denominador

$$y_k=\frac{1+p_k}{2-p_k}=\frac{11^{e_k}+c_k}{2\cdot 11^{e_k}-c_k},$$
y la suma de ambos términos es $3\cdot 11^{e_k}$, independientemente de $c_k$.

Falta ver que la fracción ya es irreducible. Un divisor común divide a $3\cdot11^{e_k}$; no puede ser $11$ (pues $11\nmid c_k$). Módulo 3: $c_1=8\equiv 2$, $11\equiv -1$, luego $c_2=c_1(c_1-11)\equiv 2(2-2)=0$, y por inducción $c_k\equiv 0 \pmod 3$ para todo $k\ge2$, con lo que $11^{e_k}+c_k\equiv \pm1\not\equiv0 \pmod 3$. Además $-1<p_k<2$, así que ambos términos son positivos. Por tanto
$$m+n=3\cdot 11^{2^{k-1}}.$$

Comprobación: $k=1$: $19+14=33=3\cdot11$; $y_2=\frac{97}{266}$, $97+266=363=3\cdot11^2$; $y_3=\frac{18121}{25802}$, suma $=43923=3\cdot11^4$. ✔

## Cálculo módulo 1000

Para $k=2025$: $m+n=3\cdot 11^{N}$ con $N=2^{2024}$.

- Módulo 8: $11^N\equiv 3^N\equiv 1$ ($N$ par).
- Módulo 125: $\lambda=100$ y $2^{2024}\equiv 16 \pmod{100}$ (período 20 desde el exponente 2; $2024\equiv4$, $2^{24}\equiv 76\cdot16\equiv16$). Entonces $11^{16}$: $11^2\equiv-4$, $11^4\equiv16$, $11^8\equiv6$, $11^{16}\equiv36$.
- CRT: $x\equiv1\pmod 8$, $x\equiv36\pmod{125}\Rightarrow x=161$.

Luego $m+n\equiv 3\cdot 161=483 \pmod{1000}$.

\boxed{483}