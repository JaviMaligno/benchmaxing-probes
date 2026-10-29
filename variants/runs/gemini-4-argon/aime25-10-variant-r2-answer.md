Para encontrar el número de formas diferentes de llenar la cuadrícula de $3 \times 6$, analicemos las restricciones por pares de celdas.

### Paso 1: Separar conjuntos y el orden interno
En cada fila $i \in \{1, 2, 3\}$ y cada bloque de $3 \times 2$ denotado por $j \in \{1, 2, 3\}$, la intersección de la fila $i$ con el bloque $j$ consiste en un par de celdas adyacentes. Sea $S_{i,j} \subset \{1, 2, 3, 4, 5, 6\}$ el conjunto de $2$ números ubicados en ese par de celdas.

Las condiciones del problema dependen únicamente de los conjuntos $S_{i,j}$ y no del orden de los dos números dentro de cada par:
1. Cada fila $i$ contiene los $6$ números si y solo si $S_{i,1}, S_{i,2}, S_{i,3}$ forman una partición de $\{1, 2, 3, 4, 5, 6\}$ en tres conjuntos de tamaño $2$.
2. Cada bloque $j$ contiene los $6$ números si y solo si $S_{1,j}, S_{2,j}, S_{3,j}$ forman una partición de $\{1, 2, 3, 4, 5, 6\}$ en tres conjuntos de tamaño $2$.

Una vez elegidos los $9$ conjuntos $S_{i,j}$ (para $1 \le i, j \le 3$), los $2$ números dentro de cada uno de los $9$ pares de celdas se pueden ordenar de $2! = 2$ maneras de forma independiente. Esto aporta un factor de $2^9$ por cada configuración válida de conjuntos $S_{i,j}$.

---

### Paso 2: Contar las configuraciones de conjuntos $S_{i,j}$
1. **Primera fila ($i = 1$):**
   El número de formas de partir $\{1, 2, 3, 4, 5, 6\}$ en tres conjuntos ordenados $(S_{1,1}, S_{1,2}, S_{1,3})$ de tamaño $2$ cada uno es:
   $$\frac{6!}{2!\,2!\,2!} = \frac{720}{8} = 90.$$

2. **Segunda y tercera fila ($i = 2, 3$):**
   Fijemos una partición para la primera fila; sin pérdida de generalidad, supongamos que:
   $$S_{1,1} = \{1, 2\}, \quad S_{1,2} = \{3, 4\}, \quad S_{1,3} = \{5, 6\}.$$
   Para que cada bloque $j$ contenga números distintos, debemos tener $S_{2,j} \cap S_{1,j} = \emptyset$, y una vez elegidos $S_{2,1}, S_{2,2}, S_{2,3}$ como una partición de $\{1, \dots, 6\}$, los conjuntos de la tercera fila quedan unívocamente determinados por $S_{3,j} = \{1, \dots, 6\} \setminus (S_{1,j} \cup S_{2,j})$.

   Contemos de cuántas maneras podemos formar $(S_{2,1}, S_{2,2}, S_{2,3})$:
   Sea $k = |S_{2,1} \cap S_{1,2}| = |S_{2,1} \cap \{3, 4\}|$, donde $k \in \{0, 1, 2\}$.
   - Como $|S_{2,1}| = 2$ y $S_{2,1} \cap \{1, 2\} = \emptyset$, $S_{2,1}$ debe contener $k$ elementos de $\{3, 4\}$ y $2 - k$ elementos de $\{5, 6\}$.
   - Los restantes $2 - k$ elementos de $\{3, 4\}$ no pueden ir a $S_{2,2}$, por lo que deben ir a $S_{2,3}$.
   - Los restantes $k$ elementos de $\{5, 6\}$ no pueden ir a $S_{2,3}$, por lo que deben ir a $S_{2,2}$.
   - Finalmente, como $|S_{2,2}| = 2$, $S_{2,2}$ debe tomar $2 - k$ elementos de $\{1, 2\}$, y los restantes $k$ elementos de $\{1, 2\}$ van a $S_{2,3}$.

   Por lo tanto, para cada $k \in \{0, 1, 2\}$, el número de maneras de elegir qué elementos de $\{1, 2\}$, $\{3, 4\}$ y $\{5, 6\}$ van a cada conjunto es:
   $$\binom{2}{k} \cdot \binom{2}{2-k} \cdot \binom{2}{2-k} = \binom{2}{k}^3.$$
   Sumando sobre todos los valores posibles de $k$:
   $$\binom{2}{0}^3 + \binom{2}{1}^3 + \binom{2}{2}^3 = 1^3 + 2^3 + 1^3 = 1 + 8 + 1 = 10.$$

Así, el número total de matrices de conjuntos $S_{i,j}$ es:
$$N = 90 \times 10 = 900.$$

---

### Paso 3: Factorización prima y cálculo final
Multiplicando por las $2^9$ formas de ordenar los elementos dentro de cada par de celdas, el número total de formas de llenar la cuadrícula es:
$$2^9 \cdot 900 = 2^9 \cdot (2^2 \cdot 3^2 \cdot 5^2) = 2^{11} \cdot 3^2 \cdot 5^2.$$

Identificando los primos $p, q, r$ y sus respectivos exponentes $a, b, c$:
- $p = 2, \quad a = 11$
- $q = 3, \quad b = 2$
- $r = 5, \quad c = 2$

Calculamos $p \cdot a + q \cdot b + r \cdot c$:
$$2 \cdot 11 + 3 \cdot 2 + 5 \cdot 2 = 22 + 6 + 10 = 38.$$

\boxed{38}