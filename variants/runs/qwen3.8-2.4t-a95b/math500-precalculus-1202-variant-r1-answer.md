

Sean  
\[
A=\arccos x,\qquad B=\arccos 2x,\qquad C=\arccos 4x.
\]
La condición dada es
\[
A+B+C=\pi.
\]

Para tres ángulos cuya suma es \(\pi\), se cumple la identidad
\[
\cos^2 A+\cos^2 B+\cos^2 C+2\cos A\cos B\cos C=1.
\]
Esto se puede obtener escribiendo \(C=\pi-(A+B)\), de modo que
\[
\cos C=-\cos(A+B)=\sin A\sin B-\cos A\cos B,
\]
y luego elevando al cuadrado tras reordenar.

Como
\[
\cos A=x,\qquad \cos B=2x,\qquad \cos C=4x,
\]
sustituimos en la identidad:
\[
x^2+(2x)^2+(4x)^2+2(x)(2x)(4x)=1.
\]
Entonces
\[
x^2+4x^2+16x^2+16x^3=1,
\]
\[
16x^3+21x^2-1=0.
\]

Así, \(x\) es raíz del polinomio
\[
p(t)=16t^3+21t^2-1.
\]

Este polinomio es primitivo. Por el teorema de la raíz racional, las únicas posibles raíces racionales serían
\[
\pm1,\ \pm\frac12,\ \pm\frac14,\ \pm\frac18,\ \pm\frac1{16},
\]
y ninguna anula \(p\). Como \(p\) es cúbico, es irreducible sobre \(\mathbb{Q}\). Por tanto, cualquier polinomio cúbico con coeficientes enteros que tenga a \(x\) como raíz debe ser un múltiplo entero de \(p\):
\[
q(t)=k(16t^3+21t^2-1),\qquad k\in\mathbb{Z}\setminus\{0\}.
\]

La suma de los valores absolutos de sus coeficientes es
\[
|16k|+|21k|+|0k|+|-k|=38|k|.
\]
El mínimo se alcanza con \(|k|=1\), dando
\[
16+21+0+1=38.
\]

\[
\boxed{38}
\]