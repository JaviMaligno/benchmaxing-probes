## Planteamiento

Como el coeficiente principal es $c_n = 2$ y todas las raíces son enteros distintos $r_1,\dots,r_n$:

$$g(x) = 2(x-r_1)(x-r_2)\cdots(x-r_n)$$

**Término constante:** $c_0 = 2\prod(-r_i) = 78 \implies \prod(-r_i) = 39 = 3\cdot 13$.

**Coeficiente siguiente:** $c_{n-1} = -2\sum r_i$, luego $|c_{n-1}| = 2\left|\sum r_i\right|$.

## Restricción sobre las raíces

Ninguna raíz es nula y $\prod |r_i| = 39$. Los únicos valores absolutos posibles son $1, 3, 13, 39$, y como las raíces son **distintas**, a lo sumo dos pueden tener el mismo valor absoluto ($+a$ y $-a$). Esto limita $n \le 4$.

## Casos

- **$n=1$:** $r=-39$ → $|c_{n-1}| = 78$.
- **$n=2$:** $\prod r_i = 39$: $\{3,13\} \to 32$; $\{-3,-13\}\to 32$; $\{1,39\}\to 80$. Mínimo **32**.
- **$n=3$:** se necesita $\prod r_i = -39$:
  - $\{1,3,-13\}$: suma $=-9 \to |c_{n-1}| = 18$
  - $\{1,-3,13\}$: suma $=11 \to 22$
  - $\{-1,3,13\}$: suma $=15 \to 30$
  - $\{-1,-3,-13\}$: suma $=-17 \to 34$
  - $\{1,-1,39\}$: suma $=39 \to 78$

  Mínimo **18**.
- **$n=4$:** valores absolutos forzados a $\{1,1,3,13\}$, con $\prod r_i = 39$: $\{1,-1,-3,13\}$ (suma $10$) o $\{1,-1,3,-13\}$ (suma $-10$) → **20**.

## Verificación del óptimo

$$2(x-1)(x-3)(x+13) = 2x^3 + 18x^2 - 98x + 78$$

Efectivamente $c_n = 2$, $c_0 = 78$, raíces enteras distintas $1, 3, -13$, y $|c_{n-1}| = 18$.

\boxed{18}