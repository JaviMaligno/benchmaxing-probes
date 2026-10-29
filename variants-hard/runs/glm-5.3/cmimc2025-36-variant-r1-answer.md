Sea \(O\) el centro del \(24\)-gono original y tomemos su circunradio igual a \(1\).

1. Para una cuerda \(\overline{B_iB_{i+k}}\), los dos extremos forman en \(O\) un ángulo central

\[
\frac{2\pi k}{24}.
\]

En el triángulo isósceles \(OB_iB_{i+k}\), la perpendicular desde \(O\) a la cuerda pasa por su punto medio. Por lo tanto, la distancia de \(O\) a la recta que contiene la cuerda es

\[
d_k=\cos\!\left(\frac{1}{2}\cdot \frac{2\pi k}{24}\right)
=\cos\!\left(\frac{k\pi}{24}\right).
\]

2. La dirección normal a esa recta es la dirección del punto medio de la cuerda. Al pasar de \(i\) a \(i+1\), esa dirección normal gira \(15^\circ\). Así, en cada construcción hay \(24\) rectas igualmente espaciadas alrededor de \(O\), todas a la misma distancia \(d_k\). Su envolvente interior es un polígono regular de \(24\) lados con apotema \(d_k\).

3. El área de un polígono regular de \(24\) lados con apotema \(a\) es

\[
A=24a^2\tan\!\left(\frac{\pi}{24}\right).
\]

Por lo tanto,

\[
\frac{A_1}{A_2}
=
\frac{d_{10}^2}{d_{11}^2}
=
\frac{\cos^2\!\left(\frac{10\pi}{24}\right)}
{\cos^2\!\left(\frac{11\pi}{24}\right)}
=
\frac{\sin^2\!\left(\frac{\pi}{12}\right)}
{\sin^2\!\left(\frac{\pi}{24}\right)}.
\]

Usando \(\sin(2x)=2\sin x\cos x\),

\[
\frac{A_1}{A_2}
=
4\cos^2\!\left(\frac{\pi}{24}\right)
=
2+2\cos\!\left(\frac{\pi}{12}\right)
=
2+\frac{\sqrt2+\sqrt6}{2}.
\]

\[
\boxed{\dfrac{4+\sqrt2+\sqrt6}{2}}
\]