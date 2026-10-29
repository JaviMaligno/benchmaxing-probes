Para encontrar el número total de formas de llenar la cuadrícula de $3 \times 9$, podemos analizar el problema por bloques de $3 \times 3$ de izquierda a derecha.

**Paso 1: Llenar el primer bloque de $3 \times 3$**
El primer bloque de $3 \times 3$ contiene los números del $1$ al $9$ sin repeticiones. El número de formas de colocar los $9$ números en estas $9$ celdas es:
$$9!$$

Sea $A$ el conjunto de los $3$ números que quedaron en la primera fila de este primer bloque, $B$ el conjunto de los $3$ números en la segunda fila, y $C$ el conjunto de los $3$ números en la tercera fila. Notemos que $A$, $B$ y $C$ son disjuntos y su unión es $\{1, 2, \dots, 9\}$.

**Paso 2: Elegir los conjuntos de números para las filas del segundo y tercer bloque**
En el segundo bloque de $3 \times 3$, llamemos $S_1, S_2, S_3$ a los conjuntos de $3$ números que se colocan en la primera, segunda y tercera fila, respectivamente. De manera análoga, sean $T_1, T_2, T_3$ los conjuntos de $3$ números en las filas del tercer bloque.

Para que las filas no tengan números repetidos y cada bloque contenga los números del $1$ al $9$, se debe cumplir que:
1. $S_1, S_2, S_3$ formen una partición de $\{1, 2, \dots, 9\}$ con $|S_1| = |S_2| = |S_3| = 3$.
2. $S_1 \cap A = \emptyset$, $S_2 \cap B = \emptyset$, y $S_3 \cap C = \emptyset$.

Una vez elegidos $S_1, S_2, S_3$ cumpliendo estas condiciones, los conjuntos del tercer bloque quedan unívocamente determinados por $T_1 = \{1,\dots,9\} \setminus (A \cup S_1)$, $T_2 = \{1,\dots,9\} \setminus (B \cup S_2)$, y $T_3 = \{1,\dots,9\} \setminus (C \cup S_3)$. Además, dado que cada elemento de $\{1, \dots, 9\}$ aparece exactamente una vez en $\{A, B, C\}$ y exactamente una vez en $\{S_1, S_2, S_3\}$ en filas distintas, automáticamente aparecerá exactamente una vez en $\{T_1, T_2, T_3\}$, garantizando que el tercer bloque también contenga los $9$ números distintos.

Contemos cuántas formas hay de formar $S_1, S_2, S_3$:
- Como $S_1 \cap A = \emptyset$, los $3$ elementos de $S_1$ deben provenir de $B \cup C$.
- Sea $k = |S_1 \cap B|$ el número de elementos de $B$ que van a $S_1$, donde $0 \le k \le 3$. Entonces, los otros $3 - k$ elementos de $S_1$ deben provenir de $C$, es decir, $|S_1 \cap C| = 3 - k$.
- Como $S_2 \cap B = \emptyset$, los restantes $3 - k$ elementos de $B$ deben ir forzosamente a $S_3$.
- Como $|S_3| = 3$ y $S_3 \subset A \cup B$, $S_3$ debe contener exactamente $k$ elementos de $A$.
- Los restantes $3 - k$ elementos de $A$ y los restantes $k$ elementos de $C$ deben ir a $S_2$.

Para un valor fijo de $k \in \{0, 1, 2, 3\}$, debemos elegir $k$ elementos de $A$ (para $S_3$), $k$ elementos de $B$ (para $S_1$) y $k$ elementos de $C$ (para $S_2$). El número de maneras de hacer esto es $\binom{3}{k} \cdot \binom{3}{k} \cdot \binom{3}{k} = \binom{3}{k}^3$. Sumando sobre todos los posibles valores de $k$:
$$\sum_{k=0}^{3} \binom{3}{k}^3 = \binom{3}{0}^3 + \binom{3}{1}^3 + \binom{3}{2}^3 + \binom{3}{3}^3 = 1^3 + 3^3 + 3^3 + 1^3 = 1 + 27 + 27 + 1 = 56$$

**Paso 3: Permutar los números dentro de las filas del segundo y tercer bloque**
Una vez determinados los conjuntos de $3$ números para cada una de las $3$ filas del segundo bloque y las $3$ filas del tercer bloque (un total de $6$ subfilas de $3$ celdas), podemos ordenar los $3$ números dentro de cada subfila de $3! = 6$ maneras. Esto nos da:
$$(3!)^6 = 6^6 \text{ formas.}$$

**Paso 4: Factorización prima del total**
Multiplicando todos los factores obtenidos, el número total de formas de llenar la cuadrícula es:
$$\text{Total} = 9! \cdot 56 \cdot (3!)^6$$

Descomponemos cada término en sus factores primos:
- $9! = 9 \cdot 8 \cdot 7 \cdot 6 \cdot 5 \cdot 4 \cdot 3 \cdot 2 \cdot 1 = 2^7 \cdot 3^4 \cdot 5^1 \cdot 7^1$
- $56 = 8 \cdot 7 = 2^3 \cdot 7^1$
- $(3!)^6 = 6^6 = 2^6 \cdot 3^6$

Agrupando los factores primos:
$$\text{Total} = 2^{7+3+6} \cdot 3^{4+6} \cdot 5^1 \cdot 7^{1+1} = 2^{16} \cdot 3^{10} \cdot 5^1 \cdot 7^2$$

Identificando con la expresión $p^a \cdot q^b \cdot r^c \cdot s^d$, tenemos las parejas $(2, 16)$, $(3, 10)$, $(5, 1)$ y $(7, 2)$. Por lo tanto:
$$p \cdot a + q \cdot b + r \cdot c + s \cdot d = 2 \cdot 16 + 3 \cdot 10 + 5 \cdot 1 + 7 \cdot 2 = 32 + 30 + 5 + 14 = 81$$

\boxed{81}