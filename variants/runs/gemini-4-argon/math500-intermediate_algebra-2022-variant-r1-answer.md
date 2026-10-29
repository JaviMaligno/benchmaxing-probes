Para encontrar todos los posibles valores de $n$, podemos utilizar la desigualdad de Cauchy-Schwarz. 

Consideremos las sucesiones de números reales positivos $(\sqrt{b_1}, \sqrt{b_2}, \dots, \sqrt{b_n})$ y $(b_1^{3/2}, b_2^{3/2}, \dots, b_n^{3/2})$. Aplicando la desigualdad de Cauchy-Schwarz a estas dos sucesiones, obtenemos:

$$\left( \sum_{i=1}^n \left(\sqrt{b_i}\right)^2 \right) \left( \sum_{i=1}^n \left(b_i^{3/2}\right)^2 \right) \ge \left( \sum_{i=1}^n \sqrt{b_i} \cdot b_i^{3/2} \right)^2$$

Lo cual se simplifica a:

$$\left( \sum_{i=1}^n b_i \right) \left( \sum_{i=1}^n b_i^3 \right) \ge \left( \sum_{i=1}^n b_i^2 \right)^2$$

Sustituyendo los valores dados en el problema:
* $\left( \sum_{i=1}^n b_i \right) \left( \sum_{i=1}^n b_i^3 \right) = 108 \times 192 = 20736$
* $\left( \sum_{i=1}^n b_i^2 \right)^2 = 144^2 = 20736$

Como ambos lados son iguales a $20736$, se cumple la igualdad en la desigualdad de Cauchy-Schwarz. Dado que todos los $b_i > 0$, la condición de igualdad implica que las dos sucesiones deben ser proporcionales; es decir, existe una constante $c$ tal que para todo $i \in \{1, 2, \dots, n\}$:

$$\frac{b_i^{3/2}}{\sqrt{b_i}} = c \implies b_i = c$$

Por lo tanto, todos los términos de la sucesión son iguales: $b_1 = b_2 = \dots = b_n = b$.

Sustituyendo esto en las dos primeras ecuaciones dadas:
1. $\sum_{i=1}^n b = n b = 108$
2. $\sum_{i=1}^n b^2 = n b^2 = 144$

Dividiendo la segunda ecuación entre la primera, obtenemos:
$$b = \frac{144}{108} = \frac{4}{3}$$

Ahora sustituimos el valor de $b$ en la primera ecuación para hallar $n$:
$$n \left(\frac{4}{3}\right) = 108 \implies n = \frac{108 \times 3}{4} = 27 \times 3 = 81$$

(Podemos verificar que para $n = 81$ y $b = \frac{4}{3}$, la tercera suma también se cumple: $n b^3 = 81 \times \left(\frac{4}{3}\right)^3 = 81 \times \frac{64}{27} = 3 \times 64 = 192$).

Como $n = 81$ es el único valor posible, la suma de todos los valores posibles de $n$ es $81$.

\boxed{81}