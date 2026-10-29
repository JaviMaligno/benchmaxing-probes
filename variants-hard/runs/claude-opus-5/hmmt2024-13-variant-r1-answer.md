## Clasificación de posiciones

En un cubo $3\times3\times3$, cada cubito pertenece a uno de cuatro tipos según cuántas caras del cubo grande toca:

| Tipo | Cantidad | Caras visibles |
|---|---|---|
| Centro | 1 | 0 |
| Centro de cara | 6 | 1 |
| Arista | 12 | 2 |
| Vértice | 8 | 3 |

Si los dos cubitos azules ocupan posiciones con conjuntos de caras $A$ y $B$, la condición es $|A\cup B| = 3$.

## Casos

**Vértice + centro ($3+0$):** la unión es automáticamente 3.
$8 \cdot 1 = 8$

**Vértice + centro de cara ($3+1$):** la cara debe estar entre las 3 del vértice.
$8 \cdot 3 = 24$

**Vértice + arista ($3+2$):** las 2 caras de la arista deben estar entre las 3 del vértice; hay $\binom{3}{2}=3$ pares, cada uno corresponde a una arista única.
$8 \cdot 3 = 24$

**Arista + arista ($2+2$):** los dos pares de caras deben compartir exactamente una cara. Fijada una arista con caras $\{f,g\}$: las aristas con $f$ y otra cara adyacente distinta de $g$ son 3, e igual con $g$, total 6.
$\dfrac{12\cdot 6}{2} = 36$

**Arista + centro de cara ($2+1$):** la cara del centro no debe estar en el par de la arista: $6-2=4$ opciones.
$12 \cdot 4 = 48$

**Casos descartados:** dos vértices (comparten a lo sumo 2 caras ⇒ unión $\ge 4$), dos aristas disjuntas (unión 4), arista+centro (unión 2), dos centros de cara (unión $\le 2$), centro de cara+centro, etc.

## Total

$$8 + 24 + 24 + 36 + 48 = 140$$

\boxed{140}