

Sean

\[
\alpha=\angle PAB=\angle PDA,\quad
\beta=\angle PBA=\angle PCB,
\]
\[
\gamma=\angle PBC=\angle PCD,\quad
\delta=\angle PAD=\angle PDC.
\]

Como \(P\) está dentro del cuadrilátero, los ángulos en \(P\) suman \(360^\circ\). En los cuatro triángulos alrededor de \(P\),

\[
\angle APB=180^\circ-\alpha-\beta,\quad
\angle BPC=180^\circ-\beta-\gamma,
\]
\[
\angle CPD=180^\circ-\gamma-\delta,\quad
\angle DPA=180^\circ-\delta-\alpha.
\]

Sumando:

\[
720^\circ-2(\alpha+\beta+\gamma+\delta)=360^\circ
\]

\[
\alpha+\beta+\gamma+\delta=180^\circ.
\]

Sea \(x=PD\). Por ley de senos:

En \(\triangle PAB\):

\[
\frac{\sin\alpha}{\sin\beta}=\frac{PB}{PA}=\frac54.
\]

En \(\triangle PBC\):

\[
\frac{\sin\gamma}{\sin\beta}=\frac{PC}{PB}=2.
\]

En \(\triangle PDA\):

\[
\frac{x}{4}=\frac{\sin\delta}{\sin\alpha}.
\]

En \(\triangle PCD\):

\[
\frac{x}{10}=\frac{\sin\gamma}{\sin\delta}.
\]

Igualando \(x\):

\[
4\frac{\sin\delta}{\sin\alpha}=10\frac{\sin\gamma}{\sin\delta}
\]

\[
4\sin^2\delta=10\sin\alpha\sin\gamma.
\]

Usando \(\sin\alpha=\frac54\sin\beta\) y \(\sin\gamma=2\sin\beta\):

\[
4\sin^2\delta=10\cdot \frac54\sin\beta\cdot 2\sin\beta=25\sin^2\beta
\]

\[
\sin\delta=\frac52\sin\beta.
\]

Entonces

\[
x=4\frac{\sin\delta}{\sin\alpha}
=4\cdot \frac{\frac52\sin\beta}{\frac54\sin\beta}=8.
\]

Así, \(PD=8\).

Ahora, por ley de senos y usando \(\alpha+\beta+\gamma+\delta=180^\circ\),

\[
AB=CD
\]

y

\[
\frac{AD}{BC}=\frac{16}{25}.
\]

Sea \(\theta=\angle APB\). Entonces \(\angle CPD=180^\circ-\theta\). Como \(AB=CD\),

\[
AB^2=4^2+5^2-2\cdot4\cdot5\cos\theta=41-40\cos\theta,
\]

\[
CD^2=8^2+10^2-2\cdot8\cdot10\cos(180^\circ-\theta)=164+160\cos\theta.
\]

Igualando:

\[
41-40\cos\theta=164+160\cos\theta
\]

\[
\cos\theta=-\frac{123}{200}.
\]

Por tanto,

\[
AB^2=41+\frac{40\cdot123}{200}=\frac{328}{5},
\]

\[
AB=CD=\sqrt{\frac{328}{5}}=\frac{2\sqrt{410}}{5}.
\]

Sea \(\phi=\angle BPC\). Entonces \(\angle DPA=180^\circ-\phi\). Tenemos

\[
BC^2=5^2+10^2-2\cdot5\cdot10\cos\phi=125-100\cos\phi,
\]

\[
AD^2=4^2+8^2-2\cdot4\cdot8\cos(180^\circ-\phi)=80+64\cos\phi.
\]

Como \(AD/BC=16/25\),

\[
\frac{80+64\cos\phi}{125-100\cos\phi}=\frac{256}{625}.
\]

Resolviendo:

\[
625(80+64\cos\phi)=256(125-100\cos\phi)
\]

\[
50000+40000\cos\phi=32000-25600\cos\phi
\]

\[
\cos\phi=-\frac{45}{164}.
\]

Entonces

\[
BC^2=125+\frac{4500}{164}=\frac{6250}{41},
\]

\[
BC=\frac{25\sqrt{410}}{41}.
\]

Y

\[
AD=\frac{16}{25}BC=\frac{16\sqrt{410}}{41}.
\]

El perímetro es

\[
AB+BC+CD+AD
=2\cdot\frac{2\sqrt{410}}{5}+\frac{25\sqrt{410}}{41}+\frac{16\sqrt{410}}{41}.
\]

Como

\[
\frac{25+16}{41}\sqrt{410}=\sqrt{410},
\]

\[
\text{Perímetro}=\frac{4\sqrt{410}}{5}+\sqrt{410}
=\frac{9\sqrt{410}}{5}.
\]

\[
\boxed{\frac{9\sqrt{410}}{5}}
\]