# Solución

## Paso 1: Triángulos $PQR$ y $TPT$

En el triángulo $PQR$, con $PQ=38$, $QR=19$ y $\angle Q = 60^\circ$, el teorema del coseno da:
$$PR^2 = 38^2 + 19^2 - 2(38)(19)\cos 60^\circ = 1444 + 361 - 722 = 1083 \implies PR = 19\sqrt{3}.$$

Además, $\cos\angle R = \dfrac{19^2 + 1083 - 38^2}{2\cdot 19\cdot 19\sqrt3} = 0$, así que $\angle R = 90^\circ$ y $\angle P = 30^\circ$.

Por simetría de datos ($TP=38$, $ST=19$, $\angle T=60^\circ$), el triángulo $TPS$ es congruente: $PS = 19\sqrt{3}$, $\angle S = 90^\circ$.

## Paso 2: Coordenadas

En el triángulo $PRS$ con $PR=PS=19\sqrt3$ y $RS=48$:
$$\cos\angle RPS = \frac{1083+1083-2304}{2\cdot 1083} = -\frac{23}{361},$$
de donde $\cos\frac{\angle RPS}{2} = \frac{13}{19}$, $\sin\frac{\angle RPS}{2} = \frac{8\sqrt3}{19}$.

Colocando la bisectriz de $\angle RPS$ sobre el eje $x$ con $P=(0,0)$:
$$R = 19\sqrt3\left(\tfrac{13}{19}, \tfrac{8\sqrt3}{19}\right) = (13\sqrt3,\ 24), \qquad S = (13\sqrt3,\ -24),$$
(compruébese: $RS = 48$ ✓). Como $QR \perp PR$ con $QR = 19$:
$$Q = R + 19\cdot\tfrac{(-8\sqrt3,\,13)}{19} = (5\sqrt3,\ 37), \qquad T = (5\sqrt3,\ -37).$$

Verificación: $PQ = PT = \sqrt{75+1369} = 38$ ✓, $QR = ST = \sqrt{192+169}=19$ ✓, $\cos\angle Q = \frac{361}{38\cdot 19} = \frac12$ ✓, y todos los productos cruzados de lados consecutivos tienen el mismo signo (pentágono convexo) ✓.

## Paso 3: El minimizador está en el eje de simetría

La función $g$ es convexa y simétrica respecto al eje $x$, así que para todo $Y=(x,y)$:
$$g(x, 0) = g\left(\tfrac{(x,y)+(x,-y)}{2}\right) \le \frac{g(x,y)+g(x,-y)}{2} = g(x,y).$$
Basta entonces minimizar sobre el eje $x$. Sea $Y = (x,0)$ con $x\ge 0$:
$$f(x) = x + 2\sqrt{(x-5\sqrt3)^2 + 1369} + 2\sqrt{(x-13\sqrt3)^2 + 576}.$$

## Paso 4: Punto crítico

$$f'(x) = 1 + \frac{2(x-5\sqrt3)}{\sqrt{(x-5\sqrt3)^2+1369}} + \frac{2(x-13\sqrt3)}{\sqrt{(x-13\sqrt3)^2+576}}.$$

Evaluando en $x = 5\sqrt3$:
$$f'(5\sqrt3) = 1 + 0 + \frac{2(-8\sqrt3)}{\sqrt{192+576}} = 1 - \frac{16\sqrt3}{16\sqrt3} = 0.$$

Como $f$ es estrictamente convexa (suma de funciones estrictamente convexas), $x^\ast = 5\sqrt3$ es el mínimo global. En efecto, en $Y^\ast = (5\sqrt3, 0)$ los vectores unitarios hacia los vértices suman cero:
$$\underbrace{(1,0)}_{P} + \underbrace{(0,-1)}_{Q} + \underbrace{(0,1)}_{T} + \underbrace{\left(-\tfrac12, -\tfrac{\sqrt3}{2}\right)}_{R} + \underbrace{\left(-\tfrac12, \tfrac{\sqrt3}{2}\right)}_{S} = (0,0). ✓$$

## Paso 5: Valor mínimo

- $PY^\ast = 5\sqrt3$
- $QY^\ast = TY^\ast = 37$ (¡$Y^\ast$ está sobre el segmento $QT$!)
- $RY^\ast = SY^\ast = \sqrt{192 + 576} = \sqrt{768} = 16\sqrt3$

$$g(Y^\ast) = 5\sqrt3 + 37 + 37 + 16\sqrt3 + 16\sqrt3 = 74 + 37\sqrt{3}.$$

Por lo tanto $m = 74$, $n = 37$, $p = 3$:

$$m + n + p = \boxed{114}$$