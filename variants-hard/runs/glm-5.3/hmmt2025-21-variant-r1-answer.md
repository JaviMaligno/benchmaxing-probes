# Resolución paso a paso

## Configurar la línea base

Los puntos están en orden $Q, T, U, R$ sobre una recta. Coloco coordenadas con $Q$ en el origen:
- $T = (11, 0)$ (pues $QT = 11$)
- $U = (11 + 13,\, 0) = (24, 0)$ (pues $TU = 13$)
- $R = (24 + 24,\, 0) = (48, 0)$ (pues $UR = 24$)

Por lo tanto $QR = 11 + 13 + 24 = 48$, que es el lado del triángulo equilátero $\triangle PQR$.

## Ubicar los vértices $P$ y $S$

Como $\triangle PQR$ es equilátero de lado 48, el vértice $P$ está sobre la mediatriz de $QR$:
$$P = \left(24,\ 24\sqrt{3}\right)$$

Como $\triangle STU$ es equilátero de lado 13 (con base $TU$ sobre la recta), y $S$ debe estar dentro de $\triangle PQR$ (es decir, del mismo lado de la recta que $P$):
$$S = \left(11 + 6.5,\ \tfrac{13\sqrt{3}}{2}\right) = \left(17.5,\ 6.5\sqrt{3}\right)$$

*(Verificación de que $S$ está dentro: en $x = 17.5$ el lado $QP$ tiene altura $17.5\sqrt{3}\approx 30.3$, mientras que $S$ tiene altura $\approx 11.3$; está dentro.)*

## Calcular $PS$

$$\Delta x = 24 - 17.5 = 6.5 = \tfrac{13}{2}, \qquad \Delta y = 24\sqrt{3} - 6.5\sqrt{3} = 17.5\sqrt{3} = \tfrac{35\sqrt{3}}{2}$$

Entonces:
$$PS^2 = \left(\frac{13}{2}\right)^2 + \left(\frac{35\sqrt{3}}{2}\right)^2 = \frac{169}{4} + \frac{3 \cdot 1225}{4} = \frac{169 + 3675}{4} = \frac{3844}{4} = 961$$

$$PS = \sqrt{961} = 31$$

$\boxed{31}$