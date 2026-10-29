# Planteamiento

Como $a_n = 2$ y todas las raíces $r_1, \dots, r_n$ son enteros distintos:

$$f(x) = 2\prod_{i=1}^n (x - r_i)$$

**Condición sobre $a_0$:**
$$a_0 = 2\prod(-r_i) = 2(-1)^n \prod r_i = 66 \implies \prod r_i = 33\cdot(-1)^n$$

Ninguna raíz es cero, y como $33 = 3\cdot 11$ es primo relativo a cualquier otra factorización, cada $|r_i|$ debe ser un divisor de $33$, con producto de valores absolutos igual a $33$.

**Objetivo:** $|a_{n-1}| = 2\left|\sum r_i\right|$, así que hay que minimizar $|\text{suma de raíces}|$.

## Análisis por casos

**$n=1$:** única raíz $r$ con $-r = 33$, es decir $r = -33$. Entonces $a_{n-1} = a_0 = 66$.

**$n=2$:** $r_1 r_2 = 33$ (mismo signo). Opciones: $\{3,11\}$ con suma $\pm 14$; $\{1,33\}$ con suma $\pm 34$. Mínimo: $|a_1| = 2(14) = 28$.

**$n=3$:** $r_1 r_2 r_3 = -33$. Factorizaciones posibles de $|33|$ en tres factores: $1\cdot 1\cdot 33$ (raíces $1,-1,\pm 33$, suma $\pm 33$) o $1\cdot 3\cdot 11$. Con signos de producto $-33$:
- $\{1, 3, -11\}$: suma $-7$ ✓
- $\{1, -3, 11\}$: suma $9$
- $\{-1, 3, 11\}$: suma $13$

Mínimo: $|a_2| = 2(7) = 14$.

**$n=4$:** Las raíces deben ser $\{\pm 1, \pm 3, \pm 11\}$ con algún signo (o incluir $\pm 1$ repetido como $1$ y $-1$). Con producto $33$: $\{1, -1, 3, -11\}$, suma $= -8$, dando $|a_3| = 16$.

Para $n \geq 5$ no hay suficientes divisores distintos de $33$ (con valores absolutos multiplicando $33$ solo se pueden usar los pares $\pm 1, \pm 3, \pm 11, \pm 33$, y usar tanto $1$ como $-1$ consume un factor $1$).

## Verificación del mejor caso

Con raíces $1, 3, -11$:
$$f(x) = 2(x-1)(x-3)(x+11) = 2(x^3 + 7x^2 - 31x + 33)$$
- $a_3 = 2$ ✓, $a_0 = 66$ ✓, $a_2 = 14$.

El mínimo de $|a_{n-1}|$ es $14$.

$$\boxed{14}$$