**Paso 1: Contar los enteros positivos impares menores que 4000.**

Los impares positivos menores que 4000 son 1, 3, 5, …, 3999. Su cantidad es:
$$\frac{3999 + 1}{2} = 2000$$

**Paso 2: Condición para que $1/k$ tenga expansión decimal terminante.**

Una fracción tiene expansión decimal terminante si y solo si su denominador (en forma reducida) no tiene factores primos distintos de 2 y 5. Como $k$ es impar, el factor 2 está excluido, así que $k$ debe ser de la forma $5^a$.

**Paso 3: Contar las potencias de 5 impares menores que 4000.**

$$5^0 = 1,\quad 5^1 = 5,\quad 5^2 = 25,\quad 5^3 = 125,\quad 5^4 = 625,\quad 5^5 = 3125$$

y $5^6 = 15625 > 4000$. Hay **6** valores válidos.

**Paso 4: Calcular la probabilidad.**

$$\frac{6}{2000} = \frac{3}{1000}$$

con $m = 3$ y $n = 1000$ relativamente primos. Por lo tanto:

$$m + n = 3 + 1000 = 1003$$

\boxed{1003}