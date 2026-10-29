Para encontrar cuántos valores posibles existen para $a$, comencemos descomponiendo $210$ en sus factores primos:
$$210 = 2 \cdot 3 \cdot 5 \cdot 7$$

Dado que $\gcd(a,b) = 210$ y $\mathop{\text{lcm}}[a,b] = 210^3 = 2^3 \cdot 3^3 \cdot 5^3 \cdot 7^3$, los números $a$ y $b$ solo pueden tener como factores primos a $2, 3, 5$ y $7$. Podemos escribirlos como:
$$a = 2^{a_2} 3^{a_3} 5^{a_5} 7^{a_7}$$
$$b = 2^{b_2} 3^{b_3} 5^{b_5} 7^{b_7}$$

Por las propiedades del máximo común divisor y del mínimo común múltiplo, para cada primo $p \in \{2, 3, 5, 7\}$ se debe cumplir que:
$$\min(a_p, b_p) = 1 \quad \text{y} \quad \max(a_p, b_p) = 3$$

Esto significa que para cada uno de los $4$ factores primos, el par ordenado de exponentes $(a_p, b_p)$ tiene exactamente $2$ opciones: $(1, 3)$ o $(3, 1)$.

Como hay $4$ primos independientes, el número total de pares ordenados $(a, b)$ que cumplen con las condiciones del $\gcd$ y $\mathop{\text{lcm}}$ es:
$$2^4 = 16$$

Observemos además que:
1. Cada valor de $a$ determina de forma única el valor de $b$, ya que $a \cdot b = \gcd(a,b) \cdot \mathop{\text{lcm}}[a,b] = 210^4$.
2. En ningún caso es posible que $a = b$, puesto que para cada primo sus exponentes son distintos ($1 \neq 3$).

Por simetría, de los $16$ pares posibles $(a, b)$, exactamente la mitad cumple que $a < b$ y la otra mitad cumple que $a > b$. Por lo tanto, la cantidad de valores posibles para $a$ tales que $a < b$ es:
$$\frac{16}{2} = 8$$

\boxed{8}