Sea \(\alpha=\sqrt3+\sqrt2\) y \(\beta=\sqrt3-\sqrt2\). Entonces
\[
\alpha-\beta=2\sqrt2,\qquad \alpha^2-\beta^2=4\sqrt6,
\]
y
\[
\alpha^3=9\sqrt3+11\sqrt2,\qquad \beta^3=9\sqrt3-11\sqrt2.
\]

- No existe un \(P\) lineal mónico, pues \(P(\alpha)-P(\beta)=2\sqrt2\ne0\).
- Si \(P(x)=x^2+cx+d\), entonces
  \[
  P(\alpha)-P(\beta)=4\sqrt6+2c\sqrt2\ne0,
  \]
  así que tampoco hay soluciones cuadráticas.

Para \(P(x)=x^3+ax^2+bx+c\), se obtiene
\[
P(\alpha)-P(\beta)=(22+2b)\sqrt2+4a\sqrt6.
\]
Como \(\sqrt2\) y \(\sqrt6\) son linealmente independientes sobre \(\mathbb Q\), debe cumplirse \(a=0\) y \(b=-11\). Por tanto,
\[
Q(x)=x^3-11x+c
\]
para cualquier \(c\in\mathbb Z\), y el grado mínimo es \(3\). Finalmente,
\[
Q(10)-Q(0)=(1000-1100+c)-c=\boxed{-100}.
\]