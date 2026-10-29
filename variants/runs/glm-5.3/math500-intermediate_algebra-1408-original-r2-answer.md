## Desarrollo paso a paso

**Paso 1: Identificar el valor.**
Sea $\phi = \frac{1+\sqrt{5}}{2}$ (la proporción áurea). La ecuación es:
$$z + \frac{1}{z} = \phi$$

**Paso 2: Parametrizar $z$.**
Multiplicando por $z$: $z^2 - \phi z + 1 = 0$. El discriminante es $\phi^2 - 4 < 0$, así que las raíces son complejas conjugadas con producto $1$; por lo tanto $|z| = 1$ y podemos escribir $z = e^{i\theta}$. Entonces:
$$z + \frac{1}{z} = 2\cos\theta = \phi \implies \cos\theta = \frac{\phi}{2} = \frac{1+\sqrt{5}}{4}$$

**Paso 3: Reconocer el ángulo.**
Se sabe que $\cos 36° = \frac{1+\sqrt{5}}{4}$, luego $\theta = 36° = \frac{\pi}{5}$ (el caso $\theta = -\frac{\pi}{5}$ da el mismo resultado final por simetría).

**Paso 4: Calcular la potencia pedida.**
$$z^{85} + \frac{1}{z^{85}} = 2\cos(85\theta) = 2\cos\!\left(\frac{85\pi}{5}\right) = 2\cos(17\pi)$$

Como $17\pi \equiv \pi \pmod{2\pi}$:
$$2\cos(17\pi) = 2\cos\pi = -2$$

**Verificación:** $z^5 = e^{i\pi} = -1$, así que $z^{85} = (z^5)^{17} = -1$ y $z^{-85} = -1$; la suma es $-1 + (-1) = -2$. ✓

$$\boxed{-2}$$