Vamos a resolver la ecuación paso a paso.

La ecuación es:

\[
10x^2 + 7xy - 12y^2 = 0
\]

---

**1. Factorizar la ecuación**

Buscamos factorizar el polinomio \(10x^2 + 7xy - 12y^2\).

Como es homogéneo de grado 2, podemos escribir:

\[
10x^2 + 7xy - 12y^2 = (ax + by)(cx + dy)
\]

Al expandir:

\[
(ax + by)(cx + dy) = acx^2 + (ad + bc)xy + bdy^2
\]

Entonces:

\[
\begin{aligned}
ac &= 10, \\
ad + bc &= 7, \\
bd &= -12.
\end{aligned}
\]

Probamos \(a = 2\), \(c = 5\), pues \(2 \cdot 5 = 10\). Luego:

\[
bd = -12.
\]

Probamos \(b = 3\), \(d = -4\), pues \(3 \cdot (-4) = -12\).

Comprobamos el término cruzado:

\[
ad + bc = 2(-4) + 3(5) = -8 + 15 = 7
\]

Funciona. Entonces:

\[
10x^2 + 7xy - 12y^2 = (2x + 3y)(5x - 4y)
\]

---

**2. Resolver la ecuación**

\[
(2x + 3y)(5x - 4y) = 0
\]

Hay dos casos:

**Caso A:**

\[
2x + 3y = 0
\]

Despejamos:

\[
2x = -3y \quad \Rightarrow \quad x = -\frac{3}{2}y
\]

**Caso B:**

\[
5x - 4y = 0
\]

Despejamos:

\[
5x = 4y \quad \Rightarrow \quad x = \frac{4}{5}y
\]

---

**3. Contar soluciones enteras en el rango**

Tanto \(x\) como \(y\) son enteros entre \(-100\) y \(100\), inclusive. Hay que encontrar los pares que cumplen cada caso y tener cuidado de no contar dos veces el par que satisface ambos casos.

Para que los dos factores sean cero a la vez:

\[
2x + 3y = 0 \quad \text{y} \quad 5x - 4y = 0
\]

Resolvemos el sistema. De la primera, \(x = -\frac{3}{2}y\). Sustituyendo en la segunda:

\[
5\left(-\frac{3}{2}y\right) - 4y = 0
\]

\[
-\frac{15}{2}y - 4y = 0
\]

\[
-\frac{23}{2}y = 0 \quad \Rightarrow \quad y = 0
\]

Entonces \(x = 0\). Es decir, \((0,0)\) satisface ambos casos, así que habrá que restarlo de la suma.

---

**Caso A: \(x = -\frac{3}{2}y\)**

Para que \(x\) sea entero, \(y\) debe ser múltiplo de 2, es decir, \(y = 2k\), con \(k\) entero. Entonces:

\[
x = -\frac{3}{2}(2k) = -3k
\]

Las restricciones:

\[
-100 \le x \le 100 \quad \Rightarrow \quad -100 \le -3k \le 100
\]

\[
-\frac{100}{3} \le k \le \frac{100}{3}
\]

Es decir:

\[
-33{,}\overline{3} \le k \le 33{,}\overline{3}
\]

Como \(k\) es entero:

\[
-33 \le k \le 33
\]

Eso da:

\[
33 - (-33) + 1 = 67
\]

valores de \(k\).

También verificamos \(y = 2k\):

\[
-100 \le 2k \le 100 \quad \Rightarrow \quad -50 \le k \le 50
\]

La condición más restrictiva es \(-33 \le k \le 33\), así que hay **67** soluciones en el caso A.

---

**Caso B: \(x = \frac{4}{5}y\)**

Para que \(x\) sea entero, \(y\) debe ser múltiplo de 5, es decir, \(y = 5k\), con \(k\) entero. Entonces:

\[
x = \frac{4}{5}(5k) = 4k
\]

Las restricciones:

\[
-100 \le x \le 100 \quad \Rightarrow \quad -100 \le 4k \le 100
\]

\[
-25 \le k \le 25
\]

Y también:

\[
-100 \le y \le 100 \quad \Rightarrow \quad -100 \le 5k \le 100
\]

\[
-20 \le k \le 20
\]

La condición más restrictiva es \(-20 \le k \le 20\), así que hay:

\[
20 - (-20) + 1 = 41
\]

valores de \(k\). Por tanto, **41** soluciones en el caso B.

---

**4. Restar la solución repetida**

El punto \((0,0)\) fue contado en ambos casos, porque corresponde a \(k = 0\) en cada uno.

Total:

\[
67 + 41 - 1 = 107
\]

---

Por lo tanto, el número de pares ordenados \((x, y)\) es:

\[
\boxed{107}
\]