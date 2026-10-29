## Planteamiento

El grafo tiene $9\times 13=117$ vértices (habitaciones) y las aristas son las puertas:

$$9\cdot 12 + 13\cdot 8 = 108+104 = 212 \text{ puertas.}$$

Un paseo cerrado sin repetir aristas es un **circuito euleriano** del subgrafo formado por las puertas usadas. Por tanto hay que hallar el subgrafo con más aristas tal que:

- todos los grados sean **pares**,
- las aristas formen una sola componente **conexa**.

## Vértices de grado impar

- Esquinas: grado 2 (par).
- Borde no esquina: grado 3 (impar).
- Interior: grado 4 (par).

Vértices impares: $2\cdot 11 + 2\cdot 7 = 36$ (11 en cada lado largo, 7 en cada lado corto).

## Cota inferior del número de puertas a descartar

El conjunto de aristas eliminadas debe ser un *T-join* con $T$ = esos 36 vértices, es decir, un emparejamiento de los 36 vértices por caminos disjuntos: 18 parejas.

En cada lado, el número de vértices impares es impar (11, 11, 7, 7), así que en cada lado una cantidad **impar** de ellos debe emparejarse con un vértice de otro lado: al menos 1 por lado, luego hay al menos $4/2 = 2$ parejas "entre lados".

Dos vértices impares de lados distintos nunca son adyacentes (p. ej. $(1,2)$ y $(2,1)$ están a distancia 2), así que cada pareja cruzada cuesta $\ge 2$. Con $c\ge 2$ parejas cruzadas:

$$\text{aristas eliminadas} \ \ge\ (18-c)\cdot 1 + 2c = 18 + c \ \ge\ 20.$$

## Construcción con exactamente 20

Con filas $i=1..9$ y columnas $j=1..13$, eliminamos:

- Fila superior: $(1,3)(1,4),\,(1,5)(1,6),\,(1,7)(1,8),\,(1,9)(1,10),\,(1,11)(1,12)$ — 5 aristas.
- Fila inferior: $(9,2)(9,3),\,(9,4)(9,5),\,(9,6)(9,7),\,(9,8)(9,9),\,(9,10)(9,11)$ — 5.
- Columna izquierda: $(3,1)(4,1),\,(5,1)(6,1),\,(7,1)(8,1)$ — 3.
- Columna derecha: $(2,13)(3,13),\,(4,13)(5,13),\,(6,13)(7,13)$ — 3.
- Cruces por esquinas: $(1,2)(1,1),(1,1)(2,1)$ y $(9,12)(9,13),(9,13)(8,13)$ — 4.

Total: 20. Todos los grados quedan pares (las esquinas $(1,1)$ y $(9,13)$ quedan aisladas, grado 0, par). El interior permanece intacto y cada vértice del borde conserva su arista hacia dentro, luego todas las aristas restantes forman una componente conexa con grados pares: admite circuito euleriano.

$$212-20=192$$

\boxed{192}