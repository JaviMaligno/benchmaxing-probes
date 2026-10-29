## Planteamiento

Modelemos la cuadrícula como columnas $1, 2, 3, \dots$ con dos celdas cada una (arriba y abajo), con Philip empezando en la celda superior de la columna 1. Hay puertas horizontales (entre columnas consecutivas, una por fila) y verticales (dentro de cada columna), cada una abierta con probabilidad $\tfrac12$.

## Paso 1: conexión por la derecha

Sea $q$ la probabilidad de que las dos celdas de la columna $n$ estén conectadas usando solo puertas en las columnas $\ge n$ (incluida la vertical de la columna $n$). Por la infinitud, $q$ no depende de $n$:

$$q = \frac12 + \frac12\cdot\frac14\cdot q \implies \frac78 q = \frac12 \implies q = \frac47.$$

(O la vertical está abierta, o ambas horizontales hacia la columna $n+1$ están abiertas y la conexión ocurre desde la columna $n+1$.)

## Paso 2: cadena de Markov sobre la frontera izquierda

Sea $S_n \subseteq \{T, B\}$ el conjunto de celdas de la columna $n$ alcanzables usando solo las columnas $\le n$. Un argumento de "primer cruce" muestra que $S_{n+1}$ depende solo de $S_n$ y de las tres puertas nuevas. Enumerando los 8 casos de puertas:

- Desde $T$: va a $TB$ con prob. $\tfrac14$, a $T$ con $\tfrac14$, a $\varnothing$ con $\tfrac12$ (simétrico desde $B$).
- Desde $TB$: va a $TB$ con $\tfrac12$, a $T$ con $\tfrac18$, a $B$ con $\tfrac18$, a $\varnothing$ con $\tfrac14$.

Estado inicial: $S_1 = TB$ con prob. $\tfrac12$ (vertical de la columna 1 abierta), $S_1 = T$ con prob. $\tfrac12$.

## Paso 3: celdas alcanzables por columna

- Si $S_n = TB$: ambas celdas alcanzables, aporta $2$.
- Si $S_n = T$ (o $B$): la celda del estado es alcanzable; la otra lo es solo vía la derecha con la vertical de la columna $n$ cerrada: probabilidad $\tfrac14 \cdot q = \tfrac17$. Aporta $1 + \tfrac17 = \tfrac87$.
- Si $S_n = \varnothing$: nada es alcanzable de ahí en adelante, aporta $0$.

## Paso 4: sumar

Con $a_n = P(S_n = TB)$ y $b_n = P(S_n = T) + P(S_n = B)$:

$$a_{n+1} = \tfrac12 a_n + \tfrac14 b_n, \qquad b_{n+1} = \tfrac14 a_n + \tfrac14 b_n, \qquad a_1 = b_1 = \tfrac12.$$

Sumando sobre $n$, con $A = \sum a_n$ y $B = \sum b_n$:

$$A = \tfrac12 + \tfrac12 A + \tfrac14 B, \qquad B = \tfrac12 + \tfrac14 A + \tfrac14 B.$$

Resolviendo: $B = \tfrac23 + \tfrac{A}{3}$, luego $A = \tfrac85$ y $B = \tfrac65$.

El número esperado de celdas alcanzables es:

$$E = 2A + \tfrac87 B = \frac{16}{5} + \frac{48}{35} = \frac{112 + 48}{35} = \frac{160}{35} = \frac{32}{7}.$$

$$\boxed{\dfrac{32}{7}}$$