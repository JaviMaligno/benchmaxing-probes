## Planteamiento

Coloco $X$ en el origen con las tres cuerdas a lo largo de los ejes coordenados, y sea $O = (a, b, c)$, con $a^2 + b^2 + c^2 = OX^2 = 2$.

**Intersección de cada eje con la esfera.** Un punto $(t, 0, 0)$ está en la esfera si $(t-a)^2 + b^2 + c^2 = r^2$, es decir:
$$t^2 - 2at + (2 - r^2) = 0.$$
Las raíces son las coordenadas de $P$ y $Q$, con producto $pq = 2 - r^2$. Lo mismo ocurre en los ejes $y$ y $z$: en los tres casos el producto de las raíces es $2 - r^2$.

Sea $k = r^2 - 2 > 0$ (positivo porque $X$ es interior). Entonces:

- Eje $x$: una raíz tiene módulo $1$ (pues $PX = 1$), así que las raíces son $\pm 1$ y $\mp k$, y $a = \pm\frac{1-k}{2}$, luego $a^2 = \frac{(1-k)^2}{4}$.
- Eje $y$: raíces $\pm 2$ y $\mp k/2$, luego $b^2 = \frac{(2 - k/2)^2}{4}$.
- Eje $z$: raíces $\pm 3$ y $\mp k/3$, luego $c^2 = \frac{(3 - k/3)^2}{4}$.

**Condición $OX^2 = 2$:**
$$(1-k)^2 + \left(2 - \tfrac{k}{2}\right)^2 + \left(3 - \tfrac{k}{3}\right)^2 = 8.$$

Expandiendo:
$$14 - 6k + k^2\left(1 + \tfrac14 + \tfrac19\right) = 8 \;\Longrightarrow\; \tfrac{49}{36}k^2 - 6k + 6 = 0 \;\Longrightarrow\; 49k^2 - 216k + 216 = 0.$$

El discriminante es $216^2 - 4\cdot 49 \cdot 216 = 216 \cdot 20 = 4320 > 0$, y como la suma ($216/49$) y el producto ($216/49$) de las raíces son positivos, ambas raíces cumplen $k > 0$, así que las dos son válidas.

**Suma de los valores de $r^2$:** como $r^2 = k + 2$,
$$\sum r^2 = \frac{216}{49} + 4 = \frac{216 + 196}{49} = \frac{412}{49}.$$

$$\boxed{\dfrac{412}{49}}$$