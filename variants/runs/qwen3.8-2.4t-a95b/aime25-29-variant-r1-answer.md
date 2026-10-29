

Coloquemos coordenadas con

\[
P=(0,0),\qquad Q=(a,0),\qquad R=(0,b),
\]

donde \(a,b>0\). Como \(\angle P=90^\circ\) y \(QR=4\sqrt{301}\),

\[
a^2+b^2=(4\sqrt{301})^2=4816.
\]

Como \(PX=PY=26\), escribimos

\[
X=26(\cos\alpha,\sin\alpha),\qquad Y=26(\cos\beta,\sin\beta),
\]

con \(0<\alpha,\beta<\frac{\pi}{2}\).

La condición \(QX=26\) da

\[
(26\cos\alpha-a)^2+(26\sin\alpha)^2=26^2,
\]

de donde

\[
a=52\cos\alpha.
\]

Análogamente, de \(RY=26\),

\[
(26\cos\beta)^2+(26\sin\beta-b)^2=26^2
\]

y por tanto

\[
b=52\sin\beta.
\]

Entonces

\[
4816=a^2+b^2=2704(\cos^2\alpha+\sin^2\beta),
\]

así que

\[
\cos^2\alpha+\sin^2\beta=\frac{301}{169}.
\]

Además, \(PX=PY=XY=26\), por lo que \(\triangle PXY\) es equilátero y

\[
|\beta-\alpha|=\frac{\pi}{3}.
\]

Como

\[
\frac{301}{169}>1,
\]

tenemos \(\sin^2\beta>\sin^2\alpha\), y como \(\alpha,\beta\in(0,\pi/2)\), se sigue que \(\beta>\alpha\). Por tanto,

\[
\beta=\alpha+\frac{\pi}{3}.
\]

Ahora

\[
\frac{301}{169}-1
=\sin^2\beta-\sin^2\alpha
=\sin(\alpha+\beta)\sin(\beta-\alpha).
\]

Con \(\beta-\alpha=\pi/3\),

\[
\frac{132}{169}
=\sin\left(2\alpha+\frac{\pi}{3}\right)\cdot \frac{\sqrt3}{2}.
\]

Definamos

\[
S=\sin\left(2\alpha+\frac{\pi}{3}\right).
\]

Entonces

\[
S=\frac{264}{169\sqrt3}=\frac{88\sqrt3}{169}.
\]

Ahora calculamos el área del cuadrilátero \(QXYR\). El triángulo \(PQR\) se descompone en los triángulos \(PQX\), \(PXY\), \(PYR\) y el cuadrilátero \(QXYR\).

El área de \(PQR\) es

\[
[PQR]=\frac{ab}{2}
=1352\cos\alpha\sin\beta.
\]

Usando identidades de producto a suma,

\[
\cos\alpha\sin\beta
=\frac12\left(\sin(\alpha+\beta)+\sin(\beta-\alpha)\right)
=\frac12\left(S+\frac{\sqrt3}{2}\right).
\]

Por tanto,

\[
[PQR]=676S+338\sqrt3.
\]

El triángulo \(PXY\) es equilátero de lado \(26\), así que

\[
[PXY]=\frac{\sqrt3}{4}\cdot 26^2=169\sqrt3.
\]

Además,

\[
[PQX]=\frac12(52\cos\alpha)(26\sin\alpha)=338\sin 2\alpha,
\]

y

\[
[PYR]=\frac12(52\sin\beta)(26\cos\beta)=338\sin 2\beta.
\]

Luego,

\[
[PQX]+[PYR]
=338(\sin 2\alpha+\sin 2\beta)
=338\cdot 2\sin(\alpha+\beta)\cos(\alpha-\beta).
\]

Como \(\beta-\alpha=\pi/3\),

\[
[PQX]+[PYR]=338S.
\]

Finalmente,

\[
[QXYR]=[PQR]-[PQX]-[PXY]-[PYR],
\]

\[
[QXYR]=(676S+338\sqrt3)-(338S+169\sqrt3)
=338S+169\sqrt3.
\]

Sustituyendo \(S=\frac{88\sqrt3}{169}\),

\[
[QXYR]=338\cdot \frac{88\sqrt3}{169}+169\sqrt3
=176\sqrt3+169\sqrt3
=345\sqrt3.
\]

Por lo tanto, \(n=345\).

\[
\boxed{345}
\]