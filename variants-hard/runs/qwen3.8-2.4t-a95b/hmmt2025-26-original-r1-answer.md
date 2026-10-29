

Coloquemos el trapecio en coordenadas. Sea

\[
A=(0,0),\qquad B=(11,0),
\]

y como \(AB\parallel CD\) con \(CD=19\), escribimos

\[
D=(x,h),\qquad C=(x+19,h).
\]

Las longitudes de los lados dan

\[
DA^2=x^2+h^2=4^2=16,
\]

\[
BC^2=(x+19-11)^2+h^2=(x+8)^2+h^2=8^2=64.
\]

Restando:

\[
(x+8)^2-x^2=48
\]

\[
16x+64=48 \implies x=-1.
\]

Entonces

\[
h^2=16-1=15 \implies h=\sqrt{15}.
\]

Así,

\[
D=(-1,h),\qquad C=(18,h).
\]

Ahora calculemos los circuncentros.

Para \(\triangle DAB\) y \(\triangle ABC\), el circuncentro está sobre la mediatriz de \(AB\), es decir, sobre \(x=\frac{11}{2}\).

- Circuncentro de \(\triangle DAB\): sea \(\left(\frac{11}{2},y\right)\). Igualando distancias a \(A\) y \(D\):

\[
\left(\frac{11}{2}\right)^2+y^2=\left(\frac{13}{2}\right)^2+(y-h)^2.
\]

Esto da

\[
2hy=27 \implies y=\frac{27}{2h}=\frac{9h}{10}.
\]

Así,

\[
O_{DAB}=\left(\frac{11}{2},\frac{9h}{10}\right).
\]

- Circuncentro de \(\triangle ABC\): sea \(\left(\frac{11}{2},y\right)\). Igualando distancias a \(A\) y \(C\):

\[
\left(\frac{11}{2}\right)^2+y^2=\left(\frac{25}{2}\right)^2+(y-h)^2.
\]

Esto da

\[
2hy=141 \implies y=\frac{47h}{10}.
\]

Así,

\[
O_{ABC}=\left(\frac{11}{2},\frac{47h}{10}\right).
\]

Para \(\triangle BCD\) y \(\triangle CDA\), el circuncentro está sobre la mediatriz de \(CD\). El punto medio de \(CD\) es \(\left(\frac{17}{2},h\right)\), así que la mediatriz es \(x=\frac{17}{2}\).

- Circuncentro de \(\triangle BCD\): sea \(\left(\frac{17}{2},y\right)\). Igualando distancias a \(D\) y \(B\):

\[
\left(\frac{19}{2}\right)^2+(y-h)^2=\left(\frac{5}{2}\right)^2+y^2.
\]

Esto da

\[
2hy=99 \implies y=\frac{33h}{10}.
\]

Así,

\[
O_{BCD}=\left(\frac{17}{2},\frac{33h}{10}\right).
\]

- Circuncentro de \(\triangle CDA\): sea \(\left(\frac{17}{2},y\right)\). Igualando distancias a \(D\) y \(A\):

\[
\left(\frac{19}{2}\right)^2+(y-h)^2=\left(\frac{17}{2}\right)^2+y^2.
\]

Esto da

\[
2hy=33 \implies y=\frac{11h}{10}.
\]

Así,

\[
O_{CDA}=\left(\frac{17}{2},\frac{11h}{10}\right).
\]

Los cuatro circuncentros son

\[
\left(\frac{11}{2},\frac{47h}{10}\right),\quad
\left(\frac{17}{2},\frac{33h}{10}\right),\quad
\left(\frac{17}{2},\frac{11h}{10}\right),\quad
\left(\frac{11}{2},\frac{9h}{10}\right).
\]

Forman un cuadrilátero convexo con dos lados verticales paralelos. Sus longitudes verticales son

\[
\frac{47h}{10}-\frac{9h}{10}=\frac{38h}{10}=\frac{19h}{5},
\]

\[
\frac{33h}{10}-\frac{11h}{10}=\frac{22h}{10}=\frac{11h}{5}.
\]

La distancia horizontal entre ambas rectas verticales es

\[
\frac{17}{2}-\frac{11}{2}=3.
\]

Por tanto, el área es

\[
\frac12\left(\frac{19h}{5}+\frac{11h}{5}\right)\cdot 3
=
\frac12\cdot 6h\cdot 3
=
9h.
\]

Como \(h=\sqrt{15}\), el área pedida es

\[
\boxed{9\sqrt{15}}
\]