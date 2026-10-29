Para encontrar el valor de $y_{2025}$, reescribimos primero la relación de recurrencia:
$$y_{k+1} = \frac{1}{3}\left(y_k + \frac{1}{y_k} - 1\right) = \frac{y_k^2 - y_k + 1}{3y_k}$$

Representemos cada término de la sucesión en su forma irreducible como $y_k = \frac{m_k}{n_k}$, donde $m_k$ y $n_k$ son enteros positivos coprimos ($\gcd(m_k, n_k) = 1$). Sustituyendo en la recurrencia, obtenemos:
$$y_{k+1} = \frac{m_k^2 - m_k n_k + n_k^2}{3 m_k n_k}$$

Analicemos el máximo común divisor del numerador y el denominador de esta fracción:
1. Como $\gcd(m_k, n_k) = 1$, se tiene que $\gcd(m_k^2 - m_k n_k + n_k^2, m_k) = \gcd(n_k^2, m_k) = 1$, y análogamente $\gcd(m_k^2 - m_k n_k + n_k^2, n_k) = \gcd(m_k^2, n_k) = 1$.
2. Por lo tanto, el único factor común posible entre el numerador $m_k^2 - m_k n_k + n_k^2$ y el denominador $3 m_k n_k$ es un divisor de $3$.

Observemos el comportamiento de $m_k$ y $n_k$ módulo $3$:
- Para $k = 1$, tenemos $m_1 = 19 \equiv 1 \pmod 3$ y $n_1 = 14 \equiv 2 \pmod 3$.
- Si para algún $k \ge 1$ se cumple que $m_k \equiv 1 \pmod 3$ y $n_k \equiv 2 \pmod 3$, entonces $m_k + n_k$ es múltiplo de $3$, es decir, $n_k = 3t - m_k$ para algún entero $t$. Sustituyendo esto en el numerador:
  $$m_k^2 - m_k(3t - m_k) + (3t - m_k)^2 = 3(m_k^2 - 3t m_k + 3t^2)$$
  Esto muestra que el numerador es divisible por $3$, y al dividirlo por $3$ obtenemos:
  $$m_{k+1} = \frac{m_k^2 - m_k n_k + n_k^2}{3} = m_k^2 - 3t m_k + 3t^2 \equiv m_k^2 \equiv 1 \pmod 3$$
  Asimismo, el nuevo denominador simplificado es:
  $$n_{k+1} = m_k n_k \equiv 1 \cdot 2 = 2 \pmod 3$$

Por inducción, para todo $k \ge 1$, la fracción reducida $y_{k+1} = \frac{m_{k+1}}{n_{k+1}}$ viene dada exactamente por:
$$m_{k+1} = \frac{m_k^2 - m_k n_k + n_k^2}{3}, \qquad n_{k+1} = m_k n_k$$

Sea $S_k = m_k + n_k$. Sumando ambas expresiones obtenemos una recurrencia directa para $S_k$:
$$S_{k+1} = m_{k+1} + n_{k+1} = \frac{m_k^2 - m_k n_k + n_k^2}{3} + m_k n_k = \frac{m_k^2 + 2m_k n_k + n_k^2}{3} = \frac{(m_k + n_k)^2}{3} = \frac{S_k^2}{3}$$

Como $S_1 = 19 + 14 = 33 = 3 \cdot 11$, calculamos los primeros términos:
- $S_1 = 3 \cdot 11^{2^0}$
- $S_2 = \frac{(3 \cdot 11)^2}{3} = 3 \cdot 11^2 = 3 \cdot 11^{2^1}$
- $S_3 = \frac{(3 \cdot 11^2)^2}{3} = 3 \cdot 11^4 = 3 \cdot 11^{2^2}$

Por inducción, para todo $k \ge 1$:
$$S_k = 3 \cdot 11^{2^{k-1}}$$

En particular, para $k = 2025$:
$$m + n = S_{2025} = 3 \cdot 11^{2^{2024}}$$

Para hallar el residuo de $S_{2025}$ módulo $1000$, notamos por el teorema del binomio que para cualquier entero positivo $N$:
$$11^N = (1 + 10)^N \equiv 1 + 10N + 50N(N-1) \pmod{1000}$$
De aquí se deduce que $11^{100} \equiv 1 \pmod{1000}$, por lo que solo necesitamos calcular el exponente $2^{2024} \pmod{100}$:
- $2^{2024} \equiv 0 \pmod 4$.
- Por el teorema de Euler, como $\phi(25) = 20$ y $2024 = 20 \cdot 101 + 4$, se tiene $2^{2024} \equiv 2^4 = 16 \pmod{25}$.

Por el teorema chino del resto, $2^{2024} \equiv 16 \pmod{100}$. Entonces:
$$11^{2^{2024}} \equiv 11^{16} = (1 + 10)^{16} \equiv 1 + \binom{16}{1} \cdot 10 + \binom{16}{2} \cdot 100 \pmod{1000}$$
$$11^{16} \equiv 1 + 160 + 12000 \equiv 161 \pmod{1000}$$

Finalmente, multiplicando por $3$:
$$m + n \equiv 3 \cdot 161 = 483 \pmod{1000}$$

\boxed{483}