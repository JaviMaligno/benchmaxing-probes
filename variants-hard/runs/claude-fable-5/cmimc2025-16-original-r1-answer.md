## Planteamiento

Cuento las configuraciones fila por fila (matriz de transferencia). Cada fila del tablero $4\times4$ es una cadena binaria de longitud 4 sin dos 1s adyacentes (condición horizontal). Hay 8 patrones posibles:

$$P_0=0000,\ P_1=0001,\ P_2=0010,\ P_3=0100,\ P_4=1000,\ P_5=0101,\ P_6=1010,\ P_7=1001$$

**Condición entre filas consecutivas $x, y$:**
- Sin adyacencia vertical: $x \wedge y = 0$ (soportes disjuntos).
- Cada cuadrado $2\times2$ con moneda: la unión $u = x \vee y$ no puede tener dos ceros consecutivos (si $u_j = u_{j+1} = 0$, el cuadrado $2\times2$ en las columnas $j, j+1$ quedaría vacío).

## Grafo de transiciones

Verificando cada par ordenado de patrones disjuntos cuya unión no tiene "00":

| Patrón | Vecinos válidos | Grado |
|---|---|---|
| $P_0$ | $P_5, P_6$ | 2 |
| $P_1$ | $P_3, P_6$ | 2 |
| $P_2$ | $P_3, P_4, P_5, P_7$ | 4 |
| $P_3$ | $P_1, P_2, P_6, P_7$ | 4 |
| $P_4$ | $P_2, P_5$ | 2 |
| $P_5$ | $P_0, P_2, P_4, P_6$ | 4 |
| $P_6$ | $P_0, P_1, P_3, P_5$ | 4 |
| $P_7$ | $P_2, P_3$ | 2 |

(La relación es simétrica, como debe ser.)

## Conteo de caminos de 4 filas

Necesito el número de caminos de longitud 3 en este grafo, es decir $\mathbf{1}^T T^3 \mathbf{1}$. Itero el vector:

- $v_1$ (grados): $(2,2,4,4,2,4,4,2)$
- $v_2[x] = \sum_{y \in N(x)} v_1[y]$: $(8,8,12,12,8,12,12,8)$
- $v_3[x] = \sum_{y \in N(x)} v_2[y]$: $(24,24,40,40,24,40,40,24)$

Total: $4 \cdot 24 + 4 \cdot 40 = 96 + 160 = 256$.

$$\boxed{256}$$