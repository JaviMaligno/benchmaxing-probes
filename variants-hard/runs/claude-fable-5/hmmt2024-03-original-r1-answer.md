## Resolución

Sea $N = 100a + 10b + c$ un múltiplo de $x$, y $M = 100b + 10c + a$ su rotación. Observemos que:

$$10N - M = 1000a + 100b + 10c - (100b + 10c + a) = 999a$$

Por lo tanto $M = 10N - 999a$. Si $x \mid N$, entonces $x \mid M$ si y solo si $x \mid 999a$.

La condición del problema exige que $x \mid 999a$ para **todo** múltiplo de tres cifras de $x$, donde $a$ es el dígito inicial de ese múltiplo.

**Punto clave:** como $x \le 99$, el intervalo $[100, 199]$ (de longitud 100 > x) siempre contiene algún múltiplo de $x$. Es decir, siempre existe un múltiplo de tres cifras de $x$ con dígito inicial $a = 1$.

Aplicando la condición a ese múltiplo: $x \mid 999 \cdot 1 = 999$.

Recíprocamente, si $x \mid 999$, entonces $x \mid 999a$ para cualquier $a$, y la condición se cumple siempre.

**Conclusión:** los valores válidos de $x$ son exactamente los divisores de dos cifras de $999 = 3^3 \cdot 37$. Los divisores de 999 son $1, 3, 9, 27, 37, 111, 333, 999$; los de dos cifras son $27$ y $37$.

Verificación rápida: con $x = 27$, por ejemplo $135 \to 351 = 27 \cdot 13$ ✓; con $x = 37$, $148 \to 481 = 37 \cdot 13$ ✓.

$$27 + 37 = 64$$

$$\boxed{64}$$