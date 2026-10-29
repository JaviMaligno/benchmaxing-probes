## Planteamiento

El grid de $11\times 11$ tiene $121$ celdas. Las puertas son las aristas del grafo cuadriculado:
- Horizontales: $11 \times 10 = 110$
- Verticales: $10 \times 11 = 110$
- **Total: $220$ puertas.**

Un recorrido cerrado que no repite aristas es un **circuito euleriano** sobre el subgrafo de aristas usadas. Para que exista, cada vértice del subgrafo debe tener **grado par**, y el subgrafo debe ser conexo.

## Vértices de grado impar

En el grid:
- Las 4 esquinas tienen grado $2$ (par).
- Las celdas interiores tienen grado $4$ (par).
- Las celdas del borde que no son esquinas tienen grado $3$ (impar). Hay $9$ por lado, es decir $36$ vértices impares.

Debemos **eliminar** un conjunto de aristas tal que, en el grafo eliminado, los vértices de grado impar sean exactamente esos $36$ (así el grafo restante queda con todos los grados pares). Queremos eliminar lo mínimo posible.

## Cota inferior de aristas eliminadas

El conjunto eliminado se descompone en caminos que emparejan los vértices impares. Una sola arista eliminada arregla dos vértices impares **solo si los conecta directamente**. Dos vértices impares adyacentes deben ser celdas de borde consecutivas del **mismo lado** (las esquinas no son impares y separan los lados).

Cada lado tiene $9$ vértices impares, un número impar: dentro de un lado se pueden emparejar a lo sumo $4$ parejas con $4$ aristas, quedando **1 vértice sobrante por lado** ($4$ sobrantes en total).

Esos $4$ sobrantes deben emparejarse entre sí mediante caminos de longitud $\geq 2$ (no hay aristas entre lados distintos). El camino más corto entre vértices impares de lados distintos pasa por una esquina y tiene longitud $2$. Emparejamos los sobrantes en $2$ parejas, con costo $2$ aristas cada una.

Mínimo de aristas eliminadas:
$$4 \text{ lados} \times 4 \text{ aristas} + 2 \text{ caminos} \times 2 \text{ aristas} = 16 + 4 = 20.$$

## Construcción

Eliminando exactamente esas $20$ aristas (4 parejas adyacentes por lado, más dos caminos de longitud 2 a través de dos esquinas opuestas, eligiendo los sobrantes junto a esas esquinas), el grafo restante tiene todos los grados pares y se verifica que queda conexo, por lo que admite un circuito euleriano con $220 - 20 = 200$ puertas.

## Respuesta

$$\boxed{200}$$