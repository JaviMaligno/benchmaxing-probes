# Planteamiento

Elegimos $x, y$ uniformes en $(0,3)$, así que el espacio muestral es el cuadrado $(0,3)\times(0,3)$, de área $9$.

# Condición de triángulo

Tres longitudes $1, x, y$ forman triángulo si y solo si se cumplen las tres desigualdades:

$$x + y > 1, \qquad 1 + x > y, \qquad 1 + y > x.$$

Las dos últimas equivalen a $|x - y| < 1$ (banda alrededor de la diagonal).

# Área favorable

Parto del cuadrado completo (área $9$) y resto las zonas prohibidas:

**Zona $x + y \le 1$:** triángulo rectángulo de catetos $1$, área $\tfrac12$.

**Zona $x - y \ge 1$:** vértices $(1,0)$ y $(3,2)$; área $= \int_0^2 (2-y)\,dy = 2$.

**Zona $y - x \ge 1$:** simétrica, área $2$.

Estas zonas no se solapan más que en measure cero (si $x+y\le 1$, entonces $|x-y|\le 1$ con igualdad solo en puntos aislados), así que:

$$\text{Área favorable} = 9 - \tfrac12 - 2 - 2 = \tfrac{9}{2}.$$

# Verificación (shoelace)

La región favorable es el pentágono de vértices $(1,0), (3,2), (3,3), (2,3), (0,1)$. La fórmula del cordón da:

$$\frac{1}{2}\left|2 + 3 + 3 + 2 - 1\right| = \frac{9}{2}. \checkmark$$

# Resultado

$$P = \frac{9/2}{9} = \frac{1}{2}$$

\boxed{\dfrac{1}{2}}