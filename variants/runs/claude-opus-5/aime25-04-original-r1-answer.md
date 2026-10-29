## Razonamiento

**Factorización.** La forma cuadrática se factoriza:

$$12x^2 - xy - 6y^2 = (3x + 2y)(4x - 3y)$$

(Verificación: $12x^2 - 9xy + 8xy - 6y^2 = 12x^2 - xy - 6y^2$ ✓)

Por tanto el producto es cero si y solo si $3x = -2y$ o $4x = 3y$.

**Caso 1: $3x + 2y = 0$.** Como $\gcd(3,2)=1$, las soluciones enteras son $x = -2t$, $y = 3t$ con $t \in \mathbb{Z}$. Las restricciones dan $|2t| \le 100$ (es decir $|t| \le 50$) y $|3t| \le 100$ (es decir $|t| \le 33$). La condición más fuerte es $|t| \le 33$, lo que da $67$ pares.

**Caso 2: $4x - 3y = 0$.** Las soluciones son $x = 3t$, $y = 4t$. Las restricciones dan $|3t| \le 100$ ($|t| \le 33$) y $|4t| \le 100$ ($|t| \le 25$). La condición más fuerte es $|t| \le 25$, lo que da $51$ pares.

**Intersección.** Si ambas ecuaciones se cumplen, entonces $3x=-2y$ y $4x=3y$ fuerzan $x=y=0$. Así que solo $(0,0)$ se cuenta dos veces.

**Total:** $67 + 51 - 1 = 117$.

\boxed{117}