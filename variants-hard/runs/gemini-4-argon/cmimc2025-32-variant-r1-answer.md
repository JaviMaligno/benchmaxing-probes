Para hallar $q(1) + q(2) + q(3) + q(5) + q(7)$, analizamos el procedimiento como una cadena de Markov sobre las posiciones de los números en el árbol.

### 1. Reformulación del problema
Inicialmente, el número $4$ está en la raíz y se registra en el primer paso. A partir de ese momento, el procedimiento termina exactamente cuando el número $6$ llega a la raíz por primera vez. 

Por lo tanto, para cualquier $a \in \{1, 2, 3, 5, 7\}$, el número $a$ llega a ser registrado durante la ejecución si y solo si **$a$ alcanza el nodo raíz antes de que el número $6$ alcance el nodo raíz**.

Para un $a$ fijo, las posiciones de los demás números (distintos de $a$ y $6$) no afectan la probabilidad de que $a$ llegue a la raíz antes que $6$. Así, basta con seguir el par ordenado $(u, v)$ de vértices distintos que representan las posiciones actuales de $a$ y $6$, respectivamente.

Denotemos los $7$ vértices del árbol según su configuración inicial:
- Nivel 1 (raíz): $R$ (contiene inicialmente al $4$).
- Nivel 2: $L$ (hijo izquierdo de $R$, contiene al $2$) y $M$ (hijo derecho de $R$, contiene al $6$).
- Nivel 3 (hojas): $LL, LR$ (hijos de $L$, contienen a $1$ y $3$) y $ML, MR$ (hijos de $M$, contienen a $5$ y $7$).

Sea $p(u, v)$ la probabilidad de que una partícula que comienza en el vértice $u$ alcance la raíz $R$ antes que una partícula que comienza en el vértice $v$ (con $u \neq v$ y $u, v \neq R$). Buscamos calcular:
$$q(1) + q(2) + q(3) + q(5) + q(7) = p(LL, M) + p(L, M) + p(LR, M) + p(ML, M) + p(MR, M)$$

---

### 2. Propiedades de simetría
Como el proceso termina con probabilidad $1$ y las reglas de transición son completamente simétricas respecto a las dos partículas, para todo par de vértices distintos $u, v \in V \setminus \{R\}$ se cumple:
$$p(u, v) + p(v, u) = 1$$

Además, usando los automorfismos del árbol (que fijan la raíz $R$ y preservan la distribución uniforme sobre las $6$ aristas):
1. **Dos vértices de nivel 2 ($L$ y $M$):** El automorfismo que intercambia el subárbol izquierdo con el derecho intercambia $L$ y $M$. Por simetría:
   $$p(L, M) = p(M, L) = \frac{1}{2}$$
   De aquí obtenemos directamente que **$q(2) = \frac{1}{2}$**.

2. **Dos hojas cualesquiera ($u, v \in \{LL, LR, ML, MR\}$ con $u \neq v$):** 
   - Si son hojas hermanas (por ejemplo, $ML$ y $MR$), existe un automorfismo del árbol que las intercambia dejando fijos los demás vértices, por lo que $p(ML, MR) = \frac{1}{2}$.
   - Si están en distintos subárboles (por ejemplo, $LL$ y $ML$), el automorfismo que intercambia el subárbol izquierdo con el derecho envía $(LL, ML)$ a $(ML, LL)$, por lo que $p(LL, ML) = p(LL, MR) = \frac{1}{2}$.
   
   En consecuencia, **para cualquier par de hojas distintas $u, v$, se tiene $p(u, v) = \frac{1}{2}$**.

3. **Un vértice de nivel 3 y uno de nivel 2:** Quedan únicamente dos casos por simetría:
   - $x = p(LL, M) = p(LR, M)$, que corresponde a $q(1) = q(3) = x$ (la hoja y el vértice de nivel 2 están en subárboles distintos).
   - $y = p(ML, M) = p(MR, M)$, que corresponde a $q(5) = q(7) = y$ (la hoja es hija del vértice de nivel 2).

---

### 3. Cálculo de $x = q(1) = q(3)$
Partiendo del estado $(LL, M)$, en cada paso se elige una de las $6$ aristas al azar:
- **Arista $(R, M)$:** $M$ pasa a la raíz $R$ (el número $6$ llega primero), probabilidad de éxito $0$.
- **Arista $(L, LL)$:** $LL$ sube a $L$, pasando al estado $(L, M)$, donde la probabilidad de éxito es $p(L, M) = \frac{1}{2}$.
- **Arista $(M, ML)$:** $M$ baja a $ML$, pasando al estado $(LL, ML)$ (dos hojas), con probabilidad de éxito $\frac{1}{2}$.
- **Arista $(M, MR)$:** $M$ baja a $MR$, pasando al estado $(LL, MR)$ (dos hojas), con probabilidad de éxito $\frac{1}{2}$.
- **Aristas $(R, L)$ y $(L, LR)$:** no mueven ni a $LL$ ni a $M$, permaneciendo en el estado $(LL, M)$ con probabilidad $x$.

Planteando la ecuación de primer paso:
$$x = \frac{1}{6}\left(0 + \frac{1}{2} + \frac{1}{2} + \frac{1}{2} + 2x\right) \implies 4x = \frac{3}{2} \implies x = \frac{3}{8}$$
Por tanto, **$q(1) = q(3) = \frac{3}{8}$**.

---

### 4. Cálculo de $y = q(5) = q(7)$
Partiendo del estado $(ML, M)$, analizamos el efecto de elegir cada una de las $6$ aristas:
- **Arista $(R, M)$:** $M$ sube a $R$ (gana el $6$), probabilidad de éxito $0$.
- **Arista $(M, ML)$:** intercambia las posiciones de $ML$ y $M$, pasando al estado $(M, ML)$, cuya probabilidad de éxito es $p(M, ML) = 1 - p(ML, M) = 1 - y$.
- **Arista $(M, MR)$:** $M$ pasa a $MR$, llevando al estado $(ML, MR)$ (dos hojas hermanas), cuya probabilidad de éxito es $\frac{1}{2}$.
- **Aristas $(R, L)$, $(L, LL)$ y $(L, LR)$:** no afectan a $ML$ ni a $M$, manteniendo el estado $(ML, M)$ con probabilidad $y$.

Planteando la ecuación de primer paso:
$$y = \frac{1}{6}\left(0 + (1 - y) + \frac{1}{2} + 3y\right) \implies 6y = \frac{3}{2} + 2y \implies 4y = \frac{3}{2} \implies y = \frac{3}{8}$$
Por tanto, **$q(5) = q(7) = \frac{3}{8}$**.

---

### 5. Suma total
Sumando las probabilidades obtenidas:
$$q(1) + q(2) + q(3) + q(5) + q(7) = \frac{3}{8} + \frac{1}{2} + \frac{3}{8} + \frac{3}{8} + \frac{3}{8} = \frac{16}{8} = 2$$

\boxed{2}