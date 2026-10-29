## Planteamiento

Coloco $A$ en el origen, con $B = (c, 0)$ y $C = (0, b)$, de modo que $b^2 + c^2 = 38^2 = 1444$.

**Ubicación de K y L.** Como $AK = BK = 14$, el triángulo $ABK$ es isósceles; en él, $\cos(\angle KAB) = \frac{c/2}{14} = \frac{c}{28}$. Análogamente, $\cos(\angle LAC) = \frac{b}{28}$. Como $AK = AL = KL = 14$, el triángulo $AKL$ es equilátero, así que $\angle KAL = 60^\circ$.

Los tres ángulos en $A$ suman $90^\circ$:
$$\underbrace{\arccos\tfrac{c}{28}}_{u} + 60^\circ + \underbrace{\arccos\tfrac{b}{28}}_{v} = 90^\circ \implies u + v = 30^\circ.$$

**Usando la hipotenusa.** Con $c = 28\cos u$, $b = 28\cos v$:
$$784(\cos^2 u + \cos^2 v) = 1444 \implies \cos^2 u + \cos^2 v = \frac{361}{196}.$$

Como $\cos^2 u + \cos^2 v = 1 + \cos(u+v)\cos(u-v) = 1 + \frac{\sqrt{3}}{2}\cos(u-v)$:
$$\cos(u-v) = \frac{2}{\sqrt{3}}\cdot\frac{165}{196} = \frac{55\sqrt{3}}{98}.$$

## Cálculo de áreas

**Área de $\triangle ABC$:**
$$bc = 784\cos u\cos v = 392\big(\cos(u+v) + \cos(u-v)\big) = 392\left(\frac{\sqrt{3}}{2} + \frac{55\sqrt{3}}{98}\right) = 392\sqrt{3}\cdot\frac{104}{98} = 416\sqrt{3},$$
así que $[ABC] = 208\sqrt{3}$.

**Áreas a restar:**
- $[ABK] = \frac{1}{2}\cdot 14 \cdot 28\cos u \cdot \sin u = 98\sin 2u$, y análogamente $[ACL] = 98\sin 2v$. Entonces:
$$[ABK] + [ACL] = 98\cdot 2\sin(u+v)\cos(u-v) = 196\cdot\frac{1}{2}\cdot\frac{55\sqrt{3}}{98} = 55\sqrt{3}.$$
- $[AKL] = \frac{\sqrt{3}}{4}\cdot 14^2 = 49\sqrt{3}$ (equilátero).

**Área del cuadrilátero:**
$$[BKLC] = 208\sqrt{3} - 55\sqrt{3} - 49\sqrt{3} = 104\sqrt{3}.$$

$$\boxed{104}$$