## Planteamiento

El pentágono es simétrico: $PQ=TP=38$, $QR=ST=19$, $\angle Q=\angle T=60°$. 

**Diagonales:** En el triángulo $PQR$, por ley de cosenos:
$$PR^2 = 38^2+19^2-2\cdot38\cdot19\cdot\tfrac12 = 1083 \implies PR = 19\sqrt3$$
Como $PR^2+QR^2 = 1083+361 = 1444 = PQ^2$, el ángulo en $R$ es recto. Por simetría, $PS=19\sqrt3$ con ángulo recto en $S$.

**Coordenadas** (eje de simetría = eje $y$): con $R=(-24,0)$, $S=(24,0)$ y $RS=48$:
$$P=(0,\,13\sqrt3) \quad\text{pues } (19\sqrt3)^2-24^2=507=(13\sqrt3)^2$$
Colocando $Q$ a distancia 19 de $R$, perpendicular a $RP$ (lado convexo): $Q=(-37,\,8\sqrt3)$, y por simetría $T=(37,\,8\sqrt3)$. Se verifica $PQ=\sqrt{37^2+(5\sqrt3)^2}=\sqrt{1444}=38$ ✓ y $\angle Q=60°$ ✓.

## Minimización

Como $g$ es convexa y la figura es simétrica, el mínimo está en el eje: $Y=(0,y)$, con
$$h(y)=(13\sqrt3-y) + 2\sqrt{1369+(y-8\sqrt3)^2} + 2\sqrt{576+y^2}$$

Derivando:
$$h'(y) = -1 + \frac{2(y-8\sqrt3)}{\sqrt{1369+(y-8\sqrt3)^2}} + \frac{2y}{\sqrt{576+y^2}}$$

En $y=8\sqrt3$: el segundo término se anula, y el tercero vale
$$\frac{16\sqrt3}{\sqrt{576+192}} = \frac{16\sqrt3}{\sqrt{768}} = \frac{16\sqrt3}{16\sqrt3} = 1$$
así que $h'(8\sqrt3)=0$ exactamente: el mínimo es $Y=(0,\,8\sqrt3)$, a la misma altura que $Q$ y $T$.

## Valor mínimo

- $PY = 13\sqrt3-8\sqrt3 = 5\sqrt3$
- $QY = TY = 37$ (segmentos horizontales)
- $RY = SY = \sqrt{576+192} = \sqrt{768} = 16\sqrt3$

$$g(Y) = 5\sqrt3 + 2(37) + 2(16\sqrt3) = 74 + 37\sqrt3$$

Entonces $m=74$, $n=37$, $p=3$, y $m+n+p = 114$.

$$\boxed{114}$$