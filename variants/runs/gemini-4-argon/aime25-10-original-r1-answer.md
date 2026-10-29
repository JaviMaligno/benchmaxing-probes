Para determinar de cuántas maneras diferentes se puede llenar la cuadrícula de $3 \times 9$, podemos analizar la estructura por bloques de $3 \times 3$ (las columnas $1\text{--}3$, $4\text{--}6$ y $7\text{--}9$).

### Paso 1: Llenar el primer bloque de $3 \times 3$
El primer bloque de $3 \times 3$ debe contener los números del $1$ al $9$ sin repetir. Como no hay restricciones adicionales dentro de este bloque por sí solo, hay exactamente:
$$9!$$
maneras de llenarlo. 

Sean $A$, $B$ y $C$ los conjuntos de $3$ números que quedaron en la primera, segunda y tercera fila de este primer bloque, respectivamente. Así, $\{A, B, C\}$ forma una partición de $\{1, 2, \dots, 9\}$ en tres conjuntos de tamaño $3$.

### Paso 2: Elegir los conjuntos de números para el segundo y tercer bloque
En cada fila $i \in \{1, 2, 3\}$, el segundo bloque contiene un subconjunto $S_{i,2}$ de $3$ números y el tercer bloque contiene un subconjunto $S_{i,3}$ de $3$ números.

Para que cada fila tenga los $9$ números distintos y cada bloque tenga los $9$ números distintos:
1. $S_{1,2} \cap A = \emptyset$, $S_{2,2} \cap B = \emptyset$ y $S_{3,2} \cap C = \emptyset$.
2. $\{S_{1,2}, S_{2,2}, S_{3,2}\}$ debe ser una partición de $\{1, 2, \dots, 9\}$ en tres conjuntos de tamaño $3$.
3. Una vez elegidos $S_{1,2}, S_{2,2}, S_{3,2}$ cumpliendo lo anterior, los conjuntos del tercer bloque quedan determinados de forma única como $S_{1,3} = \{1,\dots,9\} \setminus (A \cup S_{1,2})$, $S_{2,3} = \{1,\dots,9\} \setminus (B \cup S_{2,2})$ y $S_{3,3} = \{1,\dots,9\} \setminus (C \cup S_{3,2})$. Además, dado que cada elemento $x \in \{1,\dots,9\}$ aparece en dos filas distintas entre los primeros dos bloques, automáticamente aparece en la fila restante en el tercer bloque, por lo que el tercer bloque contendrá también los $9$ números distintos.

Contemos de cuántas maneras se pueden formar los conjuntos $S_{1,2}, S_{2,2}, S_{3,2}$:
- Como $S_{1,2} \cap A = \emptyset$, $S_{1,2}$ solo puede contener elementos de $B$ y $C$. Supongamos que $S_{1,2}$ toma $k$ elementos de $B$ (donde $0 \le k \le 3$); entonces debe tomar $3-k$ elementos de $C$.
- Como $S_{2,2} \cap B = \emptyset$, los $3-k$ elementos restantes de $B$ deben ir forzosamente a $S_{3,2}$.
- Como $S_{3,2} \cap C = \emptyset$, los $k$ elementos restantes de $C$ deben ir forzosamente a $S_{2,2}$.
- Finalmente, para completar $3$ elementos en $S_{2,2}$, debemos elegir $3-k$ elementos de $A$, y los $k$ elementos restantes de $A$ irán a $S_{3,2}$.

Para un valor fijo de $k$, el número de formas de hacer estas elecciones independientes de elementos de $B$, $C$ y $A$ es:
$$\binom{3}{k} \cdot \binom{3}{3-k} \cdot \binom{3}{3-k} = \binom{3}{k}^3$$

Sumando sobre todos los valores posibles de $k \in \{0, 1, 2, 3\}$:
$$\sum_{k=0}^{3} \binom{3}{k}^3 = 1^3 + 3^3 + 3^3 + 1^3 = 1 + 27 + 27 + 1 = 56$$

### Paso 3: Ordenar los números dentro del segundo y tercer bloque
Una vez determinados los conjuntos $S_{i,2}$ y $S_{i,3}$ para las $3$ filas en los bloques segundo y tercero (un total de $6$ subfilas de $3$ celdas cada una), los $3$ números dentro de cada subfila se pueden permutar de $3! = 6$ maneras posibles. Esto aporta un factor de:
$$(3!)^6 = 6^6$$

### Paso 4: Factorización prima del total
Multiplicando todos los factores, el número total de maneras de llenar la cuadrícula es:
$$9! \cdot 6^6 \cdot 56$$

Descomponemos cada factor en números primos:
- $9! = 2^7 \cdot 3^4 \cdot 5^1 \cdot 7^1$
- $6^6 = 2^6 \cdot 3^6$
- $56 = 2^3 \cdot 7^1$

Multiplicando las descomposiciones obtenemos:
$$(2^7 \cdot 3^4 \cdot 5^1 \cdot 7^1) \cdot (2^6 \cdot 3^6) \cdot (2^3 \cdot 7^1) = 2^{16} \cdot 3^{10} \cdot 5^1 \cdot 7^2$$

Identificando con la expresión $p^a \cdot q^b \cdot r^c \cdot s^d$, tenemos:
$$p \cdot a + q \cdot b + r \cdot c + s \cdot d = 2 \cdot 16 + 3 \cdot 10 + 5 \cdot 1 + 7 \cdot 2 = 32 + 30 + 5 + 14 = 81$$

\boxed{81}