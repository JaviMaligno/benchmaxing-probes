

Sea \(m\) el valor mínimo de \(g\) y supongamos que se alcanza exactamente en dos puntos positivos distintos \(r\) y \(s\).

Para \(x>0\), se tiene \(g(x)-m\ge 0\). Multiplicando por \(x>0\), definimos

\[
P(x)=x(g(x)-m)=(x-8)(x-50)(x-72)(x-k)-mx.
\]

Entonces \(P(x)\ge 0\) en \((0,\infty)\) y se anula en \(x=r,s\). Como \(P\) es un polinomio mónico de grado \(4\), cada uno de esos ceros interiores debe tener multiplicidad par, al menos \(2\). Por tanto,

\[
P(x)=(x-r)^2(x-s)^2.
\]

Expandimos el producto original:

\[
(x-8)(x-50)(x-72)(x-k)
\]
\[
= x^4-(130+k)x^3+(4576+130k)x^2-(28800+4576k)x+28800k.
\]

Sea

\[
u=r+s,\qquad v=rs.
\]

Entonces

\[
(x-r)^2(x-s)^2=(x^2-ux+v)^2
\]
\[
=x^4-2ux^3+(u^2+2v)x^2-2uvx+v^2.
\]

Igualando coeficientes, obtenemos

\[
2u=130+k,
\]
\[
u^2+2v=4576+130k,
\]
\[
v^2=28800k.
\]

De la primera ecuación,

\[
k=2u-130.
\]

Como \(k>0\), tenemos \(u>65\). Escribamos

\[
u=65+t^2
\]

con \(t>0\). Entonces

\[
k=2t^2.
\]

Además,

\[
v^2=28800k=28800(2t^2)=57600t^2,
\]

por lo que, como \(v>0\),

\[
v=240t.
\]

Sustituyendo en la segunda ecuación:

\[
(t^2+65)^2+2(240t)=4576+130(2t^2).
\]

Esto da

\[
t^4+130t^2+4225+480t=4576+260t^2,
\]

\[
t^4-130t^2+480t-351=0.
\]

Factorizando,

\[
t^4-130t^2+480t-351=(t-1)(t-3)(t-9)(t+13).
\]

Como \(t>0\), las soluciones son

\[
t=1,\quad t=3,\quad t=9.
\]

Por tanto,

\[
k=2t^2
\]

da los tres valores

\[
k=2,\quad k=18,\quad k=162.
\]

Para cada uno de estos valores, \(u=65+t^2\) y \(v=240t\), y la ecuación \(z^2-uz+v=0\) tiene dos raíces positivas distintas, por lo que efectivamente el mínimo se alcanza en exactamente dos puntos positivos.

La suma pedida es

\[
2+18+162=182.
\]

\[
\boxed{182}
\]