Sea $x$ el número de monedas de plata que hay inicialmente en cada una de las 9 bolsas.

1. **Cantidad inicial de monedas:**
   Antes de encontrar la nueva bolsa, el número total de monedas es $9x$.

2. **Condición de redistribución:**
   Al sumar las 47 monedas de la décima bolsa, el nuevo total de monedas es $9x + 47$. Como es posible redistribuir todas las monedas en partes iguales entre las 10 bolsas, el total debe ser divisible por 10:
   $$9x + 47 \equiv 0 \pmod{10}$$
   Reduciendo módulo 10 ($9 \equiv -1$ y $47 \equiv 7$):
   $$-x + 7 \equiv 0 \pmod{10} \implies x \equiv 7 \pmod{10}$$
   Por lo tanto, $x$ puede tomar valores de la forma $10k + 7$ (es decir, $7, 17, 27, 37, \dots$).

3. **Condición de tener más de 300 monedas:**
   Probamos los valores posibles de $x$:
   - Si $x = 27$, tenías $9 \times 27 = 243$ monedas inicialmente y $243 + 47 = 290$ monedas en total (menor que 300).
   - Si $x = 37$, tenías $9 \times 37 = 333$ monedas inicialmente y $333 + 47 = 380$ monedas en total (mayor que 300).

Por lo tanto, el menor número de monedas que podías tener antes de encontrar la bolsa de 47 monedas es 333.

\boxed{333}