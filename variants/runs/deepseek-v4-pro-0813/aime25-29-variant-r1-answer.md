Sea \(PQ=a\), \(PR=b\), y tomemos coordenadas
\[
P=(0,0),\quad Q=(2p,0),\quad R=(0,2q),
\]
donde \(p=a/2,\ q=b/2\).

Como \(PX=QX=26\), el punto \(X\) está en la mediatriz de \(PQ\), así que \(X=(p,u)\) con
\[
p^2+u^2=26^2=676.
\]
Análogamente, \(Y=(v,q)\) con
\[
q^2+v^2=676.
\]
Además, como \(QR=4\sqrt{301}\),
\[
(2p)^2+(2q)^2=(4\sqrt{301})^2 \implies p^2+q^2=1204.
\]

Escribamos
\[
p=26\sin A,\quad u=26\cos A,\quad q=26\sin B,\quad v=26\cos B.
\]
Entonces
\[
676(\sin^2 A+\sin^2 B)=1204
\implies \sin^2 A+\sin^2 B=\frac{301}{169}.
\]
De \(XY=26\):
\[
(v-p)^2+(q-u)^2=676.
\]
Expandiendo,
\[
676+676-2(pv+qu)=676 \implies pv+qu=338.
\]
Sustituyendo,
\[
676\sin(A+B)=338 \implies \sin(A+B)=\frac12.
\]
Como \(\sin^2 A+\sin^2 B=\frac{301}{169}>1\), debe ser
\[
A+B=150^\circ.
\]

Sea \(\delta=A-B\). Usando
\[
\sin^2A+\sin^2B=1-\cos(A+B)\cos(A-B),
\]
con \(\cos150^\circ=-\frac{\sqrt3}{2}\), obtenemos
\[
\frac{301}{169}=1+\frac{\sqrt3}{2}\cos\delta
\implies \cos\delta=\frac{88\sqrt3}{169}.
\]

El área de \(QXYR\) por determinante es
\[
\frac12\left|2pu+2qv-uv-3pq\right|.
\]
Sustituyendo las expresiones trigonométricas:
\[
2pu+2qv-uv-3pq
=676(\sin2A+\sin2B-\cos A\cos B-3\sin A\sin B).
\]
Ahora,
\[
\sin2A+\sin2B=2\sin150^\circ\cos\delta=\cos\delta,
\]
y
\[
\cos A\cos B+3\sin A\sin B=2\cos\delta+\frac{\sqrt3}{2}.
\]
Por tanto,
\[
\text{Área}=338\left(\cos\delta+\frac{\sqrt3}{2}\right).
\]
Finalmente,
\[
338\left(\frac{88\sqrt3}{169}+\frac{\sqrt3}{2}\right)
=338\sqrt3\left(\frac{88}{169}+\frac12\right)
=338\sqrt3\left(\frac{345}{338}\right)
=345\sqrt3.
\]

\[
\boxed{345}
\]