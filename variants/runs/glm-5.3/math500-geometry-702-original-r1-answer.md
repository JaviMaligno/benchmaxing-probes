## Planteamiento

Como $C$ está al sur y $D$ al este de $O$, los vectores $\vec{OC}$ y $\vec{OD}$ son perpendiculares entre sí y también perpendiculares a $\vec{OH}$ (que es vertical). Entonces:

$$HC^2 = OH^2 + OC^2, \qquad HD^2 = AH^2 + OD^2,\qquad OC^2 + OD^2 = CD^2 = 140^2$$

## Hallar las distancias base

Sumando las dos primeras ecuaciones y usando la tercera:

$$150^2 + 130^2 = 2\,OH^2 + 140^2 \;\Rightarrow\; 39400 = 2\,OH^2 + 19600 \;\Rightarrow\; AH^2 = 9900$$

Luego:
$$OC^2 = 150^2 - 9900 = 12600, \qquad OD^2 = 130^2 - 9900 = 7000$$

(verificación: $12600 + 7000 = 19600 = 140^2$ ✓).

## Minimizar $HP$

El ahorro es $HC + HD - HP = 280 - \sqrt{OH^2 + OP^2}$, así que hay que **minimizar $OP$** con $P$ en el segmento $CD$.

Escribiendo $P = (1-t)\,C + t\,D$ con $0 \le t \le 1$, y usando que $\vec{OC} \perp \vec{OD}$:

$$OP^2 = 12600(1-t)^2 + 7000\,t^2$$

Derivando: $f'(t) = -25200 + 39200t = 0 \Rightarrow t = \tfrac{9}{14} \in [0,1]$ ✓

$$OP^2_{\min} = 12600\cdot\frac{25}{196} + 7000\cdot\frac{81}{196} = \frac{882000}{196} = 4500 \;\Rightarrow\; OP = 30\sqrt{5}$$

(Equivale a la distancia de $O$ a la recta $CD$, que efectivamente cae dentro del segmento.)

## Longitud de la nueva cuerda

$$HP = \sqrt{OH^2 + OP^2_{\min}} = \sqrt{9900 + 4500} = \sqrt{14400} = 120 \text{ m}$$

## Ahorro máximo

$$280 - 120 = \boxed{160 \text{ m}}$$