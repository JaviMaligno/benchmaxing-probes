## Factorización de 12!

Primero descompongo 12! en factores primos:

- **Exponente de 2:** ⌊12/2⌋ + ⌊12/4⌋ + ⌊12/8⌋ = 6 + 3 + 1 = **10**
- **Exponente de 3:** ⌊12/3⌋ + ⌊12/9⌋ = 4 + 1 = **5**
- **Exponente de 5:** ⌊12/5⌋ = **2**
- **Exponente de 7:** **1**
- **Exponente de 11:** **1**

Por lo tanto:
$$12! = 2^{10} \cdot 3^5 \cdot 5^2 \cdot 7 \cdot 11$$

## Condición sobre y

Si $y = 2^a 3^b 5^c 7^d 11^e$, entonces $y^3 = 2^{3a} 3^{3b} 5^{3c} 7^{3d} 11^{3e}$ debe dividir a 12!, lo que exige:

| Primo | Condición | Valores posibles | Cantidad |
|---|---|---|---|
| 2 | $3a \le 10$ | $a \in \{0,1,2,3\}$ | 4 |
| 3 | $3b \le 5$ | $b \in \{0,1\}$ | 2 |
| 5 | $3c \le 2$ | $c = 0$ | 1 |
| 7 | $3d \le 1$ | $d = 0$ | 1 |
| 11 | $3e \le 1$ | $e = 0$ | 1 |

## Conteo

$$4 \cdot 2 \cdot 1 \cdot 1 \cdot 1 = 8$$

Los valores son: $1, 2, 4, 8, 3, 6, 12, 24$.

\boxed{8}