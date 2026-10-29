## Planteamiento

Un punto $(x, y)$ está en la intersección de la parábola original y su imagen rotada $60°$ si está en la parábola original **y** su rotación de $-60°$ también cae en la parábola original. La rotación de $-60°$ envía $(x,y)$ a:

$$\left(\frac{x + \sqrt{3}\,y}{2},\ \frac{-\sqrt{3}\,x + y}{2}\right)$$

Entonces necesitamos, junto con $y = x^2 - 4$:

$$\frac{y - \sqrt{3}\,x}{2} = \left(\frac{x + \sqrt{3}\,y}{2}\right)^2 - 4$$

## Desarrollo

Multiplicando por 4:

$$2y - 2\sqrt{3}\,x = x^2 + 2\sqrt{3}\,xy + 3y^2 - 16$$

Sustituyendo $y = x^2 - 4$:

- Lado izquierdo: $2x^2 - 8 - 2\sqrt{3}\,x$
- Lado derecho: $3x^4 + 2\sqrt{3}\,x^3 - 23x^2 - 8\sqrt{3}\,x + 32$

Igualando y simplificando:

$$3x^4 + 2\sqrt{3}\,x^3 - 25x^2 - 6\sqrt{3}\,x + 40 = 0$$

Esto se factoriza como:

$$(3x^2 - \sqrt{3}\,x - 10)(x^2 + \sqrt{3}\,x - 4) = 0$$

(se verifica expandiendo: los coeficientes coinciden término a término).

## Selección de la raíz en el cuarto cuadrante

**Segundo factor:** $x = \dfrac{-\sqrt{3} \pm \sqrt{19}}{2}$. La raíz positiva es $x = \dfrac{\sqrt{19} - \sqrt{3}}{2} \approx 1.313$, con

$$x^2 = \frac{19 + 3 - 2\sqrt{57}}{4} = \frac{11 - \sqrt{57}}{2} \approx 1.73$$

así que $y = x^2 - 4 \approx -2.27 < 0$: cuarto cuadrante ✓.

**Primer factor:** $x = \dfrac{\sqrt{3} \pm \sqrt{123}}{6}$ da puntos en el primer y tercer cuadrante (comprobado numéricamente), así que no sirven.

## Resultado

$$y = \frac{11 - \sqrt{57}}{2} - 4 = \frac{3 - \sqrt{57}}{2}$$

Con $a = 3$, $b = 57$, $c = 2$ (y $\gcd(3,2) = 1$):

$$a + b + c = 3 + 57 + 2 = 62$$

$$\boxed{62}$$