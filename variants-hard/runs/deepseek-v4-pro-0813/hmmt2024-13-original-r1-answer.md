

Vamos a resolverlo paso a paso.

Tenemos un cubo grande de $3 \times 3 \times 3$, formado por $27$ cubos unitarios. Usamos $2$ cubos rojos y $25$ blancos. Queremos contar las distribuciones en las que las caras rojas visibles en el exterior del cubo grande son exactamente $4$.

Primero clasificamos las posiciones de los cubos unitarios según cuántas de sus caras son visibles desde el exterior.

## Posiciones según caras visibles

En un cubo $3\times 3\times 3$:

- **Esquinas**: $8$ cubos, cada uno tiene $3$ caras visibles.
- **Aristas medias** (centro de una arista, no esquina): hay $12$ aristas, y en cada una hay $1$ cubo en posición intermedia, así que $12$ cubos con $2$ caras visibles.
- **Centros de cara**: hay $6$ caras, cada una tiene un cubo central, así que $6$ cubos con $1$ cara visible.
- **Centro del cubo**: $1$ cubo con $0$ caras visibles.

Verificamos la cuenta: $8+12+6+1=27$. ✓

Cada cubo blanco aporta $0$ caras rojas visibles, obviamente. Cada cubo rojo aporta tantas caras rojas visibles como caras visibles tenga su posición. Por tanto, el número de caras rojas visibles del cubo grande es la suma de las caras visibles de las posiciones ocupadas por los cubos rojos.

Queremos que esa suma sea exactamente $4$.

## Posibles casos

Con $2$ cubos rojos, las combinaciones posibles de posiciones y su contribución son:

- Dos esquinas: $3+3=6$.
- Una esquina y una arista media: $3+2=5$.
- Una esquina y un centro de cara: $3+1=4$. ✓
- Una esquina y el centro oculto: $3+0=3$.
- Dos aristas medias: $2+2=4$. ✓
- Una arista media y un centro de cara: $2+1=3$.
- Una arista media y el centro oculto: $2+0=2$.
- Dos centros de cara: $1+1=2$.
- Un centro de cara y el centro oculto: $1+0=1$.
- Dos centros ocultos: imposible, solo hay $1$ centro oculto.

Los casos que dan exactamente $4$ caras visibles son:

1. Una esquina y un centro de cara.
2. Dos aristas medias.

No hay más casos posibles.

## Conteo de cada caso

Las posiciones de los cubos rojos se eligen sin distinguir los cubos rojos entre sí; cada distribución queda determinada por el conjunto de dos posiciones ocupadas por los rojos.

### Caso 1: una esquina y un centro de cara

- Esquinas disponibles: $8$.
- Centros de cara disponibles: $6$.
- Como son tipos distintos de posición, el número de elecciones es:

$$
8 \cdot 6 = 48.
$$

### Caso 2: dos aristas medias

- Aristas medias disponibles: $12$.
- Hay que elegir $2$ de ellas, sin importar el orden:

$$
\binom{12}{2} = \frac{12 \cdot 11}{2} = 66.
$$

## Total

Los dos casos son disjuntos, así que el número total de distribuciones es:

$$
48 + 66 = 114.
$$

Como las rotaciones y reflexiones se consideran distintas, no dividimos por simetrías.

Por lo tanto, el número buscado es:

$$
\boxed{114}
$$