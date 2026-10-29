Para determinar la suma de todas las raíces complejas de la ecuación
\[\frac{1}{x^2 - 1} + \frac{2}{x^2 - 2} + \frac{3}{x^2 - 3} + \frac{4}{x^2 - 4} = 2022x - 4,\]
procedemos paso a paso:

**Paso 1: Simplificar la ecuación.**
Sumamos $4$ a ambos lados de la ecuación y distribuimos un $1$ a cada una de las cuatro fracciones del lado izquierdo:
\[\left(\frac{1}{x^2 - 1} + 1\right) + \left(\frac{2}{x^2 - 2} + 1\right) + \left(\frac{3}{x^2 - 3} + 1\right) + \left(\frac{4}{x^2 - 4} + 1\right) = 2022x.\]

Dado que $\frac{k}{x^2 - k} + 1 = \frac{x^2}{x^2 - k}$ para cada $k \in \{1, 2, 3, 4\}$, la ecuación se transforma en:
\[\frac{x^2}{x^2 - 1} + \frac{x^2}{x^2 - 2} + \frac{x^2}{x^2 - 3} + \frac{x^2}{x^2 - 4} = 2022x.\]

**Paso 2: Convertir a una ecuación polinómica.**
Sea $P(x) = (x^2 - 1)(x^2 - 2)(x^2 - 3)(x^2 - 4)$. Multiplicando ambos lados por $P(x)$ (observando que los valores $x = \pm\sqrt{k}$ que anulan los denominadores no anulan la ecuación resultante), obtenemos:
\[x^2 \sum_{k=1}^{4} \prod_{\substack{j=1 \\ j \neq k}}^{4} (x^2 - j) = 2022x (x^2 - 1)(x^2 - 2)(x^2 - 3)(x^2 - 4).\]

**Paso 3: Verificar que las raíces son simples.**
Observamos que $x = 0$ es una raíz simple de la ecuación. Para $x \neq 0$, la ecuación equivale a:
\[f(x) = \frac{x}{x^2 - 1} + \frac{x}{x^2 - 2} + \frac{x}{x^2 - 3} + \frac{x}{x^2 - 4} = 2022.\]
Como la derivada de cada término es $\frac{-x^2 - k}{(x^2 - k)^2} < 0$, la función $f(x)$ es estrictamente decreciente en cada uno de los intervalos determinados por sus asíntotas verticales $x = \pm 1, \pm\sqrt{2}, \pm\sqrt{3}, \pm 2$. En los $8$ intervalos donde $f(x)$ toma valores positivos hasta $+\infty$, la ecuación $f(x) = 2022$ tiene exactamente una solución real por intervalo. Junto con $x = 0$, las $9$ raíces del polinomio de grado $9$ son todas reales y distintas.

**Paso 4: Aplicar las fórmulas de Vieta.**
Desarrollando los términos de mayor grado de la ecuación polinómica:
- El lado derecho es $2022x(x^8 - 10x^6 + \dots) = 2022x^9 - 20220x^7 + \dots$ (solo potencias impares de $x$).
- El lado izquierdo es $x^2(4x^6 - 30x^4 + \dots) = 4x^8 - 30x^6 + \dots$ (solo potencias pares de $x$).

Igualando a cero, obtenemos el polinomio de grado $9$:
\[2022x^9 - 4x^8 - 20220x^7 + 30x^6 + \dots = 0.\]

Por las fórmulas de Vieta, la suma de las $9$ raíces es:
\[-\frac{-4}{2022} = \frac{4}{2022} = \frac{2}{1011}.\]

\boxed{\frac{2}{1011}}