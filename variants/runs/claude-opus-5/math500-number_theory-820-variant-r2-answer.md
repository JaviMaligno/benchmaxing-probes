## Planteamiento

$2310 = 2 \cdot 3 \cdot 5 \cdot 7 \cdot 11$, producto de cinco primos distintos, cada uno con exponente 1.

Escribimos para cada primo $p_i$ de esa lista los exponentes $a_i$ en $m$ y $b_i$ en $n$. Como ningún otro primo puede aparecer (el lcm es $2310^3$), se cumple:

- $\min(a_i, b_i) = 1$ (exponente en el gcd)
- $\max(a_i, b_i) = 3$ (exponente en el lcm $= 2310^3$)

Por tanto, para cada uno de los 5 primos, $\{a_i, b_i\} = \{1, 3\}$: hay exactamente 2 opciones independientes (cuál de los dos números recibe el 3).

## Conteo

Esto da $2^5 = 32$ pares ordenados $(m,n)$.

En ningún caso $m = n$, pues eso exigiría $a_i = b_i$ para todo $i$, imposible ya que $1 \neq 3$. Los 32 pares se agrupan entonces en parejas conjugadas $(m,n)$ y $(n,m)$, y exactamente una de cada pareja cumple $m < n$:

$$\frac{32}{2} = 16$$

Cada valor de $m$ determina unívocamente a $n$ (pues $mn = \gcd \cdot \text{lcm}$), así que hay 16 valores distintos de $m$.

\boxed{16}