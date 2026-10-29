Vamos a resolver el problema paso a paso.

Queremos encontrar la distancia mínima desde el origen \((0,0)\) hasta un punto de la parábola

\[
y=\frac{1}{2}x^2-9.
\]

La distancia desde el origen a un punto \((x,y)\) es

\[
d=\sqrt{x^2+y^2}.
\]

Para minimizar la distancia, minimizamos el cuadrado de la distancia:

\[
d^2=x^2+y^2.
\]

Dado que \(y=\frac{1}{2}x^2-9\), sustituimos:

\[
d^2=x^2+\left(\frac{1}{2}x^2-9\right)^2.
\]

Sea \(u=x^2\ge 0\). Entonces,

\[
f(u)=u+\left(\frac{1}{2}u-9\right)^2.
\]

Desarrollamos:

\[
f(u)=u+\frac{1}{4}u^2-9u+81
\]

\[
f(u)=\frac{1}{4}u^2-8u+81.
\]

Derivamos para minimizar:

\[
f'(u)=\frac{1}{2}u-8.
\]

Igualamos a cero:

\[
\frac{1}{2}u-8=0
\]

\[
u=16.
\]

Como \(u=x^2=16\), tenemos \(x=\pm 4\). La segunda derivada es \(\frac{1}{2}>0\), así que es un mínimo.

Sustituimos \(x^2=16\) en la ecuación de la parábola:

\[
y=\frac{1}{2}(16)-9=8-9=-1.
\]

Por lo tanto, el punto más cercano al origen es \((-4,-1)\) o \((4,-1)\).

El cuadrado de la distancia es:

\[
d^2=x^2+y^2=16+1=17.
\]

Entonces, \(a^2=17\).

\[
\boxed{17}
\]