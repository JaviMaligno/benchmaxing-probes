

Como \(AB\) es diámetro, por Tales se tiene

\[
\angle ADB=90^\circ,\qquad \angle ACB=90^\circ.
\]

Así, en el triángulo \(EAB\), \(D\) es el pie de la altura desde \(B\) hacia \(EA\), y \(C\) es el pie de la altura desde \(A\) hacia \(EB\).

Sean

\[
\alpha=\angle EAB,\qquad \beta=\angle EBA.
\]

En los triángulos rectángulos \(ADB\) y \(ABC\),

\[
\cos\alpha=\frac{AD}{AB}=\frac{7}{20},\qquad
\cos\beta=\frac{BC}{AB}=\frac{13}{20}.
\]

Por tanto,

\[
\sin\alpha=\frac{\sqrt{351}}{20},\qquad
\sin\beta=\frac{\sqrt{231}}{20}.
\]

Sean ahora \(s=EA\), \(t=EB\), y \(\theta=\angle AEB\). Por la ley de senos en \(EAB\),

\[
\frac{s}{t}=\frac{EA}{EB}=\frac{\sin\beta}{\sin\alpha}
=\frac{\sqrt{231}}{\sqrt{351}}.
\]

Tomemos vectores unitarios \(\mathbf u,\mathbf v\) desde \(E\) hacia \(A\) y \(B\). Entonces

\[
A=s\mathbf u,\qquad B=t\mathbf v.
\]

Como \(D\) y \(C\) son pies de alturas,

\[
ED=t\cos\theta,\qquad EC=s\cos\theta,
\]

de modo que

\[
D=t\cos\theta\,\mathbf u,\qquad C=s\cos\theta\,\mathbf v.
\]

Además,

\[
AD=s-ED=s-t\cos\theta=7,
\]
\[
BC=t-EC=t-s\cos\theta=13.
\]

Sumando ambas ecuaciones,

\[
(s+t)(1-\cos\theta)=20. \tag{1}
\]

En el triángulo \(ECD\), el excentro opuesto a \(E\), con origen en \(E\), está dado por

\[
L=\frac{ED\cdot C+EC\cdot D}{ED+EC-CD}.
\]

También,

\[
CD=20\cos\theta,
\]

pues \(CD\) corresponde a \(AB\) bajo la semejanza entre \(ECD\) y \(EBA\). Entonces

\[
L=\frac{st\cos^2\theta(\mathbf u+\mathbf v)}{\cos\theta(s+t-20)}
=\frac{st\cos\theta}{s+t-20}(\mathbf u+\mathbf v).
\]

Usando \((1)\), tenemos \(s+t-20=(s+t)\cos\theta\), así que

\[
L=\frac{st}{s+t}(\mathbf u+\mathbf v)
=\frac{t}{s+t}A+\frac{s}{s+t}B.
\]

Esto significa que \(L\) está sobre \(AB\), y de hecho es el punto donde la bisectriz interior de \(\angle AEB\) corta a \(AB\). Por el teorema de la bisectriz,

\[
\frac{AL}{LB}=\frac{EA}{EB}=\frac{s}{t}.
\]

Como \(O\) es el punto medio de \(AB\) y \(AB=20\),

\[
OL=10\cdot \frac{|t-s|}{s+t}.
\]

Como \(t>s\),

\[
OL=10\cdot \frac{1-\frac{s}{t}}{1+\frac{s}{t}}
=10\cdot \frac{\sqrt{351}-\sqrt{231}}{\sqrt{351}+\sqrt{231}}.
\]

Racionalizando,

\[
OL=10\cdot \frac{(\sqrt{351}-\sqrt{231})^2}{351-231}
=\frac{582-2\sqrt{81081}}{12}.
\]

Como \(81081=81\cdot 1001\),

\[
OL=\frac{582-18\sqrt{1001}}{12}
=\frac{97-3\sqrt{1001}}{2}.
\]

\[
\boxed{\frac{97-3\sqrt{1001}}{2}}
\]