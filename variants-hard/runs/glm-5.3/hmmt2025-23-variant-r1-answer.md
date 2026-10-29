## Planteamiento

Sea $s$ el lado del cuadrado. Pongamos $W=(0,0)$, $X=(s,0)$, $Y=(s,s)$, $Z=(0,s)$ y $Q=(x,y)$ en el interior. Cada triángulo tiene por base un lado del cuadrado y por altura la distancia de $Q$ a ese lado:

$$[QWX]=\tfrac12 sy,\quad [QXY]=\tfrac12 s(s-x),\quad [QYZ]=\tfrac12 s(s-y),\quad [QZW]=\tfrac12 sx.$$

**Paso 1 — El lado del cuadrado.** Los cuatro triángulos descomponen el cuadrado, así que $s^2 = 3+4+6+7 = 20$ y $s = 2\sqrt5$.

**Paso 2 — Parejas de triángulos opuestos.** De las fórmulas anteriores,
$$[QWX]+[QYZ] = \tfrac12 s\big(y+(s-y)\big)=\tfrac12 s^2 = 10,\qquad [QXY]+[QZW]=10.$$
Por tanto los triángulos opuestos deben llevar las parejas $\{3,7\}$ y $\{4,6\}$.

**Paso 3 — Reducción por simetría.** Una rotación de $90^\circ$ (o un reflejo) del cuadrado permuta cíclicamente los cuatro triángulos y conserva el producto de las cuatro distancias. Así que podemos fijar, sin pérdida de generalidad,
$$[QWX]=3,\quad [QXY]=4,\quad [QYZ]=7,\quad [QZW]=6.$$

**Paso 4 — Coordenadas de $Q$.** Despejando, y usando $\frac{2}{s}=\frac{1}{\sqrt5}$:
$$y=\frac{6}{s}=\frac{3}{\sqrt5},\qquad s-y=\frac{14}{s}=\frac{7}{\sqrt5},\qquad s-x=\frac{8}{s}=\frac{4}{\sqrt5},\qquad x=\frac{12}{s}=\frac{6}{\sqrt5}.$$
(Con $s=\frac{10}{\sqrt5}$; en efecto $0<x,y<s$, así que $Q$ es interior.)

**Paso 5 — Las distancias.**
$$QW^2=x^2+y^2=\frac{36+9}{5}=9,\qquad QX^2=(s-x)^2+y^2=\frac{16+9}{5}=5,$$
$$QY^2=(s-x)^2+(s-y)^2=\frac{16+49}{5}=13,\qquad QZ^2=x^2+(s-y)^2=\frac{36+49}{5}=17.$$

Con la otra asignación de parejas ($[QWX]=4$, $[QYZ]=6$, $[QXY]=3$, $[QZW]=7$) se obtienen los mismos valores $\{9,5,13,17\}$ en distinto orden, así que el producto no cambia.

**Paso 6 — El producto.**
$$QW\cdot QX\cdot QY\cdot QZ=\sqrt{9\cdot 5\cdot 13\cdot 17}=3\sqrt{1105}.$$

$$\boxed{3\sqrt{1105}}$$