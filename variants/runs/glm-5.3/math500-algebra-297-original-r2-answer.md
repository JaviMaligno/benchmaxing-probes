## Resolución paso a paso

**Sistema:**
$$y = x^2 - 8 \qquad y^2 = -5x + 44$$

**Paso 1: Sustituir** $y = x^2 - 8$ en la segunda ecuación:
$$(x^2 - 8)^2 = -5x + 44$$
$$x^4 - 16x^2 + 64 + 5x - 44 = 0$$
$$x^4 - 16x^2 + 5x + 20 = 0$$

**Paso 2: Factorizar el polinomio.** Probando $x = -4$: $256 - 256 - 20 + 20 = 0$ ✓, así que $(x+4)$ es factor:
$$x^4 - 16x^2 + 5x + 20 = (x+4)(x^3 - 4x^2 + 5)$$
Probando $x = -1$ en el cúbico: $-1 - 4 + 5 = 0$ ✓, así que $(x+1)$ es factor:
$$(x+4)(x+1)(x^2 - 5x + 5) = 0$$

**Paso 3: Raíces.**
$$x = -4, \quad x = -1, \quad x = \frac{5 \pm \sqrt{5}}{2}$$

**Paso 4: Calcular $y = x^2 - 8$ para cada raíz.**

| $x$ | $y = x^2 - 8$ | Verificación $y^2 = -5x + 44$ |
|---|---|---|
| $-4$ | $8$ | $64 = 20 + 44$ ✓ |
| $-1$ | $-7$ | $49 = 5 + 44$ ✓ |
| $\frac{5+\sqrt5}{2}$ | $\frac{5\sqrt5 - 1}{2}$ | $\frac{63 - 5\sqrt5}{2} = \frac{63 - 5\sqrt5}{2}$ ✓ |
| $\frac{5-\sqrt5}{2}$ | $\frac{-1 - 5\sqrt5}{2}$ | $\frac{63 + 5\sqrt5}{2} = \frac{63 + 5\sqrt5}{2}$ ✓ |

Las cuatro soluciones son distintas.

**Paso 5: Producto de las coordenadas $y$:**
$$8 \cdot (-7) \cdot \frac{5\sqrt5 - 1}{2} \cdot \left(-\frac{5\sqrt5 + 1}{2}\right)$$

Los dos últimos factores forman una diferencia de cuadrados:
$$\frac{5\sqrt5 - 1}{2} \cdot \left(-\frac{5\sqrt5 + 1}{2}\right) = -\frac{(5\sqrt5)^2 - 1^2}{4} = -\frac{125 - 1}{4} = -31$$

Entonces:
$$(-56) \cdot (-31) = 1736$$

$$\boxed{1736}$$