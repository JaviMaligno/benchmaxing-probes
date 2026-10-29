## Planteamiento

Modelamos la cuadrícula como un grafo: 121 celdas (vértices) y puertas (aristas). El número total de puertas es:

- Horizontales: $11 \times 10 = 110$
- Verticales: $10 \times 11 = 110$
- **Total: $220$ aristas**

Karthik necesita un **circuito cerrado sin repetir aristas** (un circuito euleriano en un subgrafo). Esto equivale a elegir un subgrafo conexo donde **todo vértice usado tenga grado par**. Por tanto, hay que **eliminar el mínimo número de aristas** de forma que:

1. Todos los grados restantes sean pares,
2. El grafo restante siga siendo conexo.

## Análisis de paridades

Grados en el grafo original:
- 4 esquinas: grado $2$ (par)
- 36 celdas del borde que no son esquinas: grado $3$ (**impar**) — son $4 \times 9$
- 81 celdas interiores: grado $4$ (par)

Eliminar una arista cambia la paridad de sus dos extremos. Así, el conjunto $D$ de aristas eliminadas debe tener **grado impar exactamente en las 36 celdas del borde no-esquina** (es un *T-join* con $|T| = 36$), y grado par en los demás vértices.

## Cota inferior

Las 36 celdas de $T$ deben emparejarse por caminos de $D$:
- Dentro de cada lado hay 9 celdas de $T$ (número impar), así que **cada lado debe dejar al menos una celda emparejada con otro lado**.
- Dos celdas de $T$ en lados distintos están a distancia $\geq 2$ (a través de una esquina o del interior).
- Si hay $k$ parejas entre lados distintos, el costo es $\geq (18 - k)\cdot 1 + k \cdot 2 = 18 + k$.
- Como se necesitan al menos $k = 2$ parejas entre lados (cada una cubre 2 lados, y son 4 lados), $|D| \geq 20$.

## Construcción con 20 eliminaciones

- En cada lado, emparejar 8 de las 9 celdas con las 4 aristas del borde entre ellas: $4 \times 4 = 16$ aristas.
- Las 4 celdas restantes (una por lado, adyacentes a esquinas) se emparejan por parejas a través de las esquinas, con 2 aristas cada una: $2 \times 2 = 4$ aristas.

Total: $|D| = 20$. Las dos esquinas usadas quedan aisladas (grado 0, que no se visita, permitido) y el resto del grafo queda conexo con todos los grados pares, por lo que existe un circuito euleriano que recorre todas las puertas restantes.

(Verificación con el caso $3\times 3$: fórmula análoga da $2n-2 = 4$ eliminaciones sobre 12 aristas $\to$ 8, que es exactamente el ciclo perimetral, correcto.)

## Resultado

$$220 - 20 = 200$$

\boxed{200}