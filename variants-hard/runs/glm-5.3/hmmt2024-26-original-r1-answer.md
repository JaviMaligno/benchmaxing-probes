Sea \(P\) el centro de la circunferencia de diámetro \(BB'\), y sea \(Q\) el centro de la de diámetro \(CC'\). Denotemos sus radios por \(\rho\) y \(\sigma\), respectivamente.

Como son tangentes exteriormente en \(T\), el punto \(T\) está en \(PQ\), con
\[
PT=\rho,\qquad TQ=\sigma,\qquad PQ=\rho+\sigma.
\]

Además,
\[
AB'=18-2\rho,\qquad AC'=36-2\sigma.
\]
Por la potencia de \(A\) respecto a \(\omega\),
\[
AB\cdot AB'=AC\cdot AC',
\]
entonces
\[
18(18-2\rho)=36(36-2\sigma).
\]
Esto simplifica a
\[
\sigma=\frac{\rho+27}{2}.
\]

Ahora \(P\) y \(Q\) son puntos medios de \(BB'\) y \(CC'\), así que
\[
AP=18-\rho,\qquad AQ=36-\sigma.
\]
En el triángulo \(APQ\), el punto \(T\) divide \(PQ\) en \(\rho\) y \(\sigma\). Por el teorema de Stewart,
\[
AQ^2\cdot PT+AP^2\cdot TQ=PQ(AT^2+PT\cdot TQ).
\]
Sustituyendo \(AT=12\):
\[
(36-\sigma)^2\rho+(18-\rho)^2\sigma=(\rho+\sigma)(144+\rho\sigma).
\]
Expandiendo y simplificando,
\[
32\rho+5\sigma-3\rho\sigma=0.
\]
Usando \(\sigma=(\rho+27)/2\):
\[
\rho^2+4\rho-45=0,
\]
de donde \(\rho=5\) por ser positivo. Entonces \(\sigma=16\).

Por lo tanto,
\[
AP=13,\qquad AQ=20,\qquad PQ=21.
\]

Finalmente, como \(O\) es el centro de \(\omega\), las líneas \(OP\) y \(OQ\) son perpendiculares a las cuerdas \(BB'\) y \(CC'\). Así,
\[
\angle APO=\angle AQO=90^\circ,
\]
lo que implica que \(A,P,O,Q\) están en una circunferencia de diámetro \(AO\). Por tanto, \(AO\) es el doble del circunradio del triángulo \(APQ\).

El semiperímetro de \(\triangle APQ\) es \(27\), y su área es
\[
\Delta=\sqrt{27\cdot 14\cdot 7\cdot 6}=126.
\]
Su circunradio es
\[
\frac{13\cdot 20\cdot 21}{4\cdot 126}=\frac{65}{6}.
\]
Así,
\[
AO=2\cdot \frac{65}{6}=\frac{65}{3}.
\]

\[
\boxed{\frac{65}{3}}
\]