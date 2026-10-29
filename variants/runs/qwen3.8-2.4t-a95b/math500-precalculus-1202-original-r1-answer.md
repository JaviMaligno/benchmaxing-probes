

Sea
\[
A=\arccos x,\qquad B=\arccos 2x,\qquad C=\arccos 3x.
\]
Por el dominio de los tres términos, \(-\frac13\le x\le \frac13\). Si \(x\le 0\), entonces \(A,B,C\ge \frac{\pi}{2}\), con lo que
\[
A+B+C\ge \frac{3\pi}{2}>\pi,
\]
imposible. Por tanto, \(x>0\).

Como
\[
A+B+C=\pi,
\]
tenemos \(A+B=\pi-C\). Tomando cosenos:
\[
\cos(A+B)=\cos(\pi-C)=-\cos C=-3x.
\]
Pero
\[
\cos(A+B)=\cos A\cos B-\sin A\sin B
=2x^2-\sqrt{1-x^2}\sqrt{1-4x^2},
\]
donde los senos son no negativos. Así,
\[
2x^2-\sqrt{(1-x^2)(1-4x^2)}=-3x,
\]
es decir,
\[
\sqrt{(1-x^2)(1-4x^2)}=2x^2+3x.
\]
Elevando al cuadrado:
\[
(1-x^2)(1-4x^2)=(2x^2+3x)^2.
\]
Expandiendo,
\[
1-5x^2+4x^4=4x^4+12x^3+9x^2,
\]
de donde
\[
12x^3+14x^2-1=0.
\]

Ahora debemos asegurar que esta cúbica da la menor suma posible de coeficientes. Sea
\[
f(t)=12t^3+14t^2-1.
\]
Si \(f\) tuviera una raíz racional \(p/q\) en mínima expresión, por el teorema de la raíz racional tendríamos \(p\mid 1\) y \(q\mid 12\), así que \(7\nmid q\). Reduciendo módulo \(7\),
\[
f(t)\equiv 5t^3+6 \pmod 7.
\]
Los cubos módulo \(7\) son \(0,1,6\), y \(5u+6\) toma valores \(6,4,1\) respectivamente, nunca \(0\). Por tanto, \(f\) no tiene raíces racionales. Al ser cúbico, es irreducible sobre \(\mathbb{Q}\), así que es el polinomio mínimo de \(x\) hasta múltiplos racionales.

Si otro polinomio cúbico entero
\[
P(t)=at^3+bt^2+ct+d
\]
satisface \(P(x)=0\), entonces \(P(t)=\lambda f(t)\) para algún \(\lambda\in\mathbb{Q}\). Mirando el término constante,
\[
d=-\lambda,
\]
y como \(d\) es entero, \(\lambda\) es entero no nulo. Luego
\[
|a|+|b|+|c|+|d|
=|\lambda|\bigl(|12|+|14|+|0|+|-1|\bigr)
=27|\lambda|\ge 27.
\]
El mínimo se alcanza con \(\lambda=\pm1\).

\[
\boxed{27}
\]