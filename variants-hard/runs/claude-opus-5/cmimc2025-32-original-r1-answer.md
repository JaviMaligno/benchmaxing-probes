Voy a resolver el problema analíticamente y luego verificarlo con una simulación.

**Planteamiento.** Nombro los nodos: $r$ (raíz), $l$ y $R$ (nivel 2), hojas $a_1,a_2$ (hijas de $l$) y $b_1,b_2$ (hijas de $R$). Inicialmente: $4$ en $r$, $2$ en $l$, $6$ en $R$, $1,3$ en $a_1,a_2$, $5$ en $b_1$, $7$ en $b_2$.

Como el algoritmo escribe la raíz en cada paso y se detiene al escribir el $7$:
$$p(a)=P(T_a<T_7)$$
donde $T_x$ es el primer instante en que la etiqueta $x$ está en la raíz. Lo esencial: **el par (posición de $a$, posición de $7$) es por sí mismo una cadena de Markov** (al elegir una arista, cada etiqueta se mueve solo si está en un extremo). Basta entonces con $g(x,y)=P(T_A<T_B)$ con $A$ en $x$ y $B$ en $y$, con $g=1$ si $x=r$ y $g=0$ si $y=r$.

Por simetría del árbol quedan 7 clases: $A=g(l,R)$, $B=g(l,a_1)$, $C=g(l,b_1)$, $D=g(a_1,l)$, $E=g(a_1,R)$, $F=g(a_1,a_2)$, $G=g(a_1,b_1)$.