## Razonamiento

Factorizamos la forma cuadrática:

$$10x^2 + 7xy - 12y^2 = (2x + 3y)(5x - 4y)$$

Verificación: $2x\cdot 5x = 10x^2$, $2x\cdot(-4y) + 3y\cdot 5x = -8xy + 15xy = 7xy$, $3y\cdot(-4y) = -12y^2$. ✓

El producto es cero si y solo si uno de los factores es cero.

**Caso 1: $2x + 3y = 0$**

Entonces $2x = -3y$. Como $\gcd(2,3)=1$, se requiere $y = 2t$, lo que da $x = -3t$.
- $|x| \le 100 \Rightarrow |t| \le 33$ (pues $3\cdot 34 = 102 > 100$)
- $|y| \le 100 \Rightarrow |t| \le 50$

La restricción dominante es $|t| \le 33$, es decir $t \in \{-33,\dots,33\}$: **67 pares**.

**Caso 2: $5x - 4y = 0$**

Entonces $5x = 4y$, de donde $x = 4s$, $y = 5s$.
- $|x| \le 100 \Rightarrow |s| \le 25$
- $|y| \le 100 \Rightarrow |s| \le 20$

La restricción dominante es $|s| \le 20$, es decir $s \in \{-20,\dots,20\}$: **41 pares**.

**Intersección**

Ambos factores se anulan simultáneamente solo cuando $x = y = 0$ (el sistema lineal tiene determinante $2\cdot(-4) - 3\cdot 5 = -23 \neq 0$). Ese par se contó dos veces.

**Total:** $67 + 41 - 1 = 107$

\boxed{107}