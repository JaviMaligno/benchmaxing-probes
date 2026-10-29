Para determinar el número máximo de casillas que el rey cojo puede visitar en un tablero de $7 \times 7$, analicemos primero las restricciones de su movimiento.

### 1. Cota superior mediante coloración por columnas
Numeremos las filas del $1$ al $7$ de arriba a abajo y las columnas del $1$ al $7$ de izquierda a derecha. Una casilla se representa por sus coordenadas $(r, c)$.

Un rey normal puede moverse de $(r, c)$ a $(r', c')$ si $|r - r'| \le 1$ y $|c - c'| \le 1$ (sin quedarse en la misma casilla). Como el rey cojo no puede moverse a ninguna casilla en su misma columna, se tiene la condición adicional $c' \neq c$. Por lo tanto, en cada movimiento válido se cumple:
$$|r - r'| \le 1 \quad \text{y} \quad |c - c'| = 1$$

Esto significa que en cada paso el número de columna $c$ cambia en $+1$ o $-1$, por lo que **la paridad de la columna cambia en cada movimiento** (de columna impar a par, y de par a impar).

En un tablero de $7 \times 7$:
- Hay $4$ columnas impares ($c \in \{1, 3, 5, 7\}$), que contienen $4 \times 7 = 28$ casillas en total.
- Hay $3$ columnas pares ($c \in \{2, 4, 6\}$), que contienen $3 \times 7 = 21$ casillas en total.

Como el recorrido alterna entre columnas impares y pares y comienza en $(1,1)$ (columna impar), el camino visitará una secuencia de la forma:
$$\text{Impar} \to \text{Par} \to \text{Impar} \to \text{Par} \to \dots$$

Dado que solo existen $21$ casillas en las columnas pares, el rey cojo puede visitar como máximo $21$ casillas en columnas pares y, en consecuencia, como máximo $21 + 1 = 22$ casillas en columnas impares. 

Por lo tanto, el número total de casillas visitadas no puede superar:
$$21 + 22 = 43$$

### 2. Construcción para alcanzar el máximo
Podemos construir explícitamente un camino válido de $43$ casillas recorriendo por completo las columnas $1$ a $6$ por parejas y terminando en una casilla de la columna $7$:

1. **Columnas 1 y 2 (de arriba a abajo):**
   $$(1,1) \to (1,2) \to (2,1) \to (2,2) \to (3,1) \to (3,2) \to \dots \to (7,1) \to (7,2)$$
   *(14 casillas visitadas)*

2. **Transición y columnas 3 y 4 (de abajo a arriba):**
   Desde $(7,2)$ nos movemos a $(7,3)$ y recorremos hacia arriba:
   $$(7,3) \to (7,4) \to (6,3) \to (6,4) \to (5,3) \to (5,4) \to \dots \to (1,3) \to (1,4)$$
   *(14 casillas adicionales, 28 en total)*

3. **Transición y columnas 5 y 6 (de arriba a abajo):**
   Desde $(1,4)$ nos movemos a $(1,5)$ y recorremos hacia abajo:
   $$(1,5) \to (1,6) \to (2,5) \to (2,6) \to (3,5) \to (3,6) \to \dots \to (7,5) \to (7,6)$$
   *(14 casillas adicionales, 42 en total)*

4. **Paso final a la columna 7:**
   Desde $(7,6)$ nos movemos a $(7,7)$.
   *(1 casilla adicional, 43 en total)*

Todos los movimientos cumplen $|r - r'| \le 1$ y $|c - c'| = 1$, sin repetir ninguna casilla.

\boxed{43}