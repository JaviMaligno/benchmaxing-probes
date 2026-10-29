## Planteamiento

Contemos los llenados de la banda de 3×9 (las tres primeras filas de un Sudoku).

**Bloque 1:** se puede llenar libremente con los nueve números: $9! = 362880$ maneras.

**Bloques 2 y 3:** llamemos $R_1, R_2, R_3$ a los conjuntos de tres números que ocupan cada fila dentro del bloque 1. El bloque 2 debe contener los nueve números, repartidos en tres filas de tres, y en cada fila $i$ los números deben ser distintos de los de $R_i$.

Clasifiquemos según cuántos números toma la fila $i$ del bloque 2 de cada $R_j$ con $j \neq i$. Esto equivale a elegir una matriz $3\times 3$ no negativa con sumas de filas y columnas iguales a 3 y diagonal nula. Las soluciones son:

- El "tipo puro": cada fila toma los tres números de un solo $R_j$ (una permutación sin puntos fijos de $\{1,2,3\}$): $2$ maneras.
- Los tipos mixtos: las matrices con entradas $\le 2$ y diagonal nula; hay $54$ de ellas.

En total $2 + 54 = 56$ patrones de distribución. Para cada patrón, los números concretos quedan determinados por el patrón, y solo resta ordenar: en cada una de las $3+3 = 6$ filas de los bloques 2 y 3 hay $3!$ ordenaciones, es decir $6^6$.

Por tanto, dado el bloque 1, el número de completaciones es
$$56 \cdot 6^6 = 56 \cdot 46656 = 2612736.$$

## Total

$$N = 9! \cdot 56 \cdot 6^6 = 362880 \cdot 2612736 = 948109639680.$$

## Factorización

$$9! = 2^7\cdot 3^4\cdot 5\cdot 7,\qquad 56 = 2^3\cdot 7,\qquad 6^6 = 2^6\cdot 3^6$$

$$N = 2^{16}\cdot 3^{10}\cdot 5^{1}\cdot 7^{2}$$

## Resultado

$$2\cdot 16 + 3\cdot 10 + 5\cdot 1 + 7\cdot 2 = 32 + 30 + 5 + 14 = 81$$

\boxed{81}