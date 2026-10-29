Vamos a razonar paso a paso.

Sean las caras del dado numeradas 1 a 6. Las caras opuestas suman 7, así que los pares opuestos son:

- (1, 6)
- (2, 5)
- (3, 4)

Sea \(F\) la cara especial con probabilidad mayor que \(1/6\). Su cara opuesta, que llamamos \(7-F\), tiene probabilidad menor que \(1/6\). Las otras cuatro caras tienen probabilidad \(1/6\).

Llamemos \(p\) a la probabilidad de obtener \(F\), y \(q\) a la probabilidad de obtener su cara opuesta. Como las probabilidades deben sumar 1:

\[
p + q + 4 \cdot \frac{1}{6} = 1
\]

\[
p + q = 1 - \frac{4}{6} = \frac{1}{3}
\]

Por tanto, \(q = \frac{1}{3} - p\).

El problema dice que la probabilidad de que la suma sea 7 al lanzar dos dados es \(47/288\).

Para obtener suma 7 con dos dados, los pares posibles son:

\[
(1,6), (6,1), (2,5), (5,2), (3,4), (4,3)
\]

Ahora, \(F\) es una de las caras, y su opuesta es \(7-F\). El par \((F, 7-F)\) involucra las dos caras especiales. Al lanzar dos dados, hay 2 formas de obtener el par \((F, 7-F)\): \((F, 7-F)\) y \((7-F, F)\). Cada una tiene probabilidad \(p \cdot q\).

Los otros dos pares de opuestos involucran caras con probabilidad \(1/6\). Para cada uno de esos dos pares, hay 2 ordenamientos distintos, cada uno con probabilidad \((1/6)(1/6)\).

Entonces la probabilidad total de suma 7 es:

\[
2pq + 2 \cdot 2 \cdot \frac{1}{36}
\]

\[
2pq + \frac{4}{36} = 2pq + \frac{1}{9}
\]

Sustituyendo \(q = \frac{1}{3} - p\):

\[
\text{Prob}(7) = 2p\left(\frac{1}{3} - p\right) + \frac{1}{9}
\]

Igualando a \(47/288\):

\[
2p\left(\frac{1}{3} - p\right) + \frac{1}{9} = \frac{47}{288}
\]

Primero, convertimos \(1/9\) a denominador 288:

\[
\frac{1}{9} = \frac{32}{288}
\]

Entonces:

\[
2p\left(\frac{1}{3} - p\right) = \frac{47}{288} - \frac{32}{288} = \frac{15}{288} = \frac{5}{96}
\]

Dividimos entre 2:

\[
p\left(\frac{1}{3} - p\right) = \frac{5}{192}
\]

\[
\frac{p}{3} - p^2 = \frac{5}{192}
\]

Multiplicamos todo por 192:

\[
64p - 192p^2 = 5
\]

\[
192p^2 - 64p + 5 = 0
\]

Aplicamos la fórmula cuadrática:

\[
p = \frac{64 \pm \sqrt{64^2 - 4 \cdot 192 \cdot 5}}{2 \cdot 192}
\]

\[
p = \frac{64 \pm \sqrt{4096 - 3840}}{384}
\]

\[
p = \frac{64 \pm \sqrt{256}}{384}
\]

\[
p = \frac{64 \pm 16}{384}
\]

Las dos soluciones son:

\[
p = \frac{80}{384} = \frac{5}{24}
\]

y

\[
p = \frac{48}{384} = \frac{1}{8}
\]

Ahora bien, \(p > 1/6\). Comparamos:

\[
\frac{5}{24} \approx 0{,}2083 > 0{,}1667
\]

\[
\frac{1}{8} = 0{,}125 < 0{,}1667
\]

Por tanto, la solución válida es \(p = \frac{5}{24}\).

Se pide \(m+n\), donde \(p = m/n\) en forma irreducible. Tenemos \(m = 5\), \(n = 24\).

\[
m + n = 5 + 24 = 29
\]

\[
\boxed{29}
\]