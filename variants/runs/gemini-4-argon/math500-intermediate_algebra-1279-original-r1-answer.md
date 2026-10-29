Para encontrar la suma de todas las soluciones complejas de la ecuación
\[\frac{1}{x^2 - 1} + \frac{2}{x^2 - 2} + \frac{3}{x^2 - 3} + \frac{4}{x^2 - 4} = 2010x - 4,\]
primero sumamos $4$ a ambos lados de la ecuación y distribuimos un $1$ en cada una de las cuatro fracciones del lado izquierdo:
\[\left(\frac{1}{x^2 - 1} + 1\right) + \left(\frac{2}{x^2 - 2} + 1\right) + \left(\frac{3}{x^2 - 3} + 1\right) + \left(\frac{4}{x^2 - 4} + 1\right) = 2010x.\]

Simplificando cada término mediante la identidad $\frac{k}{x^2 - k} + 1 = \frac{x^2}{x^2 - k}$, obtenemos:
\[\frac{x^2}{x^2 - 1} + \frac{x^2}{x^2 - 2} + \frac{x^2}{x^2 - 3} + \frac{x^2}{x^2 - 4} = 2010x.\]

Observamos inmediatamente que $x = 0$ es una solución válida (pues anula ambos lados y no anula ningún denominador).

Para $x \neq 0$, podemos dividir ambos lados de la ecuación entre $x$:
\[\frac{x}{x^2 - 1} + \frac{x}{x^2 - 2} + \frac{x}{x^2 - 3} + \frac{x}{x^2 - 4} = 2010.\]

Sea $D(x) = (x^2 - 1)(x^2 - 2)(x^2 - 3)(x^2 - 4)$. Multiplicando toda la ecuación por $D(x)$, obtenemos la ecuación polinómica:
\[x \sum_{k=1}^4 \prod_{\substack{1 \le j \le 4 \\ j \neq k}} (x^2 - j) = 2010 (x^2 - 1)(x^2 - 2)(x^2 - 3)(x^2 - 4).\]

Verifiquemos primero que todas las raíces de este polinomio son simples y que ninguna coincide con las raíces del denominador $D(x) = 0$:
1. Si $x^2 = k \in \{1, 2, 3, 4\}$, el lado derecho se anula, mientras que el lado izquierdo vale $x \prod_{j \neq k} (k - j) \neq 0$. Por lo tanto, no se introducen soluciones extrañas al multiplicar por $D(x)$.
2. La derivada de $f(x) = \sum_{k=1}^4 \frac{x}{x^2 - k}$ es $f'(x) = -\sum_{k=1}^4 \frac{x^2 + k}{(x^2 - k)^2} < 0$ en todo su dominio real. Como $f(x)$ es estrictamente decreciente en cada uno de los intervalos determinados por sus asíntotas verticales ($\pm 1, \pm\sqrt{2}, \pm\sqrt{3}, \pm 2$), cruza la recta horizontal $y = 2010$ exactamente una vez en cada uno de los $8$ intervalos donde $\lim_{x \to a^+} f(x) = +\infty$. Esto garantiza que las $8$ raíces del polinomio de grado $8$ son reales y distintas entre sí (y distintas de $x = 0$).

Expandiendo los términos de mayor grado de ambos lados:
- En el lado derecho: $2010(x^8 - 10x^6 + \dots) = 2010x^8 - 20100x^6 + \dots$
- En el lado izquierdo: $x(4x^6 - 30x^4 + \dots) = 4x^7 - 30x^5 + \dots$

Igualando a cero, obtenemos el polinomio de grado $8$:
\[2010x^8 - 4x^7 - 20100x^6 + 30x^5 + \dots = 0.\]

Por las fórmulas de Vieta, la suma de las $8$ raíces no nulas es:
\[-\frac{-4}{2010} = \frac{4}{2010} = \frac{2}{1005}.\]

Sumando la solución $x = 0$, la suma de todas las soluciones complejas de la ecuación es $0 + \frac{2}{1005} = \frac{2}{1005}$.

\boxed{\frac{2}{1005}}