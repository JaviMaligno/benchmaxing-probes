Para hallar el valor de $g(2024,3)$, calculemos los valores de la función $g(i,j)$ para los primeros valores de $i$ y $j \in \{0, 1, 2, 3, 4\}$. Representaremos la fila $i$-ésima como la tupla $\big(g(i,0), g(i,1), g(i,2), g(i,3), g(i,4)\big)$.

1. **Para $i = 0$:**
   Por definición, $g(0,j) = \text{rem}_5(j+1)$:
   - $g(0,0) = 1$
   - $g(0,1) = 2$
   - $g(0,2) = 3$
   - $g(0,3) = 4$
   - $g(0,4) = 0$
   
   Así, la fila para $i = 0$ es $(1, 2, 3, 4, 0)$.

2. **Para $i = 1$:**
   Usando la recurrencia $g(1,0) = g(0,2)$ y $g(1,j) = g(0, g(1,j-1))$:
   - $g(1,0) = g(0,2) = 3$
   - $g(1,1) = g(0,3) = 4$
   - $g(1,2) = g(0,4) = 0$
   - $g(1,3) = g(0,0) = 1$
   - $g(1,4) = g(0,1) = 2$
   
   La fila para $i = 1$ es $(3, 4, 0, 1, 2)$.

3. **Para $i = 2$:**
   - $g(2,0) = g(1,2) = 0$
   - $g(2,1) = g(1,0) = 3$
   - $g(2,2) = g(1,3) = 1$
   - $g(2,3) = g(1,1) = 4$
   - $g(2,4) = g(1,4) = 2$
   
   La fila para $i = 2$ es $(0, 3, 1, 4, 2)$.

4. **Para $i = 3$:**
   - $g(3,0) = g(2,2) = 1$
   - $g(3,1) = g(2,1) = 3$
   - $g(3,2) = g(2,3) = 4$
   - $g(3,3) = g(2,4) = 2$
   - $g(3,4) = g(2,2) = 1$
   
   La fila para $i = 3$ es $(1, 3, 4, 2, 1)$.

5. **Para $i = 4$:**
   - $g(4,0) = g(3,2) = 4$
   - $g(4,1) = g(3,4) = 1$
   - $g(4,2) = g(3,1) = 3$
   - $g(4,3) = g(3,3) = 2$
   - $g(4,4) = g(3,2) = 4$
   
   La fila para $i = 4$ es $(4, 1, 3, 2, 4)$.

6. **Para $i = 5$:**
   - $g(5,0) = g(4,2) = 3$
   - $g(5,1) = g(4,3) = 2$
   - $g(5,2) = g(4,2) = 3$
   - $g(5,3) = g(4,3) = 2$
   - $g(5,4) = g(4,2) = 3$
   
   La fila para $i = 5$ es $(3, 2, 3, 2, 3)$.

7. **Para $i \ge 5$:**
   Observamos que si la fila $(i-1)$ es $(3, 2, 3, 2, 3)$, en particular $g(i-1, 2) = 3$ y $g(i-1, 3) = 2$, por lo que la fila $i$ vuelve a ser:
   - $g(i,0) = g(i-1,2) = 3$
   - $g(i,1) = g(i-1,3) = 2$
   - $g(i,2) = g(i-1,2) = 3$
   - $g(i,3) = g(i-1,3) = 2$
   - $g(i,4) = g(i-1,2) = 3$

Por inducción, para todo $i \ge 5$ se cumple que $g(i,j)$ se estabiliza en la secuencia $(3, 2, 3, 2, 3)$ (y de hecho, $g(i,3) = 2$ para todo $i \ge 3$). Por consiguiente, para $i = 2024$, tenemos que $g(2024,3) = 2$.

\boxed{2}