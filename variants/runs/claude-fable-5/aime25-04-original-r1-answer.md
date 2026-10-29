Factorizando la ecuación:

$$12x^2 - xy - 6y^2 = (4x - 3y)(3x + 2y) = 0$$

(verificación: $12x^2 + 8xy - 9xy - 6y^2 = 12x^2 - xy - 6y^2$ ✓)

Así que necesitamos $4x = 3y$ o $3x = -2y$.

**Caso 1: $4x = 3y$.** Las soluciones enteras son $x = 3k$, $y = 4k$. Las condiciones $|3k| \le 100$ y $|4k| \le 100$ dan $|k| \le 25$, es decir, $k \in \{-25, \dots, 25\}$: **51 pares**.

**Caso 2: $3x = -2y$.** Las soluciones enteras son $x = 2m$, $y = -3m$. Las condiciones $|2m| \le 100$ y $|3m| \le 100$ dan $|m| \le 33$, es decir, $m \in \{-33, \dots, 33\}$: **67 pares**.

**Intersección:** un par satisface ambas ecuaciones solo si $x = y = 0$, que se contó dos veces, así que restamos 1.

Total: $51 + 67 - 1 = 117$.

$$\boxed{117}$$