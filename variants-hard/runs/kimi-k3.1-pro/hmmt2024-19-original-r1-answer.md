Sea \(a=f\), \(b=g\) y \(c=h\). De las igualdades dadas se obtiene
\[
c=b^{-1}a^{-1}b=ba^{-1}b^{-1},\qquad c=a^{-1}ba,
\]
además de
\[
aba=bab,\qquad ab^2=b^2a.
\]
Combinando estas relaciones resulta
\[
a^{-2}ba^2=b^{-1}.
\]
Al elevar al cuadrado y usar que \(a\) conmuta con \(b^2\), obtenemos \(b^2=b^{-2}\), es decir, \(b^4=e\). Por simetría, también \(a^4=c^4=e\).

Si los elementos tuvieran orden \(4\), serían \(4\)-ciclos. Las relaciones anteriores implicarían \(a^2=b^2\), por lo que \(b=a\) o \(b=a^{-1}\); en ambos casos, al sustituir en las ecuaciones originales, se deduce que \(a^2=e\), una contradicción. Por tanto, \(a,b,c\) son involuciones.

Para involuciones, el sistema equivale a
\[
c=aba=bab.
\]
Además,
\[
aba=bab\iff (ab)^3=e.
\]
Así, basta contar las parejas ordenadas de involuciones \((a,b)\) cuyo producto tiene orden \(1\) o \(3\), pues \(c\) queda determinada.

- **Si \(ab=e\):** \(a=b\). En \(S_5\) hay
  \[
  1+\binom52+3\binom54=26
  \]
  involuciones.

- **Si \(ab\) es un \(3\)-ciclo y \(a,b\) son transposiciones:** deben compartir exactamente un punto. Hay \(10\) ternas de puntos y \(6\) parejas ordenadas para cada una: \(60\) parejas.

- **Si \(a,b\) son productos de dos transposiciones disjuntas:** deben compartir una transposición. Hay \(10\) elecciones para esta y \(3\cdot2=6\) para las otras dos: \(60\) parejas.

En total,
\[
26+60+60=\boxed{146}.
\]