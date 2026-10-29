## Planteamiento

Expandimos:

$$z = (2x-y)^2 - 2y^2 - 3y = 4x^2 - 4xy + y^2 - 2y^2 - 3y = 4x^2 - 4xy - y^2 - 3y.$$

## Jugada de Brahmagupta

Para $x$ fijo, vista como función de $y$:

$$z = -y^2 - (4x+3)y + 4x^2,$$

una parábola con coeficiente principal negativo, así que su máximo está en el vértice:

$$y = -\frac{4x+3}{2}.$$

Sustituyendo, el valor máximo es:

$$z_{\max}(x) = 4x^2 + \frac{(4x+3)^2}{4}.$$

## Jugada de Archimedes

Minimizamos $z_{\max}(x)$:

$$\frac{d}{dx}\left[4x^2 + \frac{(4x+3)^2}{4}\right] = 8x + 2(4x+3) = 16x + 6 = 0,$$

de donde $x = -\dfrac{3}{8}$. Como la segunda derivada es $16 > 0$, se trata de un mínimo.

$$\boxed{-\frac{3}{8}}$$