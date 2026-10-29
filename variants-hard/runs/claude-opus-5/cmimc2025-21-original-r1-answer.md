## Planteamiento

Un tetraedro regular tiene exactamente dos desarrollos (nets): el triángulo grande y la **tira de cuatro triángulos equiláteros**, que forma un paralelogramo de lados $s$ y $2s$ con ángulo de $60°$.

Con $s=1$, los vectores de los lados son
$$e_1=(2,0),\qquad e_2=(\tfrac12,\tfrac{\sqrt3}{2}).$$

## Cuadrado mínimo que lo contiene

Para un paralelogramo, la anchura en la dirección $u=(\cos\theta,\sin\theta)$ es
$$w(\theta)=|e_1\cdot u|+|e_2\cdot u|=2|\cos\theta|+|\cos(\theta-60°)|.$$

El lado del cuadrado mínimo es $\min_\theta \max\big(w(\theta),w(\theta+90°)\big)$. Sin girar ($\theta=0$) se obtiene $2.5$, pero el óptimo aparece cuando ambas anchuras coinciden. En la rama $-30°<\theta<0$:

$$2.5\cos\theta+\tfrac{\sqrt3}{2}\sin\theta=\tfrac{\sqrt3}{2}\cos\theta-2.5\sin\theta
\;\Longrightarrow\;\tan\theta=-\frac{5-\sqrt3}{5+\sqrt3}\approx-0.4854,$$

es decir $\theta\approx-25.89°$ (comprobando los demás ángulos, este es el mínimo global).

Con $a=5+\sqrt3$, $b=5-\sqrt3$: $\cos\theta=a/\sqrt{a^2+b^2}=a/\sqrt{56}$ y $5a-\sqrt3\,b=28$, luego

$$w=\frac{14\cos\theta}{a}=\frac{14}{\sqrt{56}}=\frac{7}{\sqrt{14}}.$$

## Lado y área

El cuadrado tiene lado $7$, así que
$$s=\frac{7}{7/\sqrt{14}}=\sqrt{14}\quad\Rightarrow\quad s^2=14.$$

La superficie del tetraedro es $4\cdot\frac{\sqrt3}{4}s^2=\sqrt3\,s^2$:

$$\sqrt3\cdot 14=14\sqrt3\approx 24.25.$$

\boxed{14\sqrt{3}}