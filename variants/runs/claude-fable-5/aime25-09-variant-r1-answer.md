## Planteamiento

Un punto $P$ está en la imagen de la parábola rotada $60°$ en sentido antihorario si y solo si al rotar $P$ por $-60°$ cae sobre la parábola original. La rotación por $-60°$ envía $(x,y)$ a:

$$\left(\frac{x + \sqrt{3}\,y}{2},\ \frac{y - \sqrt{3}\,x}{2}\right)$$

## Ecuación de intersección

Busco $P = (x, y)$ con $y = x^2 - 5$ (en la parábola original) tal que su imagen rotada también satisfaga la ecuación:

$$\frac{y - \sqrt{3}x}{2} = \left(\frac{x + \sqrt{3}y}{2}\right)^2 - 5$$

Multiplicando por 4 y expandiendo:

$$3y^2 + 2\sqrt{3}\,xy + x^2 - 2y + 2\sqrt{3}\,x - 20 = 0$$

Sustituyendo $y = x^2 - 5$:

$$3x^4 + 2\sqrt{3}\,x^3 - 31x^2 - 8\sqrt{3}\,x + 65 = 0$$

## Factorización

Esta cuártica se factoriza como:

$$(x^2 + \sqrt{3}\,x - 5)(3x^2 - \sqrt{3}\,x - 13) = 0$$

(Verificación: el término cúbico da $-\sqrt{3} + 3\sqrt{3} = 2\sqrt{3}$ ✓; el cuadrático da $-13 - 3 - 15 = -31$ ✓; el lineal da $-13\sqrt{3} + 5\sqrt{3} = -8\sqrt{3}$ ✓; el constante da $65$ ✓.)

**Raíces:**
- Del primer factor: $x = \dfrac{-\sqrt{3} \pm \sqrt{23}}{2}$
- Del segundo factor: $x = \dfrac{\sqrt{3} \pm \sqrt{159}}{6}$

## Selección del punto en el cuarto cuadrante

Necesito $x > 0$ y $y = x^2 - 5 < 0$, es decir $0 < x < \sqrt{5} \approx 2.236$.

- $x = \dfrac{-\sqrt{3} + \sqrt{23}}{2} \approx 1.532$: cumple, con $y \approx -2.65 < 0$. ✓ (cuarto cuadrante)
- $x = \dfrac{\sqrt{3} + \sqrt{159}}{6} \approx 2.39 > \sqrt{5}$: da $y > 0$ (primer cuadrante). ✗

## Cálculo de la coordenada $y$

Como $x$ satisface $x^2 + \sqrt{3}\,x - 5 = 0$, tenemos $x^2 = 5 - \sqrt{3}\,x$, de modo que:

$$y = x^2 - 5 = -\sqrt{3}\,x = -\sqrt{3}\cdot\frac{-\sqrt{3} + \sqrt{23}}{2} = \frac{3 - \sqrt{69}}{2}$$

Entonces $a = 3$, $b = 69$, $c = 2$, con $\gcd(3, 2) = 1$, y:

$$a + b + c = 3 + 69 + 2 = \boxed{74}$$