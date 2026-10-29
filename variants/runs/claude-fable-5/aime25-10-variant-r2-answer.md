## Solución

**Paso 1: Llenar el primer bloque.**
El primer bloque de $3\times 2$ contiene los 6 números en 6 celdas: hay $6! = 720$ maneras.

**Paso 2: Estructura de las filas.**
El bloque 1 determina una partición de $\{1,\dots,6\}$ en tres pares $A, B, C$ (los pares de cada fila). Para el bloque 2, la fila $i$ debe usar 2 números que no estén en su par del bloque 1, y el bloque 2 completo debe contener los 6 números. Si el bloque 2 es válido, el bloque 3 queda determinado como complemento y automáticamente contiene los 6 números.

**Paso 3: Contar las elecciones de conjuntos para el bloque 2.**
Sea $x_{ij}$ la cantidad de elementos del par $i$ que van al conjunto de la fila $j$ del bloque 2, con $x_{ii}=0$ y sumas de filas y columnas iguales a 2. Escribiendo las filas como $(0,a,2-a)$, $(c,0,2-c)$, $(2-c, 2-a, 0)$, la condición de columnas fuerza $a+c=2$, dando exactamente 3 matrices:

- $a=0, c=2$: entradas 0 y 2 → cada par va completo a un conjunto: $1$ asignación.
- $a=2, c=0$: igual, $1$ asignación.
- $a=c=1$: todas las entradas fuera de la diagonal valen 1 → cada par se divide, con $2$ opciones por par: $2^3 = 8$ asignaciones.

Total de formas de elegir los pares (como conjuntos) del bloque 2: $1+1+8 = 10$.

**Paso 4: Ordenar dentro de las filas.**
En cada fila, el par del bloque 2 puede ordenarse de $2$ maneras y el del bloque 3 también: $2^3 \cdot 2^3 = 64$.

**Total:**
$$720 \cdot 10 \cdot 64 = 460800 = 2^{11}\cdot 3^2 \cdot 5^2.$$

Entonces $p\cdot a + q\cdot b + r\cdot c = 2\cdot 11 + 3\cdot 2 + 5\cdot 2 = 22 + 6 + 10 = 38$.

$$\boxed{38}$$