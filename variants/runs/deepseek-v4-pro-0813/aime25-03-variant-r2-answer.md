Vamos a resolver el problema paso a paso.

Sean:

- \(m\) = número de miembros que eligieron mango,
- \(b\) = número que eligieron banana,
- \(k\) = número que eligieron kiwi.

Las condiciones son:

\[
m+b+k = 10,
\]

\[
m > b > k \ge 1.
\]

Primero enumeramos las ternas \((m,b,k)\) posibles con enteros positivos que sumen 10 y cumplan \(m>b>k\).

Posibles valores de \(k\):

- Si \(k=1\), entonces \(m+b=9\) con \(m>b>1\). Las posibilidades:
  - \(b=2,\ m=7\)
  - \(b=3,\ m=6\)
  - \(b=4,\ m=5\)

El caso \(b=5,\ m=4\) no cumple \(m>b\). Así que:

\[
(7,2,1),\ (6,3,1),\ (5,4,1).
\]

- Si \(k=2\), entonces \(m+b=8\) con \(m>b>2\). Las posibilidades:
  - \(b=3,\ m=5\)

El caso \(b=4,\ m=4\) no cumple \(m>b\). Así que:

\[
(5,3,2).
\]

- Para \(k=3\), tendríamos \(m+b=7\) con \(m>b>3\). El menor \(b\) sería 4, pero entonces \(m\le 3\), imposible. No hay más casos.

Por tanto, las ternas válidas son:

\[
(7,2,1),\ (6,3,1),\ (5,4,1),\ (5,3,2).
\]

Para cada terna, el número de asignaciones distintas de sabores a los 10 miembros es el coeficiente multinomial:

\[
\frac{10!}{m!\, b!\, k!}.
\]

Calculamos cada una.

1. Para \((7,2,1)\):

\[
\frac{10!}{7!\,2!\,1!}
= \frac{10\cdot 9}{2} = 45.
\]

Espera, calculamos con cuidado:

\[
\frac{10!}{7!\,2!\,1!}
= \frac{10\cdot 9\cdot 8!}{7!\cdot 2}
\]

Mejor directamente:

\[
\frac{10!}{7!\,2!} = \frac{10\cdot 9\cdot 8}{2} = 360.
\]

Recordemos que \(10!/7! = 10\cdot 9\cdot 8 = 720\), y dividimos entre \(2!\):

\[
720/2 = 360.
\]

2. Para \((6,3,1)\):

\[
\frac{10!}{6!\,3!\,1!}
= \frac{10\cdot 9\cdot 8\cdot 7}{3!}
= \frac{5040}{6} = 840.
\]

3. Para \((5,4,1)\):

\[
\frac{10!}{5!\,4!\,1!}
= \frac{10\cdot 9\cdot 8\cdot 7\cdot 6}{4!}
= \frac{30240}{24} = 1260.
\]

4. Para \((5,3,2)\):

\[
\frac{10!}{5!\,3!\,2!}
= \frac{10\cdot 9\cdot 8\cdot 7\cdot 6}{3!\cdot 2!}
= \frac{30240}{12} = 2520.
\]

Sumamos todo:

\[
N = 360 + 840 + 1260 + 2520 = 4980.
\]

Finalmente, el resto al dividir por 1000:

\[
4980 \bmod 1000 = 980.
\]

\[
\boxed{980}
\]