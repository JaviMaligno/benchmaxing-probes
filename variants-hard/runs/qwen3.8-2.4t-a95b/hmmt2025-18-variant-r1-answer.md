

Después de \(60\) minutos, por inducción sobre el radio del máximo,

\[
x_i^{(60)}=\max\{x_{i-60}^{(0)},x_{i-59}^{(0)},\ldots,x_{i+60}^{(0)}\},
\]

es decir, cada posición contiene el máximo de una ventana cíclica de longitud

\[
2\cdot 60+1=121.
\]

Casi seguramente los \(1011\) valores iniciales son todos distintos. Por tanto, los valores distintos después de \(60\) minutos corresponden exactamente a los índices iniciales \(j\) que son el máximo de al menos una ventana de longitud \(121\).

Fijemos un índice \(j\). Sea \(A\) la distancia hacia la izquierda hasta el primer valor inicial mayor que \(x_j\), y \(B\) la distancia hacia la derecha hasta el primer valor inicial mayor que \(x_j\). El mayor intervalo que contiene a \(j\) sin valores mayores tiene longitud

\[
A+B-1.
\]

Así, \(j\) aparece como valor distinto después de \(60\) minutos si y solo si

\[
A+B-1\ge 121,
\]

o equivalentemente

\[
A+B\ge 122.
\]

Calculamos la probabilidad complementaria: \(A+B\le 121\). Condicionemos en que \(x_j=u\). Para que \(A=a\) y \(B=b\), con \(a+b=s\le 121\), los \(s-2\) valores más cercanos entre esos dos lados deben ser menores que \(u\), y los dos valores en las distancias \(a\) y \(b\) deben ser mayores que \(u\). Esto tiene probabilidad condicional

\[
u^{s-2}(1-u)^2.
\]

Como \(121<1011\), no hay solapamiento cíclico en este evento. Entonces

\[
\mathbb{P}(A+B\le 121)
=
\sum_{s=2}^{121} (s-1)\int_0^1 u^{s-2}(1-u)^2\,du.
\]

La integral es

\[
\int_0^1 u^{s-2}(1-u)^2\,du
=
\frac{2}{(s-1)s(s+1)}.
\]

Por tanto,

\[
\mathbb{P}(A+B\le 121)
=
\sum_{s=2}^{121}\frac{2}{s(s+1)}
=
2\left(\frac12-\frac1{122}\right)
=
1-\frac1{61}
=
\frac{60}{61}.
\]

Luego la probabilidad de que un índice fijo contribuya a un valor distinto es

\[
1-\frac{60}{61}=\frac1{61}.
\]

Por linealidad de la esperanza, el número esperado de valores distintos es

\[
1011\cdot \frac1{61}=\frac{1011}{61}.
\]

\[
\boxed{\frac{1011}{61}}
\]