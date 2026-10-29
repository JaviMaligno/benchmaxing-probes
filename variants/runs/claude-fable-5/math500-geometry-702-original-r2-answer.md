## Planteamiento

Coloco el origen en $O$, con $C$ al sur, $D$ al este y $H$ a altura $h$ sobre $O$:
- $C = (0, -c, 0)$, $D = (d, 0, 0)$, $H = (0, 0, h)$.

Como $OC \perp OD$ (sur y este), por Pitágoras: $c^2 + d^2 = CD^2 = 140^2 = 19600$.

**Hallar la altura $h$.** Las cuerdas dan:
$$HC^2 = c^2 + h^2 = 150^2 = 22500, \qquad HD^2 = d^2 + h^2 = 130^2 = 16900.$$

Sumando: $(c^2 + d^2) + 2h^2 = 39400$, es decir $19600 + 2h^2 = 39400$, así que $h^2 = 9900$. Entonces $c^2 = 22500 - 9900 = 12600$ y $d^2 = 16900 - 9900 = 7000$.

## Minimizar $HP$

La cuerda nueva más corta es la distancia de $H$ a la recta $CD$ (el pie de la perpendicular cae dentro del segmento, pues los ángulos $\angle HCD$ y $\angle HDC$ son agudos). Uso el producto cruz:

$$\vec{CD} = (d, c, 0), \qquad \vec{CH} = (0, c, h)$$
$$\vec{CD} \times \vec{CH} = (ch,\, -dh,\, dc)$$
$$\|\vec{CD} \times \vec{CH}\|^2 = h^2(c^2 + d^2) + c^2 d^2 = 9900 \cdot 19600 + 12600 \cdot 7000 = 282\,240\,000$$

La raíz cuadrada es $16800$, por lo que la distancia mínima es:
$$HP_{\min} = \frac{16800}{CD} = \frac{16800}{140} = 120 \text{ m}.$$

## Ahorro máximo

La cuerda original usada era $HC + HD = 150 + 130 = 280$ m, y la nueva cuerda mínima mide $120$ m:

$$280 - 120 = 160 \text{ m}.$$

$$\boxed{160 \text{ m}}$$