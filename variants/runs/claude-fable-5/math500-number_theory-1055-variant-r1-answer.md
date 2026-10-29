Planteemos el problema: antes de encontrar la bolsa, tengo 9 bolsas con *n* monedas cada una, es decir, 9*n* monedas.

**Condición de divisibilidad:** al añadir las 47 monedas, el total 9*n* + 47 debe repartirse en partes iguales entre 10 bolsas, así que 9*n* + 47 ≡ 0 (mod 10). Como 9*n* ≡ −*n* (mod 10), queda −*n* + 7 ≡ 0 (mod 10), o sea *n* ≡ 7 (mod 10). Los valores posibles son *n* = 7, 17, 27, 37, 47, …

**Condición de cantidad:** el total debe superar las 300 monedas: 9*n* + 47 > 300, lo que da 9*n* > 253, es decir *n* ≥ 29.

El menor *n* que cumple ambas condiciones es *n* = 37. Comprobación: 9 × 37 = 333 monedas antes; 333 + 47 = 380 monedas en total, que es divisible entre 10 (38 monedas por bolsa) y mayor que 300. ✓

Las monedas que tenía antes de encontrar la bolsa eran 333.

$$\boxed{333}$$