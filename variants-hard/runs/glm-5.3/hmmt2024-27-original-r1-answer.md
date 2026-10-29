Denotemos \(a=BC\), \(b=CA\), \(c=AB\), \(h=AD\), y sean
\[
\alpha=\angle BAC,\qquad \beta=\angle ABC,\qquad \gamma=\angle BCA.
\]

Como \(BE\perp AC\) y \(CF\perp AB\), en los triángulos rectángulos correspondientes tenemos
\[
AE=c\cos\alpha,\qquad AF=b\cos\alpha.
\]
Además, \(\angle EAF=\alpha\), así que por la ley de cosenos en \(AEF\),
\[
EF^2=(c\cos\alpha)^2+(b\cos\alpha)^2-2bc\cos^2\alpha\cos\alpha
=a^2\cos^2\alpha.
\]
Por lo tanto,
\[
EF=a\cos\alpha.
\]

Ahora, usando áreas,
\[
\frac{[AEF]}{[ABC]}
=\frac{\frac12 AE\cdot AF\sin\alpha}{\frac12bc\sin\alpha}
=\cos^2\alpha.
\]
Pero también, tomando \(EF\) y \(BC\) como bases,
\[
\frac{[AEF]}{[ABC]}
=\frac{EF\cdot AQ}{BC\cdot AD}
=\cos\alpha\cdot\frac{AQ}{AD}.
\]
Como \(\alpha\) es agudo, \(\cos\alpha>0\), y por lo tanto
\[
AQ=AD\cos\alpha.
\]
Con \(AQ=20\) y \(AD=24\),
\[
\cos\alpha=\frac{20}{24}=\frac56,
\qquad
\sin\alpha=\sqrt{1-\frac{25}{36}}=\frac{\sqrt{11}}6.
\]

El triángulo \(DEF\) es el triángulo órtico, cuyos lados son
\[
EF=a\cos\alpha,\qquad FD=b\cos\beta,\qquad DE=c\cos\gamma.
\]
Así, si \(P\) es su perímetro,
\[
P=a\cos\alpha+b\cos\beta+c\cos\gamma.
\]
Sea \(R\) el circunradio de \(ABC\). Por la ley de senos, \(a=2R\sin\alpha\), etc., entonces
\[
P=R(\sin2\alpha+\sin2\beta+\sin2\gamma).
\]
Usando \(\alpha+\beta+\gamma=\pi\),
\[
\sin2\alpha+\sin2\beta+\sin2\gamma=4\sin\alpha\sin\beta\sin\gamma,
\]
de modo que
\[
P=4R\sin\alpha\sin\beta\sin\gamma.
\]
Pero
\[
AD=c\sin\beta=2R\sin\gamma\sin\beta,
\]
así que
\[
P=2AD\sin\alpha.
\]
Finalmente,
\[
P=2\cdot 24\cdot \frac{\sqrt{11}}6.
\]

\[
\boxed{8\sqrt{11}}
\]