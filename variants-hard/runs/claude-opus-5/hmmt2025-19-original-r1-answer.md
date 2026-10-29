## Planteamiento

Para dos puntos $P,Q$ uniformes e independientes en una región convexa $K$ de área $A$, conviene cambiar a coordenadas de recta: dirección $\theta$ y desplazamiento normal $t$, más las posiciones $s_1,s_2$ sobre la recta. El jacobiano da

$$dP\,dQ = |s_1-s_2|\,ds_1\,ds_2\,d\theta\,dt,$$

luego la densidad de la recta $PQ$ en $(\theta,t)$ es $\dfrac{L(\theta,t)^3}{3A^2}$, con $L$ la longitud de la cuerda.

## ¿Cuándo se cortan lados opuestos?

Hexágono de lado 1 con vértices $V_k=(\cos 60k^\circ,\sin 60k^\circ)$, $A=\tfrac{3\sqrt3}{2}$. Por simetría basta $\theta\in(0^\circ,30^\circ)$ y multiplicar por 6.

Con normal $n=(-\sin\theta,\cos\theta)$, las alturas $h_k=n\cdot V_k$ se ordenan como
$$h_2>h_1>h_3>h_0>h_4>h_5,$$
con $h_3=\sin\theta$, $h_0=-\sin\theta$. Barriendo $t$ de $h_2$ a $h_5$, los pares de lados cortados son: $(V_1V_2,V_2V_3)$, $(V_0V_1,V_2V_3)$, $(V_0V_1,V_3V_4)$, $(V_5V_0,V_3V_4)$, $(V_5V_0,V_4V_5)$. El único par opuesto es el tercero, es decir

$$t\in(-\sin\theta,\ \sin\theta).$$

(Comprobación: $\theta=30^\circ$ da cuerdas verticales con $|t|<1/2$, correcto.)

## Integración

En esa fase la cuerda cruza dos rectas paralelas a distancia $\sqrt3$ con normal a $30^\circ$, así que $L=\dfrac{\sqrt3}{\cos(30^\circ-\theta)}$, independiente de $t$. Entonces

$$I=\int_0^{\pi/6} 2\sin\theta\cdot\frac{3\sqrt3}{\cos^3(\pi/6-\theta)}\,d\theta = 6\sqrt3\,J,\qquad J=\int_0^{\pi/6}\frac{\sin\theta\,d\theta}{\cos^3(\pi/6-\theta)}.$$

Con $\phi=\pi/6-\theta$ y $\sin(\pi/6-\phi)=\tfrac12\cos\phi-\tfrac{\sqrt3}{2}\sin\phi$:

$$J=\frac12\big[\tan\phi\big]_0^{\pi/6}-\frac{\sqrt3}{2}\left[\frac{1}{2\cos^2\phi}\right]_0^{\pi/6}=\frac{1}{2\sqrt3}-\frac{\sqrt3}{12}=\frac{\sqrt3}{12}.$$

Con $3A^2=\tfrac{81}{4}$:

$$\Pr=\frac{6\,I}{3A^2}=\frac{6\cdot 6\sqrt3\cdot\frac{\sqrt3}{12}}{81/4}=\frac{9\cdot 4}{81}=\frac{4}{9}.$$

$$\boxed{\dfrac{4}{9}}$$