Vamos a resolverlo paso a paso.

Primero, descomponemos $10!$ en factores primos:

Potencias de cada primo en $10!$:

- Para el primo $2$:
  $\left\lfloor \frac{10}{2} \right\rfloor + \left\lfloor \frac{10}{4} \right\rfloor + \left\lfloor \frac{10}{8} \right\rfloor = 5 + 2 + 1 = 8$.

- Para el primo $3$:
  $\left\lfloor \frac{10}{3} \right\rfloor + \left\lfloor \frac{10}{9} \right\rfloor = 3 + 1 = 4$.

- Para el primo $5$:
  $\left\lfloor \frac{10}{5} \right\rfloor = 2$.

- Para el primo $7$:
  $\left\lfloor \frac{10}{7} \right\rfloor = 1$.

Por tanto:
\[
10! = 2^8 \cdot 3^4 \cdot 5^2 \cdot 7.
\]

Queremos valores de $x$ tales que $x^3$ sea un factor *positivo* de $10!$. 
Esto significa que $x^3 \mid 10!$.

Dado que $x$ puede ser positivo o negativo, y ambos dan $x^3$ con el mismo valor absoluto, debemos considerar ambas opciones.

Sea $x = \pm p_1^{a_1} p_2^{a_2} \cdots$. Entonces $x^3$ tiene exponentes $3a_i$ para cada primo. Para que $x^3 \mid 10!$, necesitamos:

- Para el primo $2$: $3a_2 \le 8 \Rightarrow a_2 \le \bigl\lfloor \frac{8}{3} \bigr\rfloor = 2$.
- Para el primo $3$: $3a_3 \le 4 \Rightarrow a_3 \le \bigl\lfloor \frac{4}{3} \bigr\rfloor = 1$.
- Para el primo $5$: $3a_5 \le 2 \Rightarrow a_5 \le 0$.
- Para el primo $7$: $3a_7 \le 1 \Rightarrow a_7 \le 0$.

Es decir, $x$ puede contener a lo sumo $2$ factores de $2$ y $1$ factor de $3$, y ningún factor de $5$ o $7$.

Entonces los posibles valores positivos de $x$ son:
\[
x = 2^{a} 3^{b}, \quad a \in \{0,1,2\},\; b \in \{0,1\}.
\]

Haciendo la cuenta:

- $a=0$: $x = 1, 3$ (2 valores)
- $a=1$: $x = 2, 6$ (2 valores)
- $a=2$: $x = 4, 12$ (2 valores)

Total de valores positivos: $3 \times 2 = 6$.

Como $x$ puede ser positivo o negativo (y $x^3$ es siempre positivo si $x$ es entero), cada valor positivo tiene su contraparte negativa. Por tanto:

Total: $6 \times 2 = 12$.

\[
\boxed{12}
\]