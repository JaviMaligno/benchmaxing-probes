Para resolver este problema paso a paso, definamos las variables:

1. **Planteamiento de la ecuación:**
   Sea $x$ el número de monedas de oro en cada una de las 7 bolsas iniciales.
   El número total de monedas que tenías antes de encontrar la nueva bolsa es $7x$.

   Al encontrar una bolsa con 53 monedas, el nuevo total de monedas es $7x + 53$.
   Como puedes redistribuir todas las monedas en partes iguales entre las 8 bolsas, el nuevo total debe ser divisible por 8:
   $$7x + 53 \equiv 0 \pmod{8}$$

2. **Resolución de la congruencia:**
   Reducimos los números módulo 8 (sabiendo que $7 \equiv -1 \pmod{8}$ y $53 = 6 \times 8 + 5 \equiv 5 \pmod{8}$):
   $$-x + 5 \equiv 0 \pmod{8}$$
   $$x \equiv 5 \pmod{8}$$

   Esto significa que $x$ debe ser de la forma:
   $$x = 8k + 5$$
   donde $k$ es un número entero no negativo ($k = 0, 1, 2, 3, \dots$).

3. **Aplicación de la condición de tener más de 200 monedas:**
   Evaluamos el número de monedas para distintos valores de $k$:
   - Para $k = 0$: $x = 5 \implies 7x = 35$ monedas iniciales (total final: $35 + 53 = 88$).
   - Para $k = 1$: $x = 13 \implies 7x = 91$ monedas iniciales (total final: $91 + 53 = 144$).
   - Para $k = 2$: $x = 21 \implies 7x = 147$ monedas iniciales (total final: $147 + 53 = 200$). Como el problema indica que tienes **más de 200** monedas (es decir, estrictamente mayor que 200), este caso no cumple la condición.
   - Para $k = 3$: $x = 29 \implies 7x = 203$ monedas iniciales (total final: $203 + 53 = 256$, es decir, 32 monedas en cada una de las 8 bolsas).

Por lo tanto, el menor número de monedas que podrías haber tenido antes de encontrar la bolsa de 53 monedas es 203.

\boxed{203}