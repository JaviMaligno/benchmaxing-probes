Para resolver el problema paso a paso, planteamos las condiciones dadas:

1. **Cantidad inicial de monedas:**
   Sea $x$ el número de monedas de oro que hay inicialmente en cada una de las 7 bolsas. El número total de monedas antes de encontrar la nueva bolsa es:
   $$N = 7x$$

2. **Condición de redistribución:**
   Al encontrar una bolsa con 53 monedas, el nuevo total de monedas es $7x + 53$. Como es posible redistribuir todas las monedas en partes iguales entre las 8 bolsas, el nuevo total debe ser divisible por 8:
   $$7x + 53 \equiv 0 \pmod 8$$

3. **Resolución de la congruencia:**
   Sabemos que $7 \equiv -1 \pmod 8$ y que $53 = 6 \times 8 + 5 \equiv 5 \pmod 8$. Sustituyendo en la congruencia:
   $$-x + 5 \equiv 0 \pmod 8 \implies x \equiv 5 \pmod 8$$
   Por lo tanto, $x$ debe ser de la forma $x = 8k + 5$ para algún número entero no negativo $k$.

4. **Condición de tener más de 200 monedas:**
   Evaluamos los posibles valores de $k$:
   - Para $k = 0$: $x = 5 \implies$ tenías $7(5) = 35$ monedas (y $35 + 53 = 88$ en total).
   - Para $k = 1$: $x = 13 \implies$ tenías $7(13) = 91$ monedas (y $91 + 53 = 144$ en total).
   - Para $k = 2$: $x = 21 \implies$ tenías $7(21) = 147$ monedas (y $147 + 53 = 200$ en total, lo cual no es *más* de 200).
   - Para $k = 3$: $x = 29 \implies$ tenías $7(29) = 203$ monedas (y $203 + 53 = 256$ en total).

Con $k = 3$ se cumple por primera vez que el número de monedas es estrictamente mayor que 200 (tanto antes como después de encontrar la bolsa). Por lo tanto, el menor número de monedas que podías tener inicialmente es 203.

\boxed{203}