

Coloquemos \(\omega_3\) con centro en el origen y diámetro sobre el eje \(x\):

\[
P=(-12,0),\qquad Q=(12,0).
\]

Sea \(r\) el radio de \(\omega_2\), y sea \(T=(t,0)\) el punto donde el arco de \(\omega_2\) toca \(PQ\). Como el arco de \(\omega_2\) es tangente a \(PQ\), su centro está directamente encima de \(T\):

\[
C=(t,r).
\]

El diámetro de \(\omega_2\) es una cuerda de \(\omega_3\). La distancia del centro de \(\omega_3\) al punto medio de esa cuerda es \(|OC|\), y la semicuerda mide \(r\). Por tanto,

\[
|OC|^2+r^2=12^2.
\]

Pero \(|OC|^2=t^2+r^2\), así que

\[
t^2+r^2+r^2=144
\]
\[
t^2+2r^2=144.
\]

Luego

\[
PT\cdot TQ=(t+12)(12-t)=144-t^2=2r^2.
\]

Así que basta hallar \(r\).

Ahora consideremos \(\omega_1\), de radio \(3\). Su diámetro es paralelo al de \(\omega_3\), por lo que es horizontal. Sea \(M\) su centro. Como su diámetro es una cuerda horizontal de la circunferencia de \(\omega_2\), de radio \(r\) y centro \(C=(t,r)\), tenemos

\[
M=(t,r+d)
\]

para algún \(d\). Los extremos del diámetro de \(\omega_1\) están a distancia \(3\) de \(M\), y sobre la circunferencia de \(\omega_2\), así que

\[
3^2+d^2=r^2
\]
\[
d^2=r^2-9.
\]

La línea del diámetro de \(\omega_2\) es perpendicular a \(OC\). Un vector unitario normal a esa línea es

\[
\mathbf n=\frac{(t,r)}{\sqrt{t^2+r^2}}.
\]

Como el arco de \(\omega_1\) es tangente al diámetro de \(\omega_2\), la distancia de \(M\) a esa línea es \(3\):

\[
\left|\mathbf n\cdot(M-C)\right|=3.
\]

Pero \(M-C=(0,d)\), entonces

\[
\left|\frac{r}{\sqrt{t^2+r^2}}d\right|=3.
\]

Elevando al cuadrado:

\[
\frac{r^2d^2}{t^2+r^2}=9.
\]

Usamos \(d^2=r^2-9\) y, de la relación anterior, \(t^2+r^2=144-r^2\):

\[
\frac{r^2(r^2-9)}{144-r^2}=9.
\]

Entonces

\[
r^2(r^2-9)=9(144-r^2)
\]
\[
r^4-9r^2=1296-9r^2
\]
\[
r^4=1296
\]
\[
r^2=36.
\]

Finalmente,

\[
PT\cdot TQ=2r^2=2\cdot 36=72.
\]

\[
\boxed{72}
\]