Para resolver este problema paso a paso:

1. **Plantear la ecuación principal:**
   Como se reparten las $54$ cartas en partes iguales entre $x$ jugadores y cada jugador recibe $y$ cartas, el producto del número de jugadores por el número de cartas que recibe cada uno debe ser igual al total de cartas:
   $$x \cdot y = 54$$
   Dado que tanto el número de jugadores como el número de cartas deben ser números enteros positivos, $x$ e $y$ son divisores positivos de $54$.

2. **Encontrar los divisores de $54$:**
   La factorización en números primos de $54$ es $2 \cdot 3^3$. Sus divisores positivos son:
   $$1, 2, 3, 6, 9, 18, 27, 54$$

3. **Aplicar las restricciones para $x$ e $y$:**
   - Sabemos que $x \ge 2$.
   - Sabemos que $y \ge 5$. Como $y = \frac{54}{x}$, esto implica que $\frac{54}{x} \ge 5$, o bien $x \le \frac{54}{5} = 10.8$. Como $x$ es un número entero, debemos tener $x \le 10$.

4. **Identificar los valores válidos de $x$:**
   Buscamos los divisores de $54$ que cumplan con $2 \le x \le 10$:
   - Si $x = 2$, entonces $y = 27$ (cumple $y \ge 5$).
   - Si $x = 3$, entonces $y = 18$ (cumple $y \ge 5$).
   - Si $x = 6$, entonces $y = 9$ (cumple $y \ge 5$).
   - Si $x = 9$, entonces $y = 6$ (cumple $y \ge 5$).

   Por lo tanto, los valores posibles para $x$ son $2, 3, 6$ y $9$, lo que nos da un total de $4$ valores posibles.

\boxed{4}