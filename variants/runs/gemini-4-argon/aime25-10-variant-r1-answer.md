Para determinar el número de formas diferentes de llenar la cuadrícula de $3 \times 6$, podemos dividir el problema en dos etapas: primero elegir qué par de números va en cada sub-bloque de $1 \times 2$ (la intersección de una fila con un bloque de $3 \times 2$), y luego ordenar los dos números dentro de cada uno de estos pares.

### Paso 1: Estructura de los pares de celdas
La cuadrícula tiene $3$ filas y $3$ bloques de $3 \times 2$, lo que forma una matriz de $3 \times 3$ pares de celdas de dimensión $1 \times 2$. Sea $A_{i,j}$ el conjunto de $2$ números que se colocan en la fila $i$ y el bloque $j$ (para $1 \le i, j \le 3$).

Las condiciones del problema equivalen a que:
1. En cada fila $i$, los conjuntos $A_{i,1}, A_{i,2}, A_{i,3}$ forman una partición de $\{1, 2, 3, 4, 5, 6\}$ en tres conjuntos de tamaño $2$.
2. En cada bloque $j$, los conjuntos $A_{1,j}, A_{2,j}, A_{3,j}$ también forman una partición de $\{1, 2, 3, 4, 5, 6\}$ en tres conjuntos de tamaño $2$.

### Paso 2: Elección de los conjuntos en cada fila
- **Primera fila:** 
  El número de formas de partir el conjunto $\{1, 2, 3, 4, 5, 6\}$ en tres conjuntos ordenados de tamaño $2$ ($A_{1,1}, A_{1,2}, A_{1,3}$) es:
  $$\binom{6}{2}\binom{4}{2}\binom{2}{2} = \frac{6!}{2!2!2!} = \frac{720}{8} = 90$$

- **Segunda fila:**
  Sin pérdida de generalidad, supongamos que en la primera fila hemos elegido $A_{1,1} = \{1, 2\}$, $A_{1,2} = \{3, 4\}$ y $A_{1,3} = \{5, 6\}$. Para la segunda fila, necesitamos elegir una partición $(A_{2,1}, A_{2,2}, A_{2,3})$ tal que $A_{2,j} \cap A_{1,j} = \emptyset$ para todo $j \in \{1, 2, 3\}$. Analizamos dónde pueden ubicarse los elementos $\{1, 2\}$ en la segunda fila (como no pueden estar en $A_{2,1}$, deben ir a $A_{2,2} \cup A_{2,3}$):
  - **Caso 1:** Los números $1$ y $2$ van juntos al mismo conjunto. 
    Si $A_{2,2} = \{1, 2\}$, entonces $\{5, 6\}$ no puede ir a $A_{2,3}$, por lo que forzosamente $A_{2,1} = \{5, 6\}$ y $A_{2,3} = \{3, 4\}$. Análogamente, si $A_{2,3} = \{1, 2\}$, entonces $A_{2,1} = \{3, 4\}$ y $A_{2,2} = \{5, 6\}$. Esto nos da **$2$ formas**.
  - **Caso 2:** Los números $1$ y $2$ se separan (uno en $A_{2,2}$ y otro en $A_{2,3}$).
    En este caso, para completar los conjuntos sin repetir elementos en ningún bloque, cada uno de los pares $\{1, 2\}$, $\{3, 4\}$ y $\{5, 6\}$ debe enviar exactamente un elemento a cada uno de los otros dos bloques distintos del suyo. Como hay $2$ opciones para dividir $\{1, 2\}$, $2$ opciones para dividir $\{3, 4\}$ y $2$ opciones para dividir $\{5, 6\}$, esto nos da $2 \times 2 \times 2 = \mathbf{8}$ **formas**.
  
  En total, para cualquier elección de la primera fila, hay $2 + 8 = 10$ formas de elegir los conjuntos de la segunda fila.

- **Tercera fila:**
  Una vez fijados los conjuntos de la primera y segunda fila, en cada bloque $j$ el conjunto $A_{3,j}$ queda determinado de manera única como los dos números restantes: $A_{3,j} = \{1, 2, 3, 4, 5, 6\} \setminus (A_{1,j} \cup A_{2,j})$. Como cada número del $1$ al $6$ aparece en dos bloques distintos en las dos primeras filas, aparecerá exactamente en el bloque restante en la tercera fila, garantizando automáticamente que la tercera fila contiene los $6$ números sin repetición. Por lo tanto, hay **$1$ sola forma** para los conjuntos de la tercera fila.

### Paso 3: Ordenamiento interno y conteo total
Una vez definidos los $9$ conjuntos $A_{i,j}$ de tamaño $2$, los dos números dentro de cada par de celdas se pueden ordenar de $2! = 2$ maneras independientemente. Como hay $9$ pares de celdas, esto aporta un factor de $2^9$.

Multiplicando todas las opciones posibles, obtenemos el número total de cuadrículas válidas:
$$\text{Total} = 90 \times 10 \times 1 \times 2^9 = 900 \times 2^9$$

Descomponemos este número en sus factores primos:
$$900 \times 2^9 = (2^2 \cdot 3^2 \cdot 5^2) \cdot 2^9 = 2^{11} \cdot 3^2 \cdot 5^2$$

Identificando con la expresión $p^a \cdot q^b \cdot r^c$, tenemos los primos $p = 2$, $q = 3$, $r = 5$ con exponentes $a = 11$, $b = 2$, $c = 2$. Calculamos el valor pedido:
$$p \cdot a + q \cdot b + r \cdot c = (2 \cdot 11) + (3 \cdot 2) + (5 \cdot 2) = 22 + 6 + 10 = 38$$

\boxed{38}