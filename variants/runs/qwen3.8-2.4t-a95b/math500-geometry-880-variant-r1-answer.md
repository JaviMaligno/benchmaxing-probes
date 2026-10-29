

Sean las paredes laterales \(x=0\) y \(x=15\), la pared trasera \(y=0\), la pared delantera \(y=12\), y la altura \(0\le z\le 9\).

La araña está en  
\[
S=(0,1,8)
\]
y la polilla en  
\[
M=(15,11,1).
\]

El camino más corto se obtiene desplegando las caras en el orden:

\[
\text{pared lateral izquierda} \to \text{techo} \to \text{pared delantera} \to \text{pared lateral derecha}.
\]

Colocando el techo como un rectángulo \(15\times 12\):

- La araña queda en \((-1,1)\), pues está a \(1\) pie del techo y a \(1\) pie de la pared trasera.
- La polilla queda en \((16,20)\): \(15+1\) pies en la dirección horizontal, y \(12+8\) pies en la otra dirección, ya que está a \(8\) pies del techo.

Así, la distancia en el despliegue es

\[
\sqrt{(16-(-1))^2+(20-1)^2}
=
\sqrt{17^2+19^2}
=
\sqrt{650}
=
5\sqrt{26}.
\]

Otros despliegues posibles dan distancias mayores, por ejemplo directamente por el techo da \(26\).

\[
\boxed{5\sqrt{26}}
\]