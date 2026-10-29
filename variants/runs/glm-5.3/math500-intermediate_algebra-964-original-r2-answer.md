# Solución paso a paso

## Planteamiento

Cada fila $i$ (los valores $f(i,0), f(i,1), \dots, f(i,4)$) se construye a partir de la fila anterior. Conviene observar que si $g(j) = f(i-1, j)$, entonces:

$$f(i,0) = g(1), \qquad f(i,j) = g(f(i,j-1)),$$

es decir, $f(i,j) = g^{j+1}(1)$: la fila $i$ evaluada en $j$ es la función de la fila anterior iterada $j+1$ veces sobre $1$.

## Construcción de las filas

**Fila 0:** $f(0,j) = j+1 \pmod 5$, es decir: $(1,2,3,4,0)$ — el "sucesor".

**Fila 1:** usando $g = $ sucesor:
$$f(1,j) = 1 + (j+1) = j+2 \pmod 5 \;\Rightarrow\; (2,3,4,0,1)$$

**Fila 2:** usando $g(j) = j+2$ (iterada $j+1$ veces sobre $1$):
$$f(2,j) = 1 + 2(j+1) = 2j+3 \pmod 5 \;\Rightarrow\; (3,0,2,4,1)$$

**Fila 3:** con $g(x) = 2x+3$, se cumple $g^k(1) = 4\cdot 2^k - 3 \pmod 5$:
- $f(3,0) = f(2,1) = 0$
- $f(3,1) = f(2,0) = 3$
- $f(3,2) = f(2,3) = 4$
- $f(3,3) = f(2,4) = 1$
- $f(3,4) = f(2,1) = 0$

Fila 3: $(0,3,4,1,0)$

**Fila 4:** con $g = $ fila 3 (donde $g(1)=3$, $g(3)=1$):
- $f(4,0) = f(3,1) = 3$
- $f(4,1) = f(3,3) = 1$
- $f(4,2) = f(3,1) = 3$
- $f(4,3) = f(3,3) = 1$
- $f(4,4) = f(3,1) = 3$

Fila 4: $(3,1,3,1,3)$

**Fila 5:** con $g = $ fila 4 (donde $g(1) = 1$):
- $f(5,0) = f(4,1) = 1$
- $f(5,j) = f(4, f(5,j-1)) = f(4,1) = 1$ para todo $j$

Fila 5: $(1,1,1,1,1)$ — constante igual a $1$.

**Filas $i \ge 5$:** si la fila $i-1$ es constante igual a $1$, entonces $f(i, j) = 1$ para todo $j$. Por inducción, **toda fila $i \ge 5$ es constante igual a $1$**.

## Conclusión

Como $2015 \ge 5$:

$$f(2015, 2) = 1$$

$$\boxed{1}$$