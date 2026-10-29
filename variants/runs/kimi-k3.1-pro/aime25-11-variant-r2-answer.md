Como \(|g(x)|\le 1\), toda intersección cumple \(x=66y^2\le 66\).

- En los tramos crecientes, \(x=y+4k\), con \(k=0,\dots,16\). Sustituyendo:
  \[
  66y^2-y-4k=0,
  \]
  y ambos puntos pertenecen al tramo. La suma de sus raíces es \(1/66\), así que aportan \(17/66\).

- En los tramos decrecientes, \(x=4k+2-y\). Para \(k=0,\dots,15\), ambos puntos pertenecen al tramo y las raíces de
  \[
  66y^2+y-(4k+2)=0
  \]
  suman \(-1/66\). Su aportación total es \(-16/66\).

- Para \(k=16\), solo aparece un punto adicional en el tramo decreciente, con
  \[
  y=\frac{-1+\sqrt{17425}}{132}
   =\frac{-1+5\sqrt{697}}{132}.
  \]

Por tanto, la suma buscada es
\[
\frac{17}{66}-\frac{16}{66}+\frac{-1+5\sqrt{697}}{132}
=\frac{1+5\sqrt{697}}{132}.
\]
Como \(697=17\cdot41\) es libre de cuadrados,
\[
a+b+c+d=1+5+697+132=\boxed{835}.
\]