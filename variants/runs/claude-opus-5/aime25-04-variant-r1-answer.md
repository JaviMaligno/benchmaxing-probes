## Solución

**Factorización:**

$$10x^2+7xy-12y^2=(2x+3y)(5x-4y)=0$$

Verificación: $(2x+3y)(5x-4y)=10x^2-8xy+15xy-12y^2=10x^2+7xy-12y^2$ ✓

**Caso 1: $2x+3y=0$**

Entonces $2x=-3y$. Como $\gcd(2,3)=1$, necesitamos $y=2t$, y así $x=-3t$.

Restricciones: $|{-3t}|\le 100 \Rightarrow |t|\le 33$, y $|2t|\le 100 \Rightarrow |t|\le 50$.

La condición más fuerte es $|t|\le 33$, es decir $t\in\{-33,\dots,33\}$: **67 pares**.

**Caso 2: $5x-4y=0$**

Entonces $5x=4y$, lo que da $x=4s$, $y=5s$.

Restricciones: $|4s|\le 100 \Rightarrow |s|\le 25$, y $|5s|\le 100 \Rightarrow |s|\le 20$.

La condición más fuerte es $|s|\le 20$, es decir $s\in\{-20,\dots,20\}$: **41 pares**.

**Intersección:**

Las dos rectas se cortan solo en el origen, así que $(0,0)$ se cuenta dos veces.

$$67+41-1=107$$

\boxed{107}