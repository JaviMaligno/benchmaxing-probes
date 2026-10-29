Sean \([X]\) el área de una figura \(X\). Usamos coordenadas afines, ya que las razones sobre los lados y las razones de áreas se preservan.

Tomemos como triángulo de referencia
\[
P=(0,0),\qquad Q=(1,0),\qquad R=(0,1).
\]

Las longitudes dadas implican las razones
\[
\frac{PD}{PQ}=\frac{3}{18}=\frac16,\qquad
\frac{PE}{PQ}=\frac{12}{18}=\frac23,
\]
y
\[
\frac{PF}{PR}=\frac{5}{30}=\frac16,\qquad
\frac{PG}{PR}=\frac{20}{30}=\frac23.
\]
Por tanto,
\[
D=\left(\frac16,0\right),\quad E=\left(\frac23,0\right),\quad
F=\left(0,\frac16\right),\quad G=\left(0,\frac23\right).
\]

El cuadrilátero \(DEGF\) es la región entre los triángulos semejantes \(PEG\) y \(PDF\). Así,
\[
[DEGF]=[PEG]-[PDF]
=\left(\left(\frac23\right)^2-\left(\frac16\right)^2\right)[PQR].
\]
\[
[DEGF]=\left(\frac49-\frac1{36}\right)[PQR]
=\frac5{12}[PQR].
\]
Como \([DEGF]=300\),
\[
[PQR]=300\cdot \frac{12}{5}=720.
\]

Ahora calculamos el área del heptágono. Como \(M\) es la reflexión de \(D\) respecto de \(F\),
\[
M=2F-D=\left(-\frac16,\frac13\right).
\]
Como \(N\) es la reflexión de \(G\) respecto de \(E\),
\[
N=2E-G=\left(\frac43,-\frac13\right).
\]

Los vértices del heptágono son, en orden,
\[
P,\ F,\ N,\ Q,\ R,\ E,\ M.
\]
En coordenadas de referencia, aplicamos la fórmula de área de Gauss (shoelace):
\[
2A_0=
\left|
0+\left(0\cdot\left(-\frac13\right)-\frac16\cdot\frac43\right)
+\left(\frac43\cdot0-\left(-\frac13\right)\cdot1\right)
+(1\cdot1-0)
+\left(0\cdot0-1\cdot\frac23\right)
+\left(\frac23\cdot\frac13-0\right)
+0
\right|.
\]
\[
2A_0=\left|-\frac29+\frac13+1-\frac23+\frac29\right|
=\frac23.
\]
Por tanto,
\[
A_0=\frac13.
\]

El triángulo de referencia tiene área \(\frac12\), luego la razón entre el heptágono y el triángulo es
\[
\frac{A_0}{[PQR]_0}=\frac{1/3}{1/2}=\frac23.
\]
Entonces,
\[
[PFNQREM]=\frac23[PQR]=\frac23\cdot720=480.
\]

\[
\boxed{480}
\]