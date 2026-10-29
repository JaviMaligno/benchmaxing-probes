Para encontrar el número de valores posibles para $m$, primero factorizamos $2310$ en números primos:
$$2310 = 2 \cdot 3 \cdot 5 \cdot 7 \cdot 11$$

Observamos que $2310$ es el producto de $5$ números primos distintos. Como $\gcd(m,n) = 2310$ y $\mathop{\text{lcm}}[m,n] = 2310^3$, los únicos factores primos que pueden dividir a $m$ y a $n$ son $2, 3, 5, 7$ y $11$.

Podemos escribir la factorización prima de $m$ y $n$ como:
$$m = 2^{a_1} 3^{a_2} 5^{a_3} 7^{a_4} 11^{a_5}$$
$$n = 2^{b_1} 3^{b_2} 5^{b_3} 7^{b_4} 11^{b_5}$$

A partir de las propiedades del máximo común divisor y del mínimo común múltiplo, para cada índice $i \in \{1, 2, 3, 4, 5\}$ se debe cumplir que:
$$\min(a_i, b_i) = 1 \quad \text{y} \quad \max(a_i, b_i) = 3$$

Esto significa que para cada uno de los $5$ factores primos, el par de exponentes $(a_i, b_i)$ solo puede ser $(1, 3)$ o $(3, 1)$. 

Además, sabemos que $m \cdot n = \gcd(m,n) \cdot \mathop{\text{lcm}}[m,n] = 2310^4$, por lo que cada valor válido de $m$ determina de forma única el valor de $n = \frac{2310^4}{m}$. Como $a_i$ solo puede tomar el valor $1$ o $3$ para cada uno de los $5$ primos, existen en total $2^5 = 32$ pares ordenados $(m, n)$ que cumplen las condiciones de divisibilidad.

Dado que $a_i \neq b_i$, nunca ocurre que $m = n$. Por simetría, en exactamente la mitad de estos $32$ pares se cumple que $m < n$ (y en la otra mitad, $m > n$). Por lo tanto, el número de valores posibles para $m$ es:
$$\frac{32}{2} = 16$$

\boxed{16}