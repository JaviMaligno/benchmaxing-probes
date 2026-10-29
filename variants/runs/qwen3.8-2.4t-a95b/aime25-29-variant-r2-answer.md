

Coloquemos \(P=(0,0)\), \(Q=(a,0)\) y \(R=(0,b)\), con \(a,b>0\). Entonces

\[
a^2+b^2=QR^2=(4\sqrt{301})^2=4816.
\]

Como \(PX=QX=26\), el punto \(X\) está en la mediatriz de \(PQ\), así que su coordenada \(x\) es \(a/2\). Escribamos

\[
X=26(\cos\alpha,\sin\alpha),
\]

de donde \(a=52\cos\alpha\). Análogamente, como \(PY=RY=26\), escribamos

\[
Y=26(\cos\beta,\sin\beta),
\]

y obtenemos \(b=52\sin\beta\).

Por la hipotenusa,

\[
(52\cos\alpha)^2+(52\sin\beta)^2=4816
\]

\[
2704(\cos^2\alpha+\sin^2\beta)=4816
\]

\[
\cos^2\alpha+\sin^2\beta=\frac{301}{169}.
\]

Equivalentemente,

\[
\cos^2\alpha-\cos^2\beta=\frac{132}{169}>0,
\]

así que \(\alpha<\beta\).

Además, \(PX=PY=XY=26\), por lo que \(\triangle PXY\) es equilátero. Como \(X\) y \(Y\) están sobre la circunferencia de centro \(P\) y radio \(26\), la cuerda \(XY=26\) implica

\[
\beta-\alpha=\frac{\pi}{3}.
\]

Ahora usamos la condición anterior:

\[
\cos^2\alpha-\cos^2\beta
=\frac{\cos 2\alpha-\cos 2\beta}{2}.
\]

Con \(\beta=\alpha+\pi/3\),

\[
\frac{\cos 2\alpha-\cos(2\alpha+2\pi/3)}{2}
=\frac{\sqrt3}{2}\cos\left(2\alpha-\frac{\pi}{6}\right).
\]

Por tanto,

\[
\frac{\sqrt3}{2}\cos\left(2\alpha-\frac{\pi}{6}\right)=\frac{132}{169}
\]

\[
\cos\left(2\alpha-\frac{\pi}{6}\right)=\frac{264}{169\sqrt3}.
\]

Ahora calculamos el área del cuadrilátero \(QXYR\) restando del triángulo mayor los tres triángulos cercanos a \(P\):

\[
[QXYR]=[PQR]-[PQX]-[PXY]-[PYR].
\]

Tenemos

\[
[PQR]=\frac{ab}{2}=1352\cos\alpha\sin\beta,
\]

\[
[PQX]=338\sin 2\alpha,
\]

\[
[PYR]=338\sin 2\beta,
\]

y como \(\triangle PXY\) es equilátero de lado \(26\),

\[
[PXY]=\frac{26^2\sqrt3}{4}=169\sqrt3.
\]

Sea \(t=2\alpha\). Usando \(\beta=\alpha+\pi/3\),

\[
[QXYR]
=169\sqrt3+338\left(2\sin\left(t+\frac{\pi}{3}\right)-\sin t-\sin\left(t+\frac{2\pi}{3}\right)\right).
\]

La expresión entre paréntesis se simplifica:

\[
2\sin\left(t+\frac{\pi}{3}\right)-\sin t-\sin\left(t+\frac{2\pi}{3}\right)
=\cos\left(t-\frac{\pi}{6}\right).
\]

Así,

\[
[QXYR]=169\sqrt3+338\cos\left(2\alpha-\frac{\pi}{6}\right).
\]

Sustituyendo el valor hallado,

\[
[QXYR]=169\sqrt3+338\cdot \frac{264}{169\sqrt3}.
\]

Como \(338=2\cdot 169\),

\[
[QXYR]=169\sqrt3+\frac{528}{\sqrt3}
=169\sqrt3+176\sqrt3
=345\sqrt3.
\]

Por lo tanto, \(n=345\).

\[
\boxed{345}
\]