Para encontrar el valor de la suma, primero determinamos la función generatriz de la sucesión $a_n$. 

Por definición, $a_0 = 1$ (la suma vacía) y para todo $n \ge 1$, cada representación de $n$ como suma ordenada de potencias de $3$ se obtiene añadiendo una última potencia $3^k$ a una representación de $n - 3^k$. Esto nos da la relación de recurrencia:
$$a_n = \sum_{3^k \le n} a_{n - 3^k}.$$

Sea $A(x) = \sum_{n=0}^{\infty} a_n x^n$ la función generatriz de $a_n$, y definamos $S(x) = \sum_{k=0}^{\infty} x^{3^k}$. A partir de la recurrencia tenemos que:
$$A(x) = 1 + A(x)S(x) \implies A(x) = \frac{1}{1 - S(x)}.$$

Queremos estudiar los coeficientes $a_n$ módulo $3$, por lo que podemos trabajar en el anillo de series de potencias formales $\mathbb{F}_3[[x]]$. En característica $3$, se cumple que $(f(x))^3 = f(x^3)$, de modo que:
$$S(x)^3 = \sum_{k=0}^{\infty} \left(x^{3^k}\right)^3 = \sum_{k=0}^{\infty} x^{3^{k+1}} = S(x) - x.$$

Reordenando esta identidad en $\mathbb{F}_3[[x]]$, obtenemos:
$$x = S(x) - S(x)^3 = S(x)(1 - S(x)^2) = S(x)(1 - S(x))(1 + S(x)).$$

Dividiendo entre $x(1 - S(x))$, despejamos $A(x)$ en $\mathbb{F}_3[[x]]$:
$$A(x) = \frac{1}{1 - S(x)} \equiv \frac{S(x)(1 + S(x))}{x} = \frac{S(x) + S(x)^2}{x} \pmod 3.$$

Por lo tanto, $x A(x) \equiv S(x) + S(x)^2 \pmod 3$, lo que significa que $b_n \equiv a_n \pmod 3$ es congruente módulo $3$ con el coeficiente de $x^{n+1}$ en la serie $S(x) + S(x)^2$.

Expandiendo $S(x) + S(x)^2$ en $\mathbb{Z}[[x]]$, tenemos:
$$S(x) + S(x)^2 = \sum_{k=0}^{\infty} x^{3^k} + \sum_{k=0}^{\infty} x^{2 \cdot 3^k} + \sum_{0 \le j < k} 2 x^{3^j + 3^k}.$$

Por la unicidad de la representación de los números enteros en base $3$, los exponentes de las tres sumas anteriores nunca se solapan:
1. $m = 3^k$ (un solo dígito $1$ en base $3$): el coeficiente de $x^m$ es $1$.
2. $m = 2 \cdot 3^k$ (un solo dígito $2$ en base $3$): el coeficiente de $x^m$ es $1$.
3. $m = 3^j + 3^k$ con $j < k$ (exactamente dos dígitos $1$ en base $3$): el coeficiente de $x^m$ es $2$.
4. Para cualquier otro $m$, el coeficiente de $x^m$ es $0$.

Como todos los coeficientes de $S(x) + S(x)^2$ en $\mathbb{Z}[[x]]$ pertenecen ya al conjunto $\{0, 1, 2\}$, concluimos que $b_n$ es exactamente igual al coeficiente $c_{n+1}$ de $x^{n+1}$ en $S(x) + S(x)^2$.

Haciendo el cambio de índice $m = n + 1$ y llamando $N = 2025$, la suma buscada es:
$$\sum_{n=1}^{3^{N}} b_n = \sum_{m=2}^{3^{N} + 1} c_m.$$

Contamos las contribuciones de cada uno de los tres casos en el intervalo $2 \le m \le 3^N + 1$:
- **Caso 1 ($m = 3^k$):** Se cumple $2 \le 3^k \le 3^N + 1$ para $k \in \{1, 2, \dots, N\}$. Hay $N$ valores posibles, y cada uno aporta $1$ a la suma.
- **Caso 2 ($m = 2 \cdot 3^k$):** Se cumple $2 \le 2 \cdot 3^k \le 3^N + 1$ para $k \in \{0, 1, \dots, N-1\}$. Hay $N$ valores posibles, y cada uno aporta $1$ a la suma.
- **Caso 3 ($m = 3^j + 3^k$ con $0 \le j < k$):** 
  - Si $k \le N - 1$, entonces $3^j + 3^k \le 3^{N-2} + 3^{N-1} < 3^N$, por lo que cualquier par $(j, k)$ con $0 \le j < k \le N - 1$ es válido. Hay $\binom{N}{2}$ de estos pares.
  - Si $k = N$, la condición $3^j + 3^N \le 3^N + 1$ equivale a $3^j \le 1$, lo cual solo se cumple para $j = 0$ (dando $m = 3^N + 1$). Esto aporta $1$ par adicional.
  
  En total hay $\binom{N}{2} + 1$ pares, y cada uno aporta $2$ a la suma, sumando en total $2\binom{N}{2} + 2 = N(N - 1) + 2$.

Sumando todas las contribuciones para $N = 2025$:
$$\sum_{n=1}^{3^N} b_n = N + N + N(N - 1) + 2 = N^2 + N + 2.$$

Sustituyendo $N = 2025$:
$$2025^2 + 2025 + 2 = 4100625 + 2027 = 4102652.$$

\boxed{4102652}