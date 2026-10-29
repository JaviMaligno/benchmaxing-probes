

Primero escribimos \(Q\) como una suma de cuadrados. Notamos que

\[
(x^2+12x-40)^2=x^4+24x^3+64x^2-960x+1600
\]

y

\[
(x+30)^2=x^2+60x+900.
\]

Sumando,

\[
(x^2+12x-40)^2+(x+30)^2
=x^4+24x^3+65x^2-900x+2500=Q(x).
\]

Así,

\[
Q(x)=A(x)^2+B(x)^2
\]

con

\[
A(x)=x^2+12x-40,\qquad B(x)=x+30.
\]

Factorizando sobre los enteros gaussianos,

\[
Q(x)=(A+iB)(A-iB).
\]

Consideremos el factor

\[
A-iB=x^2+12x-40-i(x+30)
=x^2+(12-i)x-40-30i.
\]

Sus raíces son

\[
x=\frac{-(12-i)\pm\sqrt{(12-i)^2-4(-40-30i)}}{2}.
\]

Calculamos el discriminante:

\[
(12-i)^2=143-24i,
\]

\[
-4(-40-30i)=160+120i,
\]

\[
(12-i)^2-4(-40-30i)=303+96i.
\]

Por tanto,

\[
x=\frac{-12+i\pm\sqrt{303+96i}}{2}.
\]

Sea \(\sqrt{303+96i}=u+vi\) con \(u,v>0\). Como

\[
u^2=\frac{\sqrt{303^2+96^2}+303}{2}>303>144,
\]

tenemos \(u>12\). Entonces la raíz con el signo \(+\) es

\[
z=\frac{-12+i+\sqrt{303+96i}}{2},
\]

cuya parte real es \(\frac{-12+u}{2}>0\) y cuya parte imaginaria es \(\frac{1+v}{2}>0\). Esta es la raíz en el primer cuadrante.

Comparando con

\[
z=\frac12\left(a+bi+\sqrt{c+di}\right),
\]

obtenemos

\[
a=-12,\qquad b=1,\qquad c=303,\qquad d=96.
\]

Luego

\[
a+b+c+d=-12+1+303+96=388.
\]

\[
\boxed{388}
\]