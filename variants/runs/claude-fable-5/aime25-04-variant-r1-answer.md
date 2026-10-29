La ecuación se factoriza:

$$10x^2 + 7xy - 12y^2 = (5x - 4y)(2x + 3y) = 0$$

(verificación: $10x^2 + 15xy - 8xy - 12y^2 = 10x^2 + 7xy - 12y^2$ ✓)

**Caso 1: $5x = 4y$.** Como $\gcd(4,5)=1$, las soluciones enteras son $x = 4t$, $y = 5t$. Las restricciones $|4t| \le 100$ y $|5t| \le 100$ dan $|t| \le 20$, es decir $41$ pares.

**Caso 2: $2x = -3y$.** Las soluciones son $x = 3s$, $y = -2s$. Las restricciones $|3s| \le 100$ y $|2s| \le 100$ dan $|s| \le 33$ (pues $3 \cdot 33 = 99 \le 100$), es decir $67$ pares.

**Intersección:** ambas condiciones a la vez obligan $x = y = 0$, que se contó dos veces, así que restamos 1.

Total: $41 + 67 - 1 = 107$.

$$\boxed{107}$$