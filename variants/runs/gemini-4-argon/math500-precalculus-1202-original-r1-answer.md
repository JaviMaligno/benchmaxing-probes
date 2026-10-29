Para encontrar el polinomio cúbico que satisface $x$, comenzamos definiendo $\alpha = \arccos x$, $\beta = \arccos 2x$ y $\gamma = \arccos 3x$. De este modo, tenemos que:
\[\cos \alpha = x, \quad \cos \beta = 2x, \quad \cos \gamma = 3x.\]

La ecuación dada en el problema se puede reescribir como:
\[\alpha + \beta + \gamma = \pi \implies \alpha + \beta = \pi - \gamma.\]

Aplicando la función coseno en ambos lados de la igualdad:
\[\cos(\alpha + \beta) = \cos(\pi - \gamma).\]

Usando las identidades trigonométricas para el coseno de la suma y el ángulo suplementario, obtenemos:
\[\cos \alpha \cos \beta - \sin \alpha \sin \beta = -\cos \gamma.\]

Como $\alpha, \beta \in [0, \pi]$, sabemos que $\sin \alpha = \sqrt{1 - \cos^2 \alpha} = \sqrt{1 - x^2}$ y $\sin \beta = \sqrt{1 - \cos^2 \beta} = \sqrt{1 - 4x^2}$. Sustituyendo estos valores en la ecuación:
\[x(2x) - \sqrt{1 - x^2}\sqrt{1 - 4x^2} = -3x.\]

Reorganizando los términos para aislar las raíces cuadradas:
\[2x^2 + 3x = \sqrt{1 - x^2}\sqrt{1 - 4x^2}.\]

Elevando ambos lados al cuadrado:
\[(2x^2 + 3x)^2 = (1 - x^2)(1 - 4x^2),\]
\[4x^4 + 12x^3 + 9x^2 = 1 - 5x^2 + 4x^4.\]

Restando $4x^4$ en ambos lados y pasando todos los términos al lado izquierdo, resulta el polinomio cúbico:
\[12x^3 + 14x^2 - 1 = 0.\]

Por el teorema de la raíz racional, podemos verificar que este polinomio no tiene raíces racionales, por lo que es irreducible sobre $\mathbb{Q}$. Como el máximo común divisor de los coeficientes $(12, 14, 0, -1)$ es $1$, los coeficientes enteros que minimizan la suma de sus valores absolutos son $a = 12$, $b = 14$, $c = 0$ y $d = -1$ (o sus opuestos).

Por lo tanto, el menor valor posible de $|a| + |b| + |c| + |d|$ es:
\[|12| + |14| + |0| + |-1| = 12 + 14 + 0 + 1 = 27.\]

\boxed{27}