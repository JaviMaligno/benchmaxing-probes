Para encontrar el número de pares ordenados $(x, y)$ de números enteros entre $-100$ y $100$ (inclusive) que satisfacen la ecuación:

$$10x^2 + 7xy - 12y^2 = 0$$

**Paso 1: Factorizar la ecuación**
Buscamos dos números cuyo producto sea $10 \times (-12) = -120$ y cuya suma sea $7$. Esos números son $15$ y $-8$. Reescribimos el término central y factorizamos por agrupación:

$$10x^2 + 15xy - 8xy - 12y^2 = 0$$
$$5x(2x + 3y) - 4y(2x + 3y) = 0$$
$$(5x - 4y)(2x + 3y) = 0$$

Esto nos da dos casos posibles para las soluciones.

**Paso 2: Analizar el Caso 1 ($5x - 4y = 0$)**
De $5x = 4y$, dado que $\text{mcd}(5, 4) = 1$, todas las soluciones enteras son de la forma:
$$x = 4k, \quad y = 5k \quad \text{para algún entero } k$$

Aplicamos las restricciones $-100 \le x \le 100$ y $-100 \le y \le 100$:
- Para $x$: $-100 \le 4k \le 100 \implies -25 \le k \le 25$
- Para $y$: $-100 \le 5k \le 100 \implies -20 \le k \le 20$

Para que ambas condiciones se cumplan simultáneamente, $k$ debe estar en el rango $-20 \le k \le 20$. Esto nos da:
$$20 - (-20) + 1 = 41 \text{ soluciones.}$$

**Paso 3: Analizar el Caso 2 ($2x + 3y = 0$)**
De $2x = -3y$, dado que $\text{mcd}(2, 3) = 1$, todas las soluciones enteras son de la forma:
$$x = -3m, \quad y = 2m \quad \text{para algún entero } m$$

Aplicamos las mismas restricciones de rango:
- Para $x$: $-100 \le -3m \le 100 \implies -33 \le m \le 33$
- Para $y$: $-100 \le 2m \le 100 \implies -50 \le m \le 50$

Para que ambas condiciones se cumplan simultáneamente, $m$ debe estar en el rango $-33 \le m \le 33$. Esto nos da:
$$33 - (-33) + 1 = 67 \text{ soluciones.}$$

**Paso 4: Eliminar duplicados**
La solución $(x, y) = (0, 0)$ aparece en ambos casos (cuando $k = 0$ y cuando $m = 0$), y es el único punto de intersección entre las dos rectas. Por lo tanto, restamos $1$ al total para no contarla dos veces:

$$41 + 67 - 1 = 107$$

\boxed{107}