Para resolver el problema paso a paso:

1. **Definir las variables:**
   Sea $x$ el número de monedas de plata que hay inicialmente en cada una de las 9 bolsas. El número total de monedas antes de encontrar la nueva bolsa es $9x$.

2. **Plantear la condición de divisibilidad:**
   Al encontrar una bolsa con 47 monedas, el número total de monedas pasa a ser $9x + 47$. Como es posible redistribuir todas las monedas en partes iguales entre las 10 bolsas, el total debe ser un múltiplo de 10:
   $$9x + 47 \equiv 0 \pmod{10}$$

3. **Resolver la congruencia:**
   Reducimos los términos módulo 10 (sabiendo que $9 \equiv -1 \pmod{10}$ y $47 \equiv 7 \pmod{10}$):
   $$-x + 7 \equiv 0 \pmod{10}$$
   $$x \equiv 7 \pmod{10}$$
   Por lo tanto, $x$ debe terminar en 7 (es decir, $x \in \{7, 17, 27, 37, \dots\}$).

4. **Aplicar la condición de tener más de 300 monedas:**
   Probamos los valores posibles de $x$:
   - Si $x = 27$: tenías inicialmente $9 \times 27 = 243$ monedas, y después de encontrar la bolsa tendrías $243 + 47 = 290$ monedas (lo cual no supera las 300 monedas).
   - Si $x = 37$: tenías inicialmente $9 \times 37 = 333$ monedas, y después de encontrar la bolsa tienes $333 + 47 = 380$ monedas (que es mayor que 300 y se reparte en 10 bolsas de 38 monedas cada una).

Por lo tanto, el menor número de monedas que podías haber tenido antes de encontrar la bolsa de 47 monedas es 333.

\boxed{333}