Sea $n$ el número de monedas en cada una de las siete bolsas originales. Antes de encontrar la bolsa tengo $7n$ monedas, y después tengo $7n + 53$.

**Condición de divisibilidad:** las $7n + 53$ monedas deben repartirse en 8 bolsas iguales, así que $7n + 53 \equiv 0 \pmod{8}$. Como $7 \equiv -1$ y $53 \equiv 5 \pmod 8$, esto da $-n + 5 \equiv 0 \pmod 8$, es decir, $n \equiv 5 \pmod 8$.

**Condición de cantidad:** el total supera 200 monedas: $7n + 53 > 200$, o sea $7n > 147$, es decir $n > 21$.

Los valores posibles de $n$ son $5, 13, 21, 29, 37, \dots$; el menor que cumple $n > 21$ es $n = 29$ (nótese que $n = 21$ daría exactamente 200 monedas, que no es "más de 200").

**Verificación:** con $n = 29$, antes tenía $7 \times 29 = 203$ monedas; con la bolsa nueva, $203 + 53 = 256 = 8 \times 32$, que se reparte perfectamente en 8 bolsas de 32 monedas y supera las 200.

$$\boxed{203}$$