Para encontrar la probabilidad $\frac{a}{b}$, sigamos estos pasos:

1. **Determinar el número total de casos posibles:**
   Los enteros positivos impares menores que $2010$ son $1, 3, 5, \dots, 2009$. 
   La cantidad total de estos números es:
   $$\frac{2010}{2} = 1005$$

2. **Determinar el número de casos favorables:**
   El recíproco de un entero positivo $n$, es decir $\frac{1}{n}$, produce un decimal exacto (terminante) si y solo si los únicos factores primos de $n$ son $2$ y $5$. 
   Dado que $n$ debe ser un número impar, no puede ser divisible por $2$. Por lo tanto, $n$ debe ser una potencia de $5$, es decir, $n = 5^k$ para algún entero $k \ge 0$.

   Enumeramos las potencias de $5$ que son menores que $2010$:
   - $5^0 = 1$
   - $5^1 = 5$
   - $5^2 = 25$
   - $5^3 = 125$
   - $5^4 = 625$
   (La siguiente potencia es $5^5 = 3125$, que supera $2010$).

   Por lo tanto, hay $5$ casos favorables.

3. **Calcular la probabilidad y simplificar:**
   La probabilidad es:
   $$\frac{5}{1005} = \frac{1}{201}$$

   Como $a = 1$ y $b = 201$ son primos relativos, tenemos que:
   $$a + b = 1 + 201 = 202$$

\boxed{202}