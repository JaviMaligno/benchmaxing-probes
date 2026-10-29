## Resolución paso a paso

Definamos, para cada $i \ge 0$, la fila $f_i(j) = g(i,j)$. La recurrencia se puede reinterpretar así: como

$$
g(i,0)=g(i-1,2),\qquad g(i,j)=g(i-1,\,g(i,j-1)),
$$

entonces

$$
g(i,j) = g(i-1)^{j+1}(2),
$$

es decir, $g(i,j)$ es el resultado de aplicar $j+1$ veces la función $f_{i-1}$ al valor $2$.

### Fila base ($i=0$)

$$
f_0 = [\,1,2,3,4,0\,],
$$

pues $g(0,j)=\mathrm{rem}_5(j+1)$.

### Fila 1

Partimos de $2$ y aplicamos $f_0$:

$$
2 \to 3 \to 4 \to 0 \to 1 \to 2.
$$

Así:

$$
f_1(0)=3,\ f_1(1)=4,\ f_1(2)=0,\ f_1(3)=1,\ f_1(4)=2,
$$

es decir

$$
f_1 = [\,3,4,0,1,2\,].
$$

### Fila 2

Órbita de $2$ bajo $f_1$: $2\to 0\to 3\to 1\to 4\to 2$. Entonces

$$
f_2 = [\,0,3,1,4,2\,].
$$

### Fila 3

Órbita de $2$ bajo $f_2$: $2\to 1\to 3\to 4\to 2$. Entonces

$$
f_3 = [\,1,3,4,2,1\,].
$$

### Fila 4

Órbita de $2$ bajo $f_3$: $2\to 4\to 1\to 3\to 2$. Entonces

$$
f_4 = [\,4,1,3,2,4\,].
$$

### Fila 5

Órbita de $2$ bajo $f_4$: $2\leftrightarrow 3$. Entonces

$$
f_5 = [\,3,2,3,2,3\,].
$$

### Punto fijo

Para $f_5 = [3,2,3,2,3]$, la órbita de $2$ vuelve a ser $2\leftrightarrow 3$, de modo que

$$
f_6 = f_5 = [\,3,2,3,2,3\,].
$$

Como cada fila depende únicamente de la anterior, todas las filas con $i\ge 5$ son iguales a

$$
[\,3,2,3,2,3\,].
$$

En particular, como $2024\ge 5$,

$$
g(2024,3)=f_{2024}(3)=2.
$$

$$
\boxed{2}
$$