## Razonamiento

Factorizamos: $210 = 2\cdot 3\cdot 5\cdot 7$, por lo que
$$210^3 = 2^3\cdot 3^3\cdot 5^3\cdot 7^3.$$

Para cada primo $p \in \{2,3,5,7\}$, sean $\alpha_p$ y $\beta_p$ los exponentes de $p$ en $a$ y $b$. Entonces:
- $\min(\alpha_p,\beta_p) = 1$ (por el gcd),
- $\max(\alpha_p,\beta_p) = 3$ (por el lcm).

Luego $\{\alpha_p,\beta_p\} = \{1,3\}$ para cada uno de los cuatro primos, es decir, hay 2 opciones por primo: el exponente $3$ va a $a$ o a $b$.

Esto da $2^4 = 16$ pares ordenados $(a,b)$. Ningún par cumple $a=b$ (eso exigiría $\alpha_p=\beta_p$, imposible). Como los pares se agrupan en intercambios $(a,b) \leftrightarrow (b,a)$, exactamente la mitad satisface $a<b$:
$$\frac{16}{2} = 8.$$

\boxed{8}