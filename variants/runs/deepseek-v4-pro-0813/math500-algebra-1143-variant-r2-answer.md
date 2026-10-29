Para encontrar la menor distancia desde el origen hasta la parábola, minimizamos $d^2 = x^2 + y^2$ sujeto a $y = \frac14 x^2 - 6$.

Sustituyendo:

$$d^2 = x^2 + \left(\frac14 x^2 - 6\right)^2 = x^2 + \frac{1}{16}x^4 - 3x^2 + 36 = \frac{1}{16}x^4 - 2x^2 + 36.$$

Sea $f(x) = \frac{1}{16}x^4 - 2x^2 + 36$. Derivamos:

$$f'(x) = \frac14 x^3 - 4x = x\left(\frac14 x^2 - 4\right).$$

Igualamos a cero:

$$x\left(\frac14 x^2 - 4\right) = 0 \implies x = 0 \quad\text{ó}\quad x^2 = 16 \implies x = \pm 4.$$

Evaluamos:
- $x=0$: $f(0) = 36$.
- $x=\pm 4$: $f(4) = \frac{1}{16}\cdot 256 - 2\cdot 16 + 36 = 16 - 32 + 36 = 20$.

El mínimo es $b^2 = 20$.

Verifico numéricamente.

```python
import numpy as np
xs = np.linspace(-10, 10, 1000001)
ys = 0.25*xs**2 - 6
d2 = xs**2 + ys**2
print(d2.min())
```

```text
20.000009728491505
```

\boxed{20}