Primero simplificamos las desigualdades usando \(x+y+z=87\).

\[
x-yz<y-zx \iff x-yz-y+zx<0 \iff (x-y)(1+z)<0.
\]

\[
y-zx<z-xy \iff y-zx-z+xy<0 \iff (y-z)(1+x)<0.
\]

Hacemos el cambio

\[
u=x+1,\qquad v=z+1.
\]

Como \(x+y+z=87\), se tiene

\[
y=87-x-z=87-(u-1)-(v-1)=89-u-v.
\]

Además,

\[
x-y = u-1-(89-u-v)=2u+v-90,
\]

\[
y-z = 89-u-v-(v-1)=90-u-2v.
\]

Por tanto, las desigualdades quedan:

\[
v(2u+v-90)<0,
\]

\[
u(90-u-2v)<0.
\]

Las rectas relevantes son

\[
2u+v=90,\qquad u+2v=90.
\]

Analizando los signos de \(u\) y \(v\), solo la región con \(u>0\), \(v>0\) resulta acotada (las demás son vacías o no acotadas). Esta región finita está definida por

\[
u>0,\quad v>0,\quad 2u+v<90,\quad u+2v>90.
\]

Sus vértices son las intersecciones de las rectas:

\[
(30,30),\qquad (0,45),\qquad (0,90).
\]

En el plano \((u,v)\), el área es

\[
\frac12\cdot 45\cdot 30=675.
\]

Como \(u=x+1\) y \(v=z+1\), la parametrización del plano \(x+y+z=87\) con \(u,v\) tiene factor de área \(\sqrt{3}\). Por lo tanto, el área real es

\[
675\sqrt3.
\]

Así, \(a=675\) y \(b=3\), luego

\[
a+b=675+3=678.
\]

\[
\boxed{678}
\]