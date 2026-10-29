Para encontrar el mayor factor primo de $45^5 - 1$, podemos factorizar la expresión paso a paso.

**Paso 1: Factorización como diferencia de potencias**
Utilizando la identidad $x^5 - 1 = (x - 1)(x^4 + x^3 + x^2 + x + 1)$ con $x = 45$:
$$45^5 - 1 = (45 - 1)(45^4 + 45^3 + 45^2 + 45 + 1) = 44(45^4 + 45^3 + 45^2 + 45 + 1)$$

**Paso 2: Factorización aurifeuilliana**
Observamos que el segundo factor tiene la forma $\Phi_5(x) = x^4 + x^3 + x^2 + x + 1$, la cual cumple la identidad algebraica:
$$x^4 + x^3 + x^2 + x + 1 = (x^2 + 3x + 1)^2 - 5x(x + 1)^2$$

Dado que $x = 45 = 5 \cdot 3^2$, el término $5x(x + 1)^2$ es un cuadrado perfecto:
$$5(45)(45 + 1)^2 = 225 \cdot 46^2 = (15 \cdot 46)^2 = 690^2$$

Por otro lado, calculamos $x^2 + 3x + 1$ para $x = 45$:
$$45^2 + 3(45) + 1 = 2025 + 135 + 1 = 2161$$

Sustituyendo ambos resultados, obtenemos una diferencia de cuadrados:
$$45^4 + 45^3 + 45^2 + 45 + 1 = 2161^2 - 690^2 = (2161 - 690)(2161 + 690) = 1471 \cdot 2851$$

Por lo tanto:
$$45^5 - 1 = 2^2 \cdot 11 \cdot 1471 \cdot 2851$$

**Paso 3: Verificación de primalidad de $2851$**
Todo factor primo $p$ de $x^4 + x^3 + x^2 + x + 1$ (distinto de $5$) debe cumplir $p \equiv 1 \pmod 5$. Como además es impar, debe cumplir $p \equiv 1 \pmod{10}$.

Para comprobar si $2851$ es primo, basta con verificar los primos $p \equiv 1 \pmod{10}$ tales que $p \le \sqrt{2851} \approx 53.39$, los cuales son $11$, $31$ y $41$:
- $2851 = 11 \cdot 259 + 2$ (no es divisible por $11$)
- $2851 = 31 \cdot 92 - 1$ (no es divisible por $31$)
- $2851 = 41 \cdot 69 + 22$ (no es divisible por $41$)

Por consiguiente, $2851$ es un número primo (al igual que $1471$), siendo este el mayor factor primo de $45^5 - 1$.

\boxed{2851}