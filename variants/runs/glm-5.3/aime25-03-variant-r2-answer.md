# Solución

## Paso 1: Plantear las variables

Sean $m$, $b$, $k$ los números de miembros que eligieron mango, banana y kiwi respectivamente. Entonces:

$$m + b + k = 10, \quad m > b > k \geq 1$$

## Paso 2: Encontrar todas las ternas $(m, b, k)$

**Caso $k = 1$:** necesitamos $b \geq 2$ y $m + b = 9$ con $m > b$:
- $(m, b) = (7, 2)$ ✓
- $(m, b) = (6, 3)$ ✓
- $(m, b) = (5, 4)$ ✓
- $(m, b) = (4, 5)$ ✗ (no cumple $m > b$)

**Caso $k = 2$:** necesitamos $b \geq 3$ y $m + b = 8$ con $m > b$:
- $(m, b) = (5, 3)$ ✓
- $(m, b) = (4, 4)$ ✗ (no cumple $m > b$)

**Caso $k = 3$:** necesitamos $b \geq 4$ y $m + b = 7$ con $m > b \geq 4$; pero entonces $m + b \geq 5 + 4 = 9 > 7$. ✗

Las ternas válidas son: $(7,2,1)$, $(6,3,1)$, $(5,4,1)$, $(5,3,2)$.

## Paso 3: Contar asignaciones para cada terna

Para cada terna, el número de asignaciones es $\binom{10}{m}\binom{10-m}{b}$:

| Terna $(m,b,k)$ | Cálculo | Asignaciones |
|---|---|---|
| $(7,2,1)$ | $\binom{10}{7}\binom{3}{2} = 120 \cdot 3$ | $360$ |
| $(6,3,1)$ | $\binom{10}{6}\binom{4}{3} = 210 \cdot 4$ | $840$ |
| $(5,4,1)$ | $\binom{10}{5}\binom{5}{4} = 252 \cdot 5$ | $1260$ |
| $(5,3,2)$ | $\binom{10}{5}\binom{5}{3} = 252 \cdot 10$ | $2520$ |

## Paso 4: Sumar y obtener el residuo

$$N = 360 + 840 + 1260 + 2520 = 4980$$

$$N \bmod 1000 = 4980 - 4\cdot 1000 = \boxed{980}$$