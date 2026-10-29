## Planteamiento

Un punto $P=(x,y)$ de la parábola original está en la imagen rotada si al rotarlo $-60^\circ$ cae sobre la parábola original. Con

$$x' = \tfrac{x}{2} + \tfrac{\sqrt3}{2}y, \qquad y' = -\tfrac{\sqrt3}{2}x + \tfrac{y}{2},$$

la condición es $y' = x'^2 - 4$, junto con $y = x^2-4$.

## Ecuación resultante

Multiplicando por 4 y sustituyendo $y=x^2-4$:

$$-2\sqrt3\,x + 2y = x^2 + 2\sqrt3\,xy + 3y^2 - 16$$

$$3x^4 + 2\sqrt3\,x^3 - 25x^2 - 6\sqrt3\,x + 40 = 0.$$

Con el cambio $t = \sqrt3\,x$ (y multiplicando por 3) se eliminan los radicales:

$$t^4 + 2t^3 - 25t^2 - 18t + 120 = 0 \;\Longrightarrow\; (t^2 - t - 10)(t^2 + 3t - 12) = 0.$$

## Selección de la raíz

En el cuarto cuadrante hace falta $x\in(0,2)$, es decir $t\in(0,2\sqrt3)\approx(0,3.46)$.

- $t^2-t-10=0$ da $t=\frac{1+\sqrt{41}}{2}\approx 3.70$: queda fuera del rango ($x>2$, luego $y>0$).
- $t^2+3t-12=0$ da $t=\frac{-3+\sqrt{57}}{2}\approx 2.275$, o sea $x\approx 1.3135$: válida.

## Coordenada $y$

De $t^2 = 12 - 3t$ y $y = \frac{t^2}{3}-4$:

$$y = \frac{12 - 3\cdot\frac{-3+\sqrt{57}}{2}}{3} - 4 = \frac{9 - 3\sqrt{57}}{6} = \frac{3-\sqrt{57}}{2} \approx -2.2749.$$

Así $a=3$, $b=57$, $c=2$, con $\gcd(3,2)=1$, y por tanto $a+b+c = 62$.

\boxed{62}