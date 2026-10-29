Para encontrar la probabilidad de que el recíproco de un número entero impar positivo menor que $4000$ tenga una expansión decimal finita (terminante), sigamos estos pasos:

1. **Determinar el número total de casos posibles:**
   Los números enteros impares positivos menores que $4000$ son $1, 3, 5, \dots, 3999$. 
   La cantidad total de estos números es:
   $$\frac{4000}{2} = 2000$$

2. **Determinar el número de casos favorables:**
   El recíproco de un entero positivo $k$, es decir $\frac{1}{k}$, tiene una expansión decimal finita si y solo si los únicos factores primos de $k$ son $2$ y $5$.
   Como estamos eligiendo únicamente números **impares**, $k$ no puede ser divisible por $2$. Por lo tanto, $k$ solo puede tener a $5$ como factor primo, lo que significa que $k$ debe ser una potencia de $5$ ($k = 5^a$ para algún entero $a \ge 0$).

   Listemos las potencias de $5$ que son menores que $4000$:
   - $5^0 = 1$
   - $5^1 = 5$
   - $5^2 = 25$
   - $5^3 = 125$
   - $5^4 = 625$
   - $5^5 = 3125$
   
   La siguiente potencia es $5^6 = 15625$, que supera $4000$. Por lo tanto, hay exactamente $6$ números que cumplen la condición.

3. **Calcular la probabilidad y simplificar:**
   La probabilidad es el cociente entre los casos favorables y los casos posibles:
   $$\frac{6}{2000} = \frac{3}{1000}$$

   Como $3$ y $1000$ son primos relativos ($\text{mcd}(3, 1000) = 1$), tenemos que $m = 3$ y $n = 1000$.

4. **Calcular $m + n$:**
   $$m + n = 3 + 1000 = 1003$$

\boxed{1003}