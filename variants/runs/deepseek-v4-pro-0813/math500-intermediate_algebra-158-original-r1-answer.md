Vamos a maximizar \(P = a b^2 c^3 d^4\) con \(a+b+c+d=10\).

Dividimos \(a\), \(b\), \(c\), \(d\) en partes asociadas a los exponentes:

- \(a\): 1 parte (exponente 1),
- \(b\): 2 partes (exponente 2),
- \(c\): 3 partes (exponente 3),
- \(d\): 4 partes (exponente 4).

Por la desigualdad de medias aritmética y geométrica ponderada:

\[
\frac{a + b + c + d}{1+2+3+4}
\ge
\left(
\frac{a}{1}\right)^{\!1/10}
\left(\frac{b}{2}\right)^{\!2/10}
\left(\frac{c}{3}\right)^{\!3/10}
\left(\frac{d}{4}\right)^{\!4/10}
\]

Como \(a+b+c+d=10\) y \(1+2+3+4=10\):

\[
1 \ge
\frac{a}{1}\left(\frac{b}{2}\right)^{\!2}
\left(\frac{c}{3}\right)^{\!3}
\left(\frac{d}{4}\right)^{\!4}
\]

Elevamos al cuadrado y reordenamos:

\[
ab^2c^3d^4 \le 1^2 \cdot 4^4 \cdot 9^3 \cdot 16^2
\]

Calculamos:

\[
4^4 = 256,\qquad 9^3 = 729,\qquad 16^2 = 256
\]

\[
256 \cdot 729 \cdot 256 = 256^2 \cdot 729
\]

\[
256^2 = 65536
\]

\[
65536 \cdot 729 = 47775744
\]

La igualdad se alcanza cuando

\[
\frac{a}{1} = \frac{b}{2} = \frac{c}{3} = \frac{d}{4}
\]

es decir,

\[
a = 1,\quad b = 2,\quad c = 3,\quad d = 4
\]

y en efecto \(1+2+3+4=10\).

\[
\boxed{47775744}
\]