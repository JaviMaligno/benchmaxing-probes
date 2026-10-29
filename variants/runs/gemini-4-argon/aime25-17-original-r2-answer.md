Para encontrar todos los enteros positivos $n$ tales que $n+2$ divide al producto $3(n+3)(n^2+9)$, podemos analizar la expresión módulo $n+2$.

1. **Reducir módulo $n+2$:**
   Sabemos que $n+2 \equiv 0 \pmod{n+2}$, por lo que $n \equiv -2 \pmod{n+2}$.
   Sustituyendo $n \equiv -2$ en el producto dado:
   $$3(n+3)(n^2+9) \equiv 3(-2+3)((-2)^2+9) \pmod{n+2}$$
   $$3(n+3)(n^2+9) \equiv 3(1)(4+9) = 3(13) = 39 \pmod{n+2}$$

2. **Encontrar los divisores de $39$:**
   Para que $n+2$ divida a $3(n+3)(n^2+9)$, es necesario y suficiente que $n+2$ divida a $39$.
   Los divisores positivos de $39$ son $1, 3, 13$ y $39$.

3. **Determinar los valores válidos de $n$:**
   Dado que $n$ es un entero positivo ($n \ge 1$), se cumple que $n+2 \ge 3$. Por lo tanto, descartamos el divisor $1$ y nos quedamos con:
   - $n+2 = 3 \implies n = 1$
   - $n+2 = 13 \implies n = 11$
   - $n+2 = 39 \implies n = 37$

4. **Calcular la suma:**
   Sumando todos los valores posibles de $n$:
   $$1 + 11 + 37 = 49$$

\boxed{49}