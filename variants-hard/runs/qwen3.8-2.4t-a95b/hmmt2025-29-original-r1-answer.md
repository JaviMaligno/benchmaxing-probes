

Sea \(w=AB\). Colocamos coordenadas:

\[
A=(0,0),\quad B=(w,0),\quad C=(w,24),\quad D=(0,24),
\]

y sea \(X=(x,y)\), con \(0<x<w\), \(0<y<24\).

Como \(\angle AXB=90^\circ\), los vectores \(A-X=(-x,-y)\) y \(B-X=(w-x,-y)\) son perpendiculares:

\[
(-x)(w-x)+(-y)(-y)=0
\]

\[
y^2=x(w-x)\quad\Longrightarrow\quad x^2+y^2=wx. \tag{1}
\]

Ahora consideramos el circuncírculo de \(\triangle AXD\). Como \(AD=24\) y el circunradio es \(13\), la distancia del centro a la cuerda \(AD\) es

\[
\sqrt{13^2-12^2}=5.
\]

El centro está sobre la mediatriz de \(AD\), es decir, sobre \(y=12\). Los posibles centros son \((5,12)\) y \((-5,12)\). Como \(\triangle AXD\) es acutángulo, su circuncentro está dentro del triángulo, por lo que debe estar del mismo lado de \(AD\) que \(X\), o sea, a la derecha. Así, el centro es \((5,12)\):

\[
(x-5)^2+(y-12)^2=169.
\]

Expandiendo y usando \((1)\):

\[
x^2+y^2-10x-24y=0
\]

\[
wx-10x-24y=0
\]

\[
24y=(w-10)x. \tag{2}
\]

Para \(\triangle BXC\), el lado \(BC=24\) y el circunradio es \(15\). La distancia del centro a la cuerda \(BC\) es

\[
\sqrt{15^2-12^2}=9.
\]

El centro está sobre \(y=12\). Como el triángulo es acutángulo, el circuncentro debe estar dentro del triángulo, del mismo lado de \(BC\) que \(X\), es decir, a la izquierda de \(BC\). Por tanto, el centro es \((w-9,12)\):

\[
(x-w+9)^2+(y-12)^2=225.
\]

Expandiendo:

\[
x^2+y^2-2(w-9)x-24y+w^2-18w=0.
\]

Usando \((1)\) y \((2)\):

\[
wx-2(w-9)x-(w-10)x+w^2-18w=0.
\]

Simplificando:

\[
(28-2w)x+w^2-18w=0,
\]

\[
2(w-14)x=w(w-18). \tag{3}
\]

Por otro lado, de \((2)\),

\[
y=\frac{(w-10)x}{24}.
\]

Sustituyendo en \((1)\):

\[
x^2+\left(\frac{(w-10)x}{24}\right)^2=wx.
\]

Como \(x>0\),

\[
x\left(1+\frac{(w-10)^2}{576}\right)=w,
\]

\[
x=\frac{576w}{(w-10)^2+576}. \tag{4}
\]

De \((3)\),

\[
x=\frac{w(w-18)}{2(w-14)}.
\]

Igualando con \((4)\) y cancelando \(w\):

\[
\frac{w-18}{2(w-14)}=\frac{576}{(w-10)^2+576}.
\]

Multiplicando en cruz:

\[
(w-18)\bigl((w-10)^2+576\bigr)=1152(w-14).
\]

Como \((w-10)^2+576=w^2-20w+676\),

\[
(w-18)(w^2-20w+676)=1152(w-14).
\]

Expandiendo y simplificando:

\[
w^3-38w^2-116w+3960=0.
\]

Factorizando:

\[
(w-10)(w^2-28w-396)=0.
\]

Las soluciones son

\[
w=10,\qquad w=14\pm 4\sqrt{37}.
\]

Pero \(w=10\) daría \(y=0\) según \((2)\), contradiciendo que \(X\) está dentro del rectángulo. Además, \(14-4\sqrt{37}<0\). Por tanto,

\[
AB=14+4\sqrt{37}.
\]

\[
\boxed{14+4\sqrt{37}}
\]