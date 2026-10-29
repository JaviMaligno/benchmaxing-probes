Para encontrar la suma de todas las raíces complejas de la ecuación dada, primero reescribimos la ecuación sumando $4$ a ambos lados y distribuyendo una unidad a cada fracción del miembro izquierdo:

\[\left(\frac{1}{x^2 - 1} + 1\right) + \left(\frac{2}{x^2 - 2} + 1\right) + \left(\frac{3}{x^2 - 3} + 1\right) + \left(\frac{4}{x^2 - 4} + 1\right) = 2022x\]

Simplificando cada término entre paréntesis, obtenemos:

\[\frac{x^2}{x^2 - 1} + \frac{x^2}{x^2 - 2} + \frac{x^2}{x^2 - 3} + \frac{x^2}{x^2 - 4} = 2022x\]

Sea $D(x) = (x^2 - 1)(x^2 - 2)(x^2 - 3)(x^2 - 4)$. Multiplicando ambos lados de la ecuación por $D(x)$ para eliminar los denominadores, obtenemos la ecuación polinómica $P(x) = 0$, donde:

\[P(x) = 2022x(x^2 - 1)(x^2 - 2)(x^2 - 3)(x^2 - 4) - x^2 \sum_{k=1}^{4} \prod_{\substack{j=1 \\ j \neq k}}^{4} (x^2 - j) = 0\]

Observamos que ningún valor de $x$ que anule el denominador $D(x)$ (es decir, $x^2 \in \{1, 2, 3, 4\}$) es raíz de $P(x) = 0$, ya que al evaluar en $x^2 = k$ con $k \in \{1, 2, 3, 4\}$, el primer término se anula pero la sumatoria toma el valor $k \prod_{j \neq k} (k - j) \neq 0$. Por lo tanto, las raíces de la ecuación original coinciden exactamente con las raíces del polinomio $P(x)$.

Desarrollando los términos de mayor grado de cada parte:
1. Para la primera expresión:
   \[2022x D(x) = 2022x(x^8 - 10x^6 + \dots) = 2022x^9 - 20220x^7 + \dots\]
2. Para la segunda expresión:
   \[x^2 \sum_{k=1}^{4} \prod_{\substack{j=1 \\ j \neq k}}^{4} (x^2 - j) = x^2(4x^6 - 30x^4 + \dots) = 4x^8 - 30x^6 + \dots\]

Así, el polinomio $P(x)$ de grado $9$ tiene la forma:
\[P(x) = 2022x^9 - 4x^8 - 20220x^7 + 30x^6 - \dots = 0\]

*(Nota: Aplicando el teorema del valor intermedio en los intervalos definidos por las asíntotas verticales $x = \pm 1, \pm\sqrt{2}, \pm\sqrt{3}, \pm 2$, junto con la raíz $x = 0$, se comprueba que existen $9$ raíces reales distintas, por lo que todas las raíces son simples).*

Por las fórmulas de Vieta, la suma de todas las raíces de $P(x) = 0$ es igual al opuesto del coeficiente de $x^8$ dividido entre el coeficiente principal (de $x^9$):

\[\text{Suma de las raíces} = -\frac{-4}{2022} = \frac{2}{1011}\]

\boxed{\frac{2}{1011}}