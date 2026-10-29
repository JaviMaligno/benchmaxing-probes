Para encontrar la distancia más pequeña entre el origen $(0,0)$ y un punto $(x,y)$ en la gráfica de $y = \frac{1}{\sqrt{3}}(x^2 - 5)$, minimizamos el cuadrado de la distancia, $D^2$:

$$D^2 = x^2 + y^2$$

Sustituyendo $y$ en la ecuación de la distancia:

$$D^2 = x^2 + \left(\frac{1}{\sqrt{3}}(x^2 - 5)\right)^2 = x^2 + \frac{1}{3}(x^2 - 5)^2$$

Sea $u = x^2$, con la restricción $u \ge 0$. Expresamos $D^2$ en términos de $u$:

$$D^2(u) = u + \frac{1}{3}(u^2 - 10u + 25) = \frac{1}{3}(u^2 - 7u + 25)$$

Completando el cuadrado para encontrar el mínimo de la función cuadrática:

$$D^2(u) = \frac{1}{3}\left[\left(u - \frac{7}{2}\right)^2 - \frac{49}{4} + 25\right] = \frac{1}{3}\left[\left(u - \frac{7}{2}\right)^2 + \frac{51}{4}\right]$$

El valor mínimo ocurre cuando $u = \frac{7}{2}$. Como $\frac{7}{2} \ge 0$, existen valores reales para $x$ ($x = \pm\sqrt{7/2}$). Evaluando el mínimo de $D^2$:

$$D^2_{\text{mín}} = \frac{1}{3} \cdot \frac{51}{4} = \frac{17}{4}$$

Tomando la raíz cuadrada para obtener la distancia mínima $D$:

$$D = \sqrt{\frac{17}{4}} = \frac{\sqrt{17}}{2}$$

Comparando con la forma $\frac{\sqrt{a}}{b}$, identificamos $a = 17$ (que es libre de cuadrados) y $b = 2$. Por lo tanto, la suma $a + b$ es $17 + 2 = 19$.

\boxed{19}