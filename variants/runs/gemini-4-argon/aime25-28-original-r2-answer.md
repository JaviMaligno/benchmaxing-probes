Para encontrar el residuo cuando $m + n$ se divide entre $1000$, analizamos la relación de recurrencia dada.

### Paso 1: Expresar la recurrencia en términos del numerador y denominador
Sea $x_k = \frac{a_k}{b_k}$, donde $a_k$ y $b_k$ son enteros positivos coprimos ($\mcd(a_k, b_k) = 1$). Para $k = 1$, tenemos $a_1 = 25$ y $b_1 = 11$.

Sustituyendo $x_k = \frac{a_k}{b_k}$ en la relación de recurrencia:
$$x_{k+1} = \frac{1}{3}\left(\frac{a_k}{b_k} + \frac{b_k}{a_k} - 1\right) = \frac{a_k^2 - a_k b_k + b_k^2}{3 a_k b_k}$$

Observemos que:
$$a_k^2 - a_k b_k + b_k^2 = (a_k + b_k)^2 - 3a_k b_k$$

### Paso 2: Analizar la simplificación de la fracción
Demostraremos por inducción que para todo $k \ge 1$, se cumple que $\mcd(a_k, b_k) = 1$ y que $3$ divide a $S_k = a_k + b_k$:

1. **Caso base ($k = 1$):** $\mcd(25, 11) = 1$ y $S_1 = 25 + 11 = 36$, el cual es divisible entre $3^2 = 9$.
2. **Paso inductivo:** Supongamos que $\mcd(a_k, b_k) = 1$ y que $3 \mid (a_k + b_k)$. Entonces $3$ divide a $(a_k + b_k)^2 - 3a_k b_k = a_k^2 - a_k b_k + b_k^2$. Definimos:
   $$a_{k+1} = \frac{a_k^2 - a_k b_k + b_k^2}{3}, \quad b_{k+1} = a_k b_k$$
   De este modo, $a_{k+1}$ y $b_{k+1}$ son enteros positivos tales que $x_{k+1} = \frac{a_{k+1}}{b_{k+1}}$.
   
   Veamos que $\mcd(a_{k+1}, b_{k+1}) = 1$. Si un primo $p$ dividiera tanto a $a_{k+1}$ como a $b_{k+1} = a_k b_k$, entonces $p$ dividiría a $a_k$ o a $b_k$, y además $p$ dividiría a $3a_{k+1} = a_k^2 - a_k b_k + b_k^2$. Si $p \mid a_k$, entonces $p \mid b_k^2 \implies p \mid b_k$, contradiciendo que $\mcd(a_k, b_k) = 1$ (y análogamente si $p \mid b_k$). Por lo tanto, la fracción $\frac{a_{k+1}}{b_{k+1}}$ es irreducible.

   Ahora calculamos la suma $S_{k+1} = a_{k+1} + b_{k+1}$:
   $$S_{k+1} = \frac{a_k^2 - a_k b_k + b_k^2}{3} + a_k b_k = \frac{a_k^2 + 2a_k b_k + b_k^2}{3} = \frac{(a_k + b_k)^2}{3} = \frac{S_k^2}{3}$$
   Como $3 \mid S_k$, se tiene que $9 \mid S_k^2$, por lo que $3 \mid S_{k+1}$. Esto completa la inducción.

### Paso 3: Encontrar una fórmula cerrada para $S_k$
De la relación $S_{k+1} = \frac{S_k^2}{3}$, dividimos ambos lados entre $3$:
$$\frac{S_{k+1}}{3} = \left(\frac{S_k}{3}\right)^2$$

Como $\frac{S_1}{3} = \frac{36}{3} = 12$, aplicando la relación sucesivamente obtenemos:
$$\frac{S_k}{3} = \left(\frac{S_1}{3}\right)^{2^{k-1}} = 12^{2^{k-1}} \implies S_k = 3 \cdot 12^{2^{k-1}}$$

Para $k = 2025$, tenemos:
$$m + n = S_{2025} = 3 \cdot 12^{2^{2024}}$$

### Paso 4: Calcular $m + n \pmod{1000}$
Calculamos $S_{2025}$ módulo $8$ y módulo $125$:

1. **Módulo $8$:**
   Dado que $12$ es múltiplo de $4$ y $2^{2024} \ge 2$, $12^{2^{2024}}$ es múltiplo de $8$. Por tanto:
   $$S_{2025} \equiv 0 \pmod{8}$$

2. **Módulo $125$:**
   Por el teorema de Euler, como $\mcd(12, 125) = 1$ y $\phi(125) = 100$, reducimos el exponente $2^{2024}$ módulo $100$:
   - $2^{2024} \equiv 0 \pmod 4$.
   - Como $\phi(25) = 20$ y $2024 \equiv 4 \pmod{20}$, tenemos $2^{2024} \equiv 2^4 = 16 \pmod{25}$.
   
   Dado que $16 \equiv 0 \pmod 4$ y $16 \equiv 16 \pmod{25}$, por el teorema chino del resto se tiene que $2^{2024} \equiv 16 \pmod{100}$.

   Así, calculamos $3 \cdot 12^{16} \pmod{125}$:
   $$\begin{aligned}
   12^2 &= 144 \equiv 19 \pmod{125} \\
   12^{16} &\equiv 19^8 = (20 - 1)^8 \equiv \binom{8}{2}20^2 - \binom{8}{1}20 + 1 \pmod{125} \\
   &\equiv 28(400) - 160 + 1 = 11041 = 88 \times 125 + 41 \equiv 41 \pmod{125}
   \end{aligned}$$
   Multiplicando por $3$:
   $$S_{2025} \equiv 3 \cdot 41 = 123 \pmod{125}$$

3. **Combinación mediante el teorema chino del resto:**
   Buscamos $S_{2025} \equiv 123 + 125t \pmod{1000}$ tal que $S_{2025} \equiv 0 \pmod 8$:
   $$123 + 125t \equiv 3 + 5t \equiv 0 \pmod 8 \implies 5t \equiv 5 \pmod 8 \implies t \equiv 1 \pmod 8$$
   Sustituyendo $t = 1$, obtenemos $S_{2025} \equiv 123 + 125 = 248 \pmod{1000}$.

\boxed{248}