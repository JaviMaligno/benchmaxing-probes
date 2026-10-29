Podemos escalar el hexágono yUn par de lados opuestos del hexágono separamos con la notación \(y = h\) y \(y = -h\), donde \(h = \frac{\sqrt{3}}{2}\) y \(x \in [-\frac{1}{2}, \frac{1}{2}]\) en cada uno de esos lados. Tomamos lado \(1\), así que el área es
\[
A = \frac{3\sqrt{3}}{2}.
\]

**Peso de una línea.** Si una línea \(L\) corta al hexágono en una cuerda de longitud \(\ell(L)\), parametrizando los dos puntos aleatorios por la línea y sus posiciones sobre la cuerda se obtiene que el peso de esa línea es proporcional a \(\ell(L)^3\). Además,
\[
\int_{\text{todas las líneas}} \ell(L)^3\,dL = 3A^2.
\]

**Par de lados opuestos fijado.** Calculamos la integral de \(\ell^3\) sobre las líneas cuyos extremos están en los lados \(y = \pm h\). Los extremos son
\[
T = (x,h), \qquad B = (u,-h),
\]
con \(x,u \in [-\frac12,\frac12]\). Sea \(r = x-u\). Entonces
\[
\ell = \sqrt{r^2 + 4h^2}.
\]
La línea es \(y = mx+b\), con \(m = \frac{2h}{r}\). Usando la medida invariante de líneas
\[
dL = \frac{dm\,db}{(1+m^2)^{3/2}},
\]
el jacobiano de \((x,u)\mapsto(m,b)\) es \(\frac{4h^2}{|r|^3}\). Como \((1+m^2)^{3/2} = \frac{\ell^3}{|r|^3}\), resulta
\[
\ell^3\,dL = 4h^2\,dx\,du.
\]
Por lo tanto, para este par de lados,
\[
J = \int \ell^3\,dL
= 4h^2 \int_{-1/2}^{1/2}\int_{-1/2}^{1/2} dx\,du
= 4h^2 = 3.
\]

**Suma de los tres pares.** Por simetría, cada uno de los tres pares de lados opuestos contribuye lo mismo, y las líneas que pasan por vértices tienen medida nula. Así,
\[
P = \frac{3J}{3A^2}
= \frac{9}{3\cdot \frac{27}{4}}
= \frac{4}{9}.
\]

\[
\boxed{\frac{4}{9}}
\]