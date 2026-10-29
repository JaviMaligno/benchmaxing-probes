Para encontrar el número de pares ordenados $(x,y)$ de números enteros entre $-100$ y $100$ (inclusive) que satisfacen la ecuación $10x^2+7xy-12y^2=0$, primero factorizamos la expresión cuadrática:

$$10x^2 + 7xy - 12y^2 = 0$$
$$10x^2 + 15xy - 8xy - 12y^2 = 0$$
$$5x(2x + 3y) - 4y(2x + 3y) = 0$$
$$(5x - 4y)(2x + 3y) = 0$$

Para que el producto sea igual a cero, al menos uno de los factores debe ser cero. Esto nos da dos casos posibles:

**Caso 1: $5x - 4y = 0 \implies 5x = 4y$**
Dado que $\text{mcd}(5, 4) = 1$ y tanto $x$ como $y$ son números enteros, las soluciones son de la forma $(x, y) = (4k, 5k)$ para algún número entero $k$.
Como $-100 \le x, y \le 100$, debemos cumplir ambas condiciones:
- $-100 \le 4k \le 100 \implies -25 \le k \le 25$
- $-100 \le 5k \le 100 \implies -20 \le k \le 20$

Para que ambas desigualdades se cumplan simultáneamente, $k$ debe estar en el rango $-20 \le k \le 20$. Esto nos da $20 - (-20) + 1 = 41$ soluciones.

**Caso 2: $2x + 3y = 0 \implies 2x = -3y$**
Dado que $\text{mcd}(2, 3) = 1$, las soluciones enteras son de la forma $(x, y) = (3m, -2m)$ para algún número entero $m$.
Aplicando las restricciones del intervalo $[-100, 100]$:
- $-100 \le 3m \le 100 \implies -33 \le m \le 33$ (ya que $m$ es entero y $100 / 3 = 33.\overline{3}$)
- $-100 \le -2m \le 100 \implies -50 \le m \le 50$

La intersección de ambas condiciones requiere que $-33 \le m \le 33$, lo cual nos da $33 - (-33) + 1 = 67$ soluciones.

**Intersección de ambos casos:**
El par $(x, y) = (0, 0)$ (que corresponde a $k = 0$ y $m = 0$) es la única solución común a ambos casos y se ha contado dos veces. Restando este duplicado, el número total de pares ordenados es:

$$41 + 67 - 1 = 107$$

\boxed{107}