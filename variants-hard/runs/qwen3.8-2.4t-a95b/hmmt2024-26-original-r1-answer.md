

Sea \(u=AB'\) y \(v=AC'\). Como \(B,B',C,C'\) están en la circunferencia \(\omega\), la potencia de \(A\) respecto a \(\omega\) da

\[
AB\cdot AB'=AC\cdot AC'
\]

es decir,

\[
18u=36v=:\Pi.
\]

Sean \(M,N\) los centros de las circunferencias con diámetros \(BB'\) y \(CC'\), y sean \(r,R\) sus radios. Entonces

\[
r=\frac{18-u}{2},\qquad R=\frac{36-v}{2},
\]

y además

\[
AM=\frac{18+u}{2}=r+u,\qquad AN=\frac{36+v}{2}=R+v.
\]

Como las dos circunferencias son tangentes exteriormente en \(T\), tenemos

\[
MN=r+R,
\]

y \(T\) está sobre \(MN\) con

\[
MT=r,\qquad TN=R.
\]

Aplicamos el teorema de Stewart en el triángulo \(AMN\) con la ceviana \(AT\):

\[
AN^2\cdot MT+AM^2\cdot TN=MN\left(AT^2+MT\cdot TN\right).
\]

Sustituyendo,

\[
(R+v)^2r+(r+u)^2R=(r+R)(AT^2+rR).
\]

Entonces

\[
(r+R)AT^2=r(R+v)^2+R(r+u)^2-rR(r+R).
\]

Expandiendo y simplificando,

\[
(r+R)AT^2=rv(2R+v)+Ru(2r+u).
\]

Pero

\[
2R+v=36,\qquad 2r+u=18,
\]

por lo que

\[
(r+R)AT^2=r(36v)+R(18u).
\]

Como \(36v=18u=\Pi\),

\[
(r+R)AT^2=(r+R)\Pi,
\]

y por tanto

\[
AT^2=\Pi.
\]

Dado que \(AT=12\),

\[
\Pi=144.
\]

Así,

\[
18u=144 \implies u=8,
\]

y

\[
36v=144 \implies v=4.
\]

Luego

\[
AB'=8,\qquad AC'=4.
\]

Ahora calculamos

\[
AM=\frac{18+8}{2}=13,\qquad AN=\frac{36+4}{2}=20,
\]

y

\[
r=\frac{18-8}{2}=5,\qquad R=\frac{36-4}{2}=16.
\]

Por tangencia exterior,

\[
MN=r+R=21.
\]

En el triángulo \(AMN\), el ángulo \(\angle MAN\) es precisamente \(\angle BAC\). Por ley de cosenos,

\[
21^2=13^2+20^2-2\cdot 13\cdot 20\cos\angle BAC.
\]

Entonces

\[
441=169+400-520\cos\angle BAC,
\]

\[
520\cos\angle BAC=128,
\]

\[
\cos\angle BAC=\frac{16}{65}.
\]

Por tanto,

\[
\sin\angle BAC=\frac{63}{65}.
\]

Finalmente, el centro \(O\) de \(\omega\) está en la perpendicular al punto medio de la cuerda \(BB'\), así que su proyección sobre \(AB\) está a distancia

\[
\frac{18+8}{2}=13
\]

de \(A\). Análogamente, su proyección sobre \(AC\) está a distancia

\[
\frac{36+4}{2}=20
\]

de \(A\).

Coloquemos \(A=(0,0)\) y \(AB\) sobre el eje \(x\). Entonces \(O=(13,h)\). Si \(\theta=\angle BAC\), el vector unitario en la dirección de \(AC\) es \((\cos\theta,\sin\theta)\). La condición de proyección sobre \(AC\) da

\[
13\cos\theta+h\sin\theta=20.
\]

Sustituyendo \(\cos\theta=\frac{16}{65}\) y \(\sin\theta=\frac{63}{65}\),

\[
13\cdot\frac{16}{65}+h\cdot\frac{63}{65}=20.
\]

De aquí,

\[
h=\frac{52}{3}.
\]

Por lo tanto,

\[
AO=\sqrt{13^2+\left(\frac{52}{3}\right)^2}
=\sqrt{169+\frac{2704}{9}}
=\sqrt{\frac{4225}{9}}
=\frac{65}{3}.
\]

\[
\boxed{\frac{65}{3}}
\]