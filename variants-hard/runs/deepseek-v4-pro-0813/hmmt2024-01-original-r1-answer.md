Vamos a razonar paso a paso.

Sean \(r, s, t\) reales no nulos.

**Primer polinomio:** \(x^2 + rx + s\) tiene raíces \(s\) y \(t\).

Por relaciones de Cardano (o Viète), para un polinomio \(x^2 + rx + s\) con raíces \(s\) y \(t\):

- Suma de raíces: \(s + t = -r\).
- Producto de raíces: \(st = s\).

Como \(s \neq 0\), de \(st = s\) se deduce:

\[
t = 1.
\]

Entonces la suma queda:

\[
s + 1 = -r \quad\Rightarrow\quad r = -s - 1.
\]

**Segundo polinomio:** \(x^2 + tx + r\) tiene \(5\) como raíz.

Sustituimos \(x = 5\):

\[
5^2 + t \cdot 5 + r = 0.
\]

Como \(t = 1\):

\[
25 + 5 + r = 0 \quad\Rightarrow\quad r = -30.
\]

Ahora usamos \(r = -s - 1\):

\[
-s - 1 = -30 \quad\Rightarrow\quad -s = -29 \quad\Rightarrow\quad s = 29.
\]

Verificamos rápidamente:

- Primer polinomio: \(x^2 + rx + s\) con \(r = -30\), \(s = 29\), es decir \(x^2 - 30x + 29\). Sus raíces son \(29\) y \(1\), que son \(s\) y \(t\). Correcto.
- Segundo polinomio: \(x^2 + tx + r = x^2 + x - 30\). Evaluado en \(5\): \(25 + 5 - 30 = 0\). Correcto.

Por lo tanto:

\[
\boxed{29}
\]