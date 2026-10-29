Para encontrar el factor primo más grande de $80^5 - 1$, procedemos paso a paso mediante factorización algebraica:

**Paso 1: Factorización como diferencia de potencias quintas**
Utilizamos la identidad $x^5 - 1 = (x - 1)(x^4 + x^3 + x^2 + x + 1)$ con $x = 80$:
$$80^5 - 1 = (80 - 1)(80^4 + 80^3 + 80^2 + 80 + 1) = 79(80^4 + 80^3 + 80^2 + 80 + 1)$$
Observamos que $79$ es un número primo.

**Paso 2: Factorización de Aurifeuille**
Para el segundo factor, notamos que cumple la identidad algebraica:
$$x^4 + x^3 + x^2 + x + 1 = (x^2 + 3x + 1)^2 - 5x(x + 1)^2$$
Como $x = 80 = 5 \cdot 4^2$, el término $5x(x+1)^2$ es un cuadrado perfecto:
$$5(80)(80 + 1)^2 = 400 \cdot 81^2 = (20 \cdot 81)^2 = 1620^2$$
Por otro lado, evaluamos $x^2 + 3x + 1$ para $x = 80$:
$$80^2 + 3(80) + 1 = 6400 + 240 + 1 = 6641$$
De este modo, obtenemos una diferencia de cuadrados:
$$80^4 + 80^3 + 80^2 + 80 + 1 = 6641^2 - 1620^2 = (6641 - 1620)(6641 + 1620) = 5021 \cdot 8261$$

**Paso 3: Factorización de $8261$ y $5021$**
Por el pequeño teorema de Fermat, cualquier divisor primo $p$ de $80^4 + 80^3 + 80^2 + 80 + 1$ debe cumplir $p \equiv 1 \pmod{10}$ (ya que el orden de $80 \pmod p$ es $5$, por lo que $5 \mid (p - 1)$ y $p$ es impar).

1. **Para $8261$:**
   Probamos con $p = 11$: $8 - 2 + 6 - 1 = 11$, por lo que es divisible entre $11$:
   $$8261 = 11 \cdot 751$$
   Para verificar si $751$ es primo, basta con probar primos $p \equiv 1 \pmod{10}$ menores o iguales a $\sqrt{751} \approx 27.4$. El único candidato es $11$, y como $7 - 5 + 1 = 3 \not\equiv 0 \pmod{11}$, concluimos que $751$ es primo.

2. **Para $5021$:**
   Verificamos si tiene factores primos $p \equiv 1 \pmod{10}$ menores o iguales a $\sqrt{5021} \approx 70.85$. Los únicos candidatos son $11, 31, 41$ y $61$:
   - $5021 = 11 \cdot 456 + 5$ (no divisible por $11$)
   - $5021 = 31 \cdot 161 + 30$ (no divisible por $31$)
   - $5021 = 41 \cdot 122 + 19$ (no divisible por $41$)
   - $5021 = 61 \cdot 82 + 19$ (no divisible por $61$)

   Por lo tanto, $5021$ es un número primo.

**Conclusión:**
La factorización prima completa de $80^5 - 1$ es:
$$80^5 - 1 = 11 \cdot 79 \cdot 751 \cdot 5021$$
El mayor factor primo es $5021$.

\boxed{5021}