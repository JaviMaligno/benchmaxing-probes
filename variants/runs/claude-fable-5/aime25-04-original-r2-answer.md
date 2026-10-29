Factorizamos la forma cuadrática:

$$12x^2 - xy - 6y^2 = (4x - 3y)(3x + 2y) = 0$$

(Verificación: $12x^2 + 8xy - 9xy - 6y^2 = 12x^2 - xy - 6y^2$. ✓)

**Caso 1: $4x = 3y$.** Como $\gcd(3,4)=1$, las soluciones enteras son $x = 3k$, $y = 4k$. La restricción $|y| \le 100$ da $|4k| \le 100 \Rightarrow k \in [-25, 25]$ (y entonces $|x| = |3k| \le 75 \le 100$ se cumple). Son $51$ pares.

**Caso 2: $3x = -2y$.** Las soluciones enteras son $x = 2m$, $y = -3m$. La restricción $|y| \le 100$ da $|3m| \le 100 \Rightarrow m \in [-33, 33]$ (y $|x| \le 66 \le 100$ se cumple). Son $67$ pares.

**Intersección:** un par en ambos casos requiere $4x = 3y$ y $3x = -2y$ simultáneamente, lo que fuerza $x = y = 0$. Solo el par $(0,0)$ se cuenta dos veces.

Total: $51 + 67 - 1 = 117$.

$$\boxed{117}$$