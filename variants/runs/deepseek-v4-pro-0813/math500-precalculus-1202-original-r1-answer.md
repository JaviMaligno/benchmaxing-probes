Voy a resolverlo paso a paso.

Sea

\[
\arccos x + \arccos 2x + \arccos 3x = \pi.
\]

Usamos la identidad para la suma de dos arcocosenos activando el coseno en ambos lados de forma adecuada.

Primero, sea
\[
A=\arccos x,\quad B=\arccos 2x,\quad C=\arccos 3x.
\]
Entonces \(A+B+C=\pi\). Esto implica
\[
A+B=\pi-C.
\]
Tomando coseno:
\[
\cos(A+B)=\cos(\pi-C)=-\cos C.
\]
Como \(\cos C=3x\), y
\[
\cos(A+B)=\cos A\cos B-\sin A\sin B,
\]
con \(\cos A=x\), \(\cos B=2x\), \(\sin A=\sqrt{1-x^2}\), \(\sin B=\sqrt{1-4x^2}\), se tiene:

\[
x(2x)-\sqrt{1-x^2}\sqrt{1-4x^2}=-3x.
\]
Es decir,
\[
2x^2-\sqrt{1-x^2}\sqrt{1-4x^2}=-3x.
\]

Reordenamos:
\[
2x^2+3x=\sqrt{(1-x^2)(1-4x^2)}.
\]

Elevamos al cuadrado:
\[
(2x^2+3x)^2=(1-x^2)(1-4x^2).
\]

Calculamos ambos lados.

Lado izquierdo:
\[
(2x^2+3x)^2 = 4x^4+12x^3+9x^2.
\]

Lado derecho:
\[
(1-x^2)(1-4x^2)=1-5x^2+4x^4.
\]

Igualamos:
\[
4x^4+12x^3+9x^2 = 1-5x^2+4x^4.
\]

Cancelamos \(4x^4\):
\[
12x^3+9x^2 = 1-5x^2.
\]

Pasamos todo a un lado:
\[
12x^3+14x^2-1=0.
\]

Así, un polinomio cúbico que satisface \(x\) es
\[
12x^3+14x^2-1=0.
\]

Aquí:
\[
a=12,\quad b=14,\quad c=0,\quad d=-1.
\]

Entonces,
\[
|a|+|b|+|c|+|d|=12+14+0+1=27.
\]

Sin embargo, debemos asegurarnos de que no exista otro polinomio entero con la misma raíz y suma de valores absolutos menor. El polinomio \(12x^3+14x^2-1\) es primitivo, ya que sus coeficientes \(12,14,0,-1\) no tienen un factor común mayor que \(1\), así que no se puede reducir a un múltiplo entero más pequeño manteniendo coeficientes enteros del mismo grado con \(a\neq 0\).

Por lo tanto, el valor mínimo es:

\[
\boxed{27}
\]