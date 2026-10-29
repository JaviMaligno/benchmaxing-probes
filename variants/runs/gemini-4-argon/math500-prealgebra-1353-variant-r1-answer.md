Para encontrar cuántos valores posibles de $x$ existen, analizamos las condiciones del problema paso a paso:

1. **Relación entre jugadores y cartas:** Se reparten las $48$ cartas en partes iguales entre $x$ jugadores, recibiendo cada uno $y$ cartas. Como el número de jugadores y de cartas debe ser entero positivo, se cumple que:
   $$x \cdot y = 48$$
   Esto significa que $x$ debe ser un divisor positivo de $48$.

2. **Restricciones para $x$ e $y$:**
   - Se nos indica que $x \ge 3$.
   - También se nos indica que $y \ge 4$. Como $y = \frac{48}{x}$, tenemos que:
     $$\frac{48}{x} \ge 4 \implies x \le \frac{48}{4} \implies x \le 12$$

3. **Divisores de $48$ dentro del rango:**
   Los divisores positivos de $48$ son: $1, 2, 3, 4, 6, 8, 12, 16, 24, 48$.
   
   Seleccionando aquellos que cumplen $3 \le x \le 12$, obtenemos:
   $$x \in \{3, 4, 6, 8, 12\}$$

Por lo tanto, hay $5$ valores posibles para $x$.

\boxed{5}