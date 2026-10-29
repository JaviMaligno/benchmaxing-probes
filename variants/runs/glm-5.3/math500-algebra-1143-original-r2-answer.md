# Solución paso a paso

**Planteamiento.** La distancia del origen a un punto $(x, y)$ es $d = \sqrt{x^2 + y^2}$, donde $y = \frac{1}{2}x^2 - 9$. Minimizar $d$ equivale a minimizar $d^2$:

$$d^2 = x^2 + \left(\frac{1}{2}x^2 - 9\right)^2$$

**Sustitución.** Sea $t = x^2 \geq 0$. Entonces:

$$d^2 = t + \left(\frac{t}{2} - 9\right)^2 = t + \frac{t^2}{4} - 9t + 81 = \frac{t^2}{4} - 8t + 81$$

**Minimización.** Es una función cuadrática en $t$; derivando:

$$\frac{d(d^2)}{dt} = \frac{t}{2} - 8 = 0 \implies t = 16$$

(Compatible con $t \geq 0$, así que $x = \pm 4$.)

**Valor mínimo.**

$$d^2 = \frac{16^2}{4} - 8(16) + 81 = 64 - 128 + 81 = 17$$

**Verificación.** En $x = 4$: $y = \frac{1}{2}(16) - 9 = -1$, así que $d^2 = 4^2 + (-1)^2 = 17$. ✓ (Comparado con el vértice $(0,-9)$: $d^2 = 81 > 17$.)

Por lo tanto, $a = \sqrt{17}$ y:

$$a^2 = \boxed{17}$$