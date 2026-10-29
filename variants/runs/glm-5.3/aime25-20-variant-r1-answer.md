## Razonamiento

**Paso 1: Identificar la circunferencia de $DEF$.**

Como $D$, $E$, $F$ son puntos medios, la circunferencia que circunscribe a $DEF$ es la circunferuencia de los nueve puntos de $PQR$ (radio $R/2$).

**Paso 2: Identificar $G$, $H$, $J$.**

La circunferencia de los nueve puntos corta al lado $QR$ en $D$ y en el pie de la altura desde $P$. Verifico que este pie cae en el segmento $QD$: con $QG = PQ\cos Q = 2\sin 42°\cos 58° \approx 0.709$ y $QD = \sin 80° \approx 0.985$, sí está entre $Q$ y $D$. Análogamente, $H$ es el pie de la altura desde $Q$ (sobre $PR$, con $PH \approx 0.232 < PE \approx 0.848$) y $J$ es el pie de la altura desde $R$ (sobre $PQ$, con $PJ \approx 0.295 < PF \approx 0.669$).

**Paso 3: Homotecia que vincula ambas circunferencias.**

Con el circuncentro en el origen y radio 1, la homotecia de centro el ortocentro $H_o$ y razón $\tfrac12$ lleva la circunferencia circunscrita a la de los nueve puntos, y **preserva los ángulos polares** (si $X' = \frac{X+H_o}{2}$, entonces $X' - N = X/2$). Los preimagenes son:
- $D, E, F \leftarrow$ antípodas $-P, -Q, -R$;
- $G, H, J \leftarrow$ los segundos puntos donde las alturas cortan la circunferencia circunscrita, $A_P, A_Q, A_R$ (reflexiones del ortocentro sobre los lados).

**Paso 4: Posiciones angulares.**

Coloco $P=0°$, $Q=84°$, $R=244°$ (arcos $PQ=84°$, $QR=160°$, $RP=116°$). Entonces:
- $-P = 180°$, $-Q = 264°$, $-R = 64°$;
- $A_P = 148°$ (pues $\angle QPA_P = 90° - 58° = 32°$, arco $= 64°$);
- $A_Q = 340°$ y $A_R = 20°$ (pues $\angle = 90° - 80° = 10°$, arco $= 20°$).

Por lo tanto, en la circunferencia de los nueve puntos:
$$G = 148°,\quad D = 180°,\quad E = 264°,\quad H = 340°,\quad J = 20°,\quad F = 64°$$
en el orden cíclico $G, D, E, H, J, F$, tal como enuncia el problema.

**Paso 5: Medir los arcos.**

Los seis arcos consecutivos son: $\wideparen{GD}=32°$, $\wideparen{DE}=84°$, $\wideparen{EH}=76°$, $\wideparen{HJ}=40°$, $\wideparen{JF}=44°$, $\wideparen{FG}=84°$ (suma $=360°$ ✓, todos menores que $180°$ ✓).

**Paso 6: Cálculo final.**

$$\wideparen{DE} + 2\,\wideparen{HJ} + 3\,\wideparen{FG} = 84 + 2(40) + 3(84) = 84 + 80 + 252 = 416$$

$$\boxed{416}$$