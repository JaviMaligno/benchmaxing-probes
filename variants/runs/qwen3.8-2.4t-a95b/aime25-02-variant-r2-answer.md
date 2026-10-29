Las posiciones de \(D,E,F,G\) y las reflexiones centrales dependen sólo de razones afines, así que podemos trabajar en coordenadas afines con

\[
P=(0,0),\qquad Q=(1,0),\qquad R=(0,1).
\]

Las áreas reales son un múltiplo constante de las áreas en estas coordenadas, por lo que las razones de áreas se conservan.

Primero hallamos las fracciones sobre los lados:

\[
PQ=3+9+6=18,\qquad PR=5+15+10=30.
\]

Entonces

\[
\frac{PD}{PQ}=\frac{3}{18}=\frac16,\qquad 
\frac{PE}{PQ}=\frac{12}{18}=\frac23,
\]

\[
\frac{PF}{PR}=\frac{5}{30}=\frac16,\qquad 
\frac{PG}{PR}=\frac{20}{30}=\frac23.
\]

Por tanto,

\[
D=\left(\frac16,0\right),\quad E=\left(\frac23,0\right),\quad
F=\left(0,\frac16\right),\quad G=\left(0,\frac23\right).
\]

Como \(M\) es el reflejo de \(D\) a través de \(F\), \(F\) es punto medio de \(\overline{DM}\), así que

\[
M=2F-D=\left(-\frac16,\frac13\right).
\]

Como \(N\) es el reflejo de \(G\) a través de \(E\), \(E\) es punto medio de \(\overline{GN}\), así que

\[
N=2E-G=\left(\frac43,-\frac23\right).
\]

Ahora calculamos el área coordenada del cuadrilátero \(DEGF\). Usando la fórmula de shoelace con

\[
D=\left(\frac16,0\right),\ E=\left(\frac23,0\right),\ G=\left(0,\frac23\right),\ F=\left(0,\frac16\right),
\]

obtenemos

\[
2[DEGF]_{\text{coord}}
=
\left|\frac49-\frac1{36}\right|
=
\frac{15}{36}
=
\frac5{12}.
\]

Por tanto,

\[
[DEGF]_{\text{coord}}=\frac5{24}.
\]

El área coordenada de \(\triangle PQR\) es

\[
[PQR]_{\text{coord}}=\frac12.
\]

Así que

\[
\frac{[DEGF]}{[PQR]}
=
\frac{5/24}{1/2}
=
\frac5{12}.
\]

Como \([DEGF]=300\),

\[
300=\frac5{12}[PQR]
\]

y entonces

\[
[PQR]=300\cdot \frac{12}{5}=720.
\]

Ahora calculamos el área coordenada del heptágono \(PFNQREM\), cuyos vértices en orden son

\[
(0,0),\ \left(0,\frac16\right),\ \left(\frac43,-\frac23\right),\ (1,0),\ (0,1),\ \left(\frac23,0\right),\ \left(-\frac16,\frac13\right).
\]

Aplicando shoelace:

\[
\sum x_i y_{i+1}=1+\frac29=\frac{11}{9},
\]

\[
\sum y_i x_{i+1}=\frac29-\frac23+\frac23=\frac29.
\]

Por tanto,

\[
2[PFNQREM]_{\text{coord}}
=
\left|\frac{11}{9}-\frac29\right|
=1,
\]

así que

\[
[PFNQREM]_{\text{coord}}=\frac12.
\]

Esto es exactamente igual al área coordenada de \(\triangle PQR\). Luego el área real del heptágono es igual al área real de \(\triangle PQR\):

\[
[PFNQREM]=[PQR]=720.
\]

\[
\boxed{720}
\]