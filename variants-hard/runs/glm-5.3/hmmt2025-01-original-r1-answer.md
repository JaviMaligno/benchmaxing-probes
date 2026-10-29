# Resolución

**Paso 1: Factorización.**
$$9! = 362880 = 2^7 \cdot 3^4 \cdot 5 \cdot 7$$

**Paso 2: Restricción por dígito de unidades.**
Un divisor con dígito de unidades $1$ es impar y no divisible entre $5$, así que solo puede usar las potencias de $3$ y $7$:
$$3^a \cdot 7^b, \quad 0 \le a \le 4, \; 0 \le b \le 1$$

**Paso 3: Lista de candidatos y sus dígitos finales.**

| Divisor | Dígito |
|---|---|
| $1, 3, 9, 27$ | $1, 3, 9, 7$ |
| $81$ | $\mathbf{1}$ |
| $7, 21, 63, 189, 567$ | $7, \mathbf{1}, 3, 9, 7$ |

Los que terminan en $1$: $1, 21, 81$.

**Paso 4: Suma.**
$$1 + 21 + 81 = 103$$

\boxed{103}