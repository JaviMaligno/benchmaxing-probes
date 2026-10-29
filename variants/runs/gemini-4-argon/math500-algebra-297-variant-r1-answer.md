Para hallar el producto de las coordenadas $y$ de todas las soluciones distintas $(x,y)$ del sistema:
1) $y = x^2 - 7$
2) $y^2 = -9x + 45$

**Paso 1: Sustituir y verificar que las soluciones son distintas**
Sustituimos $y = x^2 - 7$ de la primera ecuación en la segunda ecuación:
$$(x^2 - 7)^2 = -9x + 45$$
$$x^4 - 14x^2 + 49 = -9x + 45$$
$$x^4 - 14x^2 + 9x + 4 = 0$$

Probamos raíces enteras que dividan al término independiente $4$:
- Para $x = 1$: $1^4 - 14(1)^2 + 9(1) + 4 = 1 - 14 + 9 + 4 = 0$.
- Para $x = -4$: $(-4)^4 - 14(-4)^2 + 9(-4) + 4 = 256 - 224 - 36 + 4 = 0$.

Por tanto, podemos factorizar el polinomio dividiendo por $(x - 1)(x + 4) = x^2 + 3x - 4$:
$$(x - 1)(x + 4)(x^2 - 3x - 1) = 0$$

El factor cuadrático $x^2 - 3x - 1 = 0$ tiene discriminante $\Delta = (-3)^2 - 4(1)(-1) = 13 > 0$, lo que significa que las cuatro raíces para $x$ son reales y distintas, dando lugar a $4$ soluciones distintas $(x,y)$.

**Paso 2: Encontrar la ecuación polinómica en términos de $y$ (o calcular el producto directamente)**
De la segunda ecuación del sistema, despejamos $x$ en función de $y$:
$$9x = 45 - y^2 \implies x = 5 - \frac{y^2}{9}$$

Sustituimos esta expresión de $x$ en la primera ecuación:
$$y = \left(5 - \frac{y^2}{9}\right)^2 - 7$$
$$y = 25 - \frac{10}{9}y^2 + \frac{y^4}{81} - 7$$
$$y = \frac{y^4}{81} - \frac{10}{9}y^2 + 18$$

Multiplicando toda la ecuación por $81$ y ordenando los términos obtenemos:
$$y^4 - 90y^2 - 81y + 1458 = 0$$

Como las $4$ soluciones del sistema son distintas y cada valor de $y$ determina un único valor de $x$, las $4$ raíces de este polinomio de grado $4$ corresponden a las coordenadas $y$ de las cuatro soluciones distintas. Por las fórmulas de Vieta, el producto de las cuatro raíces $y_1 y_2 y_3 y_4$ es igual al término independiente:
$$y_1 y_2 y_3 y_4 = 1458$$

*(Alternativamente, calculando a partir de $x$: para $x_1 = 1 \implies y_1 = -6$; para $x_2 = -4 \implies y_2 = 9$; y para las raíces de $x^2 - 3x - 1 = 0$, tenemos $y = x^2 - 7 = 3x - 6$, por lo que $y_3 y_4 = (3x_3 - 6)(3x_4 - 6) = 9x_3 x_4 - 18(x_3 + x_4) + 36 = 9(-1) - 18(3) + 36 = -27$. Así, $(-6) \cdot 9 \cdot (-27) = 1458$.)*

\boxed{1458}