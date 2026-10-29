Para hallar el valor mínimo de $g(Y) = PY + QY + RY + SY + TY$, analizamos primero las propiedades geométricas del pentágono convexo $PQRST$.

### Paso 1: Geometría del pentágono y sistema de coordenadas
Observamos que el pentágono es simétrico respecto a la mediatriz del lado $RS$, la cual pasa por el vértice $P$.
En los triángulos $\triangle PQR$ y $\triangle PTS$, tenemos $PQ = PT = 38$, $QR = TS = 19$ y $\angle Q = \angle T = 60^{\circ}$. Aplicando la ley de cosenos en $\triangle PQR$:
$$PR^2 = 38^2 + 19^2 - 2(38)(19)\cos 60^{\circ} = 19^2(4 + 1 - 2) = 3 \cdot 19^2 \implies PR = 19\sqrt{3}.$$
Por tanto, $\triangle PQR$ y $\triangle PTS$ son triángulos rectángulos notables de $30^{\circ}\text{-}60^{\circ}\text{-}90^{\circ}$, con $\angle PRQ = \angle PST = 90^{\circ}$ y $\angle QPR = \angle SPT = 30^{\circ}$.

Sea $M$ el punto medio de $RS$, el cual tomamos como el origen $(0,0)$ de un sistema de coordenadas cartesianas, con la recta $RS$ sobre el eje $x$ y la recta de simetría $MP$ sobre el eje $y$.
- Como $RS = 48$, tenemos $R = (-24, 0)$ y $S = (24, 0)$.
- En el triángulo rectángulo $\triangle PMR$, $PM = \sqrt{PR^2 - RM^2} = \sqrt{(19\sqrt{3})^2 - 24^2} = \sqrt{1083 - 576} = \sqrt{507} = 13\sqrt{3}$. Así, $P = (0, 13\sqrt{3})$.
- El vector $\overrightarrow{RP} = (24, 13\sqrt{3})$ tiene longitud $19\sqrt{3}$. Como $\angle PRQ = 90^{\circ}$, $QR = 19 = \frac{1}{\sqrt{3}}PR$ y el pentágono es convexo, el vector $\overrightarrow{RQ}$ se obtiene rotando $\overrightarrow{RP}$ un ángulo de $90^{\circ}$ en sentido antihorario y escalándolo por $\frac{1}{\sqrt{3}}$:
  $$\overrightarrow{RQ} = \frac{1}{\sqrt{3}}(-13\sqrt{3}, 24) = (-13, 8\sqrt{3}).$$
- Por consiguiente, las coordenadas de $Q$ y $T$ son:
  $$Q = R + \overrightarrow{RQ} = (-24 - 13, 0 + 8\sqrt{3}) = (-37, 8\sqrt{3}), \quad T = (37, 8\sqrt{3}).$$

### Paso 2: Minimización de $g(Y)$
Dado que la función $g(Y)$ es convexa y el conjunto de vértices $\{P, Q, R, S, T\}$ es simétrico respecto al eje $y$, el mínimo global debe alcanzarse en un punto $Y(0, y)$ sobre dicho eje.

Consideremos el punto medio del segmento $QT$, es decir, $Y = (0, 8\sqrt{3})$:
- Los vectores desde $Y$ hacia $Q$ y $T$ son $(-37, 0)$ y $(37, 0)$, por lo que los vectores unitarios en estas direcciones son $\vec{u}_Q = (-1, 0)$ y $\vec{u}_T = (1, 0)$.
- El vector desde $Y$ hacia $P$ es $(0, 5\sqrt{3})$, con vector unitario $\vec{u}_P = (0, 1)$.
- Los vectores desde $Y$ hacia $R$ y $S$ son $(-24, -8\sqrt{3})$ y $(24, -8\sqrt{3})$, ambos de longitud $\sqrt{24^2 + (8\sqrt{3})^2} = \sqrt{576 + 192} = \sqrt{768} = 16\sqrt{3}$. Sus vectores unitarios son:
  $$\vec{u}_R = \left(-\frac{\sqrt{3}}{2}, -\frac{1}{2}\right), \quad \vec{u}_S = \left(\frac{\sqrt{3}}{2}, -\frac{1}{2}\right).$$

Al sumar los cinco vectores unitarios desde $Y$ hacia los vértices del pentágono, obtenemos:
$$\vec{u}_P + \vec{u}_Q + \vec{u}_T + \vec{u}_R + \vec{u}_S = (0, 1) + (-1, 0) + (1, 0) + \left(-\frac{\sqrt{3}}{2}, -\frac{1}{2}\right) + \left(\frac{\sqrt{3}}{2}, -\frac{1}{2}\right) = (0, 0).$$
Como el gradiente de $g$ se anula en $Y = (0, 8\sqrt{3})$ y $g$ es convexa en todo el plano, este punto proporciona el mínimo absoluto de $g(Y)$.

### Paso 3: Cálculo del valor mínimo
Calculamos la suma de las distancias desde $Y = (0, 8\sqrt{3})$ hasta cada vértice:
- $PY = 13\sqrt{3} - 8\sqrt{3} = 5\sqrt{3}$
- $QY = TY = 37$
- $RY = SY = 16\sqrt{3}$

Sumando todas las longitudes:
$$g(Y) = 5\sqrt{3} + 37 + 37 + 16\sqrt{3} + 16\sqrt{3} = 74 + 37\sqrt{3}.$$

Identificando con la forma $m + n\sqrt{p}$, tenemos $m = 74$, $n = 37$ y $p = 3$. Finalmente:
$$m + n + p = 74 + 37 + 3 = 114.$$

\boxed{114}