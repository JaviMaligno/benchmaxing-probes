El área de un paralelogramo limitado por rectas de pendientes \(p\) y \(q\), con diferencias de ordenadas al origen \(a\) y \(b\), vale

\[
\frac{|a|\,|b|}{|p-q|}.
\]

**Primer paralelogramo:**  
Las rectas son \(y=px+r\), \(y=px+s\), \(y=qx+r\), \(y=qx+s\).  
La diferencia de ordenadas al origen en cada familia es \(|r-s|\), así que

\[
\frac{(r-s)^2}{|p-q|}=8
\quad\Rightarrow\quad
(r-s)^2=8|p-q|.
\]

**Segundo paralelogramo:**  
Las rectas son \(y=px+r\), \(y=px-s\), \(y=qx+r\), \(y=qx-s\).  
La diferencia de ordenadas al origen es \(r-(-s)=r+s\), así que

\[
\frac{(r+s)^2}{|p-q|}=50
\quad\Rightarrow\quad
(r+s)^2=50|p-q|.
\]

Dividiendo ambas ecuaciones:

\[
\frac{(r-s)^2}{(r+s)^2}=\frac{8}{50}=\frac{4}{25}.
\]

Por lo tanto,

\[
\frac{|r-s|}{r+s}=\frac25.
\]

Como \(r,s>0\), esto implica que uno de ellos es \(\frac73\) del otro. Escribimos

\[
r=7k,\quad s=3k
\]

o al revés. En cualquier caso,

\[
r+s=10k.
\]

Sustituyendo en la segunda ecuación:

\[
(10k)^2=50|p-q|
\quad\Rightarrow\quad
100k^2=50|p-q|
\quad\Rightarrow\quad
|p-q|=2k^2.
\]

Para enteros positivos \(p,q\) con diferencia \(2k^2\), la suma mínima es

\[
p+q=2k^2+2.
\]

Entonces

\[
p+q+r+s=2k^2+2+10k.
\]

El valor mínimo se obtiene para \(k=1\):

\[
2+2+10=14.
\]

\[
\boxed{14}
\]