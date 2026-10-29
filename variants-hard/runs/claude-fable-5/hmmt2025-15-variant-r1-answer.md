**Planteamiento.** El museo es el grafo cuadriculado de $9\times 13$: tiene $117$ habitaciones y las puertas son las aristas. Contemos las aristas: horizontales $9\cdot 12=108$, verticales $13\cdot 8=104$, en total $212$. Un paseo cerrado que no repite puertas es un circuito (trail cerrado), y las aristas que usa forman un subgrafo conexo donde **todo vértice tiene grado par**. Queremos el subgrafo par conexo con el máximo número de aristas, es decir, $212$ menos el mínimo número de aristas que hay que borrar para que todos los grados queden pares.

**Vértices impares.** Los grados en la cuadrícula son: esquinas $2$ (par), borde no esquina $3$ (impar), interior $4$ (par). Los vértices de grado impar son los del borde sin las esquinas: en los lados largos hay $11$ cada uno y en los cortos $7$ cada uno, en total $36$ vértices impares.

**Cota inferior para las aristas borradas.** El conjunto borrado debe ser un $T$-join para esos $36$ vértices, y su tamaño mínimo es igual al mínimo de un emparejamiento perfecto de los $36$ vértices usando distancias de camino más corto. Dos vértices impares solo son adyacentes si están consecutivos en el mismo lado (las esquinas, de grado par, separan los lados). Como cada lado tiene una cantidad **impar** de vértices impares ($11,11,7,7$), a lo más se pueden formar $5+5+3+3=16$ parejas a distancia $1$; las $2$ parejas restantes cruzan de un lado a otro y su distancia mínima es $2$ (pasando por una esquina). Por lo tanto hay que borrar al menos
$$16\cdot 1 + 2\cdot 2 = 20 \text{ aristas}.$$

**Construcción con exactamente 20 borradas.** Con filas $1..9$ y columnas $1..13$:
- Arriba: borrar $(1,2)\text{–}(1,3),\,(1,4)\text{–}(1,5),\,(1,6)\text{–}(1,7),\,(1,8)\text{–}(1,9),\,(1,10)\text{–}(1,11)$, quedando $(1,12)$ sin pareja.
- Abajo: borrar $(9,3)\text{–}(9,4),\dots,(9,11)\text{–}(9,12)$, quedando $(9,2)$ sin pareja.
- Izquierda: borrar $(2,1)\text{–}(3,1),\,(4,1)\text{–}(5,1),\,(6,1)\text{–}(7,1)$, quedando $(8,1)$.
- Derecha: borrar $(3,13)\text{–}(4,13),\,(5,13)\text{–}(6,13),\,(7,13)\text{–}(8,13)$, quedando $(2,13)$.
- Emparejar $(1,12)$ con $(2,13)$ por la esquina: borrar $(1,12)\text{–}(1,13)$ y $(1,13)\text{–}(2,13)$; y $(8,1)$ con $(9,2)$ por la esquina: borrar $(8,1)\text{–}(9,1)$ y $(9,1)\text{–}(9,2)$.

Cada vértice impar pierde exactamente una arista (queda par) y las esquinas $(1,13)$ y $(9,1)$ pierden sus dos aristas (grado $0$, se omiten del paseo). El grafo restante es conexo (todo el interior está intacto y cada vértice no aislado se conecta a él) y todos sus grados son pares, así que admite un circuito euleriano que usa sus $212-20=192$ aristas.

**Respuesta.**

$$\boxed{192}$$