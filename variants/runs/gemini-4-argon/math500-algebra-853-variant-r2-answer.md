Para encontrar la distancia más pequeña entre el origen $(0,0)$ y un punto $(x,y)$ en la gráfica de $y = \frac{1}{\sqrt{3}}(x^2-5)$, expresamos el cuadrado de la distancia $D$ en función de $x$:

$$D^2 = x^2 + y^2 = x^2 + \frac{1}{3}(x^2-5)^2$$

Sea $u = x^2$, con la restricción $u \ge 0$. Sustituyendo $u$ en la expresión para $D^2$:

$$D^2(u) = u + \frac{1}{3}(u^2 - 10u + 25) = \frac{1}{3}(u^2 - 7u + 25)$$

Completamos el cuadrado para la expresión cuadrática en $u$:

$$D^2(u) = \frac{1}{3}\left[\left(u - \frac{7}{2}\right)^2 - \frac{49}{4} + 25\right] = \frac{1}{3}\left[\left(u - \frac{7}{2}\right)^2 + \frac{51}{4}\right]$$

Dado que $u = \frac{7}{2} \ge 0$ es un valor válido para $x^2$, el valor mínimo de $D^2$ se alcanza cuando $u = \frac{7}{2}$:

$$D_{\min}^2 = \frac{1}{3} \cdot \frac{51}{4} = \frac{17}{4}$$

Tomando la raíz cuadrada para obtener la distancia mínima:

$$D_{\min} = \sqrt{\frac{17}{4}} = \frac{\sqrt{17}}{2}$$

Esta distancia tiene la forma $\frac{\sqrt{a}}{b}$ con $a = 17$ y $b = 2$, donde $17$ es libre de cuadrados. Por lo tanto, la suma $a + b$ es:

$$a + b = 17 + 2 = 19$$

\boxed{19}