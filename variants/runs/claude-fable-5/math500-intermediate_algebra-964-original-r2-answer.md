## Resolución

**Nivel i = 0:** $f(0,j) = (j+1) \bmod 5$.

**Nivel i = 1:**
- $f(1,0) = f(0,1) = 2$
- $f(1,1) = f(0, f(1,0)) = f(0,2) = 3$
- $f(1,2) = f(0,3) = 4$, $f(1,3) = f(0,4) = 0$, $f(1,4) = f(0,0) = 1$

Es decir, $f(1,j) = (j+2) \bmod 5$.

**Nivel i = 2:**
- $f(2,0) = f(1,1) = 3$
- $f(2,1) = f(1,3) = 0$
- $f(2,2) = f(1,0) = 2$
- $f(2,3) = f(1,2) = 4$
- $f(2,4) = f(1,4) = 1$

**Nivel i = 3:**
- $f(3,0) = f(2,1) = 0$
- $f(3,1) = f(2,0) = 3$
- $f(3,2) = f(2,3) = 4$
- $f(3,3) = f(2,4) = 1$
- $f(3,4) = f(2,1) = 0$

**Nivel i = 4:**
- $f(4,0) = f(3,1) = 3$
- $f(4,1) = f(3,3) = 1$
- $f(4,2) = f(3,1) = 3$
- $f(4,3) = f(3,3) = 1$
- $f(4,4) = f(3,1) = 3$

**Nivel i = 5:**
- $f(5,0) = f(4,1) = 1$
- $f(5,1) = f(4, f(5,0)) = f(4,1) = 1$
- Análogamente, $f(5,j) = 1$ para todo $j$.

**Nivel i ≥ 6:** Como $f(5,j) = 1$ para todo $j$, entonces $f(6,0) = f(5,1) = 1$ y $f(6,j) = f(5, \cdot) = 1$ siempre. Por inducción, $f(i,j) = 1$ para todo $i \ge 5$ y todo $j$.

Como $2015 \ge 5$, se concluye que $f(2015,2) = 1$.

$$\boxed{1}$$