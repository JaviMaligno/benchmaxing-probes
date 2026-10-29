## Planteamiento

Cada bloque $3\times 2$ contiene $1,\dots,6$, así que en el bloque $j$ las parejas de las tres filas, $P_{1j},P_{2j},P_{3j}$, forman una partición de $\{1,\dots,6\}$. Cada fila también contiene $1,\dots,6$, así que $P_{i1},P_{i2},P_{i3}$ particionan $\{1,\dots,6\}$.

**Fila 1:** cualquier permutación: $6! = 720$ formas. Esto fija los conjuntos $A=P_{11}$, $B=P_{12}$, $C=P_{13}$.

**Fila 2:** debe cumplir $P_{2j}\cap P_{1j}=\varnothing$, es decir, el bloque 1 no puede recibir elementos de $A$, el bloque 2 ninguno de $B$, el bloque 3 ninguno de $C$. Contando con la matriz $n_{ij}$ = cuántos elementos del grupo $i$ van al bloque $j$: sumas de filas y columnas iguales a $2$ y diagonal nula. Si $n_{AB}=x$, todo queda determinado:
$$n_{AC}=n_{BA}=n_{CB}=2-x,\qquad n_{AB}=n_{BC}=n_{CA}=x,\qquad x\in\{0,1,2\}.$$
Las formas de elegir los elementos concretos son $\binom{2}{x}^3$:
$$x=0:1,\quad x=1:8,\quad x=2:1 \;\Longrightarrow\; 10 \text{ asignaciones de conjuntos}.$$
Cada pareja puede ordenarse de $2$ modos dentro de su bloque: $10\cdot 2^3 = 80$.

**Fila 3:** los conjuntos quedan forzados ($P_{3j}$ es el complemento de $P_{1j}\cup P_{2j}$, y automáticamente cada número aparece una vez en la fila 3). Solo restan los órdenes internos: $2^3 = 8$.

## Total

$$720\cdot 80\cdot 8 = 460800 = 2^{11}\cdot 3^{2}\cdot 5^{2}.$$

Por tanto $p\cdot a+q\cdot b+r\cdot c = 2\cdot 11 + 3\cdot 2 + 5\cdot 2 = 22+6+10 = 38$.

\boxed{38}