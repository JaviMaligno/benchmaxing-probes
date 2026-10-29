

Sea \(\alpha = \angle BAK\) y \(\beta = \angle LAC\).

Como \(AK=BK=14\), en el triángulo \(AKB\) la ley de cosenos da

\[
14^2 = AB^2+14^2-2(AB)(14)\cos\alpha
\quad\Longrightarrow\quad
AB=28\cos\alpha.
\]

Análogamente, como \(AL=CL=14\),

\[
AC=28\cos\beta.
\]

Además \(AK=AL=KL=14\), así que \(\triangle AKL\) es equilátero y

\[
\angle KAL=60^\circ.
\]

Como \(\angle A=90^\circ\) y \(K,L\) están en el interior, los rayos \(AK\) y \(AL\) están ordenados entre \(AB\) y \(AC\), luego

\[
\alpha+60^\circ+\beta=90^\circ
\quad\Longrightarrow\quad
\alpha+\beta=30^\circ.
\]

Por Pitágoras en \(\triangle ABC\),

\[
AB^2+AC^2=38^2.
\]

Sustituyendo \(AB=28\cos\alpha\) y \(AC=28\cos\beta\),

\[
784(\cos^2\alpha+\cos^2\beta)=1444,
\]

\[
\cos^2\alpha+\cos^2\beta=\frac{361}{196}.
\]

Sea \(\delta=\alpha-\beta\). Usando

\[
\cos^2\alpha+\cos^2\beta
=1+\cos(\alpha+\beta)\cos(\alpha-\beta),
\]

obtenemos

\[
1+\cos 30^\circ \cos\delta=\frac{361}{196}.
\]

Como \(\cos 30^\circ=\frac{\sqrt3}{2}\),

\[
\frac{\sqrt3}{2}\cos\delta=\frac{165}{196}
\quad\Longrightarrow\quad
\cos\delta=\frac{55\sqrt3}{98}.
\]

Ahora calculamos áreas. El área de \(\triangle ABC\) es

\[
[ABC]=\frac12 AB\cdot AC
=392\cos\alpha\cos\beta.
\]

Pero

\[
\cos\alpha\cos\beta
=\frac{\cos(\alpha+\beta)+\cos(\alpha-\beta)}2
=\frac{\frac{\sqrt3}{2}+\frac{55\sqrt3}{98}}2,
\]

así que

\[
[ABC]=196\left(\frac{\sqrt3}{2}+\frac{55\sqrt3}{98}\right)
=98\sqrt3+110\sqrt3=208\sqrt3.
\]

Las áreas de los triángulos pequeños son

\[
[AKB]=\frac12(AB)(14)\sin\alpha
=98\sin 2\alpha,
\]

\[
[ALC]=98\sin 2\beta.
\]

Entonces

\[
[AKB]+[ALC]
=98(\sin2\alpha+\sin2\beta)
=98\cdot 2\sin(\alpha+\beta)\cos(\alpha-\beta).
\]

Como \(\sin30^\circ=\frac12\),

\[
[AKB]+[ALC]=98\cos\delta
=98\cdot \frac{55\sqrt3}{98}
=55\sqrt3.
\]

Finalmente,

\[
[AKL]=\frac{\sqrt3}{4}\cdot 14^2=49\sqrt3.
\]

El cuadrilátero \(BKLC\) se obtiene restando del triángulo completo:

\[
[BKLC]=[ABC]-[AKB]-[ALC]-[AKL]
\]

\[
=208\sqrt3-55\sqrt3-49\sqrt3
=104\sqrt3.
\]

Por lo tanto, \(n=104\).

\[
\boxed{104}
\]