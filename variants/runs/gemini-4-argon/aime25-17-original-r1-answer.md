Para encontrar la suma de todos los enteros positivos $n$ tales que $n+2$ divide al producto $3(n+3)(n^2+9)$, podemos utilizar aritmética modular o división algebraica.

1. **Cambio de variable y reducción modular:**
   Sea $k = n+2$. Como $n$ es un entero positivo ($n \ge 1$), tenemos que $k \ge 3$.
   Despejando $n$, obtenemos $n = k - 2$. Sustituimos esto en la expresión $3(n+3)(n^2+9)$ y analizamos su residuo módulo $k$ (es decir, considerando $k \equiv 0 \pmod k$, o equivalentemente $n \equiv -2 \pmod{n+2}$):
   $$3(n+3)(n^2+9) \equiv 3(-2+3)((-2)^2+9) \pmod{n+2}$$
   $$3(1)(4+9) = 3 \cdot 13 = 39 \pmod{n+2}$$

2. **Condición de divisibilidad:**
   Para que $n+2$ divida a $3(n+3)(n^2+9)$, es necesario y suficiente que $n+2$ divida al residuo $39$.

3. **Encontrar los valores de $n$:**
   Los divisores positivos de $39$ son $1, 3, 13$ y $39$.
   Dado que $n \ge 1$, sabemos que $n+2 \ge 3$. Por lo tanto, los posibles valores para $n+2$ son $3, 13$ y $39$:
   - Si $n+2 = 3 \implies n = 1$
   - Si $n+2 = 13 \implies n = 11$
   - Si $n+2 = 39 \implies n = 37$

4. **Suma de las soluciones:**
   Sumamos todos los valores posibles de $n$:
   $$1 + 11 + 37 = 49$$

\boxed{49}