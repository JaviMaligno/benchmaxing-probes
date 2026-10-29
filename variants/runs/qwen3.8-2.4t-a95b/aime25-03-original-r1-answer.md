

Los jugadores son distinguibles, así que para cada reparto válido \((c,v,f)\) contamos las asignaciones con el coeficiente multinomial
\[
\frac{9!}{c!\,v!\,f!}.
\]

Necesitamos enteros positivos con
\[
c+v+f=9,\qquad c>v>f.
\]

Posibles ternas:

- Si \(f=1\): \(v=2\) da \(c=5\), y \(v=3\) da \(c=4\).  
  Ternas: \((5,2,1)\), \((4,3,1)\).
- Si \(f=2\): \(v=3\) da \(c=4\).  
  Terna: \((4,3,2)\).
- Si \(f\ge 3\), ya no hay espacio para \(c>v>f\).

Ahora sumamos:

\[
\frac{9!}{5!2!1!}=1512
\]

\[
\frac{9!}{4!3!1!}=2520
\]

\[
\frac{9!}{4!3!2!}=1260
\]

Entonces
\[
N=1512+2520+1260=5292.
\]

El residuo de \(5292\) entre \(1000\) es

\[
\boxed{292}
\]