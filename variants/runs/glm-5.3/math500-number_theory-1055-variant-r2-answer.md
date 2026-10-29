**Planteamiento:** Sea $x$ el número de monedas en cada una de las nueve bolsas originales. Antes del hallazgo tienes $9x$ monedas; al encontrar la bolsa de 47, tu total es $9x + 47$.

**Condición de redistribución:** Para repartir todo en partes iguales entre 10 bolsas, $9x + 47$ debe ser divisible entre 10:

$$9x + 47 \equiv 0 \pmod{10} \implies 9x \equiv -47 \equiv 3 \pmod{10}$$

Como $9 \equiv -1 \pmod{10}$, se sigue $x \equiv 7 \pmod{10}$.

**Condición de más de 300 monedas:** $9x + 47 > 300 \implies x > 253/9 \approx 28.1 \implies x \geq 29$.

**Buscar el mínimo:** Los valores posibles de $x$ son $7, 17, 27, 37, \dots$ El menor que cumple $x \geq 29$ es $x = 37$.

**Verificación:** Con $x = 37$: total $= 9(37) + 47 = 380$, divisible entre 10 (38 monedas por bolsa) y mayor que 300. ✓ Con $x = 27$: total $= 290 \le 300$, no cumple. ✓

**Respuesta:** Antes de encontrar la bolsa tenías $9 \times 37 = 333$ monedas.

$\boxed{333}$