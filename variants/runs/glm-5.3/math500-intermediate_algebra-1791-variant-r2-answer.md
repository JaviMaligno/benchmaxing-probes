# Resolución paso a paso

**Paso 1: Expandir la función.**

$$z = (3x - y)^2 - 3y^2 - 5y = 9x^2 - 6xy + y^2 - 3y^2 - 5y = 9x^2 - 6xy - 2y^2 - 5y.$$

**Paso 2: Jugada óptima de Hypatia (elige $y$ conociendo $x$, y quiere maximizar).**

Derivamos respecto a $y$:

$$\frac{\partial z}{\partial y} = -6x - 4y - 5 = 0 \implies y^* = -\frac{6x+5}{4}.$$

Como $\frac{\partial^2 z}{\partial y^2} = -4 < 0$, este punto crítico es un máximo.

**Paso 3: Valor del juego tras la jugada de Hypatia.**

Agrupamos los términos en $y$: $z = 9x^2 - 2y^2 - (6x+5)y$. Completando el cuadrado:

$$z = 9x^2 - 2\left(y + \frac{6x+5}{4}\right)^2 + \frac{(6x+5)^2}{8}.$$

Entonces el valor máximo que Hypatia puede asegurar es:

$$z_{\max}(x) = 9x^2 + \frac{(6x+5)^2}{8}.$$

**Paso 4: Jugada óptima de Euclid (minimiza $z_{\max}(x)$).**

$$\frac{dz_{\max}}{dx} = 18x + \frac{6(6x+5)}{8} = 18x + \frac{3(6x+5)}{4} = \frac{90x + 15}{4} = 0 \implies x = -\frac{1}{6}.$$

**Verificación:** Con $x = -\tfrac{1}{6}$, Hypatia elige $y^* = -\tfrac{4}{4} = -1$, y

$$z = \left(3\left(-\tfrac{1}{6}\right) - (-1)\right)^2 - 3(1) + 5 = \left(\tfrac{1}{2}\right)^2 + 2 = \tfrac{9}{4}.$$

$$\boxed{x = -\tfrac{1}{6}}$$