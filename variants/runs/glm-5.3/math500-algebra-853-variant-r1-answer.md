Paso a paso:

Minimizamos el cuadrado de la distancia desde el origen a un punto $(x, y)$ de la curva:
$$f(x) = x^2 + y^2 = x^2 + \frac{1}{3}(x^2-5)^2$$

Haciendo $u = x^2$ (con $u \ge 0$):
$$f(u) = u + \frac{(u-5)^2}{3} = \frac{u^2 - 10u + 25 + 3u}{3} = \frac{u^2 - 7u + 25}{3}$$

Derivando respecto a $u$:
$$f'(u) = \frac{2u - 7}{3} = 0 \implies u = \frac{7}{2}$$

Sustituyendo:
$$f\left(\frac{7}{2}\right) = \frac{\frac{49}{4} - \frac{49}{2} + 25}{3} = \frac{\frac{49 - 98 + 100}{4}}{3} = \frac{51/4}{3} = \frac{17}{4}$$

Por lo tanto, la distancia mínima es:
$$d = \sqrt{\frac{17}{4}} = \frac{\sqrt{17}}{2}$$

Con $a = 17$ (libre de cuadrados) y $b = 2$:

$a + b = 19$

\boxed{19}