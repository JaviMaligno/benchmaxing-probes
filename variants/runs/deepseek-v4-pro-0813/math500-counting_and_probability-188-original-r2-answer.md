Sean \(x,y\in(0,3)\) elegidos de forma independiente y uniforme. El espacio muestral tiene área

\[
3\cdot 3=9.
\]

Para que exista un triángulo de lados \(1,x,y\), deben cumplirse las desigualdades triangulares:

\[
x+y>1,\qquad x+1>y,\qquad y+1>x.
\]

Es decir,

\[
y>1-x,\qquad y<x+1,\qquad y>x-1.
\]

Analizamos según el valor de \(x\):

- Si \(0<x<1\), las condiciones son
  \[
  1-x<y<x+1,
  \]
  cuya longitud para \(y\) es
  \[
  (x+1)-(1-x)=2x.
  \]

- Si \(1<x<2\), las condiciones son
  \[
  x-1<y<x+1,
  \]
  cuya longitud es \(2\).

- Si \(2<x<3\), las condiciones son
  \[
  x-1<y<3,
  \]
  cuya longitud es
  \[
  3-(x-1)=4-x.
  \]

El área favorable es

\[
\int_0^1 2x\,dx+\int_1^2 2\,dx+\int_2^3 (4-x)\,dx.
\]

Calculamos:

\[
\int_0^1 2x\,dx=1,
\]

\[
\int_1^2 2\,dx=2,
\]

\[
\int_2^3 (4-x)\,dx=\frac32.
\]

Por tanto,

\[
\text{área favorable}=1+2+\frac32=\frac92.
\]

La probabilidad pedida es

\[
\frac{\frac92}{9}=\frac12.
\]

\[
\boxed{\frac12}
\]