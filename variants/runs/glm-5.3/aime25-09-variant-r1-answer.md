# Solución

**Planteamiento.** Un punto $(X, Y)$ pertenece a la parábola rotada si y solo si su preimagen (rotación de $-60^\circ$) está en la parábola original. La preimagen es:

$$\left(\frac{X + \sqrt{3}\,Y}{2},\ \frac{-\sqrt{3}\,X + Y}{2}\right)$$

de modo que la condición para estar en la imagen es:

$$\frac{-\sqrt{3}\,X + Y}{2} = \left(\frac{X + \sqrt{3}\,Y}{2}\right)^2 - 5$$

El punto de intersección también debe cumplir la ecuación original: $Y = X^2 - 5$.

**Eliminación de $X$.** Sustituyendo $X^2 = Y + 5$ en la condición anterior y multiplicando por 4:

$$-2\sqrt{3}\,X + 2Y = X^2 + 2\sqrt{3}\,XY + 3Y^2 - 20 = 3Y^2 + Y - 15 + 2\sqrt{3}\,XY$$

$$\Rightarrow \quad -2\sqrt{3}\,X(1 + Y) = 3Y^2 - Y - 15$$

Despejando $X$ y usando $X^2 = Y + 5$:

$$\frac{(15 + Y - 3Y^2)^2}{12(1+Y)^2} = Y + 5$$

**Ecuación en $Y$.** Expandiendo:

$$9Y^4 - 18Y^3 - 173Y^2 - 102Y + 165 = 0$$

que factoriza como:

$$(9Y^2 + 9Y - 11)(Y^2 - 3Y - 15) = 0$$

**Selección de la raíz correcta.** Las cuatro raíces dan los cuatro puntos de intersección:

- $Y = \frac{-3 + \sqrt{53}}{6} \approx 0.71$ → $X \approx 2.39$ (primer cuadrante)
- $Y = \frac{-3 - \sqrt{53}}{6} \approx -1.71$ → $X \approx -1.81$ (tercer cuadrante)
- $Y = \frac{3 + \sqrt{69}}{2} \approx 5.65$ → $X \approx -3.27$ (segundo cuadrante)
- $Y = \frac{3 - \sqrt{69}}{2} \approx -2.65$ → $X = \frac{15 + Y - 3Y^2}{2\sqrt{3}(1+Y)} \approx 1.53 > 0$ (cuarto cuadrante) ✓

El único punto en el cuarto cuadrante tiene:

$$Y = \frac{3 - \sqrt{69}}{2}$$

con $a = 3$, $b = 69$, $c = 2$, y $\gcd(3, 2) = 1$.

$$a + b + c = 3 + 69 + 2 = \boxed{74}$$