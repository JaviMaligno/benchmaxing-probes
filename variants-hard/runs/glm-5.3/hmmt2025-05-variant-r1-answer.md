Sea

\[
\alpha=\sqrt5+\sqrt3,\qquad \beta=\sqrt5-\sqrt3.
\]

Entonces

\[
\alpha+\beta=2\sqrt5,\qquad \alpha-\beta=2\sqrt3,\qquad \alpha\beta=2.
\]

Buscamos el menor grado posible de un polinomio mónico \(F\in\mathbb Z[x]\) con

\[
F(\alpha)=F(\beta).
\]

### Grado \(1\)

Si \(F(x)=x+a\), entonces

\[
F(\alpha)-F(\beta)=\alpha-\beta=2\sqrt3\neq 0.
\]

Así que no hay polinomios de grado \(1\).

### Grado \(2\)

Si

\[
F(x)=x^2+ax+b,
\]

entonces

\[
F(\alpha)-F(\beta)
=(\alpha-\beta)(\alpha+\beta+a)
=2\sqrt3(2\sqrt5+a).
\]

Como \(a\in\mathbb Z\), el factor \(2\sqrt5+a\) nunca es \(0\). Por tanto tampoco hay polinomios de grado \(2\).

### Grado \(3\)

Sea

\[
F(x)=x^3+ax^2+bx+c.
\]

Entonces

\[
F(\alpha)-F(\beta)
=(\alpha-\beta)\bigl(\alpha^2+\alpha\beta+\beta^2+a(\alpha+\beta)+b\bigr).
\]

Ahora,

\[
\alpha^2+\beta^2=(\alpha+\beta)^2-2\alpha\beta=20-4=16,
\]

so

\[
\alpha^2+\alpha\beta+\beta^2=16+2=18.
\]

Por lo tanto,

\[
F(\alpha)-F(\beta)
=2\sqrt3(18+2a\sqrt5+b).
\]

Para que esto sea \(0\), necesitamos

\[
18+2a\sqrt5+b=0.
\]

Como \(a,b\in\mathbb Z\), esto obliga a

\[
a=0,\qquad b=-18.
\]

Así, todo polinomio de grado mínimo tiene la forma

\[
R(x)=x^3-18x+c,
\]

con \(c\in\mathbb Z\).

Ahora,

\[
R(6)-R(1)
=(216-108+c)-(1-18+c)
=108-(-17)
=125.
\]

\[
\boxed{125}
\]