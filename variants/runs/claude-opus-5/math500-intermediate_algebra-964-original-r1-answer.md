## Cálculo paso a paso

**Caso base** $i=0$: $f(0,j)=\mathrm{mod}_5(j+1)$, es decir la fila $(1,2,3,4,0)$ para $j=0,\dots,4$.

**Fila $i=1$:**
- $f(1,0)=f(0,1)=2$
- $f(1,1)=f(0,2)=3$
- $f(1,2)=f(0,3)=4$
- $f(1,3)=f(0,4)=0$
- $f(1,4)=f(0,0)=1$ → $(2,3,4,0,1)$

**Fila $i=2$:**
- $f(2,0)=f(1,1)=3$
- $f(2,1)=f(1,3)=0$
- $f(2,2)=f(1,0)=2$
- $f(2,3)=f(1,2)=4$
- $f(2,4)=f(1,4)=1$ → $(3,0,2,4,1)$

**Fila $i=3$:**
- $f(3,0)=f(2,1)=0$
- $f(3,1)=f(2,0)=3$
- $f(3,2)=f(2,3)=4$
- $f(3,3)=f(2,4)=1$
- $f(3,4)=f(2,1)=0$ → $(0,3,4,1,0)$

**Fila $i=4$:**
- $f(4,0)=f(3,1)=3$
- $f(4,1)=f(3,3)=1$
- $f(4,2)=f(3,1)=3$
- $f(4,3)=f(3,3)=1$
- $f(4,4)=f(3,1)=3$ → $(3,1,3,1,3)$

**Fila $i=5$:**
- $f(5,0)=f(4,1)=1$
- $f(5,1)=f(4,1)=1$, y análogamente el resto → $(1,1,1,1,1)$

**Punto fijo:** si la fila $i$ es constante igual a $1$, entonces $f(i+1,0)=f(i,1)=1$ y $f(i+1,j)=f(i,1)=1$ para todo $j$. Por inducción, toda fila con $i\ge 5$ es idénticamente $1$.

Como $2015\ge 5$, se concluye $f(2015,2)=1$.

\boxed{1}