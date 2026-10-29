Para encontrar el menor valor posible de $a$, primero identificamos los elementos de la serie geométrica:

$$3 + \frac{15}{a} + \frac{75}{a^2} + \cdots$$

1. **Primer término y razón común:**
   El primer término es $t_1 = 3$ y la razón común entre términos consecutivos es:
   $$r = \frac{15/a}{3} = \frac{5}{a}$$

2. **Condición de convergencia:**
   Para que la serie geométrica infinita converja y tenga una suma finita, se debe cumplir que $|r| < 1$. Dado que $a$ es un entero positivo, esto implica que:
   $$0 < \frac{5}{a} < 1 \implies a > 5$$

3. **Fórmula de la suma:**
   La suma $S$ de la serie geométrica infinita está dada por:
   $$S = \frac{t_1}{1 - r} = \frac{3}{1 - \frac{5}{a}} = \frac{3a}{a - 5}$$
   Podemos reescribir esta expresión separando la parte entera:
   $$S = \frac{3(a - 5) + 15}{a - 5} = 3 + \frac{15}{a - 5}$$

4. **Condición de cuadrado perfecto:**
   Como $a$ es un entero mayor que $5$, $a - 5 \ge 1$. Por lo tanto, el valor de la suma cumple:
   $$3 < S \le 3 + \frac{15}{1} = 18$$
   Los únicos cuadrados perfectos enteros en el intervalo $(3, 18]$ son $4, 9$ y $16$. Analizamos cada caso para ver cuál produce un valor entero para $a$:
   - Si $S = 16$: $\quad 3 + \frac{15}{a - 5} = 16 \implies \frac{15}{a - 5} = 13 \implies a = 5 + \frac{15}{13}$ (no es entero).
   - Si $S = 9$: $\quad 3 + \frac{15}{a - 5} = 9 \implies \frac{15}{a - 5} = 6 \implies a = 5 + \frac{5}{2}$ (no es entero).
   - Si $S = 4$: $\quad 3 + \frac{15}{a - 5} = 4 \implies \frac{15}{a - 5} = 1 \implies a - 5 = 15 \implies a = 20$ (es un entero positivo).

Por lo tanto, el único —y menor— valor entero positivo posible para $a$ es $20$.

\boxed{20}