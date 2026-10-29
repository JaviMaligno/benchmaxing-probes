Sean
\[
\alpha=\angle PAB=\angle PDA,\quad \beta=\angle PAD=\angle PDC,\quad
\gamma=\angle PBA=\angle PCB,\quad \delta=\angle PBC=\angle PCD.
\]

**1. Relaciones entre los ángulos.** Los ángulos interiores de \(ABCD\) son
\[
A=D=\alpha+\beta,\qquad B=C=\gamma+\delta.
\]
Por tanto, \(\alpha+\beta+\gamma+\delta=\pi\), \(AD\parallel BC\) y \(AB=CD\): el cuadrilátero es un trapecio isósceles.

**2. Cálculo de \(PD\).** Por la ley de senos en \(APB\) y \(BPC\),
\[
\frac{\sin\gamma}{\sin\alpha}=\frac{PA}{PB}=\frac45,
\qquad
\frac{\sin\delta}{\sin\gamma}=\frac{PC}{PB}=2.
\]
Así, \(\sin\gamma=\frac45\sin\alpha\) y \(\sin\delta=\frac85\sin\alpha\).

Análogamente, en \(APD\) y \(CPD\),
\[
PD=\frac{4\sin\beta}{\sin\alpha}
=\frac{10\sin\delta}{\sin\beta}.
\]
De aquí,
\[
4\sin^2\beta=10\sin\alpha\sin\delta=16\sin^2\alpha,
\]
por lo que \(\sin\beta=2\sin\alpha\) y, en consecuencia,
\[
PD=8.
\]

**3. Longitud de los lados iguales.** Sea \(\theta=\alpha+\gamma\). Entonces
\[
\angle APB=\pi-\theta,\qquad \angle CPD=\theta.
\]
Usando la ley de cosenos,
\[
AB^2=4^2+5^2+2(4)(5)\cos\theta=41+40\cos\theta,
\]
\[
CD^2=10^2+8^2-2(10)(8)\cos\theta=164-160\cos\theta.
\]
Como \(AB=CD\), resulta \(\cos\theta=\frac{123}{200}\), y por tanto
\[
AB^2=CD^2=\frac{328}{5}.
\]

**4. Suma de las bases.** Sea \(\phi=\alpha+\beta\). Entonces
\(\angle BPC=\phi\) y \(\angle APD=\pi-\phi\). Por la ley de senos,
\[
AD=\frac{4\sin\phi}{\sin\alpha},
\qquad
BC=\frac{5\sin\phi}{\sin\gamma},
\]
de donde \(BC/AD=25/16\). Escribamos \(AD=16k\) y \(BC=25k\).

La ley de cosenos da
\[
256k^2=80+64\cos\phi,\qquad
625k^2=125-100\cos\phi.
\]
Eliminando \(\cos\phi\), obtenemos \(k^2=\frac{10}{41}\). Así,
\[
AD+BC=41k=\sqrt{410}.
\]

Finalmente, el perímetro es
\[
2\sqrt{\frac{328}{5}}+\sqrt{410}
=\frac{4\sqrt{410}}5+\sqrt{410}.
\]

\[
\boxed{\frac{9\sqrt{410}}5}
\]