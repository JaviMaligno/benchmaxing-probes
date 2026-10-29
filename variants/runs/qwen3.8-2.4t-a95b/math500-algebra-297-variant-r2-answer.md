

Sustituimos \(y=x^2-7\) en la segunda ecuación:

\[
(x^2-7)^2=-9x+45
\]

\[
x^4-14x^2+49=-9x+45
\]

\[
x^4-14x^2+9x+4=0
\]

Factorizamos el polinomio. Probando raíces racionales:

\[
x=1 \quad \Rightarrow \quad 1-14+9+4=0
\]

Así que \(x-1\) es un factor. Dividiendo:

\[
x^4-14x^2+9x+4=(x-1)(x^3+x^2-13x-4)
\]

Ahora probamos \(x=-4\) en el cúbico:

\[
(-4)^3+(-4)^2-13(-4)-4=-64+16+52-4=0
\]

Entonces:

\[
x^3+x^2-13x-4=(x+4)(x^2-3x-1)
\]

Por lo tanto,

\[
(x-1)(x+4)(x^2-3x-1)=0
\]

Los valores de \(x\) son:

\[
x=1,\quad x=-4,\quad x=\frac{3\pm\sqrt{13}}{2}
\]

Ahora calculamos las coordenadas \(y\) usando \(y=x^2-7\).

Para \(x=1\):

\[
y=1^2-7=-6
\]

Para \(x=-4\):

\[
y=(-4)^2-7=16-7=9
\]

Para las raíces de \(x^2-3x-1=0\), sabemos que

\[
x^2=3x+1
\]

Entonces:

\[
y=x^2-7=3x+1-7=3x-6
\]

Si \(x_1,x_2\) son esas dos raíces, entonces por las fórmulas de Viète:

\[
x_1+x_2=3,\qquad x_1x_2=-1
\]

El producto de sus coordenadas \(y\) es:

\[
(3x_1-6)(3x_2-6)
\]

\[
=9x_1x_2-18(x_1+x_2)+36
\]

\[
=9(-1)-18(3)+36=-9-54+36=-27
\]

Finalmente, el producto de todas las coordenadas \(y\) es:

\[
(-6)(9)(-27)=1458
\]

\[
\boxed{1458}
\]