Para encontrar cuántos valores posibles de $x$ existen, planteamos las condiciones del problema:

1. Se reparten las $54$ cartas en partes iguales entre $x$ jugadores, recibiendo cada uno $y$ cartas. Por lo tanto:
   $$x \cdot y = 54$$
   donde $x$ e $y$ son números enteros positivos (es decir, $x$ e $y$ son divisores de $54$).

2. Las restricciones dadas son:
   - $x \ge 2$
   - $y \ge 5$ (lo que equivale a $\frac{54}{x} \ge 5 \implies x \le \frac{54}{5} = 10.8$, es decir, $x \le 10$).

3. Buscamos todos los divisores positivos de $54$:
   $$1, 2, 3, 6, 9, 18, 27, 54$$

4. Filtramos los divisores $x$ que cumplen $2 \le x \le 10$:
   - Si $x = 2$, entonces $y = 27$ (cumple $x \ge 2$ e $y \ge 5$).
   - Si $x = 3$, entonces $y = 18$ (cumple $x \ge 2$ e $y \ge 5$).
   - Si $x = 6$, entonces $y = 9$ (cumple $x \ge 2$ e $y \ge 5$).
   - Si $x = 9$, entonces $y = 6$ (cumple $x \ge 2$ e $y \ge 5$).

Los valores posibles para $x$ son $2, 3, 6$ y $9$, lo que nos da un total de $4$ valores posibles.

\boxed{4}