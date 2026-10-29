Para encontrar el valor de $m+n$, calculemos primero la suma de los números en cada una de las tablas.

**1. Suma de la tabla de Priya ($S_P$):**
La tabla de Priya contiene todos los números enteros consecutivos desde $1$ hasta $mn$. La suma de estos números es:
$$S_P = \sum_{k=1}^{mn} k = \frac{mn(mn+1)}{2}$$

**2. Suma de la tabla de Tomas ($S_T$):**
La tabla de Tomas tiene el valor $ij$ en la fila $i$ y la columna $j$, para $1 \le i \le m$ y $1 \le j \le n$. La suma de todos sus elementos se puede factorizar como el producto de las sumas de las filas y las columnas:
$$S_T = \sum_{i=1}^m \sum_{j=1}^n ij = \left(\sum_{i=1}^m i\right)\left(\sum_{j=1}^n j\right) = \frac{m(m+1)}{2} \cdot \frac{n(n+1)}{2} = \frac{mn(m+1)(n+1)}{4}$$

**3. Diferencia entre las dos sumas:**
Restamos ambas cantidades:
$$S_P - S_T = \frac{mn(mn+1)}{2} - \frac{mn(m+1)(n+1)}{4}$$
$$S_P - S_T = \frac{mn}{4} \left[ 2(mn+1) - (mn + m + n + 1) \right]$$
$$S_P - S_T = \frac{mn(mn - m - n + 1)}{4} = \frac{mn(m-1)(n-1)}{4}$$

Como $m$ y $n$ son enteros positivos, $S_P \ge S_T$, y sabemos que esta diferencia es igual a $2100$:
$$\frac{m(m-1)}{2} \cdot \frac{n(n-1)}{2} = 2100$$

Esto significa que el producto de dos números triangulares, $T_{m-1} = \binom{m}{2}$ y $T_{n-1} = \binom{n}{2}$, es igual a $2100$.

**4. Búsqueda de $m$ y $n$:**
Listamos los primeros números triangulares $T_k = \frac{k(k+1)}{2}$ que dividen a $2100 = 2^2 \cdot 3 \cdot 5^2 \cdot 7$:
- $T_1 = 1 \implies 2100 / 1 = 2100$ (no es triangular)
- $T_2 = 3 \implies 2100 / 3 = 700$ (no es triangular)
- $T_3 = 6 \implies 2100 / 6 = 350$ (no es triangular)
- $T_4 = 10 \implies 2100 / 10 = 210$

Verificamos si $210$ es un número triangular:
$$\frac{k(k+1)}{2} = 210 \implies k(k+1) = 420 \implies k = 20$$
En efecto, $T_{20} = \frac{20 \cdot 21}{2} = 210$.

Por simetría, el conjunto $\{m-1, n-1\}$ es $\{4, 20\}$, lo que implica que $\{m, n\} = \{5, 21\}$.

Finalmente, calculamos $m+n$:
$$m + n = 5 + 21 = 26$$

\boxed{26}