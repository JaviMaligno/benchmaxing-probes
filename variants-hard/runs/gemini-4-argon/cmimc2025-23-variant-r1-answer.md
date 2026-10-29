Para calcular el área del pentágono $P R U V T$, podemos establecer un sistema de coordenadas cartesianas.

**Paso 1: Ubicar los puntos $P$ y $Q$**
Sea el punto medio del segmento $PQ$ el origen de coordenadas $O(0,0)$ y hagamos coincidir la recta $PQ$ con el eje $x$. Dado que $PQ = 2$ y los puntos $T, P, Q, U$ siguen ese orden sobre la recta, ubicamos $P$ a la izquierda de $Q$:
$$P = (-1, 0), \quad Q = (1, 0)$$

**Paso 2: Determinar los puntos $R$ y $S$**
Las circunferencias $\odot P$ y $\odot Q$ tienen radio $r_1 = PQ = 2$. Sus puntos de intersección $R$ y $S$ se encuentran sobre la mediatriz de $PQ$, que es el eje $y$ ($x = 0$). La distancia desde $P(-1, 0)$ hasta $R(0, y)$ es $2$:
$$(-1 - 0)^2 + (0 - y)^2 = 2^2 \implies 1 + y^2 = 4 \implies y = \pm\sqrt{3}$$
Eligiendo $R$ en el semiplano superior ($y > 0$), obtenemos:
$$R = (0, \sqrt{3}), \quad S = (0, -\sqrt{3})$$

**Paso 3: Determinar los puntos $T$ y $U$**
La distancia entre $R$ y $S$ es $RS = 2\sqrt{3}$. Las circunferencias $\odot R$ y $\odot S$ tienen radio $r_2 = RS = 2\sqrt{3}$ y sus puntos de intersección $T$ y $U$ se ubican sobre la mediatriz de $RS$, que es nuevamente el eje $x$ ($y = 0$). Para un punto $(x, 0)$ en la intersección:
$$(x - 0)^2 + (0 - \sqrt{3})^2 = (2\sqrt{3})^2 \implies x^2 + 3 = 12 \implies x^2 = 9 \implies x = \pm 3$$
Para que los puntos $T, P, Q, U$ aparezcan en ese orden sobre el eje $x$ ($-3 < -1 < 1 < 3$), asignamos:
$$T = (-3, 0), \quad U = (3, 0)$$

**Paso 4: Determinar el punto $V$**
La distancia entre $T$ y $U$ es $TU = 3 - (-3) = 6$. Las circunferencias $\odot T$ y $\odot U$ tienen radio $r_3 = TU = 6$, y sus intersecciones $V$ y $W$ yacen sobre la mediatriz de $TU$ (el eje $y$, $x = 0$). Para $(0, y)$ en la intersección:
$$(0 - 3)^2 + (y - 0)^2 = 6^2 \implies 9 + y^2 = 36 \implies y^2 = 27 \implies y = \pm 3\sqrt{3}$$
Como $R$ y $V$ están del mismo lado de la recta $PQ$ ($y > 0$), tenemos:
$$V = (0, 3\sqrt{3})$$

**Paso 5: Calcular el área del pentágono $P R U V T$**
Los vértices del pentágono son $P(-1, 0)$, $R(0, \sqrt{3})$, $U(3, 0)$, $V(0, 3\sqrt{3})$ y $T(-3, 0)$.

Observamos que el punto $P(-1,0)$ está sobre la base $TU$ del triángulo $\triangle TUV$, y el punto $R(0, \sqrt{3})$ está en el interior de dicho triángulo. Por lo tanto, el pentágono $P R U V T$ se obtiene al restar el triángulo $\triangle PUR$ del triángulo $\triangle TUV$:

1. El triángulo $\triangle TUV$ tiene base $TU = 6$ sobre el eje $x$ y altura $y_V = 3\sqrt{3}$:
   $$\text{Área}(\triangle TUV) = \frac{1}{2} \times 6 \times 3\sqrt{3} = 9\sqrt{3}$$

2. El triángulo $\triangle PUR$ tiene base $PU = 3 - (-1) = 4$ sobre el eje $x$ y altura $y_R = \sqrt{3}$:
   $$\text{Área}(\triangle PUR) = \frac{1}{2} \times 4 \times \sqrt{3} = 2\sqrt{3}$$

Restando ambas áreas obtenemos el área del pentágono $P R U V T$:
$$\text{Área}(P R U V T) = 9\sqrt{3} - 2\sqrt{3} = 7\sqrt{3}$$

\boxed{7\sqrt{3}}