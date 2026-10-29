Vamos a resolver la ecuación

\[
12x^2 - xy - 6y^2 = 0.
\]

### Paso 1: Factorizar la forma cuadrática

Tratamos la expresión como cuadrática en \(x\):

\[
12x^2 - xy - 6y^2.
\]

Buscamos factorizarla como \((ax + by)(cx + dy)\). Multiplicando:

\[
(ax + by)(cx + dy) = acx^2 + (ad + bc)xy + bd y^2.
\]

Necesitamos:

\[
ac = 12,\qquad ad + bc = -1,\qquad bd = -6.
\]

Probamos \(a = 3\), \(c = 4\), de modo que \(ac = 12\). Luego \(bd = -6\). Probamos \(b = 2\), \(d = -3\), que da \(bd = -6\). Entonces:

\[
ad + bc = 3(-3) + 2(4) = -9 + 8 = -1.
\]

¡Funciona! Por lo tanto:

\[
12x^2 - xy - 6y^2 = (3x + 2y)(4x - 3y).
\]

### Paso 2: Resolver la ecuación factorizada

La ecuación \((3x + 2y)(4x - 3y) = 0\) implica:

\[
3x + 2y = 0 \quad \text{o} \quad 4x - 3y = 0.
\]

#### Caso 1: \(3x + 2y = 0\)

\[
y = -\frac{3x}{2}.
\]

Para que \(y\) sea entero, \(x\) debe ser par. Como \(x\) está entre \(-100\) y \(100\), los valores posibles de \(x\) son los enteros pares en ese rango:

\[
-100, -98, \ldots, 98, 100.
\]

Hay \(101\) enteros pares en \([-100, 100]\). Para cada uno, \(y = -3x/2\) es entero. Además, como \(|x| \le 100\),

\[
|y| = \frac{3|x|}{2} \le 150.
\]

Verificamos el rango de \(y\): \(y\) debe estar entre \(-100\) y \(100\), inclusive. De \(y = -3x/2\):

\[
|y| \le 100 \implies \frac{|3x|}{2} \le 100 \implies |x| \le \frac{200}{3} \approx 66.67.
\]

Como \(x\) es par, los valores de \(x\) que satisfacen \(|x| \le 66\) son pares desde \(-66\) hasta \(66\). Hay \(67\) pares en \([-66, 66]\).

#### Caso 2: \(4x - 3y = 0\)

\[
y = \frac{4x}{3}.
\]

Para que \(y\) sea entero, \(x\) debe ser divisible por \(3\). Además:

\[
|y| \le 100 \implies \frac{4|x|}{3} \le 100 \implies |x| \le 75.
\]

Los múltiplos de \(3\) en \([-75, 75]\) son:

\[
-75, -72, \ldots, 72, 75.
\]

Hay \(51\) múltiplos de \(3\) en \([-75, 75]\).

### Paso 3: Contar pares sin solapamiento

Los dos casos son disjuntos salvo si ambas ecuaciones se cumplen a la vez:

\[
3x + 2y = 0 \quad \text{y} \quad 4x - 3y = 0.
\]

Resolviendo el sistema, de la primera \(y = -3x/2\), sustituyendo en la segunda:

\[
4x - 3(-3x/2) = 4x + \frac{9x}{2} = \frac{17x}{2} = 0 \implies x = 0.
\]

Entonces \(y = 0\). El punto \((0, 0)\) satisface ambas ecuaciones y se contaría en ambos casos. Por lo tanto, restamos \(1\) por el solapamiento.

### Paso 4: Total

\[
\text{Total} = 67 + 51 - 1 = 117.
\]

La respuesta final es:

\[
\boxed{117}
\]