Para determinar para cuántos valores de $N$ entre $1$ y $1000$ inclusive tiene éxito el algoritmo voraz (*greedy algorithm*), analicemos cuántas monedas utiliza este algoritmo en comparación con cualquier otra colección óptima de monedas.

### 1. Representación del algoritmo voraz
Cualquier entero positivo $N$ se puede escribir de forma única al dividir por $25$ como:
$$N = 25q + r$$
donde $q = \lfloor N / 25 \rfloor \ge 0$ es el número de monedas de $25$ centavos que elige el algoritmo voraz, y $0 \le r \le 24$ es el resto.

Para formar cualquier cantidad $M$ utilizando únicamente monedas de $10$ y $1$ centavo, la manera óptima (que coincide con la voraz, dado que $1$ divide a $10$) utiliza:
$$f(M) = \lfloor M / 10 \rfloor + (M \bmod 10)$$
monedas. Por lo tanto, el número total de monedas que emplea el algoritmo voraz para $N = 25q + r$ es:
$$G(N) = q + f(r)$$

### 2. Comparación con colecciones alternativas
Cualquier otra colección óptima para formar $N$ centavos utilizará $q - k$ monedas de $25$ centavos (con $0 \le k \le q$) y formará el resto $25k + r$ de manera óptima con monedas de $10$ y $1$ centavo. El número total de monedas para un $k$ dado es:
$$C_k(N) = (q - k) + f(25k + r)$$

Notemos que reemplazar $2$ monedas de $25$ centavos ($50$ centavos) por $5$ monedas de $10$ centavos incrementa el número total de monedas en $5 - 2 = 3$. Algebraicamente, para cualquier $k \ge 2$:
$$C_k(N) = (q - k) + f(50 + 25(k - 2) + r) = (q - k) + 5 + f(25(k - 2) + r) = C_{k-2}(N) + 3 > C_{k-2}(N)$$
Esto demuestra que nunca es óptimo reducir el número de monedas de $25$ centavos en $2$ o más unidades. Así, una colección alternativa supera al algoritmo voraz si y solo si $q \ge 1$ y para $k = 1$ se cumple que $C_1(N) < G(N)$, es decir:
$$q - 1 + f(25 + r) < q + f(r) \iff f(25 + r) \le f(r)$$

### 3. Análisis del resto $r$
Expresemos $r = 10a + b$, donde $a = \lfloor r / 10 \rfloor \in \{0, 1, 2\}$ y $b = r \bmod 10 \in \{0, 1, \dots, 9\}$. Entonces $f(r) = a + b$, y tenemos que $25 + r = 10(a + 2) + (b + 5)$. Dividimos en dos casos según el valor de $b$:

1. **Caso 1: $0 \le b \le 4$.**
   Como $b + 5 \le 9$, el resto al dividir $25 + r$ entre $10$ es $b + 5$, por lo que:
   $$f(25 + r) = (a + 2) + (b + 5) = a + b + 7 = f(r) + 7 > f(r)$$
   En este caso, el algoritmo voraz **siempre tiene éxito**.

2. **Caso 2: $5 \le b \le 9$.**
   Como $b + 5 \ge 10$, podemos reescribir $25 + r = 10(a + 3) + (b - 5)$, donde $0 \le b - 5 \le 4$. Entonces:
   $$f(25 + r) = (a + 3) + (b - 5) = a + b - 2 = f(r) - 2 < f(r)$$
   En este caso, $C_1(N) = G(N) - 3 < G(N)$, por lo que el algoritmo voraz **falla** siempre que $q \ge 1$.

Dado que $0 \le r \le 24$, los valores de $r$ que tienen $b \in \{5, 6, 7, 8, 9\}$ son exactamente $10$:
$$r \in \{5, 6, 7, 8, 9, 15, 16, 17, 18, 19\}$$

### 4. Conteo para $1 \le N \le 1000$
Contemos cuántos valores de $N$ en el rango $1 \le N \le 1000$ hacen que el algoritmo voraz **falle**:
- Para $q = 0$ ($1 \le N \le 24$), no es posible usar monedas de $25$ centavos, por lo que el algoritmo voraz no falla para ningún valor ($0$ fallos).
- Para cada $q \in \{1, 2, \dots, 39\}$ (que cubre $25 \le N \le 999$), el algoritmo voraz falla exactamente para los $10$ valores de $r$ encontrados arriba. Esto nos da $39 \times 10 = 390$ valores donde falla.
- Para $N = 1000$, tenemos $q = 40$ y $r = 0$, por lo que el algoritmo voraz tiene éxito (usa $40$ monedas de $25$ centavos).

Restando el número de fallos del total de enteros entre $1$ y $1000$, obtenemos la cantidad de valores de $N$ para los cuales el algoritmo voraz tiene éxito:
$$1000 - 390 = 610$$

\boxed{610}