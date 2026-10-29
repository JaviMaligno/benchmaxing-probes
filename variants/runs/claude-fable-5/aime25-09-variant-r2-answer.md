## Solución

**Planteamiento.** Un punto $P=(x,y)$ está en la intersección si pertenece a la parábola original, $y = x^2 - 5$, y a su imagen rotada. Que $P$ esté en la imagen equivale a que al rotarlo $-60^\circ$ caiga sobre la parábola original. Con la rotación de $-60^\circ$:

$$x' = \tfrac{x}{2} + \tfrac{\sqrt3}{2}y, \qquad y' = -\tfrac{\sqrt3}{2}x + \tfrac{y}{2},$$

la condición $y' = x'^2 - 5$ da (multiplicando por 4):

$$-2\sqrt3\,x + 2y = x^2 + 2\sqrt3\,xy + 3y^2 - 20.$$

**Sustitución.** Usando $x^2 = y+5$:

$$3y^2 - y - 15 + 2\sqrt3\,x\,(y+1) = 0 \quad\Longrightarrow\quad x = \frac{15 + y - 3y^2}{2\sqrt3\,(y+1)}.$$

Elevando al cuadrado e igualando con $x^2 = y+5$:

$$(15 + y - 3y^2)^2 = 12(y+1)^2(y+5),$$

que al expandir produce la cuártica

$$9y^4 - 18y^3 - 173y^2 - 102y + 165 = 0.$$

**Factorización.** La cuártica se factoriza exactamente como

$$(y^2 - 3y - 15)(9y^2 + 9y - 11) = 0.$$

- De $9y^2+9y-11=0$: $y = \frac{-9\pm\sqrt{477}}{18}$, es decir $y\approx 0.713$ (primer cuadrante) y $y\approx -1.713$, pero para esta última la relación lineal da $x<0$ (tercer cuadrante), así que se descarta.
- De $y^2 - 3y - 15 = 0$: $y = \frac{3\pm\sqrt{69}}{2}$. La raíz positiva da $x<0$ (segundo cuadrante); la raíz negativa, $y = \frac{3-\sqrt{69}}{2}\approx -2.6533$, da $x = \sqrt{y+5}\approx 1.532 > 0$. ✓

**Verificación.** Con $P \approx (1.5319,\, -2.6533)$: está en la original ($1.5319^2 - 5 = -2.6533$), y al rotarlo $-60^\circ$ se obtiene $(-1.5319, -2.6533)$, que también satisface $y = x^2 - 5$. Es el único punto de intersección en el cuarto cuadrante.

Por lo tanto $y = \dfrac{3-\sqrt{69}}{2}$, con $a=3$, $b=69$, $c=2$ (y $\gcd(3,2)=1$):

$$a+b+c = 3 + 69 + 2 = 74.$$

$$\boxed{74}$$