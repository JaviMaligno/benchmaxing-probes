Vamos a reescribir el polinomio como una suma de cuadrados.

Como el coeficiente de \(x^3\) es \(20\), es natural probar una forma
\[
P(x)=(x^2+10x+m)^2+(x+n)^2.
\]

Comparando coeficientes:

- Coeficiente de \(x^2\):
\[
100+2m+1=29 \implies 2m=-72 \implies m=-36.
\]

- Coeficiente de \(x\):
\[
20m+2n=-666.
\]
Con \(m=-36\),
\[
-720+2n=-666 \implies n=27.
\]

- Constante:
\[
m^2+n^2=(-36)^2+27^2=1296+729=2025,
\]
que coincide.

Por lo tanto,
\[
P(x)=(x^2+10x-36)^2+(x+27)^2.
\]

Ahora usamos
\[
A^2+B^2=(A+iB)(A-iB),
\]
con
\[
A=x^2+10x-36,\qquad B=x+27.
\]
Entonces
\[
P(x)=\left(x^2+(10+i)x-36+27i\right)\left(x^2+(10-i)x-36-27i\right).
\]

Resolvemos el segundo factor:
\[
x^2+(10-i)x-36-27i=0.
\]

Por la fórmula cuadrática,
\[
x=\frac{-(10-i)\pm\sqrt{(10-i)^2-4(-36-27i)}}{2}.
\]

Calculamos el discriminante:
\[
(10-i)^2=99-20i,
\]
y
\[
-4(-36-27i)=144+108i.
\]
Así,
\[
(10-i)^2-4(-36-27i)=243+88i.
\]

Por lo tanto,
\[
x=\frac{-10+i\pm\sqrt{243+88i}}{2}.
\]

Tomando la rama de la raíz cuadrada con parte real y parte imaginaria positivas, el signo \(+\) da la raíz en el primer cuadrante:
\[
r=\frac{-10+i+\sqrt{243+88i}}{2}.
\]

Comparando con
\[
r=\frac12(a+bi+\sqrt{c+di}),
\]
tenemos
\[
a=-10,\qquad b=1,\qquad c=243,\qquad d=88.
\]

Entonces
\[
a+b+c+d=-10+1+243+88.
\]

\[
\boxed{322}
\]