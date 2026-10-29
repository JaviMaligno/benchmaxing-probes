Para encontrar el número máximo de casillas que puede visitar el rey cojo (*limping king*), analicemos primero las reglas de su movimiento.

### 1. Cota superior mediante paridad de columnas
Numeremos las filas del tablero del $1$ al $9$ (de arriba a abajo) y las columnas del $1$ al $9$ (de izquierda a derecha). La casilla inicial (arriba a la izquierda) es $(1, 1)$.

Dos casillas comparten al menos un vértice si sus coordenadas de fila y columna difieren a lo sumo en $1$. Como el rey cojo no puede moverse a una casilla en su misma columna, desde una casilla $(r, c)$ solo puede moverse a una casilla $(r', c')$ tal que:
$$|r - r'| \le 1 \quad \text{y} \quad |c - c'| = 1$$

Dado que $|c - c'| = 1$ en cada movimiento, la paridad de la columna cambia en cada paso: el rey debe alternar estrictamente entre columnas impares ($\{1, 3, 5, 7, 9\}$) y columnas pares ($\{2, 4, 6, 8\}$).

En un tablero de $9 \times 9$:
- Hay $5$ columnas impares, con un total de $5 \times 9 = 45$ casillas.
- Hay $4$ columnas pares, con un total de $4 \times 9 = 36$ casillas.

Como el recorrido comienza en la casilla $(1, 1)$ (que está en una columna impar) y alterna entre columnas impares y pares sin repetir casillas, a lo sumo puede visitar las $36$ casillas de las columnas pares y, por tanto, a lo sumo $36 + 1 = 37$ casillas de las columnas impares.

Así, el número máximo de casillas que puede visitar es a lo sumo:
$$36 + 37 = 73$$

### 2. Construcción para alcanzar 73 casillas
Podemos alcanzar exactamente $73$ casillas siguiendo el siguiente recorrido explícito:

1. **Columnas 1 y 2 (de arriba a abajo):**
   $$(1,1) \to (1,2) \to (2,1) \to (2,2) \to (3,1) \to (3,2) \to \dots \to (9,1) \to (9,2)$$
   *(Se visitan las $18$ casillas de las columnas 1 y 2).*

2. **Columnas 3 y 4 (de abajo a arriba):**
   Desde $(9,2)$ pasamos a $(9,3)$ y subimos alternando:
   $$(9,3) \to (9,4) \to (8,3) \to (8,4) \to (7,3) \to (7,4) \to \dots \to (1,3) \to (1,4)$$
   *(Se visitan las $18$ casillas de las columnas 3 y 4).*

3. **Columnas 5 y 6 (de arriba a abajo):**
   Desde $(1,4)$ pasamos a $(1,5)$ y bajamos alternando:
   $$(1,5) \to (1,6) \to (2,5) \to (2,6) \to (3,5) \to (3,6) \to \dots \to (9,5) \to (9,6)$$
   *(Se visitan las $18$ casillas de las columnas 5 y 6).*

4. **Paso por la columna 7 y recorrido de las columnas 8 y 9 (de abajo a arriba):**
   Desde $(9,6)$ pasamos por $(9,7)$ hacia $(9,8)$ y subimos alternando entre las columnas 8 y 9:
   $$(9,7) \to (9,8) \to (9,9) \to (8,8) \to (8,9) \to \dots \to (1,8) \to (1,9)$$
   *(Se visita $1$ casilla de la columna 7 y las $18$ casillas de las columnas 8 y 9).*

En total, el camino visita $18 + 18 + 18 + 1 + 18 = 73$ casillas distintas.

\boxed{73}