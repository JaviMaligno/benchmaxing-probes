Para encontrar el valor de $f(2015, 2)$, podemos analizar el comportamiento de la función calculando sus valores para los primeros números enteros $i \ge 0$. 

Representemos la función en el nivel $i$ como una tupla de 5 elementos:
\[F_i = (f(i,0), f(i,1), f(i,2), f(i,3), f(i,4))\]

De acuerdo con la definición recursiva:
1. $f(i, 0) = f(i-1, 1)$
2. $f(i, j) = f(i-1, f(i, j-1))$ para $1 \le j \le 4$.

Calculemos $F_i$ paso a paso para los primeros valores de $i$:

- **Para $i = 0$:**
  Usando $f(0, j) = \text{mod}_5(j+1)$:
  \[F_0 = (1, 2, 3, 4, 0)\]

- **Para $i = 1$:**
  - $f(1,0) = f(0,1) = 2$
  - $f(1,1) = f(0, f(1,0)) = f(0,2) = 3$
  - $f(1,2) = f(0, f(1,1)) = f(0,3) = 4$
  - $f(1,3) = f(0, f(1,2)) = f(0,4) = 0$
  - $f(1,4) = f(0, f(1,3)) = f(0,0) = 1$
  \[F_1 = (2, 3, 4, 0, 1)\]

- **Para $i = 2$:**
  - $f(2,0) = f(1,1) = 3$
  - $f(2,1) = f(1,3) = 0$
  - $f(2,2) = f(1,0) = 2$
  - $f(2,3) = f(1,2) = 4$
  - $f(2,4) = f(1,4) = 1$
  \[F_2 = (3, 0, 2, 4, 1)\]

- **Para $i = 3$:**
  - $f(3,0) = f(2,1) = 0$
  - $f(3,1) = f(2,0) = 3$
  - $f(3,2) = f(2,3) = 4$
  - $f(3,3) = f(2,4) = 1$
  - $f(3,4) = f(2,1) = 0$
  \[F_3 = (0, 3, 4, 1, 0)\]

- **Para $i = 4$:**
  - $f(4,0) = f(3,1) = 3$
  - $f(4,1) = f(3,3) = 1$
  - $f(4,2) = f(3,1) = 3$
  - $f(4,3) = f(3,3) = 1$
  - $f(4,4) = f(3,1) = 3$
  \[F_4 = (3, 1, 3, 1, 3)\]

- **Para $i = 5$:**
  - $f(5,0) = f(4,1) = 1$
  - $f(5,1) = f(4,1) = 1$
  - $f(5,2) = f(4,1) = 1$
  - $f(5,3) = f(4,1) = 1$
  - $f(5,4) = f(4,1) = 1$
  \[F_5 = (1, 1, 1, 1, 1)\]

A partir de $i = 5$, todos los valores de $f(i,j)$ son iguales a $1$. Como consecuencia, para $i = 6$, tendremos que $f(6,0) = f(5,1) = 1$, y recursivamente $f(6,j) = 1$ para todo $j$. 

Por inducción, $f(i, j) = 1$ para todo $i \ge 5$ y todo $0 \le j \le 4$. En particular, para $i = 2015$ y $j = 2$:

\boxed{1}