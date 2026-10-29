## Planteamiento

Modelamos la cuadrícula como un grafo: 121 vértices (celdas) y las puertas como aristas. El número total de aristas es

$$2\cdot 11\cdot 10 = 220.$$

Un recorrido cerrado sin repetir puertas es un **circuito** (trail cerrado). El subgrafo formado por las puertas usadas debe tener **todos los grados pares**, y ser conexo.

## Cota superior

Coloreamos como tablero de ajedrez con coordenadas $(i,j)$, $1\le i,j\le 11$:

- Color $A$: $i+j$ par → 61 celdas (incluye las 4 esquinas).
- Color $B$: $i+j$ impar → 60 celdas.

Toda puerta une una celda $A$ con una celda $B$, así que el camino alterna colores. Como el recorrido es cerrado, de sus $E$ pasos, exactamente $E/2$ van de $A$ a $B$. Es decir:

$$\#\{\text{visitas a celdas } B\} = \frac{E}{2},$$

donde cada visita a una celda consume 2 puertas, o sea una celda de grado $d$ en el subgrafo se visita $d/2$ veces.

Contamos las celdas $B$ según su grado en la cuadrícula:

- **En el borde** (no hay esquinas en $B$): en la fila 1 son $(1,j)$ con $j$ par → 5 celdas; igual en la fila 11 y en las columnas 1 y 11 → **20 celdas de grado 3**. Como el grado usado debe ser par, es a lo más 2, luego **1 visita** cada una.
- **Interiores**: $60-20 = 40$ celdas de grado 4 → a lo más **2 visitas** cada una.

Por tanto:

$$\frac{E}{2} \le 20\cdot 1 + 40\cdot 2 = 100 \quad\Longrightarrow\quad E \le 200.$$

## La cota se alcanza

Hay que eliminar 20 puertas dejando todos los grados pares (sin tocar celdas $B$ interiores, y conservando las dos puertas de cada esquina). Una elección explícita:

- En la fila 1: quitar $(1,4)$–$(1,3)$, $(1,6)$–$(1,5)$, $(1,8)$–$(1,7)$, $(1,10)$–$(1,9)$; análogamente en la columna 1 con $(4,1)$–$(3,1),\dots,(10,1)$–$(9,1)$, y simétricamente en la fila 11 y la columna 11 (16 puertas en total).
- Cerca de la esquina $(1,1)$: quitar $(1,2)$–$(2,2)$ y $(2,1)$–$(2,2)$; cerca de $(11,11)$: quitar $(11,10)$–$(10,10)$ y $(10,11)$–$(10,10)$ (4 puertas más).

Así cada una de las 36 celdas de grado 3 pierde exactamente 1 puerta (queda en grado 2), las esquinas conservan grado 2, y las celdas $(2,2)$ y $(10,10)$ pierden 2 (quedan en grado 2). Todos los grados son pares y el subgrafo sigue conexo (el interior está intacto), así que posee un circuito euleriano que usa las $220-20 = 200$ puertas restantes.

\boxed{200}