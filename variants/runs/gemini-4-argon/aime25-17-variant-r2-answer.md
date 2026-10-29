Para encontrar todos los enteros positivos $n$ tales que $n+3$ divide al producto $2(n+5)(n^2+7)$, podemos analizar la expresión módulo $n+3$.

1. **Reducción módulo $n+3$:**
   Sabemos que $n \equiv -3 \pmod{n+3}$. Sustituyendo $n$ por $-3$ en el producto dado:
   $$2(n+5)(n^2+7) \equiv 2(-3+5)((-3)^2+7) \pmod{n+3}$$
   $$2(2)(9+7) = 4 \cdot 16 = 64 \pmod{n+3}$$

   Por lo tanto, $n+3$ divide a $2(n+5)(n^2+7)$ si y solo si $n+3$ divide a $64$.

2. **Encontrar los divisores de $64$:**
   Los divisores positivos de $64 = 2^6$ son:
   $$1, 2, 4, 8, 16, 32, 64$$

3. **Determinar los valores válidos de $n$:**
   Como $n$ debe ser un entero positivo ($n \ge 1$), tenemos que $n+3 \ge 4$.
   Los divisores de $64$ que son mayores o iguales a $4$ son $4, 8, 16, 32$ y $64$. Restando $3$ a cada uno, obtenemos los posibles valores de $n$:
   - $n+3 = 4 \implies n = 1$
   - $n+3 = 8 \implies n = 5$
   - $n+3 = 16 \implies n = 13$
   - $n+3 = 32 \implies n = 29$
   - $n+3 = 64 \implies n = 61$

4. **Calcular la suma:**
   Sumamos todos los valores obtenidos para $n$:
   $$1 + 5 + 13 + 29 + 61 = 109$$

\boxed{109}