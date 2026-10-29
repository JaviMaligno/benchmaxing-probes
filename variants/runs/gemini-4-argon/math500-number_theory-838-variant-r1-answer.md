Para encontrar cuántos valores enteros positivos posibles de $y$ cumplen que $y^3$ es un divisor de $12!$, primero hallamos la factorización en números primos de $12!$.

Los números primos menores o iguales a $12$ son $2, 3, 5, 7$ y $11$. Utilizando la fórmula de Legendre para encontrar el exponente de cada primo en $12!$:

- **Para el primo $2$:**
  $$\left\lfloor \frac{12}{2} \right\rfloor + \left\lfloor \frac{12}{4} \right\rfloor + \left\lfloor \frac{12}{8} \right\rfloor = 6 + 3 + 1 = 10$$

- **Para el primo $3$:**
  $$\left\lfloor \frac{12}{3} \right\rfloor + \left\lfloor \frac{12}{9} \right\rfloor = 4 + 1 = 5$$

- **Para el primo $5$:**
  $$\left\lfloor \frac{12}{5} \right\rfloor = 2$$

- **Para el primo $7$:**
  $$\left\lfloor \frac{12}{7} \right\rfloor = 1$$

- **Para el primo $11$:**
  $$\left\lfloor \frac{12}{11} \right\rfloor = 1$$

Por lo tanto, la factorización prima de $12!$ es:
$$12! = 2^{10} \cdot 3^5 \cdot 5^2 \cdot 7^1 \cdot 11^1$$

Sea $y = 2^a \cdot 3^b \cdot 5^c \cdot 7^d \cdot 11^e$, donde $a, b, c, d, e$ son enteros no negativos. Entonces:
$$y^3 = 2^{3a} \cdot 3^{3b} \cdot 5^{3c} \cdot 7^{3d} \cdot 11^{3e}$$

Para que $y^3$ sea un divisor de $12!$, el exponente de cada factor primo en $y^3$ no debe superar al exponente correspondiente en $12!$:

- $3a \le 10 \implies a \in \{0, 1, 2, 3\}$ ($4$ opciones)
- $3b \le 5 \implies b \in \{0, 1\}$ ($2$ opciones)
- $3c \le 2 \implies c = 0$ ($1$ opción)
- $3d \le 1 \implies d = 0$ ($1$ opción)
- $3e \le 1 \implies e = 0$ ($1$ opción)

Multiplicando el número de opciones para cada exponente, obtenemos el total de valores posibles para $y$:
$$4 \times 2 \times 1 \times 1 \times 1 = 8$$

\boxed{8}