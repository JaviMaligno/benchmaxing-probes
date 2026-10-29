Coloquemos \(P=(0,0)\), \(Q=(a,0)\) y \(R=(0,b)\). Como \(PX=QX=26\) y \(PY=RY=26\), podemos escribir
\[
X=\left(\frac a2,h\right),\qquad Y=\left(k,\frac b2\right),
\]
donde
\[
h=\sqrt{676-\frac{a^2}{4}},\qquad k=\sqrt{676-\frac{b^2}{4}}.
\]

De \(XY=26\), al desarrollar \(XY^2\), se obtiene
\[
676=1352-ak-bh
\quad\Longrightarrow\quad
ak+bh=676.
\]

Escribamos \(a=52\sin\alpha\) y \(b=52\sin\beta\), de modo que \(h=26\cos\alpha\) y \(k=26\cos\beta\). Entonces
\[
1352\sin(\alpha+\beta)=676
\quad\Longrightarrow\quad
\sin(\alpha+\beta)=\frac12.
\]
Además, por \(QR=4\sqrt{301}\),
\[
a^2+b^2=4816
\quad\Longrightarrow\quad
\sin^2\alpha+\sin^2\beta=\frac{301}{169}.
\]
Esto obliga a que \(\alpha+\beta=\frac{5\pi}{6}\). Usando
\[
\sin^2\alpha+\sin^2\beta
=1-\cos(\alpha+\beta)\cos(\alpha-\beta),
\]
resulta
\[
1+\frac{\sqrt3}{2}\cos(\alpha-\beta)=\frac{301}{169}
\quad\Longrightarrow\quad
\cos(\alpha-\beta)=\frac{88\sqrt3}{169}.
\]

El área buscada es el área de \(PQR\) menos las áreas de \(PQX\), \(PRY\) y del triángulo equilátero \(PXY\):
\[
K=\frac{ab-ah-bk}{2}-169\sqrt3.
\]
Sustituyendo las expresiones trigonométricas y simplificando,
\[
K=338\cos(\alpha-\beta)+169\sqrt3
=176\sqrt3+169\sqrt3
=345\sqrt3.
\]

\[
\boxed{345}
\]