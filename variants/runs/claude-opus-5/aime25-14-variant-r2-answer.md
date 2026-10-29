## Planteamiento

**Triángulos rectángulos escondidos.** En el triángulo $PQR$: $PQ=38=2\cdot 19=2\cdot QR$ y $\angle Q=60^\circ$, luego es un triángulo $30\text{-}60\text{-}90$ con ángulo recto en $R$, y
$$PR^2=38^2+19^2-2\cdot38\cdot19\cdot\tfrac12=1083\ \Rightarrow\ PR=19\sqrt3 .$$
Por simetría, lo mismo en $PST$: $\angle PST=90^\circ$ y $PS=19\sqrt3$.

**Coordenadas.** Como $PR=PS$, el pentágono es simétrico respecto a la mediatriz de $RS$. Tomo
$$R=(-24,0),\quad S=(24,0),\quad P=(0,13\sqrt3)$$
(pues $1083-576=507=(13\sqrt3)^2$). Con $QR\perp RP$ y $QR=19$:
$$Q=R+\frac{19}{19\sqrt3}(-13\sqrt3,24)=(-37,\,8\sqrt3),\qquad T=(37,\,8\sqrt3).$$
Verificación: $PQ^2=37^2+(5\sqrt3)^2=1369+75=1444=38^2$ ✓. Los productos cruzados consecutivos son todos positivos, así que el pentágono es convexo ✓.

## Minimización

$g$ es estrictamente convexa (los puntos no son colineales), de modo que el mínimo es único y, por simetría, está en el eje $x=0$. Pruebo $Y=(0,8\sqrt3)$, a la misma altura que $Q$ y $T$. Los vectores unitarios desde $Y$ hacia los cinco vértices:
$$(0,1),\quad(-1,0),\quad(1,0),\quad\left(-\tfrac{\sqrt3}{2},-\tfrac12\right),\quad\left(\tfrac{\sqrt3}{2},-\tfrac12\right),$$
pues $YR=\sqrt{576+192}=\sqrt{768}=16\sqrt3$ y $\frac{-24}{16\sqrt3}=-\frac{\sqrt3}{2}$, $\frac{-8\sqrt3}{16\sqrt3}=-\frac12$.

Su suma es $(0,0)$, luego $\nabla g(Y)=0$ y ese punto es el mínimo global (la mediana geométrica).

## Valor mínimo

$$g(Y)=\underbrace{5\sqrt3}_{PY}+\underbrace{37+37}_{QY+TY}+\underbrace{16\sqrt3+16\sqrt3}_{RY+SY}=74+37\sqrt3 .$$

Así $m=74$, $n=37$, $p=3$ y $m+n+p=114$.

\boxed{114}