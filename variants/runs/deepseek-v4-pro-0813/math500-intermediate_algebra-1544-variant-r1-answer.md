Vamos a razonar paso a paso.

Sea la ecuación cuadrática

\[
x^2 + px + q = 0
\]

con raíces \(r_1, r_2\). La condición es: si \(t\) es raíz, entonces \(f(t) = t^2 - 4t + 6\) también es raíz.

Como la ecuación es cuadrática, tiene a lo sumo dos raíces. Por tanto, \(f\) debe mandar el conjunto de raíces \(\{r_1, r_2\}\) dentro de sí mismo.

**Caso 1: raíz doble.**

Si \(r_1 = r_2 = r\), entonces \(f(r) = r\), es decir:

\[
r^2 - 4r + 6 = r
\]

\[
r^2 - 5r + 6 = 0
\]

\[
(r-2)(r-3) = 0
\]

Así \(r = 2\) o \(r = 3\).

- Si \(r = 2\): la ecuación es \((x-2)^2 = x^2 - 4x + 4\), luego \(p = -4, q = 4\).
- Si \(r = 3\): la ecuación es \((x-3)^2 = x^2 - 6x + 9\), luego \(p = -6, q = 9\).

**Caso 2: raíces distintas.**

Sean \(r_1 \neq r_2\). Entonces \(f(r_1)\) y \(f(r_2)\) deben ser raíces. Como \(f\) no es constante, hay dos subcasos.

**Subcaso 2a: \(f\) fija ambas raíces.**

Entonces \(f(r_1) = r_1\) y \(f(r_2) = r_2\). Como vimos, los puntos fijos de \(f\) son \(2\) y \(3\). Luego \(\{r_1, r_2\} = \{2, 3\}\).

La ecuación es \((x-2)(x-3) = x^2 - 5x + 6\), luego \(p = -5, q = 6\).

**Subcaso 2b: \(f\) intercambia las raíces.**

Entonces \(f(r_1) = r_2\) y \(f(r_2) = r_1\). Aplicando \(f\) dos veces:

\[
f(f(r_1)) = f(r_2) = r_1
\]

Así \(r_1\) y \(r_2\) son puntos de período 2 de \(f\). Calculemos \(f(f(x))\):

\[
f(x) = x^2 - 4x + 6
\]

\[
f(f(x)) = (x^2 - 4x + 6)^2 - 4(x^2 - 4x + 6) + 6
\]

Desarrollamos:

\[
(x^2 - 4x + 6)^2 = x^4 - 8x^3 + 28x^2 - 48x + 36
\]

\[
-4(x^2 - 4x + 6) = -4x^2 + 16x - 24
\]

Sumando todo con \(+6\):

\[
f(f(x)) = x^4 - 8x^3 + 24x^2 - 32x + 18
\]

Los puntos de período 2 satisfacen \(f(f(x)) = x\) pero \(f(x) \neq x\). Entonces:

\[
x^4 - 8x^3 + 24x^2 - 33x + 18 = 0
\]

Sabemos que los puntos fijos \(x = 2, 3\) son soluciones, así que factorizamos \((x-2)(x-3) = x^2 - 5x + 6\):

Dividimos \(x^4 - 8x^3 + 24x^2 - 33x + 18\) entre \(x^2 - 5x + 6\):

\[
x^4 - 8x^3 + 24x^2 - 33x + 18 = (x^2 - 5x + 6)(x^2 - 3x + 3)
\]

Verifiquemos: \((x^2 - 5x + 6)(x^2 - 3x + 3) = x^4 - 3x^3 + 3x^2 - 5x^3 + 15x^2 - 15x + 6x^2 - 18x + 18 = x^4 - 8x^3 + 24x^2 - 33x + 18\). Correcto.

Los puntos de período 2 son las raíces de \(x^2 - 3x + 3 = 0\):

\[
x = \frac{3 \pm \sqrt{9 - 12}}{2} = \frac{3 \pm i\sqrt{3}}{2}
\]

Estas dos raíces son conjugadas y distintas. Si \(r_1, r_2\) son estas dos, entonces \(f\) las intercambia. La ecuación con estas raíces es:

\[
x^2 - 3x + 3 = 0
\]

luego \(p = -3, q = 3\).

**Total de ecuaciones:**

1. \(x^2 - 4x + 4 = 0\)
2. \(x^2 - 6x + 9 = 0\)
3. \(x^2 - 5x + 6 = 0\)
4. \(x^2 - 3x + 3 = 0\)

Son 4 ecuaciones.

\[
\boxed{4}
\]