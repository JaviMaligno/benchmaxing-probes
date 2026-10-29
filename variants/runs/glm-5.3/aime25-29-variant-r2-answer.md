Sea \(\theta=\angle QPX\) y \(\varphi=\angle QPY\), medidos desde \(PQ\) dentro del ángulo recto en \(P\).

1. Como \(PX=QX=26\), en \(\triangle PQX\):
\[
26^2=26^2+PQ^2-2(26)(PQ)\cos\theta
\]
por lo que
\[
PQ=52\cos\theta.
\]

Como \(PY=RY=26\), en \(\triangle PYR\), con \(\angle YPR=90^\circ-\varphi\):
\[
26^2=26^2+PR^2-2(26)(PR)\cos(90^\circ-\varphi),
\]
así
\[
PR=52\sin\varphi.
\]

2. Además, \(PX=PY=XY=26\), hence \(\triangle PXY\) es equilátero y
\[
|\varphi-\theta|=60^\circ.
\]
La orientación \(\theta=\varphi+60^\circ\) daría \(PQ,PR<26\), lo que haría imposible que \(QR=4\sqrt{301}\). Por lo tanto,
\[
\varphi=\theta+60^\circ.
\]

3. Usando la hipotenusa:
\[
(52\cos\theta)^2+(52\sin(\theta+60^\circ))^2=(4\sqrt{301})^2.
\]
Entonces
\[
\cos^2\theta+\sin^2(\theta+60^\circ)=\frac{301}{169}.
\]
Pero
\[
\cos^2\theta+\sin^2(\theta+60^\circ)
=1+\frac{\sqrt3}{2}\sin(2\theta+60^\circ),
\]
de modo que
\[
\sin(2\theta+60^\circ)=\frac{88\sqrt3}{169}.
\]

4. Las regiones \(\triangle PQX\), \(\triangle PXY\), \(\triangle PYR\) y el cuadrilátero \(QXYR\) particionan \(\triangle PQR\). Así, con \(c=\cos\theta\),
\[
[QXYR]=[PQR]-[PQX]-[PXY]-[PYR].
\]
Tenemos
\[
[PQR]=1352c\sin\varphi,\quad [PQX]=676c\sin\theta,
\]
\[
[PXY]=169\sqrt3,\quad [PYR]=676\sin\varphi\cos\varphi.
\]
Sustituyendo y usando \(\varphi=\theta+60^\circ\):
\[
[QXYR]
=676\left(\frac12\sin(2\theta+60^\circ)+\frac{\sqrt3}{4}\right).
\]
Por lo tanto,
\[
[QXYR]
=676\left(\frac12\cdot\frac{88\sqrt3}{169}+\frac{\sqrt3}{4}\right)
=345\sqrt3.
\]

\[
\boxed{345}
\]