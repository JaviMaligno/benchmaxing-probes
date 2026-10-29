Para encontrar la distancia más pequeña entre el origen $(0,0)$ y un punto $(x,y)$ en la gráfica de $y=\frac{1}{\sqrt{2}}\left(x^2-3\right)$, minimizamos el cuadrado de la distancia, $D^2 = x^2 + y^2$.

Sustituyendo $y$ en la ecuación de la distancia al cuadrado:
$$D^2 = x^2 + \left(\frac{1}{\sqrt{2}}(x^2 - 3)\right)^2 = x^2 + \frac{1}{2}(x^2 - 3)^2$$

Sea $u = x^2$, donde $u \ge 0$. Expresamos $D^2$ en función de $u$:
$$D^2(u) = u + \frac{1}{2}(u^2 - 6u + 9) = \frac{1}{2}u^2 - 2u + \frac{9}{2}$$

Completando el cuadrado para encontrar el mínimo:
$$D^2(u) = \frac{1}{2}(u^2 - 4u) + \frac{9}{2} = \frac{1}{2}(u - 2)^2 - 2 + \frac{9}{2} = \frac{1}{2}(u - 2)^2 + \frac{5}{2}$$

Dado que $(u - 2)^2 \ge 0$, el valor mínimo se alcanza cuando $u = x^2 = 2$ (lo cual es válido ya que $2 \ge 0$). En este punto, el cuadrado de la distancia mínima es:
$$D_{\text{mín}}^2 = \frac{5}{2}$$

Por lo tanto, la distancia mínima es:
$$D_{\text{mín}} = \sqrt{\frac{5}{2}} = \frac{\sqrt{10}}{2}$$

Comparando con la forma $\frac{\sqrt{a}}{b}$, donde $a$ es libre de cuadrados, obtenemos $a = 10$ y $b = 2$. Finalmente, calculamos $a + b$:
$$a + b = 10 + 2 = 12$$

\boxed{12}