Para resolver el problema paso a paso, representemos los números de tres dígitos en base 10 algebraicamente:

1. **Planteamiento algebraico:**
   Sea $N = \underline{a}\underline{b}\underline{c} = 100a + 10b + c$ un número de tres dígitos (donde $a \in \{1, \dots, 9\}$ y $b, c \in \{0, \dots, 9\}$), y sea $M = \underline{b}\underline{c}\underline{a} = 100b + 10c + a$ el número resultante de rotar sus dígitos.

   Observemos la relación entre $10N$ y $M$:
   $$10N - M = 10(100a + 10b + c) - (100b + 10c + a) = 1000a + 100b + 10c - 100b - 10c - a = 999a$$

2. **Condición de divisibilidad:**
   Si $N$ es un múltiplo de $x$ (es decir, $x \mid N$), entonces $x \mid 10N$. Como $M = 10N - 999a$, para que $M$ sea también múltiplo de $x$, es necesario y suficiente que $x \mid 999a$ para todo múltiplo de tres dígitos $N$ de $x$.

3. **Análisis para $a = 1$:**
   Dado que $x$ es un entero positivo de dos dígitos ($10 \le x \le 99$), el intervalo $[100, 199]$ contiene exactamente $100$ números enteros consecutivos. Por lo tanto, para cualquier $x \le 99$, siempre existe al menos un múltiplo de $x$ en el rango $[100, 199]$. 
   
   Este múltiplo tiene su primer dígito $a = 1$. Aplicando la condición de divisibilidad a este número en particular, obtenemos que $x$ debe dividir a $999 \cdot 1 = 999$.

   Recíprocamente, si $x \mid 999$, entonces $x \mid 999a$ para cualquier dígito $a$, lo que garantiza que si $x \mid N$, entonces $x \mid (10N - 999a) = M$.

4. **Búsqueda de los valores de $x$:**
   Descomponemos $999$ en sus factores primos:
   $$999 = 9 \times 111 = 27 \times 37 = 3^3 \times 37$$

   Los divisores positivos de $999$ son:
   $$1, 3, 9, 27, 37, 111, 333, 999$$

   De esta lista, los únicos números de dos dígitos son $27$ y $37$.

5. **Suma final:**
   $$27 + 37 = 64$$

\boxed{64}