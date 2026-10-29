Para encontrar la suma de todos los dígitos impares que aparecen en los múltiplos positivos de $91$ menores que $1{,}000{,}000$, analicemos la estructura de estos múltiplos.

### Paso 1: Cantidad de múltiplos y representación de 6 dígitos
Notemos que $91 = 7 \times 13$ y que $1001 = 7 \times 11 \times 13 = 91 \times 11$. Por lo tanto:
$$999{,}999 = 999 \times 1001 = 999 \times 11 \times 91 = 10{,}989 \times 91$$

Esto significa que los múltiplos positivos de $91$ menores que $1{,}000{,}000$ son exactamente:
$$91k \quad \text{para } k = 1, 2, \dots, 10{,}989$$

Podemos escribir cada uno de estos $10{,}989$ múltiplos como un número de $6$ dígitos rellenando con ceros a la izquierda (desde $000091$ hasta $999999$). Añadir ceros a la izquierda no afecta la suma ni el conteo de los dígitos impares, ya que el $0$ es par.

### Paso 2: Simetría por rotación cíclica de las posiciones
Si tomamos cualquier número $x$ de $6$ dígitos entre $1$ y $999{,}998$ y rotamos cíclicamente sus dígitos una posición hacia la izquierda, el nuevo número obtenido es congruente con $10x \pmod{999{,}999}$.

Como $91$ divide a $999{,}999$ y $\gcd(10, 91) = 1$, un número $x$ es múltiplo de $91$ si y solo si su rotación cíclica también es múltiplo de $91$ (y para $x = 999{,}999$, su rotación es él mismo). 

Por lo tanto, el conjunto de los $10{,}989$ múltiplos es invariante bajo rotaciones cíclicas de sus $6$ dígitos. Esto implica que **cada una de las $6$ posiciones decimales tiene exactamente la misma distribución de dígitos**.

### Paso 3: Conteo en la posición de las unidades
Dado que todas las posiciones tienen la misma distribución, basta con calcular la suma de los dígitos impares en la posición de las unidades y multiplicar el resultado por $6$.

Para $x = 91k$, como $91 \equiv 1 \pmod{10}$, el dígito de las unidades de $91k$ coincide con el dígito de las unidades de $k$:
$$91k \equiv k \pmod{10}$$

A medida que $k$ recorre los valores del $1$ al $10{,}989$:
- En los primeros $10{,}980$ valores ($1 \le k \le 10{,}980$), hay $1{,}098$ bloques completos de $10$ números, por lo que cada dígito impar $\{1, 3, 5, 7, 9\}$ aparece $1{,}098$ veces en las unidades.
- En los últimos $9$ valores ($10{,}981 \le k \le 10{,}989$), el dígito de las unidades recorre del $1$ al $9$, añadiendo $1$ aparición más de cada dígito impar.

Así, en la posición de las unidades, cada dígito impar aparece exactamente:
$$1{,}098 + 1 = 1{,}099 \text{ veces}$$

### Paso 4: Suma total de los dígitos impares
La suma de los cinco dígitos impares posibles es:
$$1 + 3 + 5 + 7 + 9 = 25$$

En una sola posición decimal, los dígitos impares suman:
$$1{,}099 \times 25 = 27{,}475$$

Multiplicando por las $6$ posiciones decimales, obtenemos la suma total:
$$6 \times 27{,}475 = 164{,}850$$

\boxed{164850}