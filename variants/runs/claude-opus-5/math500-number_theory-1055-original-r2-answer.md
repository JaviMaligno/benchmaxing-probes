## Planteamiento

Sea $n$ el número de monedas en cada una de las siete bolsas originales. Entonces tenía $7n$ monedas, y tras encontrar la bolsa de 53 tengo $7n + 53$.

**Condición de divisibilidad:** el total debe repartirse en 8 bolsas iguales, así que
$$7n + 53 \equiv 0 \pmod 8$$

Como $7 \equiv -1$ y $53 \equiv 5 \pmod 8$:
$$-n + 5 \equiv 0 \pmod 8 \;\Longrightarrow\; n \equiv 5 \pmod 8$$

Es decir, $n \in \{5, 13, 21, 29, \dots\}$

**Condición de cantidad:** el total de monedas supera 200:
$$7n + 53 > 200 \;\Longrightarrow\; 7n > 147 \;\Longrightarrow\; n > 21$$

**Combinando ambas:** el menor valor de $n$ congruente con 5 módulo 8 y mayor que 21 es $n = 29$ (nótese que $n = 21$ daría exactamente 200, y no "más de 200").

**Verificación:** $7 \cdot 29 = 203$ monedas iniciales; $203 + 53 = 256 = 8 \cdot 32$. Las ocho bolsas quedan con 32 monedas cada una, y $256 > 200$. ✓

Por tanto, antes de encontrar la bolsa tenía $203$ monedas.

\boxed{203}