Para encontrar cuántos valores posibles de $x$ existen, analizamos las condiciones del problema paso a paso:

1. **Relación entre jugadores y cartas:** Se reparten las $48$ cartas en partes iguales entre $x$ jugadores, recibiendo cada uno $y$ cartas. Por lo tanto, el producto de $x$ e $y$ debe ser igual a $48$:
   $$x \cdot y = 48$$
   Dado que el número de jugadores y el número de cartas deben ser números enteros positivos, $x$ e $y$ son divisores positivos de $48$.

2. **Divisores de $48$:** Listamos todos los divisores positivos de $48$:
   $$1, 2, 3, 4, 6, 8, 12, 16, 24, 48$$

3. **Aplicar las restricciones:**
   - Sabemos que $x \ge 3$.
   - También sabemos que $y \ge 4$. Como $y = \frac{48}{x}$, la condición $y \ge 4$ equivale a:
     $$\frac{48}{x} \ge 4 \implies x \le \frac{48}{4} \implies x \le 12$$

4. **Contar los valores válidos de $x$:** Buscamos los divisores de $48$ que cumplan $3 \le x \le 12$. Estos son:
   - $x = 3$ (entonces $y = 16$)
   - $x = 4$ (entonces $y = 12$)
   - $x = 6$ (entonces $y = 8$)
   - $x = 8$ (entonces $y = 6$)
   - $x = 12$ (entonces $y = 4$)

Por lo tanto, hay $5$ valores posibles para $x$.

\boxed{5}