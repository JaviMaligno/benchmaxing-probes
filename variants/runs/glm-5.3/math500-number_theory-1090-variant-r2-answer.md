## Solución paso a paso

**Paso 1: Condición para expansión decimal terminante.**

La fracción $1/k$ tiene expansión decimal terminante si y solo si, al reducirse, su denominador solo tiene factores primos $2$ y $5$; es decir, $k$ debe ser de la forma $k = 2^a \cdot 5^b$.

**Paso 2: Restricción a enteros impares.**

Como el entero elegido $k$ es **impar**, debe tener $a = 0$, es decir, $k = 5^b$ con $b \geq 0$.

**Paso 3: Contar los casos favorables.**

Buscamos potencias de $5$ menores que $4000$:
$$5^0 = 1,\quad 5^1 = 5,\quad 5^2 = 25,\quad 5^3 = 125,\quad 5^4 = 625,\quad 5^5 = 3125$$
(pues $5^6 = 15625 > 4000$). Son **6** enteros favorables.

**Paso 4: Total de casos.**

Los enteros positivos impares menores que $4000$ son $1, 3, 5, \dots, 3999$, es decir:
$$\frac{3999+1}{2} = 2000$$
enteros en total.

**Paso 5: Calcular la probabilidad.**

$$\frac{m}{n} = \frac{6}{2000} = \frac{3}{1000}$$

con $\gcd(3, 1000) = 1$, así que $m = 3$ y $n = 1000$.

**Paso 6: Resultado final.**

$$m + n = 3 + 1000 = 1003$$

$$\boxed{1003}$$