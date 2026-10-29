## Planteamiento

Pongo el diámetro $AB$ sobre el eje $x$, con centro de $S_3$ en $O=(0,0)$ y radio $10$; así $A=(-10,0)$, $B=(10,0)$.

**Radio de $S_2$.** Sea $\rho$ el radio de $S_2$, con centro $M$ y diámetro $PQ$ (cuerda del círculo grande). Sea $\alpha$ el ángulo entre $PQ$ y $AB$.

- Como $PQ$ es cuerda, $OM\perp PQ$ y $OM^2 = 100-\rho^2$.
- Como el arco de $S_2$ es tangente a $AB$ en $C$, tenemos $CM\perp AB$ y $CM=\rho$; es decir, la distancia de $M$ a $AB$ es $\rho$.
- Como $OM\perp PQ$, el ángulo entre $OM$ y la vertical es $\alpha$, así que:
$$\rho = OM\cos\alpha \quad\Rightarrow\quad \cos^2\alpha = \frac{\rho^2}{100-\rho^2}. \tag{1}$$

Como $OC\perp CM$, se cumple $OC^2 = OM^2 - CM^2 = 100-2\rho^2$, y por potencia de un punto:
$$AC\cdot CB = (10+OC)(10-OC) = 100-OC^2 = 2\rho^2. \tag{2}$$

**Condición con $S_1$.** Sea $N$ el centro de $S_1$ (radio $1$), con diámetro $UV$ horizontal.

- Al ser $UV$ cuerda de la circunferencia de $S_2$, la perpendicular $MN$ biseca a $UV$; como $UV$ es horizontal, $MN$ es vertical, y con semicuerda $1$:
$$MN^2 = \rho^2 - 1. \tag{3}$$
- El arco de $S_1$ es tangente al diámetro $PQ$, así que la distancia de $N$ a la recta $PQ$ es $1$. La normal a $PQ$ forma ángulo $\alpha$ con la vertical ($MN$), de modo que usando (3):
$$1 = MN\cos\alpha = \sqrt{\rho^2-1}\,\cos\alpha \quad\Rightarrow\quad \cos^2\alpha = \frac{1}{\rho^2-1}. \tag{4}$$

**Resolver.** Igualando (1) y (4):
$$\frac{\rho^2}{100-\rho^2} = \frac{1}{\rho^2-1} \;\Rightarrow\; \rho^2(\rho^2-1) = 100-\rho^2 \;\Rightarrow\; \rho^4 = 100 \;\Rightarrow\; \rho^2 = 10.$$

**Verificación.** Con $\rho^2=10$: $\cos\alpha = \tfrac{\sqrt{10}}{\sqrt{90}}=\tfrac13$, $MN=\sqrt{10-1}=3$, distancia de $N$ a $PQ$: $3\cdot\tfrac13=1$ ✓. Entonces $M=(4\sqrt5,\sqrt{10})$, $C=(4\sqrt5,0)$, $OC^2=80$, y $AC\cdot CB = 100-80 = 20$ ✓ (numéricamente $AC\approx 18.94$, $CB\approx 1.06$).

De (2):
$$AC\cdot CB = 2\rho^2 = 20.$$