

Definamos, para cada \(i\ge 0\), la función

\[
f_i(j)=g(i,j), \qquad j\in\{0,1,2,3,4\}.
\]

Entonces \(f_i\) puede representarse como la tupla

\[
(f_i(0),f_i(1),f_i(2),f_i(3),f_i(4)).
\]

Para \(i=0\),

\[
g(0,j)=\operatorname{rem}_5(j+1),
\]

así que

\[
f_0=(1,2,3,4,0).
\]

Para \(i\ge 1\), la recursión dice

\[
f_i(0)=f_{i-1}(2)
\]

y

\[
f_i(j)=f_{i-1}(f_i(j-1)) \quad (1\le j\le 4).
\]

Por tanto,

\[
f_i(j)=f_{i-1}^{\,j+1}(2),
\]

donde \(f_{i-1}^{\,k}\) significa aplicar \(f_{i-1}\) \(k\) veces.

Calculemos las primeras filas.

### \(i=1\)

Partimos de \(2\) bajo \(f_0\):

\[
2\mapsto 3\mapsto 4\mapsto 0\mapsto 1\mapsto 2.
\]

Así,

\[
f_1=(3,4,0,1,2).
\]

### \(i=2\)

Bajo \(f_1\), empezando en \(2\):

\[
2\mapsto 0\mapsto 3\mapsto 1\mapsto 4\mapsto 2.
\]

Luego

\[
f_2=(0,3,1,4,2).
\]

### \(i=3\)

Bajo \(f_2\), empezando en \(2\):

\[
2\mapsto 1\mapsto 3\mapsto 4\mapsto 2\mapsto 1.
\]

Luego

\[
f_3=(1,3,4,2,1).
\]

### \(i=4\)

Bajo \(f_3\), empezando en \(2\):

\[
2\mapsto 4\mapsto 1\mapsto 3\mapsto 2\mapsto 4.
\]

Luego

\[
f_4=(4,1,3,2,4).
\]

### \(i=5\)

Bajo \(f_4\), empezando en \(2\):

\[
2\mapsto 3\mapsto 2\mapsto 3\mapsto 2\mapsto 3.
\]

Luego

\[
f_5=(3,2,3,2,3).
\]

### \(i=6\)

Bajo \(f_5\), empezando en \(2\):

\[
2\mapsto 3\mapsto 2\mapsto 3\mapsto 2\mapsto 3.
\]

Por tanto,

\[
f_6=(3,2,3,2,3)=f_5.
\]

Así que la sucesión se estabiliza:

\[
f_i=(3,2,3,2,3)\quad \text{para todo } i\ge 5.
\]

Como \(2024\ge 5\),

\[
g(2024,3)=f_{2024}(3)=f_5(3)=2.
\]

\[
\boxed{2}
\]