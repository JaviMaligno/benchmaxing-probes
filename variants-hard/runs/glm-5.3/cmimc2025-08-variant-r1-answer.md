Sea \(y=x+6\), es decir \(x=y-6\). Entonces

\[
\begin{aligned}
Q(y-6)
&=(y-6)^4+24(y-6)^3+65(y-6)^2-900(y-6)+2500\\
&=y^4-151y^2+48y+6352.
\end{aligned}
\]

Llamemos \(P(y)=y^4-151y^2+48y+6352\). Como no tiene término cúbico, buscamos una factorización de la forma

\[
P(y)=(y^2+\lambda y+\beta)(y^2-\lambda y+\delta).
\]

Al comparar coeficientes:

\[
\beta+\delta-\lambda^2=-151,\qquad \lambda(\delta-\beta)=48,\qquad \beta\delta=6352.
\]

Si \(u=\lambda^2\), se obtiene

\[
6352=\frac{(u-151)^2-\frac{2304}{u}}{4},
\]

lo que equivale a

\[
u^3-302u^2-2607u-2304=0.
\]

Esta ecuación tiene la solución útil \(u=-1\), así que tomamos \(\lambda=i\). Entonces

\[
\beta+\delta=-152,\qquad \delta-\beta=-48i,
\]

de donde

\[
\beta=-76+24i,\qquad \delta=-76-24i.
\]

Por lo tanto,

\[
P(y)=(y^2+iy-76+24i)(y^2-iy-76-24i).
\]

Volviendo a \(x\), esto da

\[
Q(x)=\bigl(x^2+(12+i)x-40+30i\bigr)\bigl(x^2+(12-i)x-40-30i\bigr).
\]

La raíz en el primer cuadrante sale del factor

\[
x^2+(12-i)x-40-30i=0.
\]

Usando la fórmula cuadrática:

\[
x=\frac{-12+i\pm\sqrt{303+96i}}{2}.
\]

Tomando la rama con parte real positiva,

\[
\sqrt{303+96i}\approx 17.619+2.724i,
\]

y con el signo \(+\) obtenemos

\[
z=\frac{-12+i+\sqrt{303+96i}}{2}\approx 2.810+1.862i,
\]

que efectivamente está en el primer cuadrante.

Así,

\[
a=-12,\qquad b=1,\qquad c=303,\qquad d=96,
\]

y por lo tanto

\[
a+b+c+d=-12+1+303+96=388.
\]

\[
\boxed{388}
\]