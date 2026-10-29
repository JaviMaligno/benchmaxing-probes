## Resolución

**Paso 1: Expandir la función.**

$$z = (3x-y)^2 - 3y^2 - 5y = 9x^2 - 6xy + y^2 - 3y^2 - 5y = 9x^2 - 6xy - 2y^2 - 5y.$$

**Paso 2: Jugada óptima de Hypatia (maximizar en $y$ con $x$ fijo).**

Como función de $y$, $z$ es una parábola cóncava (coeficiente $-2$ en $y^2$), así que tiene máximo. Derivando respecto a $y$:

$$\frac{\partial z}{\partial y} = -6x - 4y - 5 = 0 \quad\Longrightarrow\quad y^* = -\frac{6x+5}{4}.$$

**Paso 3: Valor que obtiene Hypatia.**

Sustituyendo $y^*$:

$$z_{\max}(x) = 9x^2 - 2(y^*)^2 - (6x+5)y^* = 9x^2 - \frac{(6x+5)^2}{8} + \frac{(6x+5)^2}{4} = 9x^2 + \frac{(6x+5)^2}{8}.$$

**Paso 4: Euclid minimiza $z_{\max}(x)$.**

Es una parábola convexa en $x$; derivando:

$$\frac{d}{dx}z_{\max} = 18x + \frac{2(6x+5)\cdot 6}{8} = 18x + \frac{3(6x+5)}{2} = 27x + \frac{15}{2} = 0,$$

lo que da $x = -\dfrac{15}{54} = -\dfrac{5}{18}$.

$$\boxed{x = -\dfrac{5}{18}}$$