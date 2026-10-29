## Planteamiento

Un punto $P=(x,y)$ está en la intersección de la parábola original y su imagen rotada si y solo si:
1. $P$ está en la parábola original: $y = x^2 - 4$, y
2. al rotar $P$ por $-60^\circ$ (deshaciendo la rotación), el resultado también cae en la parábola original.

La rotación por $-60^\circ$ envía $(x,y)$ a
$$\left(\tfrac{x}{2} + \tfrac{\sqrt3}{2}y,\; -\tfrac{\sqrt3}{2}x + \tfrac{y}{2}\right).$$

## Ecuación

La condición 2 dice:
$$-\tfrac{\sqrt3}{2}x + \tfrac{y}{2} = \left(\tfrac{x}{2} + \tfrac{\sqrt3}{2}y\right)^2 - 4.$$

Sustituyendo $y = x^2-4$ y multiplicando por 4:
$$2(x^2 - \sqrt3\,x - 4) = \left(x + \sqrt3(x^2-4)\right)^2 - 16.$$

Expandiendo el cuadrado y simplificando:
$$3x^4 + 2\sqrt3\,x^3 - 25x^2 - 6\sqrt3\,x + 40 = 0.$$

## Resolución

Con la sustitución $x = \sqrt3\,t$ los coeficientes se vuelven racionales:
$$27t^4 + 18t^3 - 75t^2 - 18t + 40 = 0,$$
que factoriza como
$$(3t^2 + 3t - 4)(9t^2 - 3t - 10) = 0.$$

**Primer factor:** $t = \dfrac{-3 \pm \sqrt{57}}{6}$. La raíz positiva es $t = \dfrac{-3+\sqrt{57}}{6} \approx 0.758$, que da $x = \sqrt3\,t \approx 1.313 \in (0,2)$, es decir $y = x^2 - 4 < 0$: **cuarto cuadrante** ✓.

**Segundo factor:** $t = \dfrac{3 \pm \sqrt{369}}{18}$; la raíz positiva da $x \approx 2.14 > 2$, con $y > 0$ (primer cuadrante), y la otra es negativa. Ninguna cae en el cuarto cuadrante.

## Coordenada $y$

Del factor $3t^2 + 3t - 4 = 0$ se tiene $3t^2 = 4 - 3t$, así que
$$y = x^2 - 4 = 3t^2 - 4 = -3t = -3\cdot\frac{-3+\sqrt{57}}{6} = \frac{3 - \sqrt{57}}{2}.$$

Entonces $a = 3$, $b = 57$, $c = 2$ (con $\gcd(3,2)=1$), y
$$a + b + c = 3 + 57 + 2 = 62.$$

$$\boxed{62}$$