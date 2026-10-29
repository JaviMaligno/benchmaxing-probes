Para encontrar el número de pares ordenados $(x, y)$ de números enteros entre $-100$ y $100$ inclusive que satisfacen la ecuación $12x^2 - xy - 6y^2 = 0$, procedemos paso a paso:

**Paso 1: Factorizar la ecuación**
Podemos factorizar el polinomio cuadrático de dos variables descomponiendo el término central:
$$12x^2 - 9xy + 8xy - 6y^2 = 0$$
$$3x(4x - 3y) + 2y(4x - 3y) = 0$$
$$(3x + 2y)(4x - 3y) = 0$$

Esto significa que cualquier solución $(x, y)$ debe cumplir al menos una de las siguientes dos ecuaciones lineales:
1. $3x + 2y = 0$
2. $4x - 3y = 0$

---

**Paso 2: Contar las soluciones del primer caso ($3x + 2y = 0$)**
Reescribiendo la ecuación tenemos $3x = -2y$. Como $\text{mcd}(3, 2) = 1$, todas las soluciones enteras son de la forma:
$$(x, y) = (2k, -3k) \quad \text{para } k \in \mathbb{Z}$$

Dado que $-100 \le x \le 100$ y $-100 \le y \le 100$, tenemos las siguientes restricciones para $k$:
* $-100 \le 2k \le 100 \implies -50 \le k \le 50$
* $-100 \le -3k \le 100 \implies -33.33\ldots \le k \le 33.33\ldots \implies -33 \le k \le 33$

Para que ambas coordenadas estén dentro del rango permitido, $k$ debe cumplir la condición más restrictiva: $-33 \le k \le 33$.
El número de valores enteros posibles para $k$ es:
$$33 - (-33) + 1 = 67$$

---

**Paso 3: Contar las soluciones del segundo caso ($4x - 3y = 0$)**
Reescribiendo la ecuación tenemos $4x = 3y$. Como $\text{mcd}(4, 3) = 1$, todas las soluciones enteras son de la forma:
$$(x, y) = (3m, 4m) \quad \text{para } m \in \mathbb{Z}$$

Aplicando nuevamente los límites $-100 \le x \le 100$ y $-100 \le y \le 100$:
* $-100 \le 3m \le 100 \implies -33.33\ldots \le m \le 33.33\ldots \implies -33 \le m \le 33$
* $-100 \le 4m \le 100 \implies -25 \le m \le 25$

La condición más restrictiva es $-25 \le m \le 25$.
El número de valores enteros posibles para $m$ es:
$$25 - (-25) + 1 = 51$$

---

**Paso 4: Eliminar soluciones duplicadas**
La única solución que satisface simultáneamente $3x + 2y = 0$ y $4x - 3y = 0$ es el par $(x, y) = (0, 0)$ (que corresponde a $k = 0$ y $m = 0$). Como esta solución fue contada en ambos casos, debemos restar $1$ a la suma total.

Por lo tanto, el número total de pares ordenados $(x, y)$ es:
$$67 + 51 - 1 = 117$$

\boxed{117}