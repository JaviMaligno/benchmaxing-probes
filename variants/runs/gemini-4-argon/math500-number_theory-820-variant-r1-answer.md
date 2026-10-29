Para encontrar el número de valores posibles para $m$, primero descomponemos $2310$ en sus factores primos:
$$2310 = 2 \times 3 \times 5 \times 7 \times 11$$

Observamos que $2310$ es el producto de $5$ números primos distintos, cada uno elevado al exponente $1$.

Sean $p_1, p_2, p_3, p_4, p_5$ estos cinco factores primos. Podemos escribir las descomposiciones en factores primos de $m$ y $n$ como:
$$m = p_1^{a_1} p_2^{a_2} p_3^{a_3} p_4^{a_4} p_5^{a_5}$$
$$n = p_1^{b_1} p_2^{b_2} p_3^{b_3} p_4^{b_4} p_5^{b_5}$$

De acuerdo con las condiciones del problema:
1. $\gcd(m,n) = 2310 = p_1^1 p_2^1 p_3^1 p_4^1 p_5^1$, lo que implica que $\min(a_i, b_i) = 1$ para cada $i \in \{1, 2, 3, 4, 5\}$.
2. $\mathop{\text{lcm}}[m,n] = 2310^3 = p_1^3 p_2^3 p_3^3 p_4^3 p_5^3$, lo que implica que $\max(a_i, b_i) = 3$ para cada $i \in \{1, 2, 3, 4, 5\}$.

Por lo tanto, para cada uno de los $5$ factores primos, el par de exponentes $(a_i, b_i)$ debe ser $(1, 3)$ o $(3, 1)$. Como $n$ queda determinado de forma única por $m$ a través de la relación $m \cdot n = \gcd(m,n) \cdot \mathop{\text{lcm}}[m,n] = 2310^4$, cada elección de exponentes $a_i \in \{1, 3\}$ genera un único par $(m, n)$.

Dado que hay $2$ opciones para cada uno de los $5$ exponentes $a_i$, existen en total:
$$2^5 = 32$$
pares ordenados $(m, n)$ que cumplen las condiciones del máximo común divisor y mínimo común múltiplo.

Como en ningún caso se puede dar que $m = n$ (ya que $a_i \neq b_i$), por simetría, exactamente la mitad de estos pares cumplen que $m < n$ y la otra mitad que $m > n$. Así, el número de valores posibles para $m$ es:
$$\frac{32}{2} = 16$$

\boxed{16}