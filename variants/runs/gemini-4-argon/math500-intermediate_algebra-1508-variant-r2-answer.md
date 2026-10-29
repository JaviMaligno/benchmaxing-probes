Para encontrar el valor de $(b_9)^9$, expresemos primero $b_2$ y $b_3$ en términos de $b_1$ usando la relación de recurrencia dada:

1. Para $k = 1$:
   \[b_2 = -\frac{1}{1 + b_1}\]

2. Para $k = 2$:
   \[b_3 = -\frac{1}{1 + b_2} = -\frac{1}{1 - \frac{1}{1 + b_1}} = -\frac{1}{\frac{b_1}{1 + b_1}} = -\frac{1 + b_1}{b_1}\]

Sabemos que $b_3 = b_1$, por lo que igualamos la expresión obtenida a $b_1$:
\[-\frac{1 + b_1}{b_1} = b_1\]

Multiplicando ambos lados por $b_1$ (con $b_1 \neq 0$):
\[-1 - b_1 = b_1^2 \implies b_1^2 + b_1 + 1 = 0\]

Observemos que si $b_1^2 + b_1 + 1 = 0$, entonces $1 + b_1 = -b_1^2$ y además $(b_1 - 1)(b_1^2 + b_1 + 1) = 0 \implies b_1^3 = 1$. Sustituyendo esto en la expresión para $b_2$:
\[b_2 = -\frac{1}{1 + b_1} = -\frac{1}{-b_1^2} = \frac{1}{b_1^2} = \frac{b_1^3}{b_1^2} = b_1\]

Por lo tanto, la sucesión es constante ($b_n = b_1$ para todo $n \ge 1$), de modo que $b_9 = b_1$. 

Finalmente, como $b_1^3 = 1$, calculamos $(b_9)^9$:
\[(b_9)^9 = (b_1)^9 = (b_1^3)^3 = 1^3 = 1\]

\boxed{1}