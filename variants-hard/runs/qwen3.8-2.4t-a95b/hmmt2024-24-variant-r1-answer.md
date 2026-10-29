

Sea \(s\) la longitud del lado del cuadrado. Colocamos

\[
P=(0,0),\quad Q=(s,0),\quad R=(s,s).
\]

El punto medio de \(\overline{PQ}\) es

\[
M=\left(\frac{s}{2},0\right).
\]

Sea \(\theta\) el ángulo agudo que forma la recta \(m\) con \(\overline{PQ}\). Como \(m\) pasa por \(M\) e interseca al segmento \(\overline{QR}\), tenemos \(0<\theta<\arctan 2\). Un vector unitario en la dirección de \(m\) es \((\cos\theta,\sin\theta)\).

La distancia de \(P\) a \(m\) es la magnitud del producto cruz entre el vector unitario de la recta y el vector \(M\to P\):

\[
M\to P=\left(-\frac{s}{2},0\right).
\]

Entonces

\[
d(P,m)=\left|\cos\theta\cdot 0-\sin\theta\left(-\frac{s}{2}\right)\right|
=\frac{s}{2}\sin\theta.
\]

Dado que esta distancia es \(5\),

\[
\frac{s}{2}\sin\theta=5
\quad\Longrightarrow\quad
s\sin\theta=10.
\]

Ahora calculamos la distancia de \(R\) a \(m\). El vector desde \(M\) hasta \(R\) es

\[
M\to R=\left(\frac{s}{2},s\right).
\]

Por tanto,

\[
d(R,m)=\left|\cos\theta\cdot s-\sin\theta\cdot \frac{s}{2}\right|.
\]

Como la recta interseca \(\overline{QR}\), se tiene \(\tan\theta<2\), así que la expresión dentro del valor absoluto es positiva:

\[
d(R,m)=s\cos\theta-\frac{s}{2}\sin\theta.
\]

Dado que esta distancia es \(8\),

\[
s\cos\theta-\frac{s}{2}\sin\theta=8.
\]

Pero \(\frac{s}{2}\sin\theta=5\), así que

\[
s\cos\theta-5=8
\quad\Longrightarrow\quad
s\cos\theta=13.
\]

Finalmente,

\[
s^2=(s\sin\theta)^2+(s\cos\theta)^2=10^2+13^2=100+169=269.
\]

El área del cuadrado es \(s^2\).

\[
\boxed{269}
\]