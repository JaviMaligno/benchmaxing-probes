Para encontrar todos los valores posibles de $n$, podemos aplicar la desigualdad de Cauchy-Schwarz a las sucesiones $(\sqrt{a_1}, \sqrt{a_2}, \dots, \sqrt{a_n})$ y $(a_1^{3/2}, a_2^{3/2}, \dots, a_n^{3/2})$, lo cual es válido dado que todos los $a_i$ son números reales positivos:

\[\left(\sum_{i = 1}^n \left(\sqrt{a_i}\right)^2\right) \left(\sum_{i = 1}^n \left(a_i^{3/2}\right)^2\right) \ge \left(\sum_{i = 1}^n \sqrt{a_i} \cdot a_i^{3/2}\right)^2\]

Esto se simplifica a:

\[\left(\sum_{i = 1}^n a_i\right) \left(\sum_{i = 1}^n a_i^3\right) \ge \left(\sum_{i = 1}^n a_i^2\right)^2\]

Sustituyendo los valores dados en el problema:
- $\left(\sum_{i = 1}^n a_i\right) \left(\sum_{i = 1}^n a_i^3\right) = 96 \times 216 = 20736$
- $\left(\sum_{i = 1}^n a_i^2\right)^2 = 144^2 = 20736$

Dado que ambos lados son iguales a $20736$, se cumple la condición de igualdad en la desigualdad de Cauchy-Schwarz. Esto implica que las dos sucesiones deben ser proporcionales; es decir, existe una constante $c > 0$ tal que para todo $i \in \{1, 2, \dots, n\}$:

\[\frac{a_i^{3/2}}{\sqrt{a_i}} = c \implies a_i = c\]

Por lo tanto, todos los términos de la sucesión son iguales a $c$. Sustituyendo $a_i = c$ en las dos primeras sumas obtenemos:

1. $\sum_{i = 1}^n c = nc = 96$
2. $\sum_{i = 1}^n c^2 = nc^2 = 144$

Dividiendo la segunda ecuación entre la primera:

\[c = \frac{144}{96} = \frac{3}{2}\]

Sustituyendo el valor de $c$ en la primera ecuación para hallar $n$:

\[n \cdot \frac{3}{2} = 96 \implies n = 96 \cdot \frac{2}{3} = 64\]

Como $n = 64$ es el único valor posible, la suma de todos los valores posibles de $n$ es $64$.

\boxed{64}