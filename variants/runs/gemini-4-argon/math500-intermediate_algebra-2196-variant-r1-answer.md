Para encontrar el mayor valor posible de la expresión
\[\frac{a - b}{a^4 + b^4 + 96}\]
donde $a$ y $b$ son números reales, seguimos los siguientes pasos:

1. **Reducción mediante simetría:**
   Como el denominador $a^4 + b^4 + 96$ es siempre positivo, el máximo de la expresión será positivo, lo que ocurre cuando $a > b$. 
   Hagamos el cambio de variables $a = x + y$ y $b = -x + y$, donde $x = \frac{a-b}{2} > 0$ e $y = \frac{a+b}{2}$. Entonces $a - b = 2x$ y:
   \[a^4 + b^4 = (x + y)^4 + (x - y)^4 = 2(x^4 + 6x^2y^2 + y^4).\]
   Para un valor fijo de $x > 0$, esta suma se minimiza cuando $y = 0$, es decir, cuando $a = x$ y $b = -x$.

2. **Optimización en una variable:**
   Sustituyendo $a = x$ y $b = -x$ (con $x > 0$) en la expresión original, obtenemos:
   \[\frac{2x}{2x^4 + 96} = \frac{x}{x^4 + 48} = \frac{1}{x^3 + \frac{48}{x}}.\]

3. **Aplicación de la desigualdad MA-MG (Media Aritmética - Media Geométrica):**
   Para maximizar la fracción, debemos minimizar el denominador $x^3 + \frac{48}{x}$ para $x > 0$. Descomponemos el término $\frac{48}{x}$ en tres partes iguales y aplicamos la desigualdad MA-MG a los cuatro términos positivos:
   \[x^3 + \frac{16}{x} + \frac{16}{x} + \frac{16}{x} \ge 4 \sqrt[4]{x^3 \cdot \frac{16}{x} \cdot \frac{16}{x} \cdot \frac{16}{x}} = 4 \sqrt[4]{16^3} = 4 \cdot 8 = 32.\]
   La igualdad se alcanza cuando $x^3 = \frac{16}{x}$, lo que implica $x^4 = 16$, es decir, $x = 2$ (dado que $x > 0$).

Por lo tanto, el valor máximo ocurre cuando $a = 2$ y $b = -2$, y dicho valor es:

\[\boxed{\frac{1}{32}}\]