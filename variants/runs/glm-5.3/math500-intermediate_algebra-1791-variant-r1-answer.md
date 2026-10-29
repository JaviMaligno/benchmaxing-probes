## Planteamiento del juego

Como Euclid elige $x$ primero y Hypatia responde con $y$, debemos resolver por **inducción hacia atrás**: primero encontramos la respuesta óptima de Hypatia para cada $x$ fijo, y luego Euclid minimiza ese valor.

## Paso 1: La jugada óptima de Hypatia

Expandimos la función:
$$z = (3x-y)^2 - 3y^2 - 5y = 9x^2 - 6xy - 2y^2 - 5y.$$

Para $x$ fijo, Hypatia maximiza respecto a $y$. Derivamos:
$$\frac{\partial z}{\partial y} = -6x - 4y - 5 = 0 \quad\Longrightarrow\quad y = -\frac{6x+5}{4}.$$

Como $\dfrac{\partial^2 z}{\partial y^2} = -4 < 0$, este punto crítico es un **máximo**, tal como Hypatia desea.

## Paso 2: El valor del juego como función de $x$

Completando el cuadrado en $y$:
$$z = -2\left(y + \frac{6x+5}{4}\right)^2 + 9x^2 + \frac{(6x+5)^2}{8}.$$

Por tanto, si Hypatia juega óptimamente, el valor resultante es:
$$z_{\max}(x) = 9x^2 + \frac{(6x+5)^2}{8} = \frac{108x^2 + 60x + 25}{8}.$$

*(Verificación con $x=0$: la fórmula da $\tfrac{25}{8}$, y directamente con $y=-\tfrac54$ se obtiene $-2\cdot\tfrac{25}{16}+\tfrac{25}{4}=\tfrac{25}{8}$. ✓)*

## Paso 3: La jugada óptima de Euclid

Euclid minimiza $z_{\max}(x)$:
$$\frac{d}{dx}\left[\frac{108x^2+60x+25}{8}\right] = 27x + \frac{15}{2} = 0 \quad\Longrightarrow\quad x = -\frac{15}{54} = -\frac{5}{18}.$$

Como la segunda derivada es $27 > 0$, se trata de un **mínimo**.

**Comprobación final:** con $x=-\tfrac{5}{18}$, Hypatia responde con $y = -\tfrac{5}{6}$, y el valor del juego es:
$$z = \left(-\frac{5}{6}+\frac{5}{6}\right)^2 - 3\cdot\frac{25}{36} + \frac{25}{6} = \frac{25}{12},$$
que coincide con el mínimo de $z_{\max}(x)$, confirmando la coherencia de la inducción hacia atrás.

Euclid debe elegir

$$\boxed{-\dfrac{5}{18}}$$