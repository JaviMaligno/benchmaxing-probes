Para encontrar el producto de las coordenadas $y$ de todas las soluciones distintas $(x,y)$ del sistema de ecuaciones:
1) $y = x^2 - 8$
2) $y^2 = -5x + 44$

Podemos despejar $x$ de la segunda ecuación y sustituirla en la primera, o bien sustituir $y$ de la primera ecuación en la segunda para hallar todas las soluciones posibles.

**Paso 1: Encontrar las soluciones $(x,y)$ sustituyendo $y$ en la segunda ecuación.**
Sustituimos $y = x^2 - 8$ en $y^2 = -5x + 44$:
$$(x^2 - 8)^2 = -5x + 44$$
$$x^4 - 16x^2 + 64 = -5x + 44$$
$$x^4 - 16x^2 + 5x + 20 = 0$$

Factorizamos este polinomio de grado 4. Probando raíces enteras que dividan a $20$, notamos que $x = -4$ es una raíz:
$$(-4)^4 - 16(-4)^2 + 5(-4) + 20 = 256 - 256 - 20 + 20 = 0$$

Dividiendo por $(x + 4)$, obtenemos:
$$(x + 4)(x^3 - 4x^2 + 5) = 0$$

Para el factor cúbico $x^3 - 4x^2 + 5$, probamos $x = -1$:
$$(-1)^3 - 4(-1)^2 + 5 = -1 - 4 + 5 = 0$$

Dividiendo por $(x + 1)$, obtenemos la factorización completa:
$$(x + 4)(x + 1)(x^2 - 5x + 5) = 0$$

Las cuatro raíces para $x$ son:
- $x_1 = -4$
- $x_2 = -1$
- $x_3 = \frac{5 + \sqrt{5}}{2}$
- $x_4 = \frac{5 - \sqrt{5}}{2}$

Como los cuatro valores de $x$ son distintos, generan cuatro pares de soluciones $(x,y)$ distintas.

**Paso 2: Calcular las coordenadas $y$ correspondientes y su producto.**
Usando $y = x^2 - 8$:
- Para $x_1 = -4$: $y_1 = (-4)^2 - 8 = 8$
- Para $x_2 = -1$: $y_2 = (-1)^2 - 8 = -7$
- Para $x_3$ y $x_4$, dado que satisfacen $x^2 = 5x - 5$, tenemos $y = (5x - 5) - 8 = 5x - 13$:
  $$y_3 = \frac{-1 + 5\sqrt{5}}{2}, \quad y_4 = \frac{-1 - 5\sqrt{5}}{2}$$

Multiplicamos todas las coordenadas $y$:
$$y_1 \cdot y_2 = 8 \cdot (-7) = -56$$
$$y_3 \cdot y_4 = \left(\frac{-1 + 5\sqrt{5}}{2}\right)\left(\frac{-1 - 5\sqrt{5}}{2}\right) = \frac{1 - 125}{4} = -31$$

*(Alternativamente, despejando $x = \frac{44 - y^2}{5}$ y sustituyendo en $y = x^2 - 8$, se obtiene el polinomio $y^4 - 88y^2 - 25y + 1736 = 0$, cuyo término independiente por las fórmulas de Vieta nos da directamente el producto de las cuatro raíces).*

Finalmente, el producto total es:
$$(-56) \cdot (-31) = 1736$$

\boxed{1736}