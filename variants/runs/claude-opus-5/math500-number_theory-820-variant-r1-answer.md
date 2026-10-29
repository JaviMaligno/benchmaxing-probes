## Planteamiento

$2310 = 2\cdot 3\cdot 5\cdot 7\cdot 11$, producto de cinco primos distintos con exponente 1. Entonces $2310^3$ tiene exponente 3 en cada uno de esos cinco primos.

Si $m=\prod p_i^{a_i}$ y $n=\prod p_i^{b_i}$, las condiciones dan para cada primo:

- $\min(a_i,b_i)=1$ (del gcd)
- $\max(a_i,b_i)=3$ (del lcm)

Ningún otro primo puede aparecer, porque el lcm solo contiene esos cinco.

## Conteo

Para cada primo, $\{a_i,b_i\}=\{1,3\}$, es decir 2 opciones: $(a_i,b_i)=(1,3)$ o $(3,1)$. Con cinco primos independientes hay

$$2^5 = 32$$

pares ordenados $(m,n)$.

Nunca ocurre $m=n$ (eso exigiría $a_i=b_i$, imposible con $\{1,3\}$), así que los 32 pares se reparten en parejas simétricas $(m,n)$ y $(n,m)$. La condición $m<n$ selecciona exactamente la mitad:

$$\frac{32}{2}=16$$

\boxed{16}