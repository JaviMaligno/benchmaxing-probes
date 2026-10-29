## Planteamiento

Tomemos el triángulo equilátero de lado $1$: $P=(-\tfrac12,0)$, $Q=(\tfrac12,0)$, $R=(0,\tfrac{\sqrt3}{2})$, con centro $G=(0,\tfrac{\sqrt3}{6})$ y circunradio $\tfrac{1}{\sqrt3}$.

**Intersección de dos elipses.** Consideremos $\mathcal{E}_{PQ}$ y $\mathcal{E}_{QR}$, que comparten el foco $Q$. Si $X$ está en ambas:
$$XP+XQ=\tfrac32,\qquad XQ+XR=\tfrac32 \;\Rightarrow\; XP=XR,$$
así que $X$ está sobre la mediatriz de $PR$, que es la recta que pasa por $Q$ y por $G$.

Parametrizo esa recta con dirección unitaria desde $Q$ hacia $G$: $X=(\tfrac12-\tfrac{\sqrt3}{2}t,\ \tfrac{t}{2})$, de modo que $XQ=|t|$ y $XP^2 = 1-\sqrt3\,t+t^2$. La condición $|t|+\sqrt{1-\sqrt3\,t+t^2}=\tfrac32$ da:

- **$t>0$ (hacia el centro):** $1-\sqrt3\,t = \tfrac94-3t \Rightarrow t=\dfrac{5(3+\sqrt3)}{24}\approx 0.986$.
- **$t<0$ (alejándose del centro):** con $t=-s$, $s=\dfrac{5(3-\sqrt3)}{24}\approx 0.264$.

Cada par de elipses se corta en dos puntos sobre el eje vértice–centro correspondiente.

**¿Cuál triángulo sirve?** Por simetría hay dos triángulos equiláteros candidatos:

- Los tres puntos "lejanos" ($t>0$): cada uno queda a distancia $\approx 0.408$ del centro en la dirección del punto medio de un lado de $PQR$, es decir, **fuera** del triángulo (su inradio es $\tfrac{\sqrt3}{6}\approx 0.289$), formando una configuración tipo hexagrama cuyos lados **sí cruzan** los de $PQR$. Se descarta.
- Los tres puntos "cercanos" ($t<0$): cada uno está sobre la prolongación de $GQ$ (y análogos) más allá del vértice, así que forman un triángulo **homotético a $PQR$ desde $G$** que lo contiene estrictamente: sus lados no cortan los de $PQR$. ✓

## Cálculo de la razón

El vértice correspondiente a $Q$ está a distancia $GQ+s=\tfrac{1}{\sqrt3}+s$ del centro, de modo que la razón de homotecia (igual a la razón de lados, todos iguales) es:
$$\frac{\tfrac{1}{\sqrt3}+s}{\tfrac{1}{\sqrt3}} = 1+\sqrt3\,s = 1+\sqrt3\cdot\frac{5(3-\sqrt3)}{24} = 1+\frac{5(\sqrt3-1)}{8} = \frac{3+5\sqrt3}{8}\approx 1.4575.$$

$$\boxed{\dfrac{3+5\sqrt{3}}{8}}$$