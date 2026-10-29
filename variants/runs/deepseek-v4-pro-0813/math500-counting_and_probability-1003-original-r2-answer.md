Vamos a resolver el problema.

Sea la cara \(F\) con número \(a\). La cara opuesta tiene número \(7-a\). La probabilidad de \(F\) es \(p=m/n>\frac16\), la de su opuesta es \(q<\frac16\), y las otras cuatro caras tienen probabilidad \(\frac16\).

Como la suma de todas las probabilidades es 1:

\[
p+q+4\cdot\frac16=1
\]

\[
p+q=1-\frac46=\frac13.
\]

Además, al lanzar dos dados, queremos obtener suma 7. Las parejas de caras opuestas suman 7:

\[
a+(7-a)=7.
\]

Las combinaciones que suman 7 son exactamente las tres parejas de caras opuestas:

- \(F\) y su opuesta,
- las otras dos parejas opuestas.

Para una pareja opuesta con probabilidades \(x,y\), la probabilidad de obtener esa suma es \(2xy\).

Para la pareja que involucra a \(F\): \(2pq\).

Para las otras dos parejas, cada cara tiene probabilidad \(\frac16\), así que cada pareja aporta:

\[
2\cdot\frac16\cdot\frac16=\frac{2}{36}=\frac{1}{18}.
\]

Entonces la probabilidad total de suma 7 es:

\[
2pq+2\cdot\frac{1}{18}=2pq+\frac19.
\]

Igualamos a \(\frac{47}{288}\):

\[
2pq+\frac19=\frac{47}{288}.
\]

Calculamos:

\[
\frac{47}{288}-\frac19=\frac{47}{288}-\frac{32}{288}=\frac{15}{288}=\frac{5}{96}.
\]

Por tanto:

\[
2pq=\frac{5}{96}
\]

\[
pq=\frac{5}{192}.
\]

Tenemos el sistema:

\[
p+q=\frac13,\qquad pq=\frac{5}{192}.
\]

Las soluciones son las raíces de:

\[
x^2-\frac13x+\frac{5}{192}=0.
\]

Multiplicamos por 192:

\[
192x^2-64x+5=0.
\]

Resolvemos:

\[
x=\frac{64\pm\sqrt{64^2-4\cdot192\cdot5}}{2\cdot192}
=\frac{64\pm\sqrt{4096-3840}}{384}
=\frac{64\pm16}{384}.
\]

Las raíces son:

\[
\frac{64+16}{384}=\frac{80}{384}=\frac{5}{24}
\]

y

\[
\frac{64-16}{384}=\frac{48}{384}=\frac18.
\]

Como \(p>\frac16\) y \(q<\frac16\), tenemos:

\[
p=\frac{5}{24},\qquad q=\frac18.
\]

Por tanto, \(m=5\), \(n=24\), y:

\[
m+n=29.
\]

\[
\boxed{29}
\]