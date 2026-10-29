## Planteamiento

**Fila 1:** se puede llenar de $9!$ maneras. Sea $A$, $B$, $C$ los conjuntos de 3 números que quedan en los bloques 1, 2 y 3 de la primera fila.

**Filas 2 y 3:** en el bloque 1 deben aparecer los 6 números de $B\cup C$, en el bloque 2 los de $A\cup C$, y en el bloque 3 los de $A\cup B$.

Sea la terna de la fila 2 en el bloque 1 con $i$ elementos de $B$ (y $3-i$ de $C$), en el bloque 2 con $j$ de $C$ (y $3-j$ de $A$), y en el bloque 3 con $k$ de $A$ (y $3-k$ de $B$). Como la fila 2 es una permutación de $1..9$:

- de $A$: $(3-j)+k=3$
- de $B$: $i+(3-k)=3$
- de $C$: $(3-i)+j=3$

De donde $i=j=k$.

Fijado $i$, hay que partir cada uno de $A$, $B$, $C$ en dos partes de tamaños $i$ y $3-i$ repartidas entre dos bloques: $\binom{3}{i}$ formas para cada conjunto. Luego

$$\sum_{i=0}^{3}\binom{3}{i}^{3}=1+27+27+1=56.$$

La fila 3 queda forzada como complemento en cada bloque (y se verifica automáticamente que es una permutación). Finalmente, en cada bloque las 3 entradas de la fila 2 y las 3 de la fila 3 se pueden ordenar libremente: $3!\cdot 3!=36$ por bloque, es decir $36^3=6^6$.

## Conteo

$$9!\cdot 56\cdot 6^6 = (2^7\cdot3^4\cdot5\cdot7)(2^3\cdot7)(2^6\cdot3^6)=2^{16}\cdot3^{10}\cdot5^1\cdot7^2$$

Por lo tanto

$$2\cdot16+3\cdot10+5\cdot1+7\cdot2=32+30+5+14=81.$$

$\boxed{81}$