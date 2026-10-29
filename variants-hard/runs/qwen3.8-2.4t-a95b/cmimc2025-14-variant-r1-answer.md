

Identificamos los vértices con vectores de \(\mathbb{F}_2^n\). Dos vértices son adyacentes si se obtienen sumando (XOR) un vector de peso de Hamming exactamente \(k\). Así, la componente conexa del vértice \(0\) es el subgrupo aditivo generado por todos los vectores de peso \(k\), y

\[
d_{n,k}=2^{n-r},
\]

donde \(r\) es la dimensión del espacio generado por esos vectores.

**Caso 1: \(k<n\).**

Para cualesquiera dos posiciones distintas \(i,j\), como \(k\le n-1\), podemos elegir un conjunto \(C\) de \(k-1\) posiciones entre las otras \(n-2\). Entonces los vectores de peso \(k\) con soportes \(C\cup\{i\}\) y \(C\cup\{j\}\) están en el conjunto generador, y su suma es

\[
e_i+e_j.
\]

Por tanto, el subgrupo contiene todos los vectores \(e_i+e_j\), que generan el subespacio de vectores de peso par, de dimensión \(n-1\).

- Si \(k\) es par, todos los generadores tienen peso par, luego el subgrupo es exactamente el subespacio de peso par. Entonces

\[
d_{n,k}=2.
\]

- Si \(k\) es impar, hay generadores de peso impar, luego el subgrupo es todo \(\mathbb{F}_2^n\). Entonces

\[
d_{n,k}=1.
\]

**Caso 2: \(k=n\).**

El único vector de peso \(n\) es el vector todo unos. Cada vértice solo se conecta con su complemento, así que hay componentes de tamaño \(2\):

\[
d_{n,n}=2^{n-1}.
\]

Por tanto, para cada \(n\),

\[
\sum_{k=1}^n d_{n,k}
=
2^{n-1}
+
\sum_{k=1}^{n-1}
\begin{cases}
1, & k \text{ impar},\\
2, & k \text{ par}.
\end{cases}
\]

Si \(m=n-1\), la suma sobre \(k=1,\dots,m\) es

\[
m+\left\lfloor \frac{m}{2}\right\rfloor.
\]

Así,

\[
\sum_{k=1}^n d_{n,k}
=
2^{n-1}+(n-1)+\left\lfloor\frac{n-1}{2}\right\rfloor.
\]

Ahora sumamos para \(n=1,\dots,12\):

\[
\sum_{n=1}^{12}2^{n-1}=2^{12}-1=4095,
\]

\[
\sum_{n=1}^{12}(n-1)=0+1+\cdots+11=66,
\]

\[
\sum_{n=1}^{12}\left\lfloor\frac{n-1}{2}\right\rfloor
=
0+0+1+1+\cdots+5+5=30.
\]

Total:

\[
4095+66+30=4191.
\]

\[
\boxed{4191}
\]