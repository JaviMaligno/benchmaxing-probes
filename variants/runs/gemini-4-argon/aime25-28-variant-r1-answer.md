Para encontrar el residuo cuando $m + n$ se divide por $1000$, analizamos la relación de recurrencia escribiendo cada término como una fracción irreducible $y_k = \frac{m_k}{n_k}$, donde $m_k$ y $n_k$ son enteros positivos coprimos ($\operatorname{mcd}(m_k, n_k) = 1$).

### Paso 1: Relación entre numeradores y denominadores
Sustituyendo $y_k = \frac{m_k}{n_k}$ en la relación de recurrencia dada:
$$y_{k+1} = \frac{1}{3}\left(\frac{m_k}{n_k} + \frac{n_k}{m_k} - 1\right) = \frac{m_k^2 - m_k n_k + n_k^2}{3 m_k n_k}$$

Observemos que como $\operatorname{mcd}(m_k, n_k) = 1$, se cumple que:
$$\operatorname{mcd}(m_k^2 - m_k n_k + n_k^2, m_k n_k) = 1$$
Por lo tanto, el único factor común posible entre el numerador $m_k^2 - m_k n_k + n_k^2$ y el denominador $3m_k n_k$ es $3$. Notemos además la identidad:
$$m_k^2 - m_k n_k + n_k^2 = (m_k + n_k)^2 - 3m_k n_k$$
De aquí se deduce que $3$ divide a $m_k^2 - m_k n_k + n_k^2$ si y solo si $3$ divide a $m_k + n_k$. Además, si $3 \mid (m_k + n_k)$ y $\operatorname{mcd}(m_k, n_k) = 1$, entonces ni $m_k$ ni $n_k$ son múltiplos de $3$, por lo que $3 \nmid m_k n_k$.

En tal caso, la fracción irreducible para $y_{k+1}$ tiene numerador y denominador dados por:
$$m_{k+1} = \frac{m_k^2 - m_k n_k + n_k^2}{3}, \qquad n_{k+1} = m_k n_k$$

### Paso 2: Recurrencia para la suma $S_k = m_k + n_k$
Sumando $m_{k+1}$ y $n_{k+1}$ obtenemos:
$$S_{k+1} = m_{k+1} + n_{k+1} = \frac{m_k^2 - m_k n_k + n_k^2}{3} + m_k n_k = \frac{m_k^2 + 2m_k n_k + n_k^2}{3} = \frac{(m_k + n_k)^2}{3} = \frac{S_k^2}{3}$$

Para $k = 1$, tenemos $y_1 = \frac{19}{14}$, con $\operatorname{mcd}(19, 14) = 1$, y:
$$S_1 = 19 + 14 = 33 = 3 \cdot 11$$
Como $3 \mid S_1$, por inducción sobre $k$ se mantiene que $3 \mid S_k$ para todo $k \ge 1$, la simplificación por $3$ ocurre exactamente en cada paso, y la fórmula cerrada para $S_k$ es:
$$S_k = 3 \cdot 11^{2^{k-1}}$$

Comprobación para los primeros términos:
- $S_1 = 3 \cdot 11^{2^0} = 33$
- $S_2 = \frac{33^2}{3} = 3 \cdot 11^2 = 363$
- $S_3 = \frac{363^2}{3} = 3 \cdot 11^4 = 43923$

Para $k = 2025$, tenemos:
$$m + n = S_{2025} = 3 \cdot 11^{2^{2024}}$$

### Paso 3: Cálculo módulo $1000$
Por el teorema del binomio, para cualquier entero positivo $r$:
$$11^r = (1 + 10)^r \equiv 1 + 10r + 100\binom{r}{2} \pmod{1000}$$
Esto implica que $11^{100} \equiv 1 \pmod{1000}$, por lo que basta con hallar el exponente $2^{2024} \pmod{100}$:
- Módulo $4$: $2^{2024} \equiv 0 \pmod 4$.
- Módulo $25$: Como $\phi(25) = 20$, tenemos $2^{20} \equiv 1 \pmod{25}$, así que:
  $$2^{2024} = (2^{20})^{101} \cdot 2^4 \equiv 16 \pmod{25}$$

Por el teorema chino del resto, $2^{2024} \equiv 16 \pmod{100}$. Entonces:
$$11^{2^{2024}} \equiv 11^{16} = (1 + 10)^{16} \equiv 1 + \binom{16}{1}\cdot 10 + \binom{16}{2}\cdot 100 \pmod{1000}$$
Como $\binom{16}{1} \cdot 10 = 160$ y $\binom{16}{2} \cdot 100 = 120 \cdot 100 = 12000 \equiv 0 \pmod{1000}$, obtenemos:
$$11^{16} \equiv 1 + 160 + 0 = 161 \pmod{1000}$$

Finalmente, multiplicando por $3$:
$$m + n = 3 \cdot 11^{2^{2024}} \equiv 3 \cdot 161 = 483 \pmod{1000}$$

\boxed{483}