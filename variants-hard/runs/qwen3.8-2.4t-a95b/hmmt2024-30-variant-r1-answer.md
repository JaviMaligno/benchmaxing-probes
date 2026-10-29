

Sean

\[
\alpha=\angle QWX=\angle QZW,\quad
\beta=\angle QWZ=\angle QZY,
\]
\[
\gamma=\angle QXW=\angle QYX,\quad
\delta=\angle QXY=\angle QYZ.
\]

Sea también \(z=QZ\). Los ángulos alrededor de \(Q\) suman \(360^\circ\). Aplicando la suma angular en los cuatro triángulos \(QWX,QXY,QYZ,QZW\), obtenemos

\[
2(\alpha+\beta+\gamma+\delta)+360^\circ=720^\circ,
\]

así que

\[
\alpha+\beta+\gamma+\delta=180^\circ.
\]

Por ley de senos en \(\triangle QWX\),

\[
\frac{3}{\sin\gamma}=\frac{5}{\sin\alpha}
\implies \sin\alpha=\frac53\sin\gamma.
\]

En \(\triangle QXY\),

\[
\frac{5}{\sin\gamma}=\frac{10}{\sin\delta}
\implies \sin\delta=2\sin\gamma.
\]

En \(\triangle QYZ\) y \(\triangle QZW\),

\[
\frac{10}{\sin\beta}=\frac{z}{\sin\delta},
\qquad
\frac{z}{\sin\beta}=\frac{3}{\sin\alpha}.
\]

Combinando,

\[
\sin^2\beta=\frac{10}{3}\sin\alpha\sin\delta
=\frac{10}{3}\cdot \frac53\sin\gamma\cdot 2\sin\gamma
=\frac{100}{9}\sin^2\gamma,
\]

por lo que \(\sin\beta=\frac{10}{3}\sin\gamma\). Entonces

\[
z=\frac{3\sin\beta}{\sin\alpha}
=\frac{3\cdot \frac{10}{3}\sin\gamma}{\frac53\sin\gamma}=6.
\]

Así, \(QZ=6\).

Ahora calculemos los lados. En \(\triangle QWX\),

\[
WX^2=3^2+5^2-2\cdot3\cdot5\cos\angle WQX.
\]

Como \(\angle WQX=180^\circ-(\alpha+\gamma)\),

\[
WX^2=34+30\cos(\alpha+\gamma).
\]

En \(\triangle QYZ\),

\[
YZ^2=10^2+6^2-2\cdot10\cdot6\cos\angle YQZ.
\]

Pero \(\angle YQZ=180^\circ-(\beta+\delta)\), y como
\(\alpha+\beta+\gamma+\delta=180^\circ\),

\[
\beta+\delta=180^\circ-(\alpha+\gamma).
\]

Por tanto,

\[
YZ^2=136-120\cos(\alpha+\gamma).
\]

Además, por ley de senos se obtiene \(WX=YZ\). Igualando:

\[
34+30\cos(\alpha+\gamma)=136-120\cos(\alpha+\gamma),
\]

\[
150\cos(\alpha+\gamma)=102
\implies \cos(\alpha+\gamma)=\frac{17}{25}.
\]

Luego

\[
WX^2=34+30\cdot\frac{17}{25}=\frac{272}{5},
\]

\[
WX=YZ=\frac{4\sqrt{85}}{5}.
\]

Para los otros dos lados, sea \(\psi=\gamma+\delta\). Por ley de senos,

\[
XY=\frac{5}{\sin\gamma}\sin\psi,
\]

y

\[
ZW=\frac{3}{\sin\alpha}\sin\psi
=\frac{9}{5\sin\gamma}\sin\psi.
\]

Así,

\[
ZW=\frac{9}{25}XY.
\]

Por ley de cosenos,

\[
XY^2=5^2+10^2-2\cdot5\cdot10\cos(180^\circ-\psi)
=125+100\cos\psi,
\]

y

\[
ZW^2=6^2+3^2-2\cdot6\cdot3\cos\psi
=45-36\cos\psi.
\]

Usando \(ZW=\frac{9}{25}XY\),

\[
\frac{81}{625}(125+100\cos\psi)=45-36\cos\psi.
\]

Resolviendo,

\[
\cos\psi=\frac{10}{17}.
\]

Entonces

\[
XY^2=125+100\cdot\frac{10}{17}=\frac{3125}{17},
\]

\[
XY=\frac{25\sqrt{85}}{17},
\]

y

\[
ZW=\frac{9}{25}XY=\frac{9\sqrt{85}}{17}.
\]

Finalmente, el perímetro es

\[
WX+XY+YZ+ZW
=2\cdot\frac{4\sqrt{85}}{5}
+\frac{25\sqrt{85}}{17}
+\frac{9\sqrt{85}}{17}.
\]

\[
=\frac{8\sqrt{85}}{5}+2\sqrt{85}
=\frac{18\sqrt{85}}{5}.
\]

\[
\boxed{\frac{18\sqrt{85}}{5}}
\]