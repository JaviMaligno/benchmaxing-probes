## Planteamiento

Tomo lado $ABC = 2$, con
$$A=(-1,0),\quad B=(1,0),\quad C=(0,\sqrt3).$$

Para $E_{AB}$: la suma de distancias es $CA+CB=4$, luego $2a=4$, $c=1$, $b^2=3$, es decir $\frac{x^2}{4}+\frac{y^2}{3}=1$. Análogamente para las otras dos (cada elipse tiene suma constante $4$).

## Intersecciones

Si $P\in E_{AB}\cap E_{BC}$, entonces
$$|PA|+|PB|=4,\qquad |PB|+|PC|=4\;\Longrightarrow\;|PA|=|PC|.$$

Así que $P$ está en la mediatriz de $AC$, que es la recta $x+\sqrt3\,y=1$ (pasa por $B$). Escribiendo $P=(1-\sqrt3 y,\;y)$ se tiene $|PB|=2|y|$ y $|PA|^2=4y^2-4\sqrt3y+4$, de modo que
$$\sqrt{4y^2-4\sqrt3 y+4}=4-2|y|.$$

- $y>0$: $y=\dfrac{12+3\sqrt3}{13}\approx1.3228$ → punto **interior** $(-1.2911,\,1.3228)$,
- $y<0$: $y=-\dfrac{12-3\sqrt3}{13}\approx-0.5234$ → punto **exterior** $\left(\dfrac{4+12\sqrt3}{13},\,-\dfrac{12-3\sqrt3}{13}\right)$.

Por simetría ternaria hay 6 puntos: tres "interiores" a distancia $\approx1.4908$ del centroide (en las direcciones $30°,150°,270°$) y tres "exteriores" a distancia $\approx2.2015$ (en las direcciones $90°,210°,330°$, las de los vértices de $ABC$).

## Elección del triángulo

- Los tres interiores forman un triángulo girado $60°$ respecto de $ABC$, con inradio $\approx0.745 < 1.1547$ (circunradio de $ABC$): los vértices $A,B,C$ sobresalen y los lados **sí** se cortan (hexagrama) → no vale.
- Los tres exteriores dan un triángulo de inradio $\approx1.1007$, mientras la proyección máxima de $ABC$ en esas direcciones es $0.577$: contiene a $ABC$ sin tocarlo → **válido**.
- Las combinaciones mixtas con dos interiores siempre encierran un vértice de $ABC$ y fallan; las que tienen dos exteriores son admisibles y su lado mayor es justamente el que une dos puntos exteriores.

En todos los casos válidos el lado mayor es la distancia entre dos puntos exteriores:
$$2\cdot\frac{4+12\sqrt3}{13}=\frac{8+24\sqrt3}{13}\approx3.8130,$$
(coherente con un equilátero de circunradio $2.2015$: $R\sqrt3=3.8130$).

## Razón

$$\frac{3.8130}{2}=\frac{4+12\sqrt3}{13}\approx1.9065$$

\boxed{\dfrac{4+12\sqrt{3}}{13}}