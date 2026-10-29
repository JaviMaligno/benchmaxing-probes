Para hallar el valor máximo de la expresión
\[\frac{x - y}{x^4 + y^4 + 6}\]
sobre todos los números reales $x$ e $y$, podemos utilizar la desigualdad entre las medias aritmética y geométrica (MA-MG).

**Paso 1: Aplicar la desigualdad MA-MG para $x$ e $y$**

Para cualquier número real $x$, dado que $x^4 \ge 0$, aplicamos la desigualdad MA-MG a los cuatro términos positivos $(x^4, 1, 1, 1)$:
\[\frac{x^4 + 1 + 1 + 1}{4} \ge \sqrt[4]{x^4 \cdot 1 \cdot 1 \cdot 1} = |x|\]
Multiplicando por $4$, obtenemos:
\[x^4 + 3 \ge 4|x| \ge 4x\]
La igualdad se cumple cuando $x^4 = 1$ y $x \ge 0$, es decir, cuando $x = 1$.

De manera análoga, para cualquier número real $y$, aplicamos la desigualdad MA-MG a $(y^4, 1, 1, 1)$:
\[y^4 + 3 \ge 4|y| \ge -4y\]
La igualdad se cumple cuando $y^4 = 1$ e $y \le 0$, es decir, cuando $y = -1$.

**Paso 2: Sumar las desigualdades**

Sumando ambas desigualdades miembro a miembro:
\[(x^4 + 3) + (y^4 + 3) \ge 4x - 4y\]
\[x^4 + y^4 + 6 \ge 4(x - y)\]

**Paso 3: Obtener la cota superior**

Dado que $x^4 + y^4 + 6 > 0$ para cualesquiera $x, y \in \mathbb{R}$, podemos dividir ambos lados de la desigualdad entre $4(x^4 + y^4 + 6)$:
\[\frac{x - y}{x^4 + y^4 + 6} \le \frac{1}{4}\]

**Paso 4: Verificar que se alcanza el máximo**

Evaluando la expresión en $x = 1$ e $y = -1$:
\[\frac{1 - (-1)}{1^4 + (-1)^4 + 6} = \frac{2}{1 + 1 + 6} = \frac{2}{8} = \frac{1}{4}\]

Por lo tanto, el valor máximo es:

\boxed{\frac{1}{4}}