Para hallar el valor de $g(2024,3)$, calculemos los valores de la función $g(i,j)$ para los primeros valores de $i$, representando cada fila como una tupla $(g(i,0), g(i,1), g(i,2), g(i,3), g(i,4))$.

**Paso 1: Calcular $g(0,j)$**
Por definición, para $i = 0$ tenemos $g(0,j) = \text{rem}_5(j+1)$:
- $g(0,0) = \text{rem}_5(1) = 1$
- $g(0,1) = \text{rem}_5(2) = 2$
- $g(0,2) = \text{rem}_5(3) = 3$
- $g(0,3) = \text{rem}_5(4) = 4$
- $g(0,4) = \text{rem}_5(5) = 0$

Así, la fila para $i = 0$ es $(1, 2, 3, 4, 0)$.

**Paso 2: Calcular $g(1,j)$**
Usando la definición recursiva $g(1,0) = g(0,2)$ y $g(1,j) = g(0, g(1,j-1))$ para $1 \le j \le 4$:
- $g(1,0) = g(0,2) = 3$
- $g(1,1) = g(0,3) = 4$
- $g(1,2) = g(0,4) = 0$
- $g(1,3) = g(0,0) = 1$
- $g(1,4) = g(0,1) = 2$

La fila para $i = 1$ es $(3, 4, 0, 1, 2)$.

**Paso 3: Calcular $g(2,j)$**
- $g(2,0) = g(1,2) = 0$
- $g(2,1) = g(1,0) = 3$
- $g(2,2) = g(1,3) = 1$
- $g(2,3) = g(1,1) = 4$
- $g(2,4) = g(1,4) = 2$

La fila para $i = 2$ es $(0, 3, 1, 4, 2)$.

**Paso 4: Calcular $g(3,j)$**
- $g(3,0) = g(2,2) = 1$
- $g(3,1) = g(2,1) = 3$
- $g(3,2) = g(2,3) = 4$
- $g(3,3) = g(2,4) = 2$
- $g(3,4) = g(2,2) = 1$

La fila para $i = 3$ es $(1, 3, 4, 2, 1)$.

**Paso 5: Calcular $g(4,j)$**
- $g(4,0) = g(3,2) = 4$
- $g(4,1) = g(3,4) = 1$
- $g(4,2) = g(3,1) = 3$
- $g(4,3) = g(3,3) = 2$
- $g(4,4) = g(3,2) = 4$

La fila para $i = 4$ es $(4, 1, 3, 2, 4)$.

**Paso 6: Calcular $g(5,j)$ y observar la estabilización**
- $g(5,0) = g(4,2) = 3$
- $g(5,1) = g(4,3) = 2$
- $g(5,2) = g(4,2) = 3$
- $g(5,3) = g(4,3) = 2$
- $g(5,4) = g(4,2) = 3$

La fila para $i = 5$ es $(3, 2, 3, 2, 3)$.

Notamos que en la fila $i = 5$ se cumple que $g(5,2) = 3$ y $g(5,3) = 2$ (igual que en $i = 4$). Por lo tanto, al calcular $g(6,j)$ se alternará nuevamente entre $3$ y $2$:
- $g(6,0) = g(5,2) = 3$
- $g(6,1) = g(5,3) = 2$
- $g(6,2) = g(5,2) = 3$
- $g(6,3) = g(5,3) = 2$
- $g(6,4) = g(5,2) = 3$

Por inducción, para todo $i \ge 5$, la fila se mantiene constante e igual a $(3, 2, 3, 2, 3)$. Es decir, para todo $i \ge 5$:
\[g(i,j) = \begin{cases} 3 & \text{si } j \text{ es par,} \\ 2 & \text{si } j \text{ es impar.} \end{cases}\]

Como $2024 \ge 5$ y $j = 3$ es impar, concluimos que $g(2024,3) = 2$.

\boxed{2}