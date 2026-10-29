Para encontrar cuántos valores enteros posibles de $x$ existen tales que $x^3$ sea un factor positivo de $10!$, primero hallamos la factorización en números primos de $10!$:

$$10! = 10 \times 9 \times 8 \times 7 \times 6 \times 5 \times 4 \times 3 \times 2 \times 1$$

Contamos las potencias de cada número primo menor o igual a $10$:
- **Potencia de $2$:** $\lfloor 10/2 \rfloor + \lfloor 10/4 \rfloor + \lfloor 10/8 \rfloor = 5 + 2 + 1 = 8$
- **Potencia de $3$:** $\lfloor 10/3 \rfloor + \lfloor 10/9 \rfloor = 3 + 1 = 4$
- **Potencia de $5$:** $\lfloor 10/5 \rfloor = 2$
- **Potencia de $7$:** $\lfloor 10/7 \rfloor = 1$

Por lo tanto, la factorización prima de $10!$ es:
$$10! = 2^8 \cdot 3^4 \cdot 5^2 \cdot 7^1$$

Como se nos pide que $x^3$ sea un factor **positivo** de $10!$, necesariamente $x^3 > 0$, lo que implica que $x$ debe ser un entero positivo ($x > 0$).

Sea la descomposición prima de $x$ de la forma:
$$x = 2^a \cdot 3^b \cdot 5^c \cdot 7^d$$

Entonces:
$$x^3 = 2^{3a} \cdot 3^{3b} \cdot 5^{3c} \cdot 7^{3d}$$

Para que $x^3$ divida a $10!$, los exponentes deben cumplir las siguientes desigualdades con $a, b, c, d \ge 0$:
- $3a \le 8 \implies a \in \{0, 1, 2\}$ ($3$ opciones)
- $3b \le 4 \implies b \in \{0, 1\}$ ($2$ opciones)
- $3c \le 2 \implies c \in \{0\}$ ($1$ opción)
- $3d \le 1 \implies d \in \{0\}$ ($1$ opción)

Multiplicando el número de opciones para cada exponente, obtenemos la cantidad total de valores posibles para $x$:
$$3 \times 2 \times 1 \times 1 = 6$$

(Los valores posibles de $x$ son $1, 2, 3, 4, 6$ y $12$).

\boxed{6}