# Solución

**Paso 1: Factorizar la forma cuadrática.**

Busco factorizar \(10x^2 + 7xy - 12y^2\) como \((5x - 4y)(2x + 3y)\):

- Verifico: \(5x \cdot 2x = 10x^2\) ✓
- \(5x \cdot 3y + (-4y) \cdot 2x = 15xy - 8xy = 7xy\) ✓
- \((-4y)(3y) = -12y^2\) ✓

Entonces:
$$10x^2 + 7xy - 12y^2 = (5x - 4y)(2x + 3y) = 0$$

Esto requiere \(5x = 4y\) o \(2x = -3y\).

**Paso 2: Analizar el caso \(5x = 4y\).**

Las soluciones enteras son \(x = 4k\), \(y = 5k\) con \(k \in \mathbb{Z}\). Las restricciones dan:

- \(|x| \le 100 \Rightarrow |4k| \le 100 \Rightarrow |k| \le 25\)
- \(|y| \le 100 \Rightarrow |5k| \le 100 \Rightarrow |k| \le 20\)

La condición más estricta es \(|k| \le 20\), dando \(41\) pares.

**Paso 3: Analizar el caso \(2x = -3y\).**

Las soluciones enteras son \(x = 3m\), \(y = -2m\) con \(m \in \mathbb{Z}\). Las restricciones dan:

- \(|x| \le 100 \Rightarrow |3m| \le 100 \Rightarrow |m| \le 33\)
- \(|y| \le 100 \Rightarrow |-2m| \le 100 \Rightarrow |m| \le 50\)

La condición más estricta es \(|m| \le 33\), dando \(67\) pares.

**Paso 4: Verificar el solapamiento entre ambos casos.**

Un par \((x, y)\) que satisface ambas condiciones debe cumplir:
$$5x = 4y \quad \text{y} \quad 2x = -3y$$

Sustituyendo \(x = 4k\), \(y = 5k\) en la segunda condición:
$$2(4k) = -3(5k) \implies 8k = -15k \implies 23k = 0 \implies k = 0$$

El único solapamiento es \((0, 0)\).

**Paso 5: Contar el total.**

$$41 + 67 - 1 = \boxed{107}$$