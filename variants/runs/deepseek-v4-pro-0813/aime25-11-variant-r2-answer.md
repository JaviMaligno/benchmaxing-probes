Sea \(x=66y^2\). Como \(y=g(x)\), hay que resolver \(y=g(66y^2)\).

La función periódica se escribe en cada tramo:
\[
g(x)=
\begin{cases}
x-4n,& 4n-1\le x<4n+1,\\[2mm]
4n+2-x,& 4n+1\le x<4n+3.
\end{cases}
\]

**Tramo ascendente:** \(y=x-4n\). Con \(x=66y^2\):
\[
66y^2-y-4n=0.
\]
Los tramos relevantes son \(n=0,1,\dots,16\), y en cada uno hay dos raíces válidas. La suma de las raíces de cada cuadrática es \(\frac{1}{66}\), luego aportan
\[
17\cdot \frac1{66}=\frac{17}{66}.
\]

**Tramo descendente:** \(y=4n+2-x\). Con \(x=66y^2\):
\[
66y^2+y-(4n+2)=0.
\]
Los tramos relevantes son \(n=0,1,\dots,16\). Para \(n=0,\dots,15\) hay dos raíces válidas; cada cuadrática completa suma \(-\frac1{66}\). Para \(n=16\), solo la raíz mayor es válida:
\[
y=\frac{-1+\sqrt{17425}}{132}=\frac{-1+5\sqrt{697}}{132}.
\]
Aportan:
\[
16\cdot\left(-\frac1{66}\right)+\frac{-1+5\sqrt{697}}{132}.
\]

Suma total:
\[
\frac{17}{66}-\frac{16}{66}+\frac{-1+5\sqrt{697}}{132}
=\frac{1+5\sqrt{697}}{132}.
\]
Así, \(a=1\), \(b=5\), \(c=697\), \(d=132\), con \(697=17\cdot 41\) libre de cuadrados y \(\gcd(1,5,132)=1\).

\[
a+b+c+d=1+5+697+132=835.
\]

\[
\boxed{835}
\]