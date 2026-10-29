

Sea

\[
\alpha=\sqrt5+\sqrt3,\qquad \beta=\sqrt5-\sqrt3.
\]

Queremos polinomios mónicos \(F\in\mathbb Z[x]\), no constantes, tales que \(F(\alpha)=F(\beta)\).

Primero calculamos algunos valores útiles:

\[
\alpha+\beta=2\sqrt5,\qquad \alpha\beta=(\sqrt5+\sqrt3)(\sqrt5-\sqrt3)=5-3=2.
\]

Además,

\[
\alpha^2+\beta^2=(\alpha+\beta)^2-2\alpha\beta=(2\sqrt5)^2-4=20-4=16.
\]

Probemos grados pequeños.

### Grado 1

Si \(F(x)=x+c\), entonces

\[
F(\alpha)-F(\beta)=\alpha-\beta=2\sqrt3\neq 0.
\]

No funciona.

### Grado 2

Si \(F(x)=x^2+ax+b\), entonces

\[
F(\alpha)-F(\beta)=\alpha^2-\beta^2+a(\alpha-\beta)
=(\alpha-\beta)(\alpha+\beta+a).
\]

Como \(\alpha\neq\beta\), necesitaríamos

\[
\alpha+\beta+a=2\sqrt5+a=0,
\]

imposible para \(a\in\mathbb Z\). No funciona.

### Grado 3

Sea

\[
F(x)=x^3+ax^2+bx+c.
\]

Entonces

\[
F(\alpha)-F(\beta)
=(\alpha-\beta)\bigl(\alpha^2+\alpha\beta+\beta^2+a(\alpha+\beta)+b\bigr).
\]

De nuevo \(\alpha\neq\beta\), así que necesitamos

\[
\alpha^2+\alpha\beta+\beta^2+a(\alpha+\beta)+b=0.
\]

Usando los valores calculados,

\[
\alpha^2+\alpha\beta+\beta^2=16+2=18,
\]

por lo que la condición es

\[
18+2a\sqrt5+b=0.
\]

Como \(a,b\in\mathbb Z\) y \(1,\sqrt5\) son linealmente independientes sobre \(\mathbb Q\), debemos tener

\[
a=0,\qquad b=-18.
\]

Así, los polinomios mónicos de grado mínimo son

\[
R(x)=x^3-18x+c,
\]

con \(c\in\mathbb Z\). El grado mínimo es \(3\).

Finalmente,

\[
R(6)=6^3-18\cdot 6+c=216-108+c=108+c,
\]

\[
R(1)=1^3-18\cdot 1+c=1-18+c=-17+c.
\]

Por tanto,

\[
R(6)-R(1)=(108+c)-(-17+c)=125.
\]

\[
\boxed{125}
\]