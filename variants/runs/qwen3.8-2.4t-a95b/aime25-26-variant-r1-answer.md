Numeramos los vértices del polígono como \(0,1,\dots,27\) módulo \(28\).

Si todos los segmentos tienen la misma longitud, entonces todos corresponden a cuerdas que unen vértices separados por una misma cantidad \(d\) de pasos, con \(d=1,2,\dots,14\). Para un \(d\) fijo, los segmentos permitidos unen cada vértice \(i\) con \(i\pm d\).

Sea \(g=\gcd(28,d)\). Las aristas permitidas forman \(g\) ciclos disjuntos, cada uno de longitud \(28/d\), salvo el caso \(d=14\), donde cada vértice se une solo con su opuesto.

Un ciclo de longitud impar no puede cubrirse con segmentos que usen todos sus vértices exactamente una vez. Un ciclo de longitud par tiene exactamente \(2\) formas de hacerlo, eligiendo aristas alternadas. Entonces:

- \(d=1,3,5,9,11,13\): \(\gcd(28,d)=1\), hay un ciclo de longitud \(28\), dando \(2\) formas para cada \(d\). Total: \(6\cdot 2=12\).
- \(d=2,6,10\): \(\gcd(28,d)=2\), hay dos ciclos de longitud \(14\), dando \(2^2=4\) formas para cada \(d\). Total: \(3\cdot 4=12\).
- \(d=4,8,12\): \(\gcd(28,d)=4\), hay cuatro ciclos de longitud \(7\), que son impares, dando \(0\) formas.
- \(d=7\): \(\gcd(28,7)=7\), hay siete ciclos de longitud \(4\), dando \(2^7=128\) formas.
- \(d=14\): los segmentos son los \(14\) diámetros que unen vértices opuestos, dando \(1\) forma.

Sumando todas las posibilidades:

\[
12+12+0+128+1=153.
\]

\[
\boxed{153}
\]