# Resolución paso a paso

**Paso 1: Igualar las ecuaciones.**
Sustituyendo $y = x^2 - 7$ en la segunda ecuación:
$$(x^2-7)^2 = -9x + 45$$
$$x^4 - 14x^2 + 49 + 9x - 45 = 0$$
$$x^4 - 14x^2 + 9x + 4 = 0$$

**Paso 2: Factorizar el polinomio.**
Probando $x=1$: $1 - 14 + 9 + 4 = 0$ ✓, así que $(x-1)$ es factor:
$$x^4 - 14x^2 + 9x + 4 = (x-1)(x^3 + x^2 - 13x - 4)$$
Probando $x = -4$ en el cúbico: $-64 + 16 + 52 - 4 = 0$ ✓:
$$x^3 + x^2 - 13x - 4 = (x+4)(x^2 - 3x - 1)$$

Entonces:
$$(x-1)(x+4)(x^2-3x-1) = 0$$
Las soluciones son: $x = 1$, $x = -4$, $x = \dfrac{3 \pm \sqrt{13}}{2}$.

**Paso 3: Calcular los valores de $y = x^2 - 7$.**
- $x = 1$: $y = 1 - 7 = -6$
- $x = -4$: $y = 16 - 7 = 9$
- $x = \dfrac{3 \pm \sqrt{13}}{2}$: 
$$x^2 = \frac{9 + 13 \pm 6\sqrt{13}}{4} = \frac{11 \pm 3\sqrt{13}}{2}, \qquad y = \frac{11 \pm 3\sqrt{13}}{2} - 7 = \frac{3(-1 \pm \sqrt{13})}{2}$$

**Paso 4: Multiplicar los cuatro valores de $y$.**
$$(-6)(9) \cdot \frac{3(-1+\sqrt{13})}{2} \cdot \frac{3(-1-\sqrt{13})}{2}$$
$$= -54 \cdot \frac{9}{4}\left((-1)^2 - 13\right) = -54 \cdot \frac{9}{4} \cdot (-12) = -54 \cdot (-27) = 1458$$

\boxed{1458}