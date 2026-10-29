Para encontrar la suma de todos los enteros positivos $n$ con $60 \leq n \leq 120$ tales que $2n+3$ no divide a $2^{n!}-1$, analizamos la condición de divisibilidad.

### Paso 1: Condición del orden multiplicativo
Sea $m = 2n+3$. Como $60 \leq n \leq 120$, $m$ es un número impar en el intervalo $123 \leq m \leq 243$. En particular, $\operatorname{mcd}(2, m) = 1$.

Sabemos que $m \mid 2^{n!}-1$ si y solo si el orden multiplicativo de $2$ módulo $m$, denotado por $d = \operatorname{ord}_m(2)$, divide a $n!$. Por el teorema de Euler, $d$ divide a $\phi(m)$.

### Paso 2: ¿Cuándo puede $d$ no dividir a $n!$?
Observemos que $\phi(m) \leq m - 1 = 2n+2 = 2(n+1)$. 
Para que $d \nmid n!$, debe existir alguna potencia prima $q^a \parallel d$ tal que $q^a \nmid n!$.
- Si $q \leq n$ y $a = 1$, entonces $q \mid n!$ trivialmente.
- Si $q \leq n$ y $a \geq 2$, como $q^a \mid \phi(m) \leq 242$, tenemos $q \leq \sqrt{242} < 16$. Para $n \geq 60$, el exponente de cualquier primo $q \leq 13$ en $n!$ (dado por la fórmula de Legendre) es al menos $v_{13}(60!) = 4$, mientras que $13^2 = 169 \leq 242 < 13^3$, y de forma análoga para $q \in \{2, 3, 5, 7, 11\}$ se cumple holgadamente que $v_q(n!) \geq a$.

Por lo tanto, $d \nmid n!$ ocurre **si y solo si** $d$ tiene un factor primo $q > n$.

### Paso 3: Reducción a números primos de Sophie Germain
Como $d \mid \phi(m)$ y $\phi(m) \leq 2(n+1)$:
1. Si $m$ es compuesto, para cada potencia prima $p^k \parallel m$ se tiene $\phi(p^k) = p^{k-1}(p-1) < m/2 < n+1$, por lo que ningún factor primo de $d$ puede superar a $n$. Así, si $m$ es compuesto, $m$ siempre divide a $2^{n!}-1$.
2. Si $m = p = 2n+3$ es primo, entonces $d \mid p-1 = 2(n+1)$. El único modo en que $2(n+1)$ tenga un factor primo $q > n$ es que $q = n+1$ sea primo.

Recíprocamente, si $q = n+1$ es primo y $p = 2n+3 = 2q+1$ también es primo, entonces los divisores de $p-1 = 2q$ son $\{1, 2, q, 2q\}$. Como $p \geq 123$, $p$ no divide a $2^1-1 = 1$ ni a $2^2-1 = 3$, de modo que $d = \operatorname{ord}_p(2) \in \{q, 2q\}$. En ambos casos $q \mid d$, y como $q = n+1$ es primo, $q \nmid n!$, lo que implica que $d \nmid n!$ y por ende $p \nmid 2^{n!}-1$.

### Paso 4: Búsqueda de los valores de $n$
El problema se reduce a encontrar todos los $n \in [60, 120]$ tales que $q = n+1 \in [61, 121]$ sea primo y $p = 2q+1$ también sea primo:

- $q = 61 \implies p = 123 = 3 \times 41$ (compuesto)
- $q = 67 \implies p = 135 = 5 \times 27$ (compuesto)
- $q = 71 \implies p = 143 = 11 \times 13$ (compuesto)
- $q = 73 \implies p = 147 = 3 \times 49$ (compuesto)
- $q = 79 \implies p = 159 = 3 \times 53$ (compuesto)
- $q = 83 \implies p = 167$ (**primo**) $\implies n = 82$
- $q = 89 \implies p = 179$ (**primo**) $\implies n = 88$
- $q = 97 \implies p = 195 = 3 \times 65$ (compuesto)
- $q = 101 \implies p = 203 = 7 \times 29$ (compuesto)
- $q = 103 \implies p = 207 = 9 \times 23$ (compuesto)
- $q = 107 \implies p = 215 = 5 \times 43$ (compuesto)
- $q = 109 \implies p = 219 = 3 \times 73$ (compuesto)
- $q = 113 \implies p = 227$ (**primo**) $\implies n = 112$

### Paso 5: Suma final
Los valores válidos de $n$ son $82$, $88$ y $112$. Calculamos su suma:
$$82 + 88 + 112 = 282$$

\boxed{282}