Queremos minimizar el cuadrado de la distancia desde el origen a un punto $(x, y)$ de la parábola, donde $y = \frac{1}{2}x^2 - 9$.

**Planteamiento:** La distancia al cuadrado es
$$d^2 = x^2 + y^2 = x^2 + \left(\tfrac{1}{2}x^2 - 9\right)^2.$$

**Sustitución:** Sea $u = x^2 \geq 0$. Entonces
$$d^2 = u + \left(\tfrac{u}{2} - 9\right)^2 = u + \tfrac{u^2}{4} - 9u + 81 = \tfrac{u^2}{4} - 8u + 81.$$

**Minimización:** Derivando respecto a $u$:
$$\tfrac{u}{2} - 8 = 0 \implies u = 16,$$
que es válido porque $u = 16 \geq 0$ (es decir, $x = \pm 4$).

**Evaluación:**
$$d^2 = \tfrac{16^2}{4} - 8(16) + 81 = 64 - 128 + 81 = 17.$$

Como $a$ es la distancia mínima, $a^2 = d^2 = 17$.

$$\boxed{17}$$