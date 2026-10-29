Para resolver este problema, analicemos la estructura de las canicas dentro de cada frasco.

Dos canicas son adyacentes si sus etiquetas difieren en $1$. Si consideramos las componentes conexas de canicas dentro de un mismo frasco (es decir, bloques maximales de números consecutivos que están en el mismo frasco), la condición de que cada canica esté acompañada por al menos una canica adyacente significa que ningún bloque puede tener tamaño $1$. 

Como cada frasco contiene exactamente $4$ canicas y cada bloque de canicas consecutivas debe tener tamaño al menos $2$, las canicas de cualquier frasco deben formar:
1. Un único bloque de $4$ canicas consecutivas (por ejemplo, $\{1, 2, 3, 4\}$), o bien
2. Dos bloques separados de $2$ canicas consecutivas cada uno (por ejemplo, $\{1, 2\}$ y $\{5, 6\}$).

En ambos casos, todos los bloques maximales de canicas consecutivas tienen longitud par ($2$ o $4$). 

Si observamos las canicas ordenadas del $1$ al $20$, estas quedan particionadas en bloques consecutivos de longitud par. Como todos los bloques tienen longitud par, el primer bloque debe comenzar en $1$ y terminar en un número par ($2$ o $4$), el siguiente debe comenzar en el siguiente número impar y terminar en un número par, y así sucesivamente. 

Por inducción (o simplemente observando la paridad de los extremos de cada bloque), para cada $m \in \{1, 2, \ldots, 10\}$, las canicas $2m-1$ y $2m$ siempre deben pertenecer al mismo bloque y, por lo tanto, deben ir en el mismo frasco.

Definamos los $10$ pares obligatorios:
$$P_1 = \{1, 2\}, \quad P_2 = \{3, 4\}, \quad \ldots, \quad P_{10} = \{19, 20\}$$

Cualquier agrupación de estos $10$ pares de dos en dos para llenar los $5$ frascos (dando $4$ canicas por frasco) cumple automáticamente la condición del problema, ya que dentro de cada par $P_m$ las dos canicas son adyacentes entre sí.

Por lo tanto, el problema se reduce a encontrar el número de formas de dividir los $10$ pares distintos $P_1, P_2, \ldots, P_{10}$ en $5$ frascos indistinguibles, poniendo exactamente $2$ pares en cada frasco.

El número de maneras de emparejar $10$ elementos distintos en $5$ grupos de tamaño $2$ sin importar el orden de los grupos es:
$$\frac{10!}{(2!)^5 \cdot 5!} = 9 \times 7 \times 5 \times 3 \times 1 = 945$$

\boxed{945}