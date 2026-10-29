## Solución

Calculo las filas sucesivas de $g$ (cada fila $i$ es una función de $j \in \{0,1,2,3,4\}$):

**Fila 0:** $g(0,j) = (j+1) \bmod 5$, es decir $[1,2,3,4,0]$.

**Fila 1:** $g(1,0) = g(0,2) = 3$, y $g(1,j) = g(0, g(1,j-1)) = g(1,j-1)+1 \pmod 5$.
Resulta $[3,4,0,1,2]$, o sea $g(1,j) = j+3 \pmod 5$.

**Fila 2:** $g(2,0) = g(1,2) = 0$, y $g(2,j) = g(2,j-1)+3 \pmod 5$.
Resulta $[0,3,1,4,2]$, o sea $g(2,j) = 3j \pmod 5$.

**Fila 3:** $g(3,0) = g(2,2) = 1$, y $g(3,j) = 3\cdot g(3,j-1) \pmod 5$.
Resulta $[1,3,4,2,1]$, o sea $g(3,j) = 3^j \pmod 5$.

**Fila 4:** $g(4,0) = g(3,2) = 4$, y $g(4,j) = 3^{\,g(4,j-1)} \pmod 5$:
- $g(4,1) = 3^4 = 81 \equiv 1$
- $g(4,2) = 3^1 = 3$
- $g(4,3) = 3^3 = 27 \equiv 2$
- $g(4,4) = 3^2 = 9 \equiv 4$

Fila 4: $[4,1,3,2,4]$.

**Fila 5:** $g(5,0) = g(4,2) = 3$, luego:
- $g(5,1) = g(4,3) = 2$
- $g(5,2) = g(4,2) = 3$
- $g(5,3) = g(4,3) = 2$
- $g(5,4) = g(4,2) = 3$

Fila 5: $[3,2,3,2,3]$.

**Fila 6:** $g(6,0) = g(5,2) = 3$, y aplicando la recursión con la fila 5 se obtiene de nuevo $[3,2,3,2,3]$. Es un punto fijo: toda fila $i \ge 5$ es $[3,2,3,2,3]$.

Como $2024 \ge 5$, se tiene $g(2024,3) = 2$.

$$\boxed{2}$$