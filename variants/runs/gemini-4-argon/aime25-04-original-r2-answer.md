Para encontrar el número de pares ordenados $(x,y)$ de números enteros entre $-100$ y $100$, ambos inclusive, que satisfacen la ecuación $12x^2 - xy - 6y^2 = 0$, primero factorizamos la expresión cuadrática:

$$12x^2 - xy - 6y^2 = 12x^2 - 9xy + 8xy - 6y^2 = 3x(4x - 3y) + 2y(4x - 3y) = (3x + 2y)(4x - 3y) = 0$$

Esto significa que un par $(x,y)$ es solución si y solo si cumple al menos una de las siguientes dos condiciones:

1. **Primer caso:** $3x + 2y = 0 \implies 3x = -2y$.
   Dado que $\text{mcd}(3, 2) = 1$, las soluciones enteras son de la forma $(x, y) = (2k, -3k)$ para algún número entero $k$.
   Como $-100 \le x, y \le 100$, tenemos:
   $$-100 \le 2k \le 100 \implies -50 \le k \le 50$$
   $$-100 \le -3k \le 100 \implies -33 \le k \le 33$$
   Ambas desigualdades se cumplen simultáneamente cuando $-33 \le k \le 33$, lo que nos da $33 - (-33) + 1 = 67$ soluciones.

2. **Segundo caso:** $4x - 3y = 0 \implies 4x = 3y$.
   Dado que $\text{mcd}(4, 3) = 1$, las soluciones enteras son de la forma $(x, y) = (3m, 4m)$ para algún número entero $m$.
   Aplicando las restricciones $-100 \le x, y \le 100$:
   $$-100 \le 3m \le 100 \implies -33 \le m \le 33$$
   $$-100 \le 4m \le 100 \implies -25 \le m \le 25$$
   Ambas desigualdades se cumplen simultáneamente cuando $-25 \le m \le 25$, lo que nos da $25 - (-25) + 1 = 51$ soluciones.

3. **Intersección de ambos casos:**
   La única solución que satisface ambas ecuaciones simultáneamente ($3x + 2y = 0$ y $4x - 3y = 0$) es $(x, y) = (0, 0)$, la cual fue contada en ambos casos (para $k = 0$ y $m = 0$).

Restando la solución repetida mediante el principio de inclusión-exclusión, el número total de pares ordenados es:
$$67 + 51 - 1 = 117$$

\boxed{117}