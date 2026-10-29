Para encontrar el producto de las coordenadas $y$ de todas las soluciones distintas $(x,y)$ del sistema:
$$y = x^2 - 7$$
$$y^2 = -9x + 45$$

**Paso 1: Despejar $x$ en términos de $y$ y sustituir.**
De la segunda ecuación, podemos despejar $x$:
$$9x = 45 - y^2 \implies x = 5 - \frac{y^2}{9}$$

Como $x$ está unívocamente determinado por $y$, cada valor distinto de $x$ produce un valor distinto de $y$. Sustituyendo esta expresión para $x$ en la primera ecuación:
$$y = \left(5 - \frac{y^2}{9}\right)^2 - 7$$
$$y = 25 - \frac{10}{9}y^2 + \frac{y^4}{81} - 7$$
$$y = 18 - \frac{10}{9}y^2 + \frac{y^4}{81}$$

Multiplicando toda la ecuación por $81$ para eliminar los denominadores y ordenando los términos:
$$y^4 - 90y^2 - 81y + 1458 = 0$$

**Paso 2: Verificar que las cuatro soluciones son distintas.**
Sustituyendo $y = x^2 - 7$ en la segunda ecuación obtenemos el polinomio en $x$:
$$(x^2 - 7)^2 = -9x + 45$$
$$x^4 - 14x^2 + 9x + 4 = 0$$

Factorizando este polinomio:
$$(x - 1)(x + 4)(x^2 - 3x - 1) = 0$$

Las raíces son $x_1 = 1$, $x_2 = -4$ y $x_{3,4} = \frac{3 \pm \sqrt{13}}{2}$, las cuales son cuatro raíces reales y distintas. Por lo tanto, el sistema tiene exactamente cuatro soluciones distintas $(x,y)$ con cuatro coordenadas $y$ distintas.

**Paso 3: Calcular el producto de las coordenadas $y$.**
Por las fórmulas de Vieta aplicadas al polinomio mónico de grado $4$ en $y$:
$$y^4 - 90y^2 - 81y + 1458 = 0$$
el producto de sus cuatro raíces $y_1 y_2 y_3 y_4$ es igual al término independiente $(-1)^4 \cdot 1458 = 1458$.

\boxed{1458}