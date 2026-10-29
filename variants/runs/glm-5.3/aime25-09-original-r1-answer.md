# Solución

**Paso 1: La rotación y su inversa.**

Una rotación de $60^\circ$ antihoraria alrededor del origen es $(x,y) \mapsto \left(\tfrac{x - \sqrt3\,y}{2},\ \tfrac{\sqrt3\,x + y}{2}\right)$. Un punto $(X, Y)$ pertenece a la parábola imagen si y solo si su preimagen (rotación de $-60^\circ$) está en la parábola original $y = x^2 - 4$:

$$\frac{-\sqrt3\,X + Y}{2} = \left(\frac{X + \sqrt3\,Y}{2}\right)^{\!2} - 4 \;\;\Longrightarrow\;\; -2\sqrt3\,X + 2Y = (X + \sqrt3\,Y)^2 - 16.$$

**Paso 2: Ecuación de intersección.**

El punto de intersección también cumple $Y = X^2 - 4$. Sustituyendo y expandiendo:

$$3X^4 + 2\sqrt3\,X^3 - 25X^2 - 6\sqrt3\,X + 40 = 0.$$

**Paso 3: Factorización.**

$$\left(X^2 + \sqrt3\,X - 4\right)\left(3X^2 - \sqrt3\,X - 10\right) = 0.$$

Raíces: $X = \dfrac{-\sqrt3 \pm \sqrt{19}}{2}$ y $X = \dfrac{\sqrt3 \pm \sqrt{123}}{6}$.

**Paso 4: Identificar el punto del cuarto cuadrante.**

Con $Y = X^2 - 4$:
- $X = \frac{\sqrt{19}-\sqrt3}{2} \approx 1.313$, $Y \approx -2.275 < 0$ → **cuarto cuadrante** ✓
- $X \approx -3.045$, $Y \approx 5.27$ (segundo); $X \approx 2.137$, $Y \approx 0.57$ (primero); $X \approx -1.560$, $Y \approx -1.57$ (tercero).

Es el único punto en el cuarto cuadrante (verificación: $Y = -\sqrt3\,X$ y $X^2 + \sqrt3\,X - 4 = 0$ se cumplen exactamente).

**Paso 5: Coordenada $y$.**

$$Y = X^2 - 4 = \frac{( \sqrt{19} - \sqrt3)^2}{4} - 4 = \frac{22 - 2\sqrt{57}}{4} - 4 = \frac{3 - \sqrt{57}}{2}.$$

**Paso 6: Conclusión.**

$a = 3$, $b = 57$, $c = 2$, con $\gcd(3, 2) = 1$:

$$a + b + c = 3 + 57 + 2 = \boxed{62}$$