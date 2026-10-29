## Razonamiento

**Factorización.** La expresión se factoriza como:

$$12x^2 - xy - 6y^2 = (3x + 2y)(4x - 3y) = 0$$

Verificación: $(3x+2y)(4x-3y) = 12x^2 - 9xy + 8xy - 6y^2 = 12x^2 - xy - 6y^2$ ✓

Por tanto, se requiere $3x + 2y = 0$ o $4x - 3y = 0$.

**Caso 1: $3x = -2y$.** Como $\gcd(2,3)=1$, las soluciones enteras son $x = -2t$, $y = 3t$ con $t \in \mathbb{Z}$.
- $|-2t| \le 100 \Rightarrow |t| \le 50$
- $|3t| \le 100 \Rightarrow |t| \le 33$

La restricción activa es $|t| \le 33$, lo que da $t \in \{-33, \dots, 33\}$: **67 pares**.

**Caso 2: $4x = 3y$.** Las soluciones enteras son $x = 3t$, $y = 4t$ con $t \in \mathbb{Z}$.
- $|3t| \le 100 \Rightarrow |t| \le 33$
- $|4t| \le 100 \Rightarrow |t| \le 25$

La restricción activa es $|t| \le 25$, lo que da $t \in \{-25, \dots, 25\}$: **51 pares**.

**Intersección.** Si ambas ecuaciones se cumplen, entonces $3x = -2y$ y $4x = 3y$ fuerzan $x = y = 0$. El par $(0,0)$ se cuenta en ambos casos: 1 par repetido.

**Total.** Por inclusión–exclusión: $67 + 51 - 1 = 117$.

\boxed{117}