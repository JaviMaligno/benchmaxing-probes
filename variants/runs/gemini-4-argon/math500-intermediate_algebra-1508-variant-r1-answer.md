Para resolver el problema paso a paso, expresemos los primeros términos de la sucesión en función de $b_1$:

1. Para $k = 1$, tenemos:
   \[b_2 = -\frac{1}{1 + b_1}\]

2. Para $k = 2$, sustituimos $b_2$ en la relación de recurrencia:
   \[b_3 = -\frac{1}{1 + b_2} = -\frac{1}{1 - \frac{1}{1 + b_1}} = -\frac{1}{\frac{b_1}{1 + b_1}} = -\frac{1 + b_1}{b_1}\]

3. El problema nos indica que $b_3 = b_1$. Igualando ambas expresiones, obtenemos:
   \[-\frac{1 + b_1}{b_1} = b_1\]
   Multiplicando ambos lados por $b_1$ (con $b_1 \neq 0$):
   \[-1 - b_1 = b_1^2 \implies b_1^2 + b_1 + 1 = 0\]

4. Observemos que si $b_1^2 + b_1 + 1 = 0$, entonces $1 + b_1 = -b_1^2$, y como las raíces de esta ecuación cuadrática cumplen que $b_1^3 = 1$ (ya que $b_1^3 - 1 = (b_1 - 1)(b_1^2 + b_1 + 1) = 0$), podemos calcular $b_2$:
   \[b_2 = -\frac{1}{1 + b_1} = -\frac{1}{-b_1^2} = \frac{1}{b_1^2} = \frac{b_1^3}{b_1^2} = b_1\]

5. Como $b_2 = b_1$, la sucesión es constante, por lo que todos sus términos son iguales a $b_1$. En particular:
   \[b_9 = b_1\]

6. Finalmente, como $b_1^3 = 1$, calculamos $(b_9)^9$:
   \[(b_9)^9 = (b_1)^9 = (b_1^3)^3 = 1^3 = 1\]

\boxed{1}