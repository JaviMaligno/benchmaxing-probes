Para resolver el problema paso a paso, expresemos los primeros términos de la sucesión en función de $a_1$:

1. Sabemos que la relación de recurrencia es:
   \[a_{i + 1} = \frac{1}{1 - a_i}\]

2. Calculamos $a_2$ y $a_3$ en términos de $a_1$:
   \[a_2 = \frac{1}{1 - a_1}\]
   \[a_3 = \frac{1}{1 - a_2} = \frac{1}{1 - \frac{1}{1 - a_1}} = \frac{1 - a_1}{(1 - a_1) - 1} = \frac{1 - a_1}{-a_1} = \frac{a_1 - 1}{a_1}\]

3. Aplicamos la condición dada $a_3 = a_1$:
   \[\frac{a_1 - 1}{a_1} = a_1\]
   Multiplicando ambos lados por $a_1$ (con $a_1 \neq 0$):
   \[a_1 - 1 = a_1^2 \implies a_1^2 - a_1 + 1 = 0\]

4. Observamos que de $a_1^2 - a_1 + 1 = 0$ se deduce que $\frac{1}{1 - a_1} = a_1$, lo cual implica que $a_2 = a_1$. Por lo tanto, la sucesión es constante para todo $n \ge 1$:
   \[a_1 = a_2 = a_3 = \dots = a_9\]

5. Multiplicando la ecuación $a_1^2 - a_1 + 1 = 0$ por $(a_1 + 1)$, obtenemos:
   \[(a_1 + 1)(a_1^2 - a_1 + 1) = 0 \implies a_1^3 + 1 = 0 \implies a_1^3 = -1\]

6. Como $a_9 = a_1$, calculamos $(a_9)^9$:
   \[(a_9)^9 = (a_1)^9 = (a_1^3)^3 = (-1)^3 = -1\]

\boxed{-1}