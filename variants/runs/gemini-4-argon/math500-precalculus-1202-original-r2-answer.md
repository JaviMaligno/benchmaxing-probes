Para encontrar el polinomio cúbico que satisface $x$, partimos de la ecuación dada:
$$\arccos x + \arccos 2x + \arccos 3x = \pi$$

Restamos $\arccos 3x$ en ambos lados de la ecuación:
$$\arccos x + \arccos 2x = \pi - \arccos 3x$$

Aplicamos la función coseno a ambos lados, recordando las identidades $\cos(\alpha + \beta) = \cos\alpha\cos\beta - \sin\alpha\sin\beta$ y $\cos(\pi - \theta) = -\cos\theta$:
$$\cos(\arccos x + \arccos 2x) = \cos(\pi - \arccos 3x)$$
$$\cos(\arccos x)\cos(\arccos 2x) - \sin(\arccos x)\sin(\arccos 2x) = -\cos(\arccos 3x)$$

Usando el hecho de que $\sin(\arccos u) = \sqrt{1 - u^2}$, obtenemos:
$$x(2x) - \sqrt{1 - x^2}\sqrt{1 - 4x^2} = -3x$$

Reorganizamos los términos para aislar las raíces cuadradas en un lado:
$$2x^2 + 3x = \sqrt{(1 - x^2)(1 - 4x^2)}$$

Elevamos ambos lados al cuadrado:
$$(2x^2 + 3x)^2 = (1 - x^2)(1 - 4x^2)$$
$$4x^4 + 12x^3 + 9x^2 = 1 - 5x^2 + 4x^4$$

Restamos $4x^4$ en ambos lados y pasamos todos los términos al lado izquierdo:
$$12x^3 + 9x^2 + 5x^2 - 1 = 0$$
$$12x^3 + 14x^2 - 1 = 0$$

Por el teorema de las raíces racionales, las posibles raíces racionales de $12x^3 + 14x^2 - 1 = 0$ son de la forma $\pm \frac{1}{k}$ donde $k \mid 12$. Al verificar estos valores, ninguno anula el polinomio, por lo que el polinomio es irreducible sobre $\mathbb{Q}$.

Dado que $\gcd(12, 14, 0, -1) = 1$, los coeficientes enteros que minimizan la suma de sus valores absolutos corresponden a $a = 12$, $b = 14$, $c = 0$ y $d = -1$ (o sus opuestos).

Por lo tanto, el menor valor posible de $|a| + |b| + |c| + |d|$ es:
$$|12| + |14| + |0| + |-1| = 12 + 14 + 0 + 1 = 27$$

\boxed{27}