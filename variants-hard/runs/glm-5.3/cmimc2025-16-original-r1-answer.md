## Planteamiento

Enumero las monedas por **filas**. Para cada fila $i$, sea $S_i \subseteq \{1,2,3,4\}$ el conjunto de columnas con moneda.

**Condición dentro de una fila** (sin adyacencia horizontal): $S_i$ no puede contener dos columnas consecutivas. Los patrones válidos son exactamente 8:

$$\emptyset,\quad \{1\},\{2\},\{3\},\{4\},\quad \{1,3\},\{1,4\},\{2,4\}$$

**Condición entre filas consecutivas $i, i+1$:**
- (a) Sin adyacencia vertical: $S_i \cap S_{i+1} = \emptyset$.
- (b) Cada $2\times 2$ con filas $i,i+1$ y columnas $c,c+1$ (para $c=1,2,3$) exige que $S_i \cup S_{i+1}$ interseque a $\{c,c+1\}$.

Como cada cuadrado $2\times 2$ involucra exactamente un par de filas consecutivas, estas condiciones sobre los 3 pares de filas capturan **todo** el problema.

## Grafo de compatibilidad

Una colocación válida equivale a un camino de longitud 3 (4 vértices) en el grafo cuyos vértices son los 8 patrones, con aristas entre pares disjuntos cuya unión cumpla (b). Verificando los 28 pares, quedan **12 aristas**:

$$\emptyset\!-\!\{1,3\},\ \emptyset\!-\!\{2,4\},\ \{1\}\!-\!\{3\},\ \{1\}\!-\!\{2,4\},\ \{2\}\!-\!\{3\},\ \{2\}\!-\!\{4\},\ \{2\}\!-\!\{1,3\},\ \{2\}\!-\!\{1,4\},\ \{3\}\!-\!\{1,4\},\ \{3\}\!-\!\{2,4\},\ \{4\}\!-\!\{1,3\},\ \{1,3\}\!-\!\{2,4\}$$

(por ejemplo, $\{2\}$ y $\{1,4\}$ son compatibles: unión $\{1,2,4\}$ toca $\{1,2\},\{2,3\},\{3,4\}$; en cambio $\{1\}$ y $\{2\}$ fallan porque $\{3,4\}$ queda sin cubrir.)

## Programación dinámica sobre filas

Sea $W_k(P)$ el número de caminos de $k$ filas terminando en el patrón $P$; se obtiene sumando sobre los vecinos del grafo:

| Patrón | $W_1$ | $W_2$ | $W_3$ | $W_4$ |
|---|---|---|---|---|
| $\emptyset$ | 1 | 2 | 8 | 24 |
| $\{1\}$ | 1 | 2 | 8 | 24 |
| $\{2\}$ | 1 | 4 | 12 | 40 |
| $\{3\}$ | 1 | 4 | 12 | 40 |
| $\{4\}$ | 1 | 2 | 8 | 24 |
| $\{1,3\}$ | 1 | 4 | 12 | 40 |
| $\{1,4\}$ | 1 | 2 | 8 | 24 |
| $\{2,4\}$ | 1 | 4 | 12 | 40 |

Por ejemplo, $W_3(\{1,3\}) = W_2(\emptyset)+W_2(\{2\})+W_2(\{4\})+W_2(\{2,4\}) = 2+4+2+4 = 12$, y $W_4(\{2\}) = W_3(\{3\})+W_3(\{4\})+W_3(\{1,3\})+W_3(\{1,4\}) = 40$.

**Verificación cruzada:** el total de la fila 3 es $\sum \deg(P)^2 = 4(2^2) + 4(4^2) = 80$ ✓, y el total de la fila 2 es $2 \times 12 = 24$ (cuenta de colocaciones en una cuadrícula $2\times 4$, verificada a mano) ✓.

Total en la fila 4:

$$4(24) + 4(40) = 96 + 160 = 256$$

Comprobación puntual: la colocación en "diagonal" con filas $\{2\},\{3\},\{2\},\{3\}$ es el camino $\{2\}\!-\!\{3\}\!-\!\{2\}\!-\!\{3\}$, contado correctamente; y el mínimo de 4 monedas (filas $\emptyset,\{2,4\},\emptyset,\{2,4\}$) también aparece como camino $\emptyset\!-\!\{2,4\}\!-\!\emptyset\!-\!\{2,4\}$.

$$\boxed{256}$$