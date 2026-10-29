Para encontrar el valor de $f(2015, 2)$, podemos analizar el comportamiento de la función calculando los valores de $f(i, j)$ para los primeros valores de $i$. 

Representemos cada fila $i$ como una tupla de 5 elementos: $f_i = (f(i,0), f(i,1), f(i,2), f(i,3), f(i,4))$. Note que de la definición recursiva se tiene que $f(i, j)$ consiste en aplicar la función $f_{i-1}$ de manera iterada $j+1$ veces sobre el valor inicial $1$, es decir, $f_i(j) = f_{i-1}^{(j+1)}(1)$.

**Para $i = 0$:**
Usando $f(0, j) = \text{mod}_5(j+1)$:
* $f(0, 0) = 1$
* $f(0, 1) = 2$
* $f(0, 2) = 3$
* $f(0, 3) = 4$
* $f(0, 4) = 0$

Por lo tanto, $f_0 = (1, 2, 3, 4, 0)$.

**Para $i = 1$:**
* $f(1, 0) = f(0, 1) = 2$
* $f(1, 1) = f(0, f(1, 0)) = f(0, 2) = 3$
* $f(1, 2) = f(0, f(1, 1)) = f(0, 3) = 4$
* $f(1, 3) = f(0, f(1, 2)) = f(0, 4) = 0$
* $f(1, 4) = f(0, f(1, 3)) = f(0, 0) = 1$

Por lo tanto, $f_1 = (2, 3, 4, 0, 1)$.

**Para $i = 2$:**
* $f(2, 0) = f(1, 1) = 3$
* $f(2, 1) = f(1, f(2, 0)) = f(1, 3) = 0$
* $f(2, 2) = f(1, f(2, 1)) = f(1, 0) = 2$
* $f(2, 3) = f(1, f(2, 2)) = f(1, 2) = 4$
* $f(2, 4) = f(1, f(2, 3)) = f(1, 4) = 1$

Por lo tanto, $f_2 = (3, 0, 2, 4, 1)$.

**Para $i = 3$:**
* $f(3, 0) = f(2, 1) = 0$
* $f(3, 1) = f(2, f(3, 0)) = f(2, 0) = 3$
* $f(3, 2) = f(2, f(3, 1)) = f(2, 3) = 4$
* $f(3, 3) = f(2, f(3, 2)) = f(2, 4) = 1$
* $f(3, 4) = f(2, f(3, 3)) = f(2, 1) = 0$

Por lo tanto, $f_3 = (0, 3, 4, 1, 0)$.

**Para $i = 4$:**
* $f(4, 0) = f(3, 1) = 3$
* $f(4, 1) = f(3, f(4, 0)) = f(3, 3) = 1$
* $f(4, 2) = f(3, f(4, 1)) = f(3, 1) = 3$
* $f(4, 3) = f(3, f(4, 2)) = f(3, 3) = 1$
* $f(4, 4) = f(3, f(4, 3)) = f(3, 1) = 3$

Por lo tanto, $f_4 = (3, 1, 3, 1, 3)$.

**Para $i = 5$:**
Observamos que $f(4, 1) = 1$, por lo que $1$ es un punto fijo de $f_4$:
* $f(5, 0) = f(4, 1) = 1$
* $f(5, 1) = f(4, f(5, 0)) = f(4, 1) = 1$
* $f(5, 2) = f(4, f(5, 1)) = f(4, 1) = 1$
* $f(5, 3) = f(4, f(5, 2)) = f(4, 1) = 1$
* $f(5, 4) = f(4, f(5, 3)) = f(4, 1) = 1$

Por lo tanto, $f_5 = (1, 1, 1, 1, 1)$.

Dado que la función $f_5$ es constante e igual a $1$, por inducción se cumple que para todo $i \ge 5$ y todo $j \in \{0, 1, 2, 3, 4\}$, tenemos que $f(i, j) = 1$. En particular, para $i = 2015$ y $j = 2$:

\boxed{1}