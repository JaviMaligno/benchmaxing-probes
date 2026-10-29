## Razonamiento

**Paso 1: estructura local de cada componente.**

Sea $G$ el grafo ($3$-regular, $12$ vértices) tal que todo par de vértices distintos tiene exactamente $0$ o $2$ vecinos comunes.

*Si una arista $uv$ tiene un vecino común:* entonces tiene exactamente dos, digamos $w_1,w_2$.
- Si $w_1\sim w_2$: $\{u,v,w_1,w_2\}$ es una $K_4$, y como cada vértice ya tiene grado $3$ dentro, la $K_4$ es una **componente conexa completa**.
- Si $w_1\nsim w_2$: sea $a_1$ el tercer vecino de $w_1$ y $a_2$ el de $w_2$. Si $a_1=a_2$, los pares $(w_1,w_2)$ tendrían $3$ vecinos comunes, imposible; luego $a_1\neq a_2$. Entonces $u$ y $a_1$ tienen como único vecino común a $w_1$ (pues $v$ y $w_2$ ya tienen su grado agotado), es decir, exactamente $1$ vecino común: **contradicción**.

Conclusión: **toda componente conexa válida o es $K_4$, o es un grafo sin triángulos** (toda arista tiene $0$ vecinos comunes).

**Paso 2: una componente sin triángulos es el cubo $Q_3$.**

Sea $v$ con vecinos $a,b,c$ (no adyacentes entre sí). Cada par, p. ej. $(a,b)$, ya comparte a $v$, así que comparte exactamente un vértice más $z$ (y $z\neq c$, por ausencia de triángulos). Definiendo $x$ (extra de $b,c$) e $y$ (extra de $a,c$), se comprueba que $x,y,z$ son distintos y que
$$N(a)=\{v,y,z\},\quad N(b)=\{v,x,z\},\quad N(c)=\{v,x,y\}.$$
Sea $x'$ el tercer vecino de $x$. El par $(x,a)$ debe tener $0$ o $2$ vecinos comunes, lo que obliga a $x'\notin\{v,y,z\}$, es decir, $x'$ es nuevo. Análogamente $y',z'$ son nuevos. Ahora el par $(x,y)$ comparte a $c$, así que debe compartir otro: eso fuerza $x'=y'$; el par $(x,z)$ fuerza $x'=z'$. Por lo tanto $x'=y'=z'=w$, y $N(w)=\{x,y,z\}$ agota su grado. Así la componente de $v$ es exactamente
$$\{v,a,b,c,x,y,z,w\}\cong Q_3 \quad (8\text{ vértices}).$$

**Paso 3: clasificación y conteo.**

Las únicas componentes válidas son $K_4$ ($4$ vértices) y $Q_3$ ($8$ vértices), ambas verifican la condición (y pares en componentes distintas tienen $0$ vecinos comunes). Como $12=4+4+4$ o $12=8+4$, hay exactamente dos familias:

- **Tres $K_4$:** particiones de $12$ pueblos en $3$ bloques de $4$:
$$\frac{12!}{(4!)^3\,3!}=5775.$$
- **Una $K_4$ y un cubo $Q_3$:** elegir los $4$ pueblos de la $K_4$: $\binom{12}{4}=495$; cubos etiquetados en los $8$ restantes: $\frac{8!}{|\mathrm{Aut}(Q_3)|}=\frac{8!}{48}=840$:
$$495\cdot 840=415800.$$

Total:
$$5775+415800=421575.$$

\boxed{421575}