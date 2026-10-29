Para encontrar cuántos valores posibles existen para $a$, sigamos estos pasos:

1. **Factorización prima de $210$:**
   Descomponemos $210$ en sus factores primos:
   $$210 = 2 \cdot 3 \cdot 5 \cdot 7$$
   Por lo tanto, el mínimo común múltiplo es:
   $$\mathop{\text{lcm}}[a,b] = 210^3 = 2^3 \cdot 3^3 \cdot 5^3 \cdot 7^3$$

2. **Análisis de los exponentes primos:**
   Dado que $\gcd(a,b) = 210$ y $\mathop{\text{lcm}}[a,b] = 210^3$, los únicos factores primos de $a$ y $b$ son $2, 3, 5$ y $7$. Podemos escribir $a$ y $b$ como:
   $$a = 2^{a_2} \cdot 3^{a_3} \cdot 5^{a_5} \cdot 7^{a_7}$$
   $$b = 2^{b_2} \cdot 3^{b_3} \cdot 5^{b_5} \cdot 7^{b_7}$$

   Para cada primo $p \in \{2, 3, 5, 7\}$, las condiciones del máximo común divisor y mínimo común múltiplo implican que:
   $$\min(a_p, b_p) = 1 \quad \text{y} \quad \max(a_p, b_p) = 3$$

3. **Conteo de pares $(a,b)$:**
   Para cada uno de los $4$ factores primos, el par de exponentes $(a_p, b_p)$ solo puede tomar dos opciones: $(1, 3)$ o $(3, 1)$. 
   Como la elección para cada uno de los $4$ primos es independiente, el número total de pares ordenados $(a, b)$ posibles es:
   $$2^4 = 16$$

4. **Aplicación de la condición $a < b$:**
   Sabemos que para cualquier par válido $(a, b)$, se cumple que $a \cdot b = \gcd(a,b) \cdot \mathop{\text{lcm}}[a,b] = 210 \cdot 210^3 = 210^4$. Así, el valor de $a$ determina de manera única el valor de $b$.
   Además, $a$ nunca puede ser igual a $b$ (pues $210 \neq 210^3$). Por simetría, de los $16$ pares ordenados $(a, b)$, exactamente la mitad cumple que $a < b$ y la otra mitad cumple que $a > b$.

   Por lo tanto, el número de valores posibles para $a$ es:
   $$\frac{16}{2} = 8$$

\boxed{8}