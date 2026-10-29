Vamos a resolver la ecuación

\[
12x^2 - xy - 6y^2 = 0
\]

## Paso 1: Ver si la cuadrática se factoriza

Buscamos factores de la forma \((ax + by)(cx + dy)\). Probemos:

\[
(3x + 2y)(4x - 3y) = 12x^2 - 9xy + 8xy - 6y^2 = 12x^2 - xy - 6y^2
\]

Funciona. Entonces la ecuación es:

\[
(3x + 2y)(4x - 3y) = 0
\]

## Paso 2: Analizar los dos casos

**Caso 1:** \(3x + 2y = 0\), es decir,

\[
y = -\frac{3}{2}x
\]

Para que \(y\) sea entero, \(x\) debe ser par. Sea \(x = 2k\), con \(k\) entero. Entonces:

\[
y = -3k
\]

Condición: \(-100 \le 2k \le 100\) y \(-100 \le -3k \le 100\).

- De \(-100 \le 2k \le 100\): \(-50 \le k \le 50\).
- De \(-100 \le -3k \le 100\): \(-\frac{100}{3} \le k \le \frac{100}{3}\), es decir, \(-33.\overline{3} \le k \le 33.\overline{3}\).

Intersección: \(-33 \le k \le 33\). Esto da \(33 - (-33) + 1 = 67\) pares.

**Caso 2:** \(4x - 3y = 0\), es decir,

\[
y = \frac{4}{3}x
\]

Para que \(y\) sea entero, \(x\) debe ser múltiplo de 3. Sea \(x = 3k\), con \(k\) entero. Entonces:

\[
y = 4k
\]

Condición: \(-100 \le 3k \le 100\) y \(-100 \le 4k \le 100\).

- De \(-100 \le 3k \le 100\): \(-33.\overline{3} \le k \le 33.\overline{3}\).
- De \(-100 \le 4k \le 100\): \(-25 \le k \le 25\).

Intersección: \(-25 \le k \le 25\). Esto da \(25 - (-25) + 1 = 51\) pares.

## Paso 3: ¿Hay pares repetidos?

Hay un par que cumple ambas condiciones: \((0, 0)\), con \(x = 0\) e \(y = 0\).

- En el caso 1 aparece con \(k = 0\).
- En el caso 2 aparece con \(k = 0\).

Se cuenta dos veces, así que hay que restar 1.

Total:

\[
67 + 51 - 1 = 117
\]

\[
\boxed{117}
\]