## Planteamiento

Un punto $(X,Y)$ está en ambas curvas si está en la parábola original **y** su rotación inversa de $60°$ también lo está.

**Parametrizo** la original: $X=t$, $Y=t^2-5$.

**Rotación inversa** ($-60°$):
$$x=\tfrac{t}{2}+\tfrac{\sqrt3}{2}(t^2-5),\qquad y=-\tfrac{\sqrt3}{2}t+\tfrac{1}{2}(t^2-5)$$

Imponiendo $y=x^2-5$ y multiplicando por 4, con $u=t^2-5$:
$$-2\sqrt3\,t+2u = t^2+2\sqrt3\,tu+3u^2-20$$

Usando $t^2=u+5$ se simplifica a $3u^2-u-15+2\sqrt3\,t(u+1)=0$, es decir:
$$3t^4+2\sqrt3\,t^3-31t^2-8\sqrt3\,t+65=0$$

## Factorización

$$(t^2+\sqrt3\,t-5)(3t^2-\sqrt3\,t-13)=0$$

- Segundo factor: $t=\frac{\sqrt3\pm\sqrt{159}}{6}$ da $t\approx2{,}39$ (con $Y>0$) o $t<0$ → no sirven.
- Primer factor: $t=\frac{-\sqrt3+\sqrt{23}}{2}\approx1{,}532>0$, con $Y\approx-2{,}65<0$ → **cuarto cuadrante**.

De $t^2+\sqrt3\,t-5=0$ se tiene $t^2-5=-\sqrt3\,t$, luego:
$$Y=-\sqrt3\cdot\frac{-\sqrt3+\sqrt{23}}{2}=\frac{3-\sqrt{69}}{2}\approx-2{,}653$$

**Verificación numérica:** $(1{,}532,\,-2{,}653)$ cumple $Y=X^2-5$, y su rotación de $-60°$ da $(-1{,}532,\,-2{,}653)$, que también cumple $y=x^2-5$. ✓

Así $a=3$, $b=69$, $c=2$ (con $\gcd(3,2)=1$), y $a+b+c=74$.

\boxed{74}