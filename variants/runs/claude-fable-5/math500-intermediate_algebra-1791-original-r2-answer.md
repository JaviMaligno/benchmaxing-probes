## Solución

**Paso 1: Expandir $z$ como función de $y$.**

$$z = (2x - y)^2 - 2y^2 - 3y = 4x^2 - 4xy + y^2 - 2y^2 - 3y = -y^2 - (4x+3)y + 4x^2.$$

**Paso 2: Jugada óptima de Brahmagupta.**

Como función de $y$, esto es una parábola cóncava (coeficiente $-1$ en $y^2$), así que Brahmagupta maximiza eligiendo el vértice:

$$y^* = -\frac{4x+3}{2}.$$

**Paso 3: Valor resultante de $z$.**

Sea $a = 4x+3$, con $y^* = -a/2$:

$$z = -\frac{a^2}{4} + \frac{a^2}{2} + 4x^2 = \frac{(4x+3)^2}{4} + 4x^2.$$

**Paso 4: Archimedes minimiza sobre $x$.**

$$\frac{dz}{dx} = 2(4x+3) + 8x = 16x + 6 = 0 \quad\Longrightarrow\quad x = -\frac{3}{8}.$$

Como el coeficiente cuadrático es positivo, es un mínimo.

$$\boxed{-\dfrac{3}{8}}$$