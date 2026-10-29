Para encontrar la suma de todos los posibles valores de $n$, podemos aplicar la desigualdad de Cauchy-Schwarz a las sumas dadas.

Consideremos las dos sucesiones de números reales positivos $(x_1, x_2, \dots, x_n)$ y $(y_1, y_2, \dots, y_n)$ definidas por $x_i = \sqrt{a_i}$ e $y_i = a_i\sqrt{a_i}$ para cada $i \in \{1, 2, \dots, n\}$. 

Por la desigualdad de Cauchy-Schwarz, tenemos que:
\[ \left( \sum_{i=1}^n x_i^2 \right) \left( \sum_{i=1}^n y_i^2 \right) \ge \left( \sum_{i=1}^n x_i y_i \right)^2 \]

Sustituyendo las definiciones de $x_i$ e $y_i$, obtenemos:
\[ \left( \sum_{i=1}^n a_i \right) \left( \sum_{i=1}^n a_i^3 \right) \ge \left( \sum_{i=1}^n a_i^2 \right)^2 \]

Evaluamos ambos lados de la desigualdad con los valores proporcionados en el problema:
- Lado izquierdo: $96 \times 216 = 20736$
- Lado derecho: $144^2 = 20736$

Como ambos lados son iguales, se cumple la condición de igualdad de la desigualdad de Cauchy-Schwarz. Esto implica que las sucesiones $(x_i)$ e $(y_i)$ son proporcionales; es decir, existe una constante $c > 0$ tal que para todo $i$:
\[ \frac{y_i}{x_i} = \frac{a_i\sqrt{a_i}}{\sqrt{a_i}} = a_i = c \]

Por lo tanto, todos los términos de la sucesión son iguales a una misma constante $c$: $a_1 = a_2 = \dots = a_n = c$.

Sustituyendo esto en las dos primeras ecuaciones dadas:
1. $\sum_{i=1}^n a_i = nc = 96$
2. $\sum_{i=1}^n a_i^2 = nc^2 = 144$

Dividiendo la segunda ecuación entre la primera:
\[ c = \frac{144}{96} = \frac{3}{2} \]

Ahora sustituimos el valor de $c$ en la primera ecuación para hallar $n$:
\[ n \left(\frac{3}{2}\right) = 96 \implies n = 96 \times \frac{2}{3} = 64 \]

Dado que $n = 64$ es el único valor posible, la suma de todos los valores posibles de $n$ es $64$.

\boxed{64}