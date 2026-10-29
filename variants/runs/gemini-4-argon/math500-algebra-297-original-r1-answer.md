Para hallar el producto de las coordenadas $y$ de todas las soluciones distintas $(x,y)$ del sistema de ecuaciones:
1) $y = x^2 - 8$
2) $y^2 = -5x + 44$

**Paso 1: Despejar $x$ en términos de $y$**
De la segunda ecuación, podemos despejar $x$:
$$5x = 44 - y^2 \implies x = \frac{44 - y^2}{5}$$

**Paso 2: Sustituir en la primera ecuación**
Sustituimos esta expresión para $x$ en la primera ecuación $y = x^2 - 8$:
$$y = \left(\frac{44 - y^2}{5}\right)^2 - 8$$

Multiplicamos ambos lados por $25$:
$$25y = (44 - y^2)^2 - 200$$
$$25y = 1936 - 88y^2 + y^4 - 200$$
$$y^4 - 88y^2 - 25y + 1736 = 0$$

**Paso 3: Verificar que las 4 soluciones producen valores distintos de $y$**
Si sustituimos $y = x^2 - 8$ en la segunda ecuación para analizar las raíces:
$$(x^2 - 8)^2 = -5x + 44$$
$$x^4 - 16x^2 + 64 = -5x + 44$$
$$x^4 - 16x^2 + 5x + 20 = 0$$

Factorizamos por agrupación:
$$x^2(x^2 - 16) + 5(x + 4) = 0$$
$$(x + 4)(x^3 - 4x^2 + 5) = 0$$

Observamos que $x = -1$ es raíz del factor cúbico, por lo que podemos seguir factorizando:
$$(x + 4)(x + 1)(x^2 - 5x + 5) = 0$$

Las cuatro soluciones para $x$ son $x_1 = -4$, $x_2 = -1$, y $x_{3,4} = \frac{5 \pm \sqrt{5}}{2}$. Evaluando $y = x^2 - 8$ para cada una:
- $y_1 = (-4)^2 - 8 = 8$
- $y_2 = (-1)^2 - 8 = -7$
- $y_3 = \frac{-1 + 5\sqrt{5}}{2}$
- $y_4 = \frac{-1 - 5\sqrt{5}}{2}$

Las cuatro soluciones $(x,y)$ son distintas y tienen coordenadas $y$ distintas.

**Paso 4: Calcular el producto de las coordenadas $y$**
Por las fórmulas de Vieta aplicadas al polinomio $y^4 - 88y^2 - 25y + 1736 = 0$ (o multiplicando directamente $y_1 \cdot y_2 \cdot y_3 \cdot y_4 = 8 \cdot (-7) \cdot (-31)$), el producto de las cuatro raíces es el término independiente:

\boxed{1736}