Para encontrar cuántos valores enteros posibles de $x$ existen tales que $x^3$ sea un factor positivo de $10!$, primero determinamos la factorización prima de $10!$:

$$10! = 10 \times 9 \times 8 \times 7 \times 6 \times 5 \times 4 \times 3 \times 2 \times 1$$

Descomponiendo cada número en sus factores primos:
- Exponente de $2$: $\lfloor \frac{10}{2} \rfloor + \lfloor \frac{10}{4} \rfloor + \lfloor \frac{10}{8} \rfloor = 5 + 2 + 1 = 8$
- Exponente de $3$: $\lfloor \frac{10}{3} \rfloor + \lfloor \frac{10}{9} \rfloor = 3 + 1 = 4$
- Exponente de $5$: $\lfloor \frac{10}{5} \rfloor = 2$
- Exponente de $7$: $\lfloor \frac{10}{7} \rfloor = 1$

Por lo tanto, la factorización prima de $10!$ es:
$$10! = 2^8 \cdot 3^4 \cdot 5^2 \cdot 7^1$$

Dado que $x^3$ debe ser un factor **positivo** de $10!$, $x^3 > 0$, lo que implica que $x$ debe ser un entero positivo ($x > 0$).

Sea la factorización prima de $x$:
$$x = 2^a \cdot 3^b \cdot 5^c \cdot 7^d$$
donde $a, b, c, d$ son enteros no negativos. Entonces:
$$x^3 = 2^{3a} \cdot 3^{3b} \cdot 5^{3c} \cdot 7^{3d}$$

Para que $x^3$ divida a $10!$, los exponentes deben cumplir:
- $3a \le 8 \implies a \in \{0, 1, 2\}$ (3 opciones)
- $3b \le 4 \implies b \in \{0, 1\}$ (2 opciones)
- $3c \le 2 \implies c = 0$ (1 opción)
- $3d \le 1 \implies d = 0$ (1 opción)

Multiplicando el número de opciones para cada exponente, obtenemos el total de valores posibles para $x$:
$$3 \times 2 \times 1 \times 1 = 6$$

\boxed{6}