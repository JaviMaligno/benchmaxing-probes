

Tratemos los números como fichas que se mueven por el árbol al intercambiar extremos de una arista elegida uniformemente.

Para dos fichas distintas $x,y$, sea $Q(x,y)$ la probabilidad de que $x$ llegue a la raíz antes que $y$. Como el algoritmo termina cuando $7$ llega a la raíz, para $a\neq 4$ se tiene

$$
p(a)=Q(a,7).
$$

Nombremos los vértices así: $r$ es la raíz; $a$ el interno izquierdo, $b$ el interno derecho; $a_1,a_2$ las hojas izquierdas, $b_1,b_2$ las hojas derechas. Inicialmente $7$ está en $b_2$.

Hechos por simetría:

- $Q(x,y)+Q(y,x)=1$, pues con probabilidad $1$ una de las dos fichas llega primero a la raíz y no pueden llegar a la vez.
- $Q(b_1,b_2)=\frac12$, porque las dos hojas derechas son simétricas.
- $Q(a_i,b_2)=\frac12$, porque una hoja izquierda y una hoja derecha son simétricas al intercambiar los dos subárboles.
- $Q(a,b)=\frac12$, porque los dos nodos internos son simétricos.

Ahora calculemos los dos casos restantes.

Sea $A=Q(b,b_2)=p(6)$. Desde el estado $(b,b_2)$, entre las $6$ aristas:

- $3$ no tocan ninguna de las dos fichas: sigue con probabilidad $A$.
- la arista $r$–$b$ lleva $b$ a la raíz: éxito $1$.
- la arista $b$–$b_2$ intercambia las fichas: queda $(b_2,b)$, con probabilidad $1-A$.
- la arista $b$–$b_1$ deja las fichas como hojas hermanas: probabilidad $\frac12$.

Por tanto,

$$
A=\frac{3A+1+(1-A)+\frac12}{6}
=\frac{2A+\frac52}{6}.
$$

De aquí,

$$
6A=2A+\frac52 \implies 4A=\frac52 \implies A=\frac58.
$$

Sea $D=Q(a,b_2)=p(2)$. Desde el estado $(a,b_2)$:

- la arista $r$–$a$ lleva $a$ a la raíz: éxito $1$.
- $2$ aristas no tocan ninguna de las dos fichas: sigue con probabilidad $D$.
- $2$ aristas mueven $a$ a una hoja izquierda: queda hoja izquierda contra $b_2$, probabilidad $\frac12$.
- la arista $b$–$b_2$ mueve $7$ al interno derecho: quedan los dos internos, probabilidad $\frac12$.

Así,

$$
D=\frac{1+2D+3\cdot \frac12}{6}
=\frac{2D+\frac52}{6},
$$

y por tanto

$$
D=\frac58.
$$

Finalmente,

$$
p(1)=\frac12,\quad
p(2)=\frac58,\quad
p(3)=\frac12,\quad
p(5)=\frac12,\quad
p(6)=\frac58.
$$

Entonces

$$
p(1)+p(2)+p(3)+p(5)+p(6)
=
\frac12+\frac58+\frac12+\frac12+\frac58
=
\frac{22}{8}
=
\frac{11}{4}.
$$

$$
\boxed{\frac{11}{4}}
$$