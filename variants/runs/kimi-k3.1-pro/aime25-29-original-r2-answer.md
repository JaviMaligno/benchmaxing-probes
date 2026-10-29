Sea \(x=\angle BAK\) e \(y=\angle LAC\). Como \(AK=AL=KL=14\), el triángulo \(AKL\) es equilátero, así que \(\angle KAL=60^\circ\). Por tanto,
\[
x+60^\circ+y=90^\circ\quad\Longrightarrow\quad x+y=30^\circ.
\]

En el triángulo isósceles \(ABK\), donde \(AK=BK=14\), la ley de cosenos da
\[
AB=28\cos x.
\]
Análogamente, \(AC=28\cos y\). Como \(BC=38\),
\[
1444=AB^2+AC^2=784(\cos^2x+\cos^2y).
\]
Usando
\[
\cos^2x+\cos^2y=1+\cos(x+y)\cos(x-y),
\]
obtenemos
\[
\frac{1444}{784}=1+\frac{\sqrt3}{2}\cos(x-y),
\]
de donde
\[
98\cos(x-y)=55\sqrt3.
\]

El área buscada es
\[
[BKLC]=[ABC]-[ABK]-[AKL]-[ALC].
\]
Las áreas relevantes son
\[
[ABC]=392\cos x\cos y,\qquad
[ABK]=98\sin2x,\qquad
[ALC]=98\sin2y,\qquad
[AKL]=49\sqrt3.
\]
Por consiguiente,
\[
\begin{aligned}
[BKLC]
&=392\cos x\cos y-98(\sin2x+\sin2y)-49\sqrt3\\
&=196\bigl(\cos(x+y)+\cos(x-y)\bigr)
-196\sin(x+y)\cos(x-y)-49\sqrt3\\
&=98\sqrt3+98\cos(x-y)-49\sqrt3\\
&=49\sqrt3+55\sqrt3=104\sqrt3.
\end{aligned}
\]

\[
\boxed{104}
\]