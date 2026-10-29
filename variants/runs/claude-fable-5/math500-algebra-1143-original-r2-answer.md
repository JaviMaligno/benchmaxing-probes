Queremos minimizar la distancia al origen de un punto $(x, y)$ con $y = \tfrac12 x^2 - 9$.

El cuadrado de la distancia es:
$$d^2 = x^2 + \left(\tfrac12 x^2 - 9\right)^2$$

Sea $u = x^2 \ge 0$:
$$d^2 = u + \left(\tfrac{u}{2} - 9\right)^2 = u + \tfrac{u^2}{4} - 9u + 81 = \tfrac{u^2}{4} - 8u + 81$$

Derivando respecto a $u$ e igualando a cero: $\tfrac{u}{2} - 8 = 0 \Rightarrow u = 16$ (válido, pues $u \ge 0$).

Sustituyendo:
$$d^2 = \tfrac{256}{4} - 128 + 81 = 64 - 128 + 81 = 17$$

Como $a$ es la distancia mínima, $a^2 = d^2 = 17$.

$$\boxed{17}$$