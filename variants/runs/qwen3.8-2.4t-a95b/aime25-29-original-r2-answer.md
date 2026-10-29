

Sea \(\angle BAK=\alpha\) y \(\angle BAL=\beta\), con \(0<\alpha<\beta<90^\circ\).

Como
\[
AK=AL=KL=14,
\]
el triángulo \(\triangle AKL\) es equilátero, así que
\[
\beta-\alpha=60^\circ.
\]

Además, \(AK=BK=14\), por lo que \(\triangle ABK\) es isósceles. Proyectando sobre \(AB\),
\[
AB=2\cdot 14\cos\alpha=28\cos\alpha.
\]
Análogamente, como \(AL=CL=14\), y el ángulo entre \(AL\) y \(AC\) es \(90^\circ-\beta\),
\[
AC=2\cdot 14\cos(90^\circ-\beta)=28\sin\beta.
\]

Como \(BC=38\) y \(\angle A=90^\circ\),
\[
AB^2+AC^2=38^2,
\]
\[
(28\cos\alpha)^2+(28\sin\beta)^2=1444.
\]
Dividiendo entre \(28^2=784\),
\[
\cos^2\alpha+\sin^2\beta=\frac{361}{196}.
\]

Con \(\beta=\alpha+60^\circ\),
\[
\cos^2\alpha+\sin^2(\alpha+60^\circ)
=1+\frac{\sqrt3}{2}\sin(2\alpha+60^\circ).
\]
Por tanto,
\[
1+\frac{\sqrt3}{2}\sin(2\alpha+60^\circ)=\frac{361}{196},
\]
\[
\sin(2\alpha+60^\circ)=\frac{55\sqrt3}{98}.
\]

Ahora calculamos áreas. El área de \(\triangle ABC\) es
\[
[ABC]=\frac12 AB\cdot AC
=392\cos\alpha\sin\beta.
\]
Usando producto a suma,
\[
\cos\alpha\sin\beta=\frac12\left(\sin(\alpha+\beta)+\sin(\beta-\alpha)\right),
\]
\[
[ABC]=196\left(\sin(2\alpha+60^\circ)+\sin60^\circ\right).
\]
Así,
\[
[ABC]=196\cdot \frac{55\sqrt3}{98}+196\cdot\frac{\sqrt3}{2}
=110\sqrt3+98\sqrt3=208\sqrt3.
\]

Las áreas de \(\triangle ABK\) y \(\triangle ALC\) son
\[
[ABK]=98\sin2\alpha,\qquad [ALC]=98\sin2\beta.
\]
Entonces
\[
[ABK]+[ALC]=98(\sin2\alpha+\sin2\beta).
\]
Como \(\beta=\alpha+60^\circ\),
\[
\sin2\alpha+\sin2\beta
=2\sin(\alpha+\beta)\cos(\alpha-\beta)
=2\sin(2\alpha+60^\circ)\cos60^\circ
=\sin(2\alpha+60^\circ).
\]
Luego
\[
[ABK]+[ALC]=98\cdot\frac{55\sqrt3}{98}=55\sqrt3.
\]

Finalmente, \(\triangle AKL\) es equilátero de lado \(14\), así que
\[
[AKL]=\frac{\sqrt3}{4}\cdot 14^2=49\sqrt3.
\]

El cuadrilátero \(BKLC\) es el triángulo \(ABC\) menos los tres triángulos \(ABK\), \(AKL\) y \(ALC\):
\[
[BKLC]=208\sqrt3-55\sqrt3-49\sqrt3=104\sqrt3.
\]

Por tanto, \(n=104\).

\[
\boxed{104}
\]