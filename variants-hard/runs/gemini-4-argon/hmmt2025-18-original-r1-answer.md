Para calcular el valor esperado de la cantidad de valores distintos que quedan después de $t = 100$ segundos, analicemos cómo evolucionan los números en el pizarrón.

### 1. Caracterización de los valores tras $t$ segundos
Sea $a_i^{(0)}$ el valor inicial en la posición $i$ (para $i = 1, 2, \ldots, 2025$, considerando los índices módulo $2025$), y sea $a_i^{(t)}$ el valor en la posición $i$ después de $t$ segundos. 

Como en cada segundo el valor de una posición se reemplaza por el máximo entre sí mismo y sus dos vecinos adyacentes, por inducción se cumple que tras $t$ segundos el valor en la posición $i$ es el máximo de los valores iniciales que se encuentran a distancia a lo sumo $t$ de $i$:
$$a_i^{(t)} = \max_{j \in [i-t,\, i+t]} a_j^{(0)}$$

Dado que los $N = 2025$ números iniciales se eligen de manera uniforme e independiente en el intervalo $[0,1]$, con probabilidad $1$ todos los valores iniciales $a_1^{(0)}, \ldots, a_{2025}^{(0)}$ son distintos entre sí. Por lo tanto, el número de valores distintos que quedan después de $t$ segundos es igual a la cantidad de índices $k \in \{1, \ldots, 2025\}$ tales que $a_k^{(0)}$ aparece al menos una vez en la lista $a_1^{(t)}, \ldots, a_{2025}^{(t)}$.

### 2. Condición de supervivencia de un valor inicial
Para un índice fijo $k$, el valor $a_k^{(0)}$ sobrevive después de $t$ segundos si y solo si existe algún $i$ tal que $a_i^{(t)} = a_k^{(0)}$. Esto ocurre si y solo si existe un intervalo circular de $2t+1$ posiciones consecutivas que contiene a $k$ en el cual $a_k^{(0)}$ es el máximo elemento.

Para $t = 100$, los intervalos que contienen a $k$ abarcan posiciones dentro de $[k-2t, k+2t]$, lo que involucra un total de $4t+1 = 401$ elementos. Como $401 \le 2025$, todas estas posiciones son distintas en el círculo.

Existen exactamente $2t+1$ intervalos de longitud $2t+1$ que contienen la posición $k$:
$$I_m = [k - 2t + m - 1,\, k + m - 1] \quad \text{para } m = 1, 2, \ldots, 2t+1.$$
Sea $E_m$ el evento en el que $a_k^{(0)}$ es el máximo elemento en el intervalo $I_m$. Queremos calcular la probabilidad de la unión $\bigcup_{m=1}^{2t+1} E_m$.

### 3. Cálculo de la probabilidad
Observemos que si $a_k^{(0)}$ es el máximo tanto en $I_m$ como en $I_r$ (con $m < r$), entonces $a_k^{(0)}$ es el máximo en toda la unión $I_m \cup I_r = [k - 2t + m - 1,\, k + r - 1]$, la cual contiene a todos los intervalos intermedios $I_s$ para $m < s < r$. Es decir:
$$E_m \cap E_r \subseteq E_s \quad \text{para todo } m < s < r.$$

Por el principio de inclusión-exclusión (o porque el conjunto de índices $m$ donde ocurre $E_m$ siempre forma un bloque contiguo), la probabilidad de la unión se simplifica únicamente a la suma de las probabilidades de los eventos individuales menos las probabilidades de las intersecciones de eventos consecutivos:
$$\mathbb{P}\left(\bigcup_{m=1}^{2t+1} E_m\right) = \sum_{m=1}^{2t+1} \mathbb{P}(E_m) - \sum_{m=1}^{2t} \mathbb{P}(E_m \cap E_{m+1}).$$

- Cada $I_m$ consta de $2t+1$ variables aleatorias independientes e idénticamente distribuidas, por lo que la probabilidad de que $a_k^{(0)}$ sea el máximo en $I_m$ es:
  $$\mathbb{P}(E_m) = \frac{1}{2t+1}.$$
- El evento $E_m \cap E_{m+1}$ equivale a que $a_k^{(0)}$ sea el máximo en $I_m \cup I_{m+1}$, que es un intervalo de $2t+2$ variables independientes e idénticamente distribuidas. Por tanto:
  $$\mathbb{P}(E_m \cap E_{m+1}) = \frac{1}{2t+2}.$$

Sustituyendo estos valores obtenemos:
$$\mathbb{P}\left(\bigcup_{m=1}^{2t+1} E_m\right) = (2t+1)\cdot\frac{1}{2t+1} - 2t\cdot\frac{1}{2t+2} = 1 - \frac{2t}{2t+2} = 1 - \frac{t}{t+1} = \frac{1}{t+1}.$$

### 4. Valor esperado
Por linealidad de la esperanza, el número esperado de valores distintos que quedan después de $t = 100$ segundos es:
$$\mathbb{E}[\text{valores distintos}] = \sum_{k=1}^{2025} \mathbb{P}(a_k^{(0)} \text{ sobrevive}) = 2025 \cdot \frac{1}{100 + 1} = \frac{2025}{101}.$$

\boxed{\frac{2025}{101}}