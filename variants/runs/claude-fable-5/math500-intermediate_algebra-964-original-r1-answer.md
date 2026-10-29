Voy a calcular las primeras filas de la función hasta encontrar un patrón estable.

**Fila $i=0$:** $f(0,j) = j+1 \pmod 5$, es decir: $1, 2, 3, 4, 0$ para $j=0,\dots,4$.

**Fila $i=1$:**
- $f(1,0) = f(0,1) = 2$
- $f(1,j) = f(0, f(1,j-1)) = f(1,j-1)+1 \pmod 5$, así que: $2, 3, 4, 0, 1$.

**Fila $i=2$:**
- $f(2,0) = f(1,1) = 3$
- $f(2,j) = f(1, f(2,j-1)) = f(2,j-1)+2 \pmod 5$, así que: $3, 0, 2, 4, 1$.

**Fila $i=3$:** usando $f(3,j) = f(2, f(3,j-1))$:
- $f(3,0) = f(2,1) = 0$
- $f(3,1) = f(2,0) = 3$
- $f(3,2) = f(2,3) = 4$
- $f(3,3) = f(2,4) = 1$
- $f(3,4) = f(2,1) = 0$

Fila: $0, 3, 4, 1, 0$.

**Fila $i=4$:** usando $f(4,j) = f(3, f(4,j-1))$:
- $f(4,0) = f(3,1) = 3$
- $f(4,1) = f(3,3) = 1$
- $f(4,2) = f(3,1) = 3$
- $f(4,3) = f(3,3) = 1$
- $f(4,4) = f(3,1) = 3$

Fila: $3, 1, 3, 1, 3$.

**Fila $i=5$:**
- $f(5,0) = f(4,1) = 1$
- $f(5,1) = f(4, f(5,0)) = f(4,1) = 1$
- Por inducción, $f(5,j) = f(4,1) = 1$ para todo $j$.

**Filas $i \ge 5$:** si $f(i,j) = 1$ para todo $j$, entonces $f(i+1,0) = f(i,1) = 1$ y $f(i+1,j) = f(i, f(i+1,j-1)) = 1$. Por lo tanto, la función es constante igual a $1$ para todo $i \ge 5$.

Como $2015 \ge 5$, tenemos $f(2015, 2) = 1$.

$$\boxed{1}$$