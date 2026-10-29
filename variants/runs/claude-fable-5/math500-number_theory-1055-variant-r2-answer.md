Sea $n$ el número de monedas en cada una de las nueve bolsas originales. Al encontrar la bolsa de 47 monedas, el total es $9n + 47$, que debe repartirse en partes iguales entre 10 bolsas, así que:

$$9n + 47 \equiv 0 \pmod{10}$$

Como $9n \equiv -n \pmod{10}$ y $47 \equiv 7 \pmod{10}$, queda $-n + 7 \equiv 0 \pmod{10}$, es decir, $n \equiv 7 \pmod{10}$.

Además, el total supera las 300 monedas: $9n + 47 > 300$, o sea $9n > 253$, lo que da $n \geq 29$. El menor $n \geq 29$ con $n \equiv 7 \pmod{10}$ es $n = 37$.

Verificación: con $n = 37$, el total es $9(37) + 47 = 333 + 47 = 380$, que se reparte en 10 bolsas de 38 monedas cada una, y $380 > 300$. ✓

Antes de encontrar la bolsa, tenía $9 \times 37 = 333$ monedas.

$$\boxed{333}$$