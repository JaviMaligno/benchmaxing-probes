## Resolución

**Caso base (i = 0):** g(0,j) = (j+1) mod 5, es decir: 1, 2, 3, 4, 0 para j = 0,…,4.

**Fila i = 1:**
- g(1,0) = g(0,2) = 3
- g(1,1) = g(0,3) = 4
- g(1,2) = g(0,4) = 0
- g(1,3) = g(0,0) = 1
- g(1,4) = g(0,1) = 2

**Fila i = 2:**
- g(2,0) = g(1,2) = 0
- g(2,1) = g(1,0) = 3
- g(2,2) = g(1,3) = 1
- g(2,3) = g(1,1) = 4
- g(2,4) = g(1,4) = 2

**Fila i = 3:**
- g(3,0) = g(2,2) = 1
- g(3,1) = g(2,1) = 3
- g(3,2) = g(2,3) = 4
- g(3,3) = g(2,4) = 2
- g(3,4) = g(2,2) = 1

**Fila i = 4:**
- g(4,0) = g(3,2) = 4
- g(4,1) = g(3,4) = 1
- g(4,2) = g(3,1) = 3
- g(4,3) = g(3,3) = 2
- g(4,4) = g(3,2) = 4

**Fila i = 5:**
- g(5,0) = g(4,2) = 3
- g(5,1) = g(4,3) = 2
- g(5,2) = g(4,2) = 3
- g(5,3) = g(4,3) = 2
- g(5,4) = g(4,2) = 3

**Fila i = 6:**
- g(6,0) = g(5,2) = 3
- g(6,1) = g(5,3) = 2
- g(6,2) = g(5,2) = 3
- g(6,3) = g(5,3) = 2
- g(6,4) = g(5,2) = 3

La fila 6 es idéntica a la fila 5, así que por inducción todas las filas con i ≥ 5 son iguales: g(i,j) = 3 si j es par y g(i,j) = 2 si j es impar.

Como 2024 ≥ 5 y j = 3 es impar:

\[\boxed{2}\]