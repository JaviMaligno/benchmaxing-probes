## Planteamiento

**Paso 1: Dos triángulos congruentes.** En $\triangle PQR$: $PQ=38$, $QR=19$, $\angle Q = 60^\circ$, así que
$$PR^2 = 38^2+19^2-2(38)(19)\cos 60^\circ = 1444+361-722 = 1083 \implies PR = 19\sqrt3.$$
Análogamente, en $\triangle TSP$ (con $TP=38$, $ST=19$, $\angle T=60^\circ$): $SP = 19\sqrt3$.

**Paso 2: Simetría.** Los datos son invariantes bajo el intercambio $Q\leftrightarrow T$, $R\leftrightarrow S$ (pues $PQ=TP$, $QR=ST$, $\angle Q = \angle T$), con $P$ fijo. Entonces el pentágono es simétrico respecto al eje $PS$, con $PR=PS=19\sqrt3$ y $RS=48$.

**Paso 3: Coordenadas.** Pongo $P=(0,0)$ y el eje de simetría como eje $x$. Como $RS=48$ y $PR=PS=19\sqrt3$:
$$R=(13\sqrt3,\,24),\qquad S=(13\sqrt3,\,-24),$$
pues $13\sqrt3 = \sqrt{1083-576}$. Sea $Q=(a,b)$. De $PQ=38$ y $QR=19$:
$$a^2+b^2=1444,\qquad (a-13\sqrt3)^2+(b-24)^2=361 \implies 13\sqrt3\,a+24b=1083.$$
Escribiendo $a=38\cos\theta,\ b=38\sin\theta$, la ecuación lineal da $\cos(\theta-\varphi)=\tfrac{\sqrt3}{2}$ con $\cos\varphi=\tfrac{13}{19},\ \sin\varphi=\tfrac{8\sqrt3}{19}$, y la solución convexa es $\theta=\varphi+30^\circ$:
$$Q=(5\sqrt3,\,37),\qquad T=(5\sqrt3,\,-37).$$
(Verificación: $\cos\angle Q = \frac{1444+361-1083}{2\cdot38\cdot19}=\frac12$ ✓, y los productos cruzados de lados consecutivos tienen signo constante, así que el pentágono es convexo.)

**Paso 4: El mínimo ocurre en el eje.** $g$ es estrictamente convexa (suma de normas) y simétrica respecto al eje $x$, así que su único minimizador está en el eje: $Y=(x,0)$, con
$$g(x)=|x|+2\sqrt{(x-5\sqrt3)^2+37^2}+2\sqrt{(x-13\sqrt3)^2+24^2}.$$

**Paso 5: Punto crítico.** Para $x>0$,
$$g'(x)=1+\frac{2(x-5\sqrt3)}{\sqrt{(x-5\sqrt3)^2+1369}}+\frac{2(x-13\sqrt3)}{\sqrt{(x-13\sqrt3)^2+576}}.$$
Evalúo en $x=5\sqrt3$:
$$g'(5\sqrt3)=1+0+\frac{2(-8\sqrt3)}{\sqrt{192+576}}=1-\frac{16\sqrt3}{16\sqrt3}=0.$$
Como $g$ es estrictamente convexa, $Y_0=(5\sqrt3,0)$ (el punto medio de $QT$) es el minimizador global.

**Paso 6: Valor mínimo.**
$$g(Y_0)=\underbrace{5\sqrt3}_{PY}+2\underbrace{(37)}_{QY=TY}+2\underbrace{\sqrt{(8\sqrt3)^2+24^2}}_{RY=SY}=5\sqrt3+74+2\sqrt{768}=5\sqrt3+74+32\sqrt3=74+37\sqrt3.$$

Así $m=74$, $n=37$, $p=3$, y $m+n+p=114$.

$$\boxed{114}$$