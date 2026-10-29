# Resolución paso a paso

**Paso 1: Expandir la función.**

$$z = (2x-y)^2 - 2y^2 - 3y = 4x^2 - 4xy + y^2 - 2y^2 - 3y = 4x^2 - 4xy - y^2 - 3y$$

**Paso 2: Jugada óptima de Brahmagupta.**

Como Brahmagupta elige después y conoce $x$, para cada $x$ fijo maximiza $z$ respecto a $y$. Con $x$ fijo:

$$\frac{\partial z}{\partial y} = -4x - 2y - 3 = 0 \quad\Longrightarrow\quad y^* = -2x - \tfrac{3}{2}$$

Como $\frac{\partial^2 z}{\partial y^2} = -2 < 0$, efectivamente es un máximo (la parábola en $y$ abre hacia abajo, así que Brahmagupta siempre puede alcanzar este máximo).

**Paso 3: Valor del juego tras la respuesta óptima.**

Sustituyendo $y^*$ (o usando $z_{\max} = c - \frac{b^2}{4a}$ con $a = -1$, $b = -(4x+3)$, $c = 4x^2$):

$$f(x) = z(x, y^*) = 4x^2 + \frac{(4x+3)^2}{4} = 8x^2 + 6x + \frac{9}{4}$$

**Paso 4: Archimedes minimiza $f(x)$.**

$$f'(x) = 16x + 6 = 0 \quad\Longrightarrow\quad x = -\frac{3}{8}$$

y como $f''(x) = 16 > 0$, es un mínimo.

**Verificación:** con $x = -\tfrac{3}{8}$, se tiene $y^* = -\tfrac{3}{4}$, luego $2x - y = -\tfrac{3}{4} + \tfrac{3}{4} = 0$, y

$$z = 0^2 - 2\left(\tfrac{9}{16}\right) + \tfrac{9}{4} = \tfrac{9}{8},$$

que coincide con $f(-\tfrac{3}{8}) = 8\cdot\tfrac{9}{64} - \tfrac{18}{8} + \tfrac{9}{4} = \tfrac{9}{8}$. ✓

$$\boxed{x = -\frac{3}{8}}$$