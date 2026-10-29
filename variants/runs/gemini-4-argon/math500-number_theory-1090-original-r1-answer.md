Para resolver este problema paso a paso:

1. **Determinar el número total de casos posibles:**
   Los enteros positivos impares menores que $2010$ son $1, 3, 5, \dots, 2009$. 
   La cantidad total de estos números es:
   $$\frac{2010}{2} = 1005$$

2. **Determinar la condición para obtener un decimal exacto (finito):**
   El recíproco de un número entero positivo $n$, es decir $\frac{1}{n}$, produce un decimal finito si y solo si los únicos factores primos de $n$ son $2$ y $5$.
   Dado que $n$ debe ser un número impar, no puede ser divisible por $2$. Por lo tanto, los únicos factores primos posibles de $n$ son el $5$, lo que significa que $n$ debe ser una potencia de $5$ de la forma $n = 5^k$ con $k \ge 0$.

3. **Contar los casos favorables:**
   Listamos las potencias de $5$ que son menores que $2010$:
   - $5^0 = 1$
   - $5^1 = 5$
   - $5^2 = 25$
   - $5^3 = 125$
   - $5^4 = 625$
   
   Como $5^5 = 3125 > 2010$, solo hay $5$ valores posibles para $n$.

4. **Calcular la probabilidad $\frac{a}{b}$:**
   La probabilidad es el número de casos favorables dividido entre el número total de casos:
   $$\frac{a}{b} = \frac{5}{1005} = \frac{1}{201}$$

5. **Calcular $a + b$:**
   Como $a = 1$ y $b = 201$ son enteros positivos coprimos entre sí, tenemos que:
   $$a + b = 1 + 201 = 202$$

\boxed{202}