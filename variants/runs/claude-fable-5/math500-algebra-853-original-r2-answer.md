Queremos minimizar la distancia al origen, o equivalentemente su cuadrado:

$$d^2 = x^2 + y^2 = x^2 + \frac{(x^2-3)^2}{2}.$$

Sea $u = x^2 \ge 0$. Entonces

$$f(u) = u + \frac{(u-3)^2}{2}.$$

Derivando: $f'(u) = 1 + (u-3) = u - 2$, que se anula en $u = 2$ (válido, pues $u \ge 0$, y es un mínimo porque $f''(u) = 1 > 0$).

Evaluando:

$$f(2) = 2 + \frac{(2-3)^2}{2} = 2 + \frac{1}{2} = \frac{5}{2}.$$

Por lo tanto, la distancia mínima es

$$d = \sqrt{\tfrac{5}{2}} = \frac{\sqrt{10}}{2},$$

con $a = 10$ (libre de cuadrados) y $b = 2$, así que $a + b = 12$.

$$\boxed{12}$$