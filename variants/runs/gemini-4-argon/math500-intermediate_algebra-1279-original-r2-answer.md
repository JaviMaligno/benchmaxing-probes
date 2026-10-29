Para hallar la suma de todas las soluciones complejas de la ecuación

\[\frac{1}{x^2 - 1} + \frac{2}{x^2 - 2} + \frac{3}{x^2 - 3} + \frac{4}{x^2 - 4} = 2010x - 4,\]

procedemos paso a paso:

**Paso 1: Simplificar la expresión sumando $4$ a ambos lados**
Sumamos $4$ en ambos miembros de la ecuación y distribuimos un $1$ a cada una de las cuatro fracciones del lado izquierdo:
\[\left(\frac{1}{x^2 - 1} + 1\right) + \left(\frac{2}{x^2 - 2} + 1\right) + \left(\frac{3}{x^2 - 3} + 1\right) + \left(\frac{4}{x^2 - 4} + 1\right) = 2010x.\]

Observando que $\frac{k}{x^2 - k} + 1 = \frac{x^2}{x^2 - k}$ para cada $k \in \{1, 2, 3, 4\}$, la ecuación se transforma en:
\[\frac{x^2}{x^2 - 1} + \frac{x^2}{x^2 - 2} + \frac{x^2}{x^2 - 3} + \frac{x^2}{x^2 - 4} = 2010x.\]

**Paso 2: Expresar la ecuación en forma polinómica**
Sea $D(x) = (x^2 - 1)(x^2 - 2)(x^2 - 3)(x^2 - 4)$. Para $x^2 \notin \{1, 2, 3, 4\}$, multiplicamos ambos lados por $D(x)$:
\[x^2 \sum_{k=1}^{4} \prod_{\substack{j=1 \\ j \neq k}}^{4} (x^2 - j) = 2010x D(x).\]

Observemos los términos de mayor grado de cada parte:
- $D(x) = (x^2 - 1)(x^2 - 2)(x^2 - 3)(x^2 - 4) = x^8 - 10x^6 + \cdots + 24$, por lo que $2010x D(x) = 2010x^9 - 20100x^7 + \cdots$.
- Cada uno de los $4$ sumandos de $\sum_{k=1}^{4} \prod_{j \neq k} (x^2 - j)$ es un polinomio mónico de grado $6$, por lo que su suma tiene término principal $4x^6$. Al multiplicar por $x^2$, obtenemos $4x^8 - \cdots$.

Reordenando todos los términos en un solo polinomio $P(x) = 0$:
\[P(x) = 2010x^9 - 4x^8 - 20100x^7 + \cdots = 0.\]

**Paso 3: Verificar que no hay raíces extrañas ni múltiples**
1. Si $x^2 \in \{1, 2, 3, 4\}$, entonces $D(x) = 0$, mientras que el término del lado izquierdo no se anula; por tanto, ninguna raíz de $P(x)$ anula los denominadores originales.
2. Claramente $x = 0$ es una solución simple. Para $x \neq 0$, la ecuación equivale a:
   \[f(x) = \frac{x}{x^2 - 1} + \frac{x}{x^2 - 2} + \frac{x}{x^2 - 3} + \frac{x}{x^2 - 4} = 2010.\]
   Dado que $f'(x) = -\sum_{k=1}^{4} \frac{x^2 + k}{(x^2 - k)^2} < 0$ en todo su dominio real, $f(x)$ es estrictamente decreciente en cada intervalo entre sus asíntotas verticales. Como $f(x)$ toma todos los valores de $(-\infty, +\infty)$ en los $7$ intervalos acotados por las asíntotas $\pm 2, \pm\sqrt{3}, \pm\sqrt{2}, \pm 1$ y todos los valores de $(0, +\infty)$ en $(2, +\infty)$, la ecuación $f(x) = 2010$ tiene exactamente $8$ soluciones reales distintas no nulas. Junto con $x = 0$, las $9$ raíces del polinomio de grado $9$ son todas simples (distintas).

**Paso 4: Aplicar las fórmulas de Vieta**
Por las fórmulas de Vieta para el polinomio $P(x) = 2010x^9 - 4x^8 - 20100x^7 + \cdots = 0$, la suma de sus $9$ raíces es:
\[-\frac{-4}{2010} = \frac{4}{2010} = \frac{2}{1005}.\]

\boxed{\frac{2}{1005}}