Para resolver este problema paso a paso, primero determinamos el espacio muestral y luego contamos los casos favorables.

**Paso 1: Calcular el número total de casos posibles**
Se elige al azar un número entero positivo e impar menor que $4000$. Los enteros positivos impares menores que $4000$ son $1, 3, 5, \dots, 3999$. 
La cantidad total de tales números es:
$$\frac{4000}{2} = 2000$$

**Paso 2: Determinar la condición para una expansión decimal finita**
El recíproco de un número entero positivo $k$, es decir $\frac{1}{k}$, tiene una expansión decimal finita (terminante) si y solo si los únicos factores primos de $k$ son $2$ y $5$, ya que la base de nuestro sistema numérico es $10 = 2 \cdot 5$.

Dado que el número elegido $k$ debe ser impar, no puede ser divisible por $2$. Por lo tanto, $k$ solo puede tener a $5$ como factor primo; es decir, $k$ debe ser de la forma $5^a$ para algún número entero no negativo $a$.

**Paso 3: Contar los casos favorables**
Listamos las potencias de $5$ que son menores que $4000$:
- $5^0 = 1$
- $5^1 = 5$
- $5^2 = 25$
- $5^3 = 125$
- $5^4 = 625$
- $5^5 = 3125$
- $5^6 = 15625$ (que es mayor que $4000$)

Hay exactamente $6$ enteros impares positivos menores que $4000$ cuyo recíproco tiene una expansión decimal finita.

**Paso 4: Calcular la probabilidad y hallar $m+n$**
La probabilidad es el cociente entre los casos favorables y los casos posibles:
$$\frac{6}{2000} = \frac{3}{1000}$$

Como $3$ y $1000$ son primos relativos ($\text{mcd}(3, 1000) = 1$), tenemos que $m = 3$ y $n = 1000$.

Finalmente, sumamos $m$ y $n$:
$$m + n = 3 + 1000 = 1003$$

\boxed{1003}