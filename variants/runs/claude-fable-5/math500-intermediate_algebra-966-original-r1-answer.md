Queremos minimizar $x^4 + 4y^2 + 4z^4$ con $xyz = 2$.

**Aplicando AM-GM con una división adecuada de términos:**

Dividimos el término central en dos partes para que el producto genere $(xyz)^4$:

$$x^4 + 4y^2 + 4z^4 = x^4 + 2y^2 + 2y^2 + 4z^4 \ge 4\sqrt[4]{x^4 \cdot 2y^2 \cdot 2y^2 \cdot 4z^4} = 4\sqrt[4]{16\,x^4y^4z^4} = 8xyz = 16.$$

**Verificación de la igualdad:** se necesita $x^4 = 2y^2 = 4z^4$. Tomando $x = \sqrt{2}$, $y = \sqrt{2}$, $z = 1$:
- $xyz = \sqrt{2}\cdot\sqrt{2}\cdot 1 = 2$ ✓
- $x^4 + 4y^2 + 4z^4 = 4 + 8 + 4 = 16$ ✓

Por lo tanto, el valor mínimo es

$$\boxed{16}$$