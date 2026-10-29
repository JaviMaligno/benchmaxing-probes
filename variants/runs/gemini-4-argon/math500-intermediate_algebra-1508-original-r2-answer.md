Para encontrar el valor de $(a_9)^9$, primero expresamos los primeros términos de la sucesión en función de $a_1$ utilizando la relación de recurrencia dada:

1. Para $i = 1$:
   \[a_2 = \frac{1}{1 - a_1}\]

2. Para $i = 2$:
   \[a_3 = \frac{1}{1 - a_2} = \frac{1}{1 - \frac{1}{1 - a_1}} = \frac{1 - a_1}{(1 - a_1) - 1} = \frac{1 - a_1}{-a_1} = \frac{a_1 - 1}{a_1}\]

Sabemos por el enunciado que $a_3 = a_1$. Igualando la expresión obtenida para $a_3$ con $a_1$, tenemos:
\[\frac{a_1 - 1}{a_1} = a_1\]

Multiplicando ambos lados por $a_1$ (asumiendo $a_1 \neq 0$):
\[a_1 - 1 = a_1^2 \implies a_1^2 - a_1 + 1 = 0\]

Observamos que si $a_1^2 - a_1 + 1 = 0$, entonces $\frac{1}{1 - a_1} = a_1$, lo que significa que $a_2 = a_1$. Por lo tanto, la sucesión es constante y todos sus términos son iguales a $a_1$; en particular, $a_9 = a_1$.

Además, multiplicando la ecuación $a_1^2 - a_1 + 1 = 0$ por $(a_1 + 1)$, obtenemos:
\[(a_1 + 1)(a_1^2 - a_1 + 1) = 0 \implies a_1^3 + 1 = 0 \implies a_1^3 = -1\]

Finalmente, calculamos $(a_9)^9$:
\[(a_9)^9 = (a_1)^9 = (a_1^3)^3 = (-1)^3 = -1\]

\boxed{-1}