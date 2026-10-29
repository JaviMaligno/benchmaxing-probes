

Sean \(c,v,s\) las cantidades de jugadores que eligieron chocolate, vainilla y fresa. Se requiere:

\[
c>v>s\ge 1,\qquad c+v+s=9.
\]

Las únicas ternas posibles son:

\[
(6,2,1),\quad (5,3,1),\quad (4,3,2).
\]

Para cada terna, el número de asignaciones a 9 jugadores distintos es el coeficiente multinomial correspondiente:

\[
\frac{9!}{6!2!1!}=252,
\]

\[
\frac{9!}{5!3!1!}=504,
\]

\[
\frac{9!}{4!3!2!}=1260.
\]

Por tanto,

\[
N=252+504+1260=2016.
\]

El residuo de \(N\) al dividirlo entre \(1000\) es

\[
2016 \equiv 16 \pmod{1000}.
\]

\[
\boxed{16}
\]