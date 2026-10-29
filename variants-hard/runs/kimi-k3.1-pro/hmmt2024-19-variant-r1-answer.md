Escribimos las composiciones como productos. De
\[
pqr=q,\qquad qrp=r,\qquad rpq=p
\]
obtenemos, componiendo adecuadamente,
\[
pr=qp=rq.
\]
Análogamente, las otras tres igualdadess dan
\[
pq=qr=rp.
\]

De \(pqr=q\) se sigue \(r=q^{-1}p^{-1}q\), mientras que \(pq=qr\) da \(r=q^{-1}pq\). Por tanto \(p=p^{-1}\), es decir, \(p^2=e\). Similarmente, \(q^2=r^2=e\), así que \(p,q,r\) son involuciones.

Ahora \(r=qpq\), y la relación \(pq=rp\) equivale a
\[
pqp=qpq.
\]
En consecuencia,
\[
(pq)^3=(pqp)(qpq)=e.
\]
Recíprocamente, si \(p,q\) son involuciones con \((pq)^3=e\), definiendo \(r=qpq\) se cumplen todas las condiciones. Basta, pues, contar las parejas ordenadas \((p,q)\).

La permutación \(pq\) solo tiene ciclos de longitud \(1\) o \(3\). En los puntos fijos de \(pq\), las involuciones \(p\) y \(q\) coinciden. Sobre cada ciclo de longitud \(3\), actúan como dos transposiciones distintas; hay \(3\cdot2=6\) parejas ordenadas posibles.

- **Sin ciclos de longitud \(3\):** \(p=q\), una involución cualquiera de \(S_6\). Su número es
  \[
  1+15+45+15=76.
  \]

- **Un ciclo de longitud \(3\):** elegimos su soporte, las dos transposiciones y una involución arbitraria sobre los tres puntos restantes:
  \[
  \binom63\cdot6\cdot4=480.
  \]

- **Dos ciclos de longitud \(3\):** dividimos los seis puntos en dos bloques no ordenados y elegimos independientemente las transposiciones en cada bloque:
  \[
  \frac{\binom63\binom33}{2}\cdot6^2=360.
  \]

Cada pareja determina un único \(r\), por lo que el número total de triples es
\[
\boxed{916}
\]