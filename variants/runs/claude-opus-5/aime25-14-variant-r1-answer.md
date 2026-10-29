## Planteamiento

**Diagonales desde $P$.** En el triángulo $PQR$: $PQ=38$, $QR=19$, $\angle Q=60^\circ$, luego
$$PR^2=38^2+19^2-2\cdot38\cdot19\cdot\tfrac12=1083\ \Rightarrow\ PR=19\sqrt3 .$$
Como $19^2+1083=1444=38^2$, el triángulo es rectángulo en $R$ (es un $30$-$60$-$90$). Por simetría, $PS=19\sqrt3$ y el ángulo en $S$ del triángulo $PST$ también es recto.

**Coordenadas.** El pentágono es simétrico respecto a la mediatriz de $RS$ (tomada como eje $y$). Con $R=(-24,0)$, $S=(24,0)$:
$$P=(0,\sqrt{1083-576})=(0,13\sqrt3).$$
Imponiendo $RQ\perp RP$ con $|RQ|=19$ (y la orientación que da convexidad):
$$Q=(-37,8\sqrt3),\qquad T=(37,8\sqrt3).$$
Se comprueba: $QR=\sqrt{169+192}=19$, $TP=\sqrt{1369+75}=38$, $\angle Q=\angle T=60^\circ$ y el pentágono es convexo.

**Minimización.** $g$ es convexa y simétrica respecto al eje $y$, así que el mínimo está en $Y=(0,t)$:
$$g(t)=(13\sqrt3-t)+2\sqrt{37^2+(8\sqrt3-t)^2}+2\sqrt{24^2+t^2}.$$
$$g'(t)=-1+\frac{2(t-8\sqrt3)}{\sqrt{1369+(8\sqrt3-t)^2}}+\frac{2t}{\sqrt{576+t^2}}.$$
En $t=8\sqrt3$ el segundo término se anula y
$$\frac{2\cdot 8\sqrt3}{\sqrt{576+192}}=\frac{16\sqrt3}{16\sqrt3}=1,$$
luego $g'(8\sqrt3)=-1+0+1=0$. Por convexidad, ese es el mínimo global; el punto óptimo es el punto medio de $QT$.

**Valor mínimo.**
$$PY=13\sqrt3-8\sqrt3=5\sqrt3,\quad QY=TY=37,\quad RY=SY=\sqrt{768}=16\sqrt3,$$
$$g_{\min}=5\sqrt3+74+32\sqrt3=74+37\sqrt3\approx138.09 .$$

Así $m=74$, $n=37$, $p=3$, y $m+n+p=114$.

\boxed{114}