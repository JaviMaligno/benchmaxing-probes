Factorizamos la forma cuadrática:

$$10x^2 + 7xy - 12y^2 = (5x - 4y)(2x + 3y) = 0$$

(Verificación: $5x\cdot 2x = 10x^2$, $5x\cdot 3y - 4y\cdot 2x = 15xy - 8xy = 7xy$, $-4y\cdot 3y = -12y^2$.) ✓

Entonces cada solución satisface $5x = 4y$ o $2x = -3y$.

**Caso 1: $5x = 4y$.** Como $\gcd(5,4)=1$, las soluciones enteras son $x = 4t$, $y = 5t$. Las restricciones $|4t| \le 100$ y $|5t| \le 100$ dan $t \in [-20, 20]$, es decir, **41 pares**.

**Caso 2: $2x = -3y$.** Las soluciones son $x = 3s$, $y = -2s$. Las restricciones $|3s| \le 100$ y $|2s| \le 100$ dan $s \in [-33, 33]$, es decir, **67 pares**.

**Intersección:** ambas rectas solo comparten el punto $(0,0)$, contado dos veces.

Total: $41 + 67 - 1 = 107$.

$$\boxed{107}$$