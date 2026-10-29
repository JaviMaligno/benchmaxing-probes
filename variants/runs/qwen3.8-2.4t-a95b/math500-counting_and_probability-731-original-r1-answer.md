

Sea el rectángulo centrado en \(O=(0,0)\), con vértices \((\pm a,\pm b)\). Entonces \(AB=2a\), \(AD=2b\), y por tanto \(a/b=k\).

Consideremos el primer cuadrante dentro del rectángulo: \(0\le x\le a\), \(0\le y\le b\). Para un punto \(P=(x,y)\) en ese cuadrante, el vértice más cercano es \(B=(a,b)\), ya que los otros vértices están más lejos en al menos una coordenada. Así que basta exigir que \(P\) esté más cerca de \(O\) que de \(B\).

La condición es

\[
x^2+y^2 < (x-a)^2+(y-b)^2.
\]

Simplificando,

\[
2ax+2by < a^2+b^2,
\]

o sea

\[
ax+by < \frac{a^2+b^2}{2}.
\]

La frontera es la recta

\[
ax+by=\frac{a^2+b^2}{2}.
\]

Esta recta pasa por \(\left(\frac a2,\frac b2\right)\), que es el centro del rectángulo correspondiente al primer cuadrante. Cualquier recta que pasa por el centro de un rectángulo divide su área en dos partes iguales. Por tanto, en el primer cuadrante, exactamente la mitad de los puntos están más cerca de \(O\) que de \(B\).

Por simetría, lo mismo ocurre en cada uno de los cuatro cuadrantes. Entonces el área favorable total es la mitad del área del rectángulo.

Por lo tanto, la probabilidad es

\[
\boxed{\frac{1}{2}}
\]