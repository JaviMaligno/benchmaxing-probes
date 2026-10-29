## Solución

**Simplificar las desigualdades.** La primera desigualdad:
$$x - yz < y - zx \iff (x-y) + z(x-y) < 0 \iff (x-y)(1+z) < 0.$$

La segunda:
$$y - zx < z - xy \iff (y-z) + x(y-z) < 0 \iff (y-z)(1+x) < 0.$$

Cada desigualdad se cumple en dos casos según los signos de los factores, lo que genera las tres regiones. La región acotada corresponde al caso:
$$x < y,\quad z > -1,\quad y < z,\quad x > -1,$$
es decir $-1 < x < y < z$ (y entonces $z > -1$ se cumple automáticamente).

**Parametrizar en el plano.** Con $z = 87 - x - y$, las condiciones son:
- $x > -1$,
- $y > x$,
- $y < z = 87 - x - y \iff 2y < 87 - x \iff y < \tfrac{87-x}{2}$.

Para que exista $y$, necesitamos $x < \tfrac{87-x}{2}$, es decir $x < 29$. La región proyectada en el plano $(x,y)$ es el triángulo con vértices:
$$(-1,-1),\qquad (-1,44),\qquad (29,29).$$

**Área de la proyección.** La base vertical en $x=-1$ va de $y=-1$ a $y=44$, con longitud $45$; la distancia horizontal al vértice $(29,29)$ es $30$:
$$\text{Área proyectada} = \tfrac{1}{2}\cdot 45 \cdot 30 = 675.$$

**Corregir por la inclinación del plano.** El plano $x+y+z=87$ tiene normal $(1,1,1)/\sqrt{3}$, cuyo ángulo con el eje $z$ satisface $\cos\theta = \tfrac{1}{\sqrt{3}}$. Por lo tanto el área real en el plano es:
$$675 \cdot \sqrt{3} = 675\sqrt{3}.$$

Así $a = 675$, $b = 3$, y $a+b = 678$.

$$\boxed{678}$$