

Sea \(\Gamma\) la circunferencia circunscrita de \(\triangle DEF\).

Como \(D,E,F\) son los puntos medios de los lados de \(\triangle ABC\), el triángulo \(DEF\) es el triángulo medial. Por tanto,

\[
DE\parallel AB,\qquad EF\parallel BC,\qquad FD\parallel CA.
\]

Así que los ángulos de \(\triangle DEF\) son los mismos que los de \(\triangle ABC\):

\[
\angle EDF=84^\circ,\qquad \angle DEF=60^\circ,\qquad \angle DFE=36^\circ.
\]

Por el teorema del ángulo inscrito, los arcos entre \(D,E,F\) en \(\Gamma\) son

\[
\widehat{DE}=2\angle DFE=72^\circ,
\]
\[
\widehat{EF}=2\angle EDF=168^\circ,
\]
\[
\widehat{FD}=2\angle DEF=120^\circ.
\]

Asignemos coordenadas de ángulo central en \(\Gamma\), en el sentido del dibujo:

\[
D=0^\circ,\qquad E=72^\circ,\qquad F=72^\circ+168^\circ=240^\circ.
\]

Usamos el hecho de que si dos cuerdas \(PQ\) y \(RS\) son paralelas, y sus extremos tienen ángulos centrales \(p,q,r,s\), entonces

\[
p+q\equiv r+s \pmod{360^\circ}.
\]

Esto se debe a que la dirección de una cuerda con extremos en ángulos \(x,y\) es \(\frac{x+y}{2}+90^\circ\) módulo \(180^\circ\).

Ahora hallamos \(G,H,J\).

- \(G\) está sobre \(BD\subset BC\), y \(EF\parallel BC\), así que \(DG\parallel EF\):

\[
g+D\equiv E+F \pmod{360^\circ}
\]
\[
g\equiv 72^\circ+240^\circ=312^\circ.
\]

- \(H\) está sobre \(AE\subset AC\), y \(DF\parallel AC\), así que \(EH\parallel DF\):

\[
h+E\equiv D+F \pmod{360^\circ}
\]
\[
h\equiv 0^\circ+240^\circ-72^\circ=168^\circ.
\]

- \(J\) está sobre \(AF\subset AB\), y \(DE\parallel AB\), así que \(FJ\parallel DE\):

\[
J+F\equiv D+E \pmod{360^\circ}
\]
\[
J\equiv 0^\circ+72^\circ-240^\circ=-168^\circ\equiv 192^\circ.
\]

Por tanto, en orden cíclico tenemos

\[
G(312^\circ),\ D(0^\circ),\ E(72^\circ),\ H(168^\circ),\ J(192^\circ),\ F(240^\circ).
\]

Los seis arcos menores consecutivos son

\[
\widehat{GD}=48^\circ,\quad
\widehat{DE}=72^\circ,\quad
\widehat{EH}=96^\circ,
\]
\[
\widehat{HJ}=24^\circ,\quad
\widehat{JF}=48^\circ,\quad
\widehat{FG}=72^\circ.
\]

Entonces

\[
\widehat{DE}+2\widehat{HJ}+3\widehat{FG}
=
72^\circ+2(24^\circ)+3(72^\circ).
\]

\[
=72+48+216=336.
\]

\[
\boxed{336}
\]