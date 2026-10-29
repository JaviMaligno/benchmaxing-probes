## Planteamiento

**Paso 1: Primer bloque.** El bloque de la izquierda puede llenarse con los números 1–9 en cualquier orden: hay $9! = 362880$ formas.

**Paso 2: Contenidos de los bloques 2 y 3.** Sean $A$, $B$, $C$ los conjuntos de 3 números de las filas 1, 2 y 3 del primer bloque. En el bloque 2, la fila 1 solo puede usar números de $B \cup C$, la fila 2 de $A \cup C$, y la fila 3 de $A \cup B$ (para no repetir en la fila). Si la fila 1 toma $x$ números de $B$, la fila 2 toma $y$ de $A$ y la fila 3 toma $z$ de $A$, las condiciones de que el bloque 2 use los 9 números exactamente una vez fuerzan $y = 3-x$, $z = x$, y los números de $C$ quedan determinados por complemento. El número de elecciones de contenido es:

$$\sum_{x=0}^{3} \binom{3}{x}\binom{3}{3-x}\binom{3}{3-x} = 1 + 27 + 27 + 1 = 56.$$

Una vez fijado el contenido del bloque 2, el contenido de cada fila del bloque 3 queda completamente determinado (son los números restantes de cada fila).

**Paso 3: Ordenamientos internos.** Cada una de las 6 filas-de-bloque (3 filas en el bloque 2 y 3 en el bloque 3) puede permutarse internamente en $3!$ formas: $(3!)^6 = 6^6 = 46656$.

**Total:**
$$9! \cdot 56 \cdot 6^6 = 948{,}109{,}639{,}680.$$

**Paso 4: Factorización.** Con $9! = 2^7 \cdot 3^4 \cdot 5 \cdot 7$, $56 = 2^3 \cdot 7$ y $6^6 = 2^6 \cdot 3^6$:

$$2^{16} \cdot 3^{10} \cdot 5^1 \cdot 7^2.$$

**Paso 5: Cálculo final.**
$$2 \cdot 16 + 3 \cdot 10 + 5 \cdot 1 + 7 \cdot 2 = 32 + 30 + 5 + 14 = 81.$$

$$\boxed{81}$$