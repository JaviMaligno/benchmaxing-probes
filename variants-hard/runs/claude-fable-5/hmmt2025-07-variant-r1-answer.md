## Solución

**Sustitución trigonométrica.** Como $x, y, z > 0$ y $xy + yz + zx = 1$, podemos escribir $x = \tan A$, $y = \tan B$, $z = \tan C$ con $A, B, C \in (0, \pi/2)$ y $A + B + C = \pi/2$ (esa identidad de tangentes es equivalente a $xy+yz+zx=1$).

Entonces $x^2 + 1 = \sec^2 A$, etc., y la condición común $3\sec^2 A = 4\sec^2 B = 5\sec^2 C = k$ da:

$$\cos^2 A = \frac{3}{k}, \quad \cos^2 B = \frac{4}{k}, \quad \cos^2 C = \frac{5}{k}.$$

**Usar la restricción angular.** Como $C = \frac{\pi}{2} - (A+B)$, se cumple $\cos C = \sin(A+B) = \sin A \cos B + \cos A \sin B$. Con $u = 1/k$:

$$\sqrt{5u} = \sqrt{1-3u}\cdot 2\sqrt{u} + \sqrt{3u}\cdot\sqrt{1-4u}.$$

Dividiendo entre $\sqrt{u}$:

$$2\sqrt{1-3u} + \sqrt{3}\sqrt{1-4u} = \sqrt{5}.$$

**Resolver.** Elevando al cuadrado:

$$4(1-3u) + 3(1-4u) + 4\sqrt{3}\sqrt{(1-3u)(1-4u)} = 5 \;\Longrightarrow\; 2\sqrt{3}\sqrt{(1-3u)(1-4u)} = 12u - 1.$$

Elevando al cuadrado otra vez:

$$12(1 - 7u + 12u^2) = 144u^2 - 24u + 1 \;\Longrightarrow\; 12 - 84u = -24u + 1 \;\Longrightarrow\; u = \frac{11}{60},$$

es decir $k = \frac{60}{11}$ (y $12u - 1 > 0$, así que la raíz es válida).

**Recuperar las variables.**

$$x^2 = \frac{k}{3} - 1 = \frac{9}{11}, \quad y^2 = \frac{k}{4} - 1 = \frac{4}{11}, \quad z^2 = \frac{k}{5} - 1 = \frac{1}{11},$$

así que $x = \frac{3}{\sqrt{11}}$, $y = \frac{2}{\sqrt{11}}$, $z = \frac{1}{\sqrt{11}}$.

**Verificación:** $xy + yz + zx = \frac{6 + 2 + 3}{11} = 1$ ✓.

Por lo tanto:

$$x + y + z = \frac{6}{\sqrt{11}} = \frac{6\sqrt{11}}{11}.$$

$$\boxed{\dfrac{6\sqrt{11}}{11}}$$