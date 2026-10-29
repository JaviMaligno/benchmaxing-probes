## Planteamiento

Un punto $P=(x,y)$ pertenece a ambas curvas si está en la parábola original ($y=x^2-5$) y además, al rotarlo $-60^\circ$ (rotación inversa), cae también sobre la parábola original.

Rotación de $-60^\circ$:
$$x' = \tfrac{x}{2} + \tfrac{\sqrt3}{2}y, \qquad y' = -\tfrac{\sqrt3}{2}x + \tfrac{y}{2}$$

## Ecuación

Con $y=x^2-5$, imponiendo $y'=x'^2-5$ y multiplicando por 4:

$$-2\sqrt3 x + 2(x^2-5) = x^2 + 2\sqrt3x^3 - 10\sqrt3 x + 3(x^2-5)^2 - 20$$

que se reduce a

$$3x^4 + 2\sqrt3\,x^3 - 31x^2 - 8\sqrt3\,x + 65 = 0$$

## Factorización

Sustituyendo $x=\sqrt3\,s$ se obtiene $27s^4+18s^3-93s^2-24s+65=(3s^2+3s-5)(9s^2-3s-13)$, es decir:

$$(x^2+\sqrt3\,x-5)(3x^2-\sqrt3\,x-13)=0$$

- Segundo factor: raíz positiva $x=\frac{\sqrt3+\sqrt{159}}{6}\approx 2.39$, con $y\approx 0.72>0$ → no es del cuarto cuadrante.
- Primer factor: $x=\frac{-\sqrt3+\sqrt{23}}{2}\approx 1.532>0$, y como $x^2-5=-\sqrt3\,x$:

$$y=-\sqrt3\cdot\frac{-\sqrt3+\sqrt{23}}{2}=\frac{3-\sqrt{69}}{2}\approx -2.653<0$$

Este sí está en el cuarto cuadrante (verificación numérica: al rotar $(1.5319,\,-2.6533)$ por $-60^\circ$ se obtiene $(-1.5319,\,-2.6533)$, que cumple $y'=x'^2-5$).

Así $a=3$, $b=69$, $c=2$ (con $\gcd(3,2)=1$), luego $a+b+c=74$.

\boxed{74}