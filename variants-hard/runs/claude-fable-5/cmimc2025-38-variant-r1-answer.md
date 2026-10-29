## Planteamiento

Las raíces del primer factor son fijas: $x^2+4x+5=0$ da $A=-2+i$ y $\bar A=-2-i$. Las raíces $p,q$ del segundo factor cumplen $pq=25$ y $p+q=2m$, es decir $q=25/p$.

Como $A$ y $\bar A$ son reflejos respecto al eje real, **toda circunferencia que pasa por ambos tiene centro real** $c$, con radio $r^2=(c+2)^2+1$.

## Condición sobre $p$

Exigir que $p$ y $q=25/p$ estén en esa circunferencia da, con $s=p+\bar p$, $t=|p|^2$:

- Eq1: $t - cs + c^2 = r^2$
- Eq2: $625 - 25cs + c^2 t = r^2 t$

Combinándolas: $(25-t)(25+t) = cs\,(25-t)$, lo que da dos casos.

**Caso 1: $t=25$ (es decir $|p|=5$).** Entonces $q=25/p=\bar p$, con lo cual $m=\operatorname{Re}p$ es real y $m\in[-5,5]$. Para cada $m$ real en ese intervalo existe centro $c=10/(2+m)$ (en $m=-2$ los cuatro puntos son colineales, un solo punto que no afecta la longitud). Esto aporta el **segmento $[-5,5]$, de longitud $10$**.

**Caso 2: $cs = 25+t$.** Sustituyendo en Eq1 queda $r^2=c^2-25$, y junto con $r^2=(c+2)^2+1$ se fuerza $c=-\tfrac{15}{2}$, $r=\tfrac{5\sqrt5}{2}$. Entonces $p$ (y automáticamente $q$) están sobre la circunferencia fija $C$: centro $-\tfrac{15}{2}$, radio $\tfrac{5\sqrt5}{2}$ (que, en efecto, pasa por $-2\pm i$).

## Imagen en el plano de $m$

Escribiendo $p=-\tfrac{15}{2}+\tfrac{5\sqrt5}{2}e^{i\alpha}$, $q=-\tfrac{15}{2}+\tfrac{5\sqrt5}{2}e^{i\beta}$, la condición $pq=25$ se reduce (con $\varphi=\tfrac{\alpha+\beta}{2}$, $\delta=\tfrac{\alpha-\beta}{2}$) a
$$\cos\delta = \frac{\sqrt5}{3}\cos\varphi,$$
siempre resoluble pues $\tfrac{\sqrt5}{3}<1$. Entonces
$$m=\frac{p+q}{2}=-\frac{15}{2}+\frac{5\sqrt5}{2}e^{i\varphi}\cos\delta
=-\frac{15}{2}+\frac{25}{6}\,e^{i\varphi}\cos\varphi
=-\frac{65}{12}+\frac{25}{12}e^{2i\varphi}.$$

Es decir, una **circunferencia de centro $-\tfrac{65}{12}$ y radio $\tfrac{25}{12}$**, recorrida completa; su longitud es $2\pi\cdot\tfrac{25}{12}=\tfrac{25\pi}{6}$. (El caso de raíces $p,q$ reales con $|m|\ge 5$ fuerza $m=-\tfrac{15}{2}$, que ya es el punto izquierdo de esta circunferencia; la intersección con el segmento es solo el punto $-\tfrac{10}{3}$, sin solapamiento de longitud.)

## Longitud total

$$10+\frac{25\pi}{6}$$

$$\boxed{10+\dfrac{25\pi}{6}}$$