**Paso 1: Identificar el espacio muestral.**

Los enteros positivos impares menores que 2010 son: 1, 3, 5, ..., 2009. Su cantidad es:
$$\frac{2009 - 1}{2} + 1 = \frac{2008}{2} + 1 = 1004 + 1 = 1005$$

**Paso 2: Condición para que $1/n$ sea un decimal terminante.**

Un decimal termina si y solo si, en fracción reducida, el denominador solo tiene factores primos 2 y/o 5. Como $n$ es impar, el factor 2 está excluido, así que $n$ solo puede tener el primo 5. Es decir, $n$ debe ser una potencia de 5 (incluyendo $5^0 = 1$).

**Paso 3: Contar los casos favorables.**

Potencias de 5 menores que 2010:
$$5^0 = 1,\quad 5^1 = 5,\quad 5^2 = 25,\quad 5^3 = 125,\quad 5^4 = 625$$
($5^5 = 3125 > 2009$, se descarta). Hay **5** casos favorables.

**Paso 4: Calcular la probabilidad y simplificar.**

$$\frac{a}{b} = \frac{5}{1005} = \frac{1}{201}$$

Como $1$ y $201$ son relativamente primos, $a = 1$ y $b = 201$.

**Paso 5: Resultado final.**

$$a + b = 1 + 201 = 202$$

$$\boxed{202}$$