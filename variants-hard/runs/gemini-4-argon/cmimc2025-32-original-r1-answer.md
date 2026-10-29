Para encontrar la suma $p(1)+p(2)+p(3)+p(5)+p(6)$, analicemos el proceso como una cadena de Markov sobre las posiciones de los números en el árbol.

### 1. Estructura del árbol y condición de éxito
Etiquetemos los nodos del árbol como $u_1, u_2, u_3, u_4, u_5, u_6, u_7$ según el número que contienen inicialmente:
- **Nivel 1 (Raíz):** $u_4$
- **Nivel 2:** $u_2$ (izquierda), $u_6$ (derecha)
- **Nivel 3 (Hojas):** $u_1, u_3$ (hijos de $u_2$) y $u_5, u_7$ (hijos de $u_6$)

El árbol tiene $6$ aristas: $(u_4, u_2)$, $(u_4, u_6)$, $(u_2, u_1)$, $(u_2, u_3)$, $(u_6, u_5)$ y $(u_6, u_7)$.

En cada paso se elige una de estas $6$ aristas uniformemente al azar y se intercambian los números en sus extremos. Como en cada intercambio a lo sumo un nuevo número puede entrar en la raíz $u_4$, dos números distintos nunca pueden llegar a la raíz simultáneamente. Por lo tanto, para cualquier $a \in \{1, 2, 3, 5, 6\}$, la probabilidad $p(a)$ de que escribamos alguna vez el número $a$ es exactamente la probabilidad de que el número $a$ llegue a la raíz $u_4$ antes que el número $7$.

Para dos nodos distintos $x, y \neq u_4$, definamos $P(x, y)$ como la probabilidad de que una partícula que comienza en $x$ llegue a la raíz $u_4$ antes que una partícula que comienza en $y$. Como el algoritmo termina con probabilidad $1$ y las dinámicas de ambas partículas son idénticas, para todo par $x \neq y$ se cumple:
$$P(x, y) + P(y, x) = 1$$

Con esta notación, dado que el número $7$ comienza en $u_7$, tenemos que $p(a) = P(u_a, u_7)$.

---

### 2. Cálculo de $p(1)$, $p(3)$ y $p(5)$ por simetría
Las probabilidades de transición son invariantes bajo cualquier automorfismo del árbol que fije la raíz $u_4$:
- El automorfismo que intercambia las hojas hermanas $u_5 \leftrightarrow u_7$ implica que $P(u_5, u_7) = P(u_7, u_5)$. Como $P(u_5, u_7) + P(u_7, u_5) = 1$, obtenemos:
  $$p(5) = P(u_5, u_7) = \frac{1}{2}$$
- De manera análoga, intercambiando los subárboles izquierdo y derecho de la raíz, existen automorfismos que intercambian $u_1 \leftrightarrow u_7$ y $u_3 \leftrightarrow u_7$. Por lo tanto:
  $$p(1) = P(u_1, u_7) = \frac{1}{2}, \qquad p(3) = P(u_3, u_7) = \frac{1}{2}$$

En general, siempre que dos números comiencen en el mismo nivel del árbol (ambos en el nivel 2 o ambos en el nivel 3), la probabilidad de que uno llegue a la raíz antes que el otro es $\frac{1}{2}$.

---

### 3. Cálculo de $p(6)$ y $p(2)$
Condicionamos en el primer intercambio (cada una de las $6$ aristas se elige con probabilidad $\frac{1}{6}$):

**Para $\alpha = p(6) = P(u_6, u_7)$:**
1. **Arista $(u_4, u_6)$:** el número en $u_6$ sube a la raíz $u_4$ (éxito con probabilidad $1$).
2. **Aristas $(u_4, u_2)$, $(u_2, u_1)$, $(u_2, u_3)$:** ni $u_6$ ni $u_7$ se mueven (probabilidad $\alpha$ en cada caso).
3. **Arista $(u_6, u_5)$:** el número en $u_6$ pasa a $u_5$, llegando al estado $(u_5, u_7)$ donde ambos están en el nivel 3 (probabilidad $\frac{1}{2}$).
4. **Arista $(u_6, u_7)$:** las posiciones se intercambian, pasando al estado $(u_7, u_6)$ (probabilidad $P(u_7, u_6) = 1 - \alpha$).

Sumando los $6$ casos equiprobables:
$$6\alpha = 1 + 3\alpha + \frac{1}{2} + (1 - \alpha) \implies 4\alpha = \frac{5}{2} \implies p(6) = \alpha = \frac{5}{8}$$

**Para $\beta = p(2) = P(u_2, u_7)$:**
1. **Arista $(u_4, u_2)$:** el número en $u_2$ sube a la raíz $u_4$ (éxito con probabilidad $1$).
2. **Aristas $(u_4, u_6)$, $(u_6, u_5)$:** ni $u_2$ ni $u_7$ se mueven (probabilidad $\beta$ en cada caso).
3. **Aristas $(u_2, u_1)$, $(u_2, u_3)$:** el número en $u_2$ baja a una hoja ($u_1$ o $u_3$), quedando ambos en el nivel 3 (probabilidad $\frac{1}{2}$ en cada caso).
4. **Arista $(u_6, u_7)$:** el número en $u_7$ sube a $u_6$, llegando al estado $(u_2, u_6)$ donde ambos están en el nivel 2 (probabilidad $\frac{1}{2}$).

Sumando los $6$ casos equiprobables:
$$6\beta = 1 + 2\beta + \frac{1}{2} + \frac{1}{2} + \frac{1}{2} \implies 4\beta = \frac{5}{2} \implies p(2) = \beta = \frac{5}{8}$$

---

### 4. Suma total
Finalmente, sumamos todas las probabilidades:
$$p(1) + p(2) + p(3) + p(5) + p(6) = \frac{1}{2} + \frac{5}{8} + \frac{1}{2} + \frac{1}{2} + \frac{5}{8} = \frac{11}{4}$$

\boxed{\frac{11}{4}}