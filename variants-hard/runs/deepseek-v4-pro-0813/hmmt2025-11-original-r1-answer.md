Pensemos paso a paso.

Colocamos los números $1,2,3,4,5,6,7$ en un círculo. La condición es que el producto de cada pareja de números adyacentes sea a lo sumo $20$. Rotaciones y reflexiones cuentan como arreglos distintos.

Primero observemos qué vecinos puede tener cada número.

- El número $7$: para que $7\cdot k\le 20$, necesitamos $k\le 20/7\approx 2.857$, así que sus únicos vecinos posibles son $1$ y $2$.
- El número $6$: $6k\le 20$ da $k\le 3.33$, así que sus vecinos posibles son $1,2,3$.
- El número $5$: $5k\le 20$ da $k\le 4$, así que sus vecinos posibles son $1,2,3,4$.
- El número $4$: $4k\le 20$ da $k\le 5$, así que sus vecinos posibles son $1,2,3,4,5$. Pero con $5$ da $20$, que está permitido.
- El número $3$: sus vecinos posibles son $1,2,3,4,5,6$.
- El número $2$: vecinos posibles $1,2,3,4,5,6,7$.
- El número $1$: vecinos posibles $1,2,3,4,5,6,7$.

El número $7$ es muy restrictivo: en el círculo debe estar entre $1$ y $2$. Como reflexiones cuentan como distintas, no nos preocupamos por simetría, pero tratemos el bloque.

El número $7$ tiene exactamente dos vecinos: uno debe ser $1$ y el otro $2$. Así que en el círculo aparece el tramo

\[
1-7-2
\]

o equivalentemente $2-7-1$; ambos son la misma situación salvo orientación.

Ahora el número $6$ también es muy restrictivo: debe tener como vecinos dos números del conjunto $\{1,2,3\}$. Además el $6$ no puede ser adyacente a $7$ porque $6\cdot 7=42>20$.

Consideremos las posiciones restantes. Tenemos el círculo con las posiciones de $1,7,2$ fijadas consecutivas. Llamemos a las posiciones alrededor del círculo en orden:

\[
A, 1, 7, 2, B, C, D
\]

donde $A,B,C,D$ son las posiciones para $3,4,5,6$ (los números restantes, en algún orden). Falta verificar que $C$ y $D$ no son adyacentes; en realidad sí son adyacentes en el círculo porque las posiciones se cierran: el orden circular completo es $A-1-7-2-B-C-D-A$.

Condiciones de adyacencia:

- $A$ es vecino de $1$ y de $D$.
- $B$ es vecino de $2$ y de $C$.
- $C$ es vecino de $B$ y de $D$.
- $D$ es vecino de $C$ y de $A$.

Los números $3,4,5,6$ ocupan $A,B,C,D$.

Veamos las restricciones del $6$: sus dos vecinos deben estar en $\{1,2,3\}$.

- Si $6$ está en $A$, sus vecinos son $1$ (ok) y $D$, luego $D$ debe estar en $\{1,2,3\}$, pero $D$ es uno de $3,4,5$, así que $D=3$.
- Si $6$ está en $B$, sus vecinos son $2$ (ok) y $C$, luego $C$ debe ser $3$.
- Si $6$ está en $C$, sus vecinos son $B$ y $D$, ambos deben estar en $\{1,2,3\}$. Entre $B$ y $D$ solo puede aparecer el $3$ (pues $4$ y $5$ no sirven), y necesitaríamos dos números del conjunto, imposible porque solo hay un $3$. Así que $C$ no puede ser $6$.
- Si $6$ está en $D$, sus vecinos son $C$ y $A$, y de nuevo solo habría un número disponible ($3$) entre $C$ y $A$ que cumpla, insuficiente. Así que $D$ no puede ser $6$.

Por tanto hay dos casos:

### Caso 1: $6$ en $A$, y entonces $D=3$

Posiciones:

\[
6-1-7-2-B-C-3-6
\]

Faltan $4$ y $5$ para $B$ y $C$. Verifiquemos.

- $B$ es vecino de $2$ y $C$.
  - Si $B=4$, $C=5$: $2\cdot 4=8\le 20$ ok; $4\cdot 5=20$ ok; y $C=5$ con $3$: $15\le 20$ ok.
  - Si $B=5$, $C=4$: $2\cdot 5=10$ ok; $5\cdot 4=20$ ok; $4\cdot 3=12$ ok.

También hay que verificar $D=3$ con $A=6$: $3\cdot 6=18\le 20$ ok, y $A=6$ con $1$: $6$ ok.

Ambas asignaciones funcionan. Entonces hay $2$ arreglos en este caso.

### Caso 2: $6$ en $B$, y entonces $C=3$

Posiciones:

\[
A-1-7-2-6-3-D-A
\]

Faltan $4$ y $5$ para $A$ y $D$. Verifiquemos.

- $A$ es vecino de $1$ y $D$.
- $D$ es vecino de $3$ y $A$.

Posibilidades:

- $A=4$, $D=5$: $1\cdot 4=4$ ok; $4\cdot 5=20$ ok; $5\cdot 3=15$ ok. Funciona.
- $A=5$, $D=4$: $1\cdot 5=5$ ok; $5\cdot 4=20$ ok; $4\cdot 3=12$ ok. Funciona.

Entonces hay $2$ arreglos en este caso.

En total $2+2=4$ arreglos circulares con una posición fija para el bloque $1-7-2$.

Ahora, ¿cuántas veces hemos contado cada arreglo si ahora permitimos rotaciones y reflexiones como distintas?

Recordemos que queremos contar arreglos circulares donde rotaciones y reflexiones son distintas. Para pasar de un círculo abstracto a arreglos etiquetados alrededor de un círculo con posiciones fijas, podemos fijar, por ejemplo, la posición del número $7$.

Pero en nuestro razonamiento consideramos el bloque $1-7-2$ en una orientación fija. En un arreglo circular etiquetado con posiciones fijas, el $7$ puede ocupar cualquiera de las $7$ posiciones, y sus dos vecinos $1$ y $2$ pueden estar en dos órdenes distintos ($1$ a la izquierda y $2$ a la derecha, o al revés).

En nuestro bloque fijo pusimos $1$ a la izquierda de $7$ y $2$ a la derecha. Para contar todos los arreglos circulares etiquetados:

- Elegimos la posición de $7$: $7$ opciones.
- Elegimos cuál de sus vecinos es $1$ y cuál es $2$: $2$ opciones.
- Para cada una, el resto se arregla de $4$ maneras según lo anterior.

Por lo tanto el número total es

\[
7 \cdot 2 \cdot 4 = 56.
\]

Comprobemos que no hemos contado dos veces un mismo arreglo. Al fijar la posición de $7$ y el orden relativo de $1$ y $2$, cada arreglo circular con posiciones etiquetadas queda determinado de forma única. En efecto, dado un arreglo alrededor de un círculo con posiciones fijas, el $7$ está en una posición concreta, y al recorrer el círculo en un sentido fijo, $1$ y $2$ aparecen en un orden determinado alrededor del $7$. Por tanto la correspondencia es biunívoca.

Así, el número de arreglos es $56$.

\[
\boxed{56}
\]