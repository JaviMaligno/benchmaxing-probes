Para encontrar el número de ternas ordenadas $(p, q, r)$ de permutaciones en el grupo simétrico $S_6$ que cumplen las condiciones dadas, reescribimos las ecuaciones en términos de composición en el grupo $S_6$ (donde denotamos la identidad por $e$):

$$pqr = rqp = q, \qquad qrp = prq = r, \qquad rpq = qpr = p.$$

### Paso 1: Simplificación algebraica de las relaciones

Utilizando la asociatividad de la composición de permutaciones y las ecuaciones dadas, obtenemos:
1. $p(qrp) = (pqr)p \implies pr = qp$.
2. $q(rpq) = (qrp)q \implies qp = rq$.
3. $r(qpr) = (rqp)r \implies rp = qr$.
4. $p(rqp) = (prq)p \implies pq = rp$.

De aquí se deduce que:
$$pq = qr = rp \quad \text{y} \quad qp = rq = pr.$$

Sustituyendo $qr = pq$ en la primera ecuación $p(qr) = q$, tenemos:
$$p(pq) = q \implies p^2 q = q \implies p^2 = e.$$
Por simetría entre $p, q$ y $r$, las tres permutaciones son involuciones:
$$p^2 = q^2 = r^2 = e.$$

Además, de $qr = pq$ y $q^2 = e$, multiplicando por $q$ por la izquierda obtenemos que $r$ queda unívocamente determinado por $p$ y $q$:
$$r = qpq.$$

Finalmente, sea $g = pq$. Entonces:
$$g^3 = (pq)(pq)(pq) = (pq)(qr)(rp) = p q^2 r^2 p = p^2 = e.$$
Como $q = pg$ (pues $p^2 = e$), la condición $q^2 = e$ equivale a:
$$(pg)(pg) = e \iff pgp = g^{-1}.$$

Recíprocamente, si $(g, p) \in S_6 \times S_6$ cumplen $g^3 = e$, $p^2 = e$ y $pgp = g^{-1}$, entonces definiendo $q = pg$ y $r = pg^2$ se satisfacen $p^2 = q^2 = r^2 = e$ y $pq = qr = rp = g$, de donde se siguen inmediatamente las seis ecuaciones originales.

Por lo tanto, el número de ternas $(p, q, r)$ buscadas es igual al número de pares $(g, p) \in S_6 \times S_6$ tales que:
$$g^3 = e, \qquad p^2 = e, \qquad pgp^{-1} = g^{-1}.$$

---

### Paso 2: Conteo por estructura de ciclos de $g$

Como $g^3 = e$ en $S_6$, los ciclos disjuntos de $g$ solo pueden tener longitud $1$ o $3$. Dividimos el conteo en tres casos según el tipo de ciclos de $g$:

#### Caso 1: $g = e$ (seis $1$-ciclos)
* Hay **$1$** elemento $g$ de este tipo.
* La condición $pep^{-1} = e$ se cumple siempre, por lo que $p$ puede ser cualquier involución ($p^2 = e$) en $S_6$.
* Contamos las involuciones en $S_6$ según el número $k$ de $2$-ciclos disjuntos ($k \in \{0, 1, 2, 3\}$):
  * $k = 0$: $1$
  * $k = 1$: $\binom{6}{2} = 15$
  * $k = 2$: $\frac{1}{2!}\binom{6}{2}\binom{4}{2} = 45$
  * $k = 3$: $\frac{1}{3!}\binom{6}{2}\binom{4}{2}\binom{2}{2} = 15$
  
  Total de involuciones: $1 + 15 + 45 + 15 = 76$.
* Pares en el Caso 1: $1 \times 76 = 76$.

#### Caso 2: $g$ tiene un $3$-ciclo y tres puntos fijos, tipo $(3, 1, 1, 1)$
* Número de tales permutaciones $g$: elegimos $3$ elementos de $\binom{6}{3} = 20$ formas y hay $2$ ciclos de longitud $3$ posibles con ellos, dando $20 \times 2 = 40$ elementos $g$.
* Fijemos $g = (1, 2, 3)(4)(5)(6)$, de modo que $g^{-1} = (1, 3, 2)(4)(5)(6)$.
* Para que $pgp^{-1} = g^{-1}$ con $p^2 = e$, la permutación $p$ debe preservar el conjunto $\{1, 2, 3\}$ y el conjunto $\{4, 5, 6\}$:
  * En $\{1, 2, 3\}$, $p$ debe ser una involución que invierta el ciclo $(1, 2, 3)$; las únicas opciones son las $3$ transposiciones $(1,2)$, $(2,3)$ y $(1,3)$.
  * En $\{4, 5, 6\}$, $p$ puede ser cualquier involución de $S_3$; hay $1 + \binom{3}{2} = 4$ opciones.
* Esto da $3 \times 4 = 12$ opciones para $p$ por cada $g$.
* Pares en el Caso 2: $40 \times 12 = 480$.

#### Caso 3: $g$ tiene dos $3$-ciclos disjuntos, tipo $(3, 3)$
* Número de tales permutaciones $g$: hay $\frac{1}{2}\binom{6}{3} = 10$ formas de partir el conjunto en dos bloques de $3$, y $2 \times 2 = 4$ formas de orientar ambos ciclos, dando $10 \times 4 = 40$ elementos $g$.
* Fijemos $g = (1, 2, 3)(4, 5, 6)$, de modo que $g^{-1} = (1, 3, 2)(4, 6, 5)$.
* Como $p^2 = e$ y $pgp^{-1} = g^{-1}$, hay dos subcasos para la acción de $p$ sobre las órbitas $O_1 = \{1, 2, 3\}$ y $O_2 = \{4, 5, 6\}$:
  1. **$p$ preserva cada órbita ($p(O_1) = O_1$ y $p(O_2) = O_2$):** $p$ actúa como una transposición en $O_1$ ($3$ opciones) y como una transposición en $O_2$ ($3$ opciones), dando $3 \times 3 = 9$ opciones.
  2. **$p$ intercambia las dos órbitas ($p(O_1) = O_2$ y $p(O_2) = O_1$):** Como $p^2 = e$, $p$ queda determinada por los valores $(p(1), p(2), p(3))$, que deben formar el ciclo $(4, 6, 5)$. Como el ciclo $(4, 6, 5)$ se puede escribir de $3$ maneras posibles —a saber, $(4, 6, 5)$, $(6, 5, 4)$ y $(5, 4, 6)$—, esto produce exactamente $3$ involuciones: $(1,4)(2,6)(3,5)$, $(1,6)(2,5)(3,4)$ y $(1,5)(2,4)(3,6)$.
* Esto da $9 + 3 = 12$ opciones para $p$ por cada $g$.
* Pares en el Caso 3: $40 \times 12 = 480$.

---

### Paso 3: Suma total

Sumando las soluciones de los tres casos obtenemos:
$$76 + 480 + 480 = 1036.$$

\boxed{1036}