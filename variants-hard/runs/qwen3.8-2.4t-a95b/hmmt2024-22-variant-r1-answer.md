

Sea \(L=QR\), \(a=PQ\) y \(b=PR\). Como \(\angle QPR=90^\circ\), \(QR\) es la hipotenusa.

Coloquemos los puntos sobre \(QR\) midiendo desde \(Q\).

- Por el teorema de la proyección en un triángulo rectángulo, la huella \(X\) de la altura desde \(P\) cumple
\[
QX=\frac{a^2}{L}.
\]

- Por el teorema de la bisectriz, la huella \(Y\) de la bisectriz desde \(P\) cumple
\[
\frac{QY}{YR}=\frac{PQ}{PR}=\frac{a}{b},
\]
así que
\[
QY=\frac{a}{a+b}L.
\]

- La huella \(Z\) de la mediana desde \(P\) es el punto medio de \(QR\), luego
\[
QZ=\frac{L}{2}.
\]

Por simetría, podemos suponer \(a\le b\). Sea \(r=\frac{b}{a}\ge 1\). Entonces, dividiendo por \(L\),
\[
\frac{QX}{L}=\frac{1}{1+r^2},\qquad
\frac{QY}{L}=\frac{1}{1+r},\qquad
\frac{QZ}{L}=\frac12.
\]

Como \(r\ge 1\), se tiene \(X,Y,Z\) en ese orden sobre \(QR\). Por tanto,
\[
\frac{XY}{L}=\frac{1}{1+r}-\frac{1}{1+r^2}
=\frac{r(r-1)}{(1+r)(1+r^2)},
\]
y
\[
\frac{YZ}{L}=\frac12-\frac{1}{1+r}
=\frac{r-1}{2(1+r)}.
\]

Luego
\[
\frac{XY}{YZ}
=
\frac{\frac{r(r-1)}{(1+r)(1+r^2)}}{\frac{r-1}{2(1+r)}}
=
\frac{2r}{1+r^2}.
\]

Dado que \(XY=5\) y \(YZ=13\),
\[
\frac{2r}{1+r^2}=\frac{5}{13}.
\]

Entonces
\[
26r=5+5r^2,
\]
\[
5r^2-26r+5=0.
\]

Sus raíces son
\[
r=\frac{26\pm 24}{10},
\]
es decir,
\[
r=5 \quad \text{o} \quad r=\frac15.
\]

Como \(r\ge 1\), tomamos \(r=5\). Entonces
\[
\frac{YZ}{L}=\frac{5-1}{2(5+1)}=\frac{4}{12}=\frac13.
\]

Como \(YZ=13\),
\[
\frac{L}{3}=13,
\]
por lo que
\[
L=39.
\]

\[
\boxed{39}
\]