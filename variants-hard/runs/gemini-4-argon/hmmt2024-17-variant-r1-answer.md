Para hallar el número esperado de celdas que Mira puede alcanzar, podemos analizar la cuadrícula de dimensiones $2 \times \infty$ de manera recursiva.

### 1. Notación y probabilidades de las puertas
Denotemos por $G$ la cuadrícula infinita con columnas $1, 2, 3, \dots$, y sean $u = (1, 1)$ (la celda superior izquierda donde empieza Mira) y $v = (2, 1)$ (la celda inferior izquierda).
- Cada puerta vertical (entre dos celdas de la misma columna) está abierta con probabilidad $p_v = 1 - \frac{1}{4} = \frac{3}{4}$ y cerrada con probabilidad $\frac{1}{4}$.
- Cada puerta horizontal (entre dos celdas adyacentes de la misma fila) está abierta con probabilidad $p_h = 1 - \frac{1}{2} = \frac{1}{2}$ y cerrada con probabilidad $\frac{1}{2}$.

Sea $G'$ la subcuadrícula infinita formada por las columnas $2, 3, 4, \dots$, con vértices izquierdos $u' = (1, 2)$ y $v' = (2, 2)$. Por invarianza por traslación, $G'$ tiene exactamente la misma distribución de probabilidad que $G$, y es independiente del estado de las tres puertas que inciden en la primera columna:
- $e_v$: la puerta vertical entre $u$ y $v$.
- $e_1$: la puerta horizontal entre $u$ y $u'$.
- $e_2$: la puerta horizontal entre $v$ y $v'$.

---

### 2. Probabilidad de que $u$ y $v$ estén conectados
Definamos el evento $A$ como el suceso de que $u$ y $v$ estén en la misma componente conexa de $G$, y sea $B$ el evento complementario (en el que $u$ y $v$ están en componentes conexas disjuntas de $G$). Análogamente, definimos $A'$ y $B'$ para $u'$ y $v'$ en $G'$.

Sea $q = P(A) = P(A')$. Los vértices $u$ y $v$ están conectados en $G$ si y solo si:
1. La puerta vertical $e_v$ está abierta (probabilidad $\frac{3}{4}$), o bien
2. La puerta $e_v$ está cerrada (probabilidad $\frac{1}{4}$), pero ambas puertas horizontales $e_1$ y $e_2$ están abiertas (probabilidad $\frac{1}{2} \cdot \frac{1}{2} = \frac{1}{4}$) y además $u'$ y $v'$ están conectados en $G'$ (probabilidad $q$).

Por lo tanto:
$$q = \frac{3}{4} + \frac{1}{4} \cdot \frac{1}{4} \cdot q = \frac{3}{4} + \frac{1}{16}q$$
Resolviendo para $q$:
$$\frac{15}{16}q = \frac{3}{4} \implies q = \frac{4}{5}, \qquad P(B) = 1 - q = \frac{1}{5}.$$

---

### 3. Ecuaciones recursivas para el tamaño esperado de la componente
Sea $C_G(u)$ la componente conexa de $u$ en $G$, y sean $X = |C_{G'}(u')|$ e $Y = |C_{G'}(v')|$ los tamaños de las componentes conexas de $u'$ y $v'$ en $G'$.
- Si ocurre $A'$, entonces $C_{G'}(u') = C_{G'}(v')$, por lo que $X = Y$ y $|C_{G'}(u') \cup C_{G'}(v')| = X$.
- Si ocurre $B'$, entonces $C_{G'}(u')$ y $C_{G'}(v')$ son disjuntos, por lo que $|C_{G'}(u') \cup C_{G'}(v')| = X + Y$.

Definimos las esperanzas parciales:
$$a = E\left[|C_G(u)| \cdot \mathbf{1}_A\right] = E\left[X \cdot \mathbf{1}_{A'}\right], \qquad b = E\left[|C_G(u)| \cdot \mathbf{1}_B\right] = E\left[X \cdot \mathbf{1}_{B'}\right] = E\left[Y \cdot \mathbf{1}_{B'}\right].$$
El número esperado total de celdas alcanzables desde $u$ es $E[|C_G(u)|] = a + b$.

Analizamos los $8$ casos posibles para el estado de las puertas $(e_v, e_1, e_2)$, donde $1$ indica puerta abierta y $0$ puerta cerrada:

#### Caso 1: $e_v = 1$ (probabilidad $\frac{3}{4}$)
En este caso $u$ y $v$ están directamente conectados, por lo que siempre ocurre el evento $A$ y $\{u, v\} \subseteq C_G(u)$. Cada una de las $4$ configuraciones de $(e_1, e_2)$ tiene probabilidad $\frac{3}{4} \cdot \frac{1}{4} = \frac{3}{16}$:
- $(e_1, e_2) = (0, 0)$: $|C_G(u)| = 2$. Esperanza: $2$.
- $(e_1, e_2) = (1, 0)$: $|C_G(u)| = 2 + X$. Esperanza: $2 + E[X] = 2 + a + b$.
- $(e_1, e_2) = (0, 1)$: $|C_G(u)| = 2 + Y$. Esperanza: $2 + E[Y] = 2 + a + b$.
- $(e_1, e_2) = (1, 1)$: $|C_G(u)| = 2 + X$ en $A'$, y $|C_G(u)| = 2 + X + Y$ en $B'$. Esperanza:
  $$E[(2 + X)\mathbf{1}_{A'} + (2 + X + Y)\mathbf{1}_{B'}] = 2P(A') + a + 2P(B') + 2b = 2 + a + 2b.$$

#### Caso 2: $e_v = 0$ (probabilidad $\frac{1}{4}$)
Cada una de las $4$ configuraciones de $(e_1, e_2)$ tiene probabilidad $\frac{1}{4} \cdot \frac{1}{4} = \frac{1}{16}$:
- $(e_1, e_2) = (0, 0)$: ocurre $B$ y $|C_G(u)| = 1$. Esperanza en $B$: $1$.
- $(e_1, e_2) = (1, 0)$: ocurre $B$ y $|C_G(u)| = 1 + X$. Esperanza en $B$: $1 + a + b$.
- $(e_1, e_2) = (0, 1)$: ocurre $B$ y $|C_G(u)| = 1$. Esperanza en $B$: $1$.
- $(e_1, e_2) = (1, 1)$:
  - Si ocurre $A'$, entonces $u$ y $v$ se conectan a través de $G'$, por lo que ocurre $A$ y $|C_G(u)| = 2 + X$. Su contribución a $a$ es $\frac{1}{16} E[(2 + X)\mathbf{1}_{A'}] = \frac{1}{16}(2q + a)$.
  - Si ocurre $B'$, entonces $u$ y $v$ no se conectan, por lo que ocurre $B$ y $|C_G(u)| = 1 + X$. Su contribución a $b$ es $\frac{1}{16} E[(1 + X)\mathbf{1}_{B'}] = \frac{1}{16}(1 - q + b)$.

---

### 4. Resolución del sistema lineal
Sumando las contribuciones para $a$ y $b$:
$$a = \frac{3}{16}\big(2 + (2 + a + b) + (2 + a + b) + (2 + a + 2b)\big) + \frac{1}{16}(2q + a)$$
$$b = \frac{1}{16}\big(1 + (1 + a + b) + 1 + (1 - q + b)\big)$$

Simplificando la primera ecuación:
$$16a = 3(8 + 3a + 4b) + 2q + a = 24 + 2q + 10a + 12b \implies 6a - 12b = 24 + 2q.$$
Sustituyendo $q = \frac{4}{5}$:
$$3a - 6b = 12 + \frac{4}{5} = \frac{64}{5}.$$

Simplificando la segunda ecuación:
$$16b = 4 - q + a + 2b \implies a = 14b - 4 + q = 14b - \frac{16}{5}.$$

Sustituyendo $a$ en la primera ecuación:
$$3\left(14b - \frac{16}{5}\right) - 6b = \frac{64}{5} \implies 36b = \frac{64 + 48}{5} = \frac{112}{5} \implies b = \frac{112}{180} = \frac{28}{45}.$$

Finalmente, calculamos $a + b$:
$$a + b = 15b - \frac{16}{5} = 15 \cdot \frac{28}{45} - \frac{16}{5} = \frac{28}{3} - \frac{16}{5} = \frac{140 - 48}{15} = \frac{92}{15}.$$

\boxed{\frac{92}{15}}