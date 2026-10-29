Para encontrar los posibles valores de $n$, analizamos las tres ecuaciones dadas para la sucesión de números reales positivos $(b_1, b_2, \dots, b_n)$:
\[\sum_{i=1}^n b_i = 108, \quad \sum_{i=1}^n b_i^2 = 144, \quad \sum_{i=1}^n b_i^3 = 192.\]

Observamos la relación entre los valores de las sumas aplicando la desigualdad de Cauchy-Schwarz a las sucesiones $\left(\sqrt{b_1}, \sqrt{b_2}, \dots, \sqrt{b_n}\right)$ y $\left(b_1^{3/2}, b_2^{3/2}, \dots, b_n^{3/2}\right)$, lo cual es válido dado que $b_i > 0$ para todo $i$:
\[\left(\sum_{i=1}^n \sqrt{b_i} \cdot b_i^{3/2}\right)^2 \le \left(\sum_{i=1}^n b_i\right)\left(\sum_{i=1}^n b_i^3\right).\]

Sustituyendo los valores dados en el problema:
\[\left(\sum_{i=1}^n b_i^2\right)^2 = 144^2 = 20736,\]
\[\left(\sum_{i=1}^n b_i\right)\left(\sum_{i=1}^n b_i^3\right) = 108 \times 192 = 20736.\]

Como ambos lados son iguales, se cumple la igualdad en la desigualdad de Cauchy-Schwarz. Dado que todos los términos $b_i$ son estrictamente positivos, la igualdad se alcanza si y solo si los términos correspondientes de las dos sucesiones son proporcionales, es decir, existe una constante $c$ tal que para todo $i \in \{1, 2, \dots, n\}$:
\[\frac{b_i^{3/2}}{\sqrt{b_i}} = b_i = c.\]

Por lo tanto, todos los números $b_i$ son iguales a una misma constante $c$. Sustituyendo esto en las dos primeras ecuaciones obtenemos:
1. $n c = 108$
2. $n c^2 = 144$

Dividiendo la segunda ecuación entre la primera:
\[c = \frac{144}{108} = \frac{4}{3}.\]

Sustituyendo el valor de $c$ en la primera ecuación para hallar $n$:
\[n \left(\frac{4}{3}\right) = 108 \implies n = 108 \times \frac{3}{4} = 81.\]

Dado que $n = 81$ es el único valor posible, la suma de todos los valores posibles de $n$ es $81$.

\boxed{81}