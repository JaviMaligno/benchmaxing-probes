Necesitamos maximizar

\[
P=p\,q^2r^2s^3
\]

con \(p,q,r,s>0\) y \(p+q+r+s=16\).

Aplicamos multiplicadores de Lagrange o ponderación de términos. La idea es repartir el total \(16\) proporcionalmente a los exponentes \(1,2,2,3\).

Reescribimos:

\[
P = p\cdot q^2\cdot r^2\cdot s^3.
\]

La condición de máximo con multiplicadores de Lagrange da

\[
\frac{\partial \ln P}{\partial p}=\frac{1}{p}=\lambda,
\]

\[
\frac{\partial \ln P}{\partial q}=\frac{2}{q}=\lambda,
\]

\[
\frac{\partial \ln P}{\partial r}=\frac{2}{r}=\lambda,
\]

\[
\frac{\partial \ln P}{\partial s}=\frac{3}{s}=\lambda.
\]

Así,

\[
p=\frac{1}{\lambda},\quad q=\frac{2}{\lambda},\quad r=\frac{2}{\lambda},\quad s=\frac{3}{\lambda}.
\]

Entonces

\[
p+q+r+s=\frac{1+2+2+3}{\lambda}=\frac{8}{\lambda}=16.
\]

Por lo tanto,

\[
\lambda=\frac{8}{16}=\frac12.
\]

Luego

\[
p=2,\qquad q=4,\qquad r=4,\qquad s=6.
\]

Verificamos la suma:

\[
2+4+4+6=16.
\]

El valor máximo es

\[
P=2\cdot 4^2\cdot 4^2\cdot 6^3.
\]

Calculamos:

\[
4^2=16,
\]

\[
16\cdot 16=256,
\]

\[
2\cdot 256=512,
\]

\[
6^3=216.
\]

Entonces

\[
P=512\cdot 216.
\]

Multiplicamos:

\[
512\cdot 200=102400,
\]

\[
512\cdot 16=8192.
\]

Por lo tanto,

\[
P=102400+8192=110592.
\]

\[
\boxed{110592}
\]