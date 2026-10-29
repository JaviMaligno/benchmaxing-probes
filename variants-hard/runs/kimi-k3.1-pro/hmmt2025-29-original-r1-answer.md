Sea \(\delta=\angle BAX\). Como \(\angle AXB=90^\circ\), en el triángulo rectángulo \(AXB\):
\[
AX=AB\cos\delta,\qquad BX=AB\sin\delta.
\]

**1. Determinamos los ángulos en \(X\).**

Sean \(\alpha=\angle AXD\) y \(\beta=\angle BXC\). Por la ley de senos, usando \(AD=BC=24\):
\[
24=2(13)\sen\alpha,\qquad 24=2(15)\sen\beta.
\]
Como ambos triángulos son agudos, \(\alpha\) y \(\beta\) son agudos, así que
\[
\sen\alpha=\frac{12}{13},\quad \cos\alpha=\frac5{13},
\qquad
\sen\beta=\frac45,\quad \cos\beta=\frac35.
\]

**2. Expresamos \(AX\) y \(BX\) en función de \(\delta\).**

Como \(\angle XAD=90^\circ-\delta\), se tiene
\[
\angle ADX=90^\circ+\delta-\alpha.
\]
Aplicando la ley de senos en \(\triangle AXD\):
\[
AX=26\sen(90^\circ+\delta-\alpha)
=26\cos(\delta-\alpha)
=10\cos\delta+24\sen\delta.
\]

Análogamente, \(\angle XBC=\delta\), por lo que \(\angle BCX=180^\circ-\beta-\delta\). En \(\triangle BXC\):
\[
BX=30\sen(\beta+\delta)
=24\cos\delta+18\sen\delta.
\]

**3. Calculamos \(AB\).**

Escribiendo \(k=\tan\delta\), las relaciones del triángulo rectángulo \(AXB\) dan
\[
AB=\frac{AX}{\cos\delta}=10+24k,
\]
y también
\[
AB=\frac{BX}{\sen\delta}=18+\frac{24}{k}.
\]
Por tanto,
\[
10+24k=18+\frac{24}{k}
\quad\Longrightarrow\quad
3k^2-k-3=0.
\]
Como \(k>0\),
\[
k=\frac{1+\sqrt{37}}6.
\]
Finalmente,
\[
AB=10+24k=10+4(1+\sqrt{37})
=\boxed{14+4\sqrt{37}}.
\]