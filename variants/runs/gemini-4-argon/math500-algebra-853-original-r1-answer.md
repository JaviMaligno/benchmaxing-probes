Para encontrar la distancia más pequeña entre el origen $(0,0)$ y un punto $(x, y)$ en la gráfica de $y = \frac{1}{\sqrt{2}}(x^2 - 3)$, minimizamos el cuadrado de la distancia, $D^2$:

$$D^2 = x^2 + y^2$$

Sustituyendo la expresión de $y$ en la ecuación:

$$D^2 = x^2 + \left(\frac{1}{\sqrt{2}}(x^2 - 3)\right)^2 = x^2 + \frac{1}{2}(x^2 - 3)^2$$

Sea $u = x^2$, con la restricción $u \ge 0$. Podemos reescribir $D^2$ en función de $u$:

$$D^2(u) = u + \frac{1}{2}(u^2 - 6u + 9) = \frac{1}{2}u^2 - 2u + \frac{9}{2}$$

Completando el cuadrado para encontrar el mínimo de esta función cuadrática:

$$D^2(u) = \frac{1}{2}(u^2 - 4u + 4) - 2 + \frac{9}{2} = \frac{1}{2}(u - 2)^2 + \frac{5}{2}$$

El valor mínimo se alcanza cuando $u = 2$ (lo cual es válido ya que $u = x^2 = 2 \ge 0$). En este punto, el cuadrado de la distancia mínima es:

$$D^2_{\text{mín}} = \frac{5}{2}$$

Tomando la raíz cuadrada para obtener la distancia mínima $D$:

$$D = \sqrt{\frac{5}{2}} = \frac{\sqrt{10}}{2}$$

Esta expresión tiene la forma $\frac{\sqrt{a}}{b}$ con $a = 10$ y $b = 2$, donde $10$ es libre de cuadrados. Por lo tanto, la suma $a + b$ es:

$$a + b = 10 + 2 = 12$$

\boxed{12}