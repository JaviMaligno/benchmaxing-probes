# Solución paso a paso

**Planteamiento del juego**

Archimedes elige $x$ primero; luego Brahmagupta, conociendo $x$, elige $y$ para **maximizar** $z$. Archimedes debe anticipar esto y elegir $x$ que minimice el valor máximo que Brahmagupta puede lograr (minimax).

**Paso 1: Expresar $z$ como función de $y$, con $x$ fijo**

Expandimos:
$$z = (2x-y)^2 - 2y^2 - 3y = 4x^2 - 4xy + y^2 - 2y^2 - 3y = -y^2 - (4x+3)y + 4x^2.$$

**Paso 2: Jugada óptima de Brahmagupta**

Como función de $y$, es una parábola cóncava (coeficiente de $y^2$ es $-1 < 0$), así que tiene un máximo. Derivamos:
$$\frac{\partial z}{\partial y} = -2y - (4x+3) = 0 \quad\Longrightarrow\quad y^* = -\frac{4x+3}{2}.$$

Sustituyendo, el valor máximo que logra Brahmagupta es:
$$z_{\max}(x) = 4x^2 + \frac{(4x+3)^2}{4}.$$

**Paso 3: Jugada óptima de Archimedes**

Ahora Archimedes minimiza $z_{\max}(x)$ respecto a $x$:
$$\frac{d}{dx}\left[4x^2 + \frac{(4x+3)^2}{4}\right] = 8x + 2(4x+3) = 16x + 6 = 0 \quad\Longrightarrow\quad x = -\frac{3}{8}.$$

(Verificación: $z_{\max}''(x) = 16 > 0$, es un mínimo.)

Con $x = -\tfrac{3}{8}$, Brahmagupta responde con $y^* = -\tfrac{4(-3/8)+3}{2} = -\tfrac{3}{4}$, y el valor del juego es $z = -\tfrac{9}{4}$.

$$\boxed{-\frac{3}{8}}$$