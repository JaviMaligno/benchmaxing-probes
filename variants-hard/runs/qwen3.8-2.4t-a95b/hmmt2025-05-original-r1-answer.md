Sea  
\[
\alpha=\sqrt3+\sqrt2,\qquad \beta=\sqrt3-\sqrt2.
\]
Entonces
\[
\alpha+\beta=2\sqrt3,\qquad \alpha\beta=3-2=1.
\]

Queremos polinomios mónicos \(P\in\mathbb Z[x]\) no constantes tales que
\[
P(\alpha)=P(\beta).
\]

Probemos primero grados pequeños.

**Grado 1:**  
Si \(P(x)=x+c\), entonces
\[
P(\alpha)-P(\beta)=\alpha-\beta=2\sqrt2\neq 0.
\]
No funciona.

**Grado 2:**  
Si \(P(x)=x^2+ax+b\), entonces
\[
P(\alpha)-P(\beta)=\alpha^2-\beta^2+a(\alpha-\beta).
\]
Como \(\alpha^2-\beta^2=(\alpha-\beta)(\alpha+\beta)\), obtenemos
\[
P(\alpha)-P(\beta)=(\alpha-\beta)(\alpha+\beta+a)
=2\sqrt2(2\sqrt3+a).
\]
Para que esto sea cero necesitaríamos \(a=-2\sqrt3\), que no es entero. No funciona.

**Grado 3:**  
Sea
\[
P(x)=x^3+ax^2+bx+c.
\]
Entonces
\[
P(\alpha)-P(\beta)
=(\alpha^3-\beta^3)+a(\alpha^2-\beta^2)+b(\alpha-\beta).
\]
Factorizando \(\alpha-\beta\):
\[
P(\alpha)-P(\beta)
=(\alpha-\beta)\left(\alpha^2+\alpha\beta+\beta^2+a(\alpha+\beta)+b\right).
\]
Ahora
\[
\alpha^2+\beta^2=(\alpha+\beta)^2-2\alpha\beta
=(2\sqrt3)^2-2=12-2=10.
\]
Por tanto,
\[
\alpha^2+\alpha\beta+\beta^2=10+1=11.
\]
Así que la condición es
\[
11+a(2\sqrt3)+b=0.
\]
Como \(a,b\in\mathbb Z\), la parte racional y la parte con \(\sqrt3\) deben anularse por separado:
\[
2a=0\implies a=0,
\]
\[
11+b=0\implies b=-11.
\]
El coeficiente \(c\) queda libre. Luego los polinomios de grado mínimo son
\[
Q(x)=x^3-11x+c,\qquad c\in\mathbb Z.
\]

Finalmente,
\[
Q(10)-Q(0)=\bigl(10^3-11\cdot 10+c\bigr)-c
=1000-110=890.
\]

\[
\boxed{890}
\]