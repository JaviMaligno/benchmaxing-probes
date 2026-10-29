## Planteamiento

Tomo lado $PQ=QR=RP=1$ y suma de distancias $3/2$ en cada elipse.

**Intersecciones de dos elipses.** Si $W\in\mathcal{E}_{PQ}\cap\mathcal{E}_{PR}$, entonces
$$WP+WQ=\tfrac32=WP+WR\ \Rightarrow\ WQ=WR,$$
así que $W$ está en la mediatriz de $QR$, que en el triángulo equilátero es la recta por $P$ y el punto medio $M$ de $QR$. Cada par de elipses aporta pues exactamente 2 puntos (una recta corta una elipse en ≤2 puntos): en total **6 puntos**.

**Cálculo sobre ese eje.** Con $P=(0,0)$, $M=(\tfrac{\sqrt3}{2},0)$, $Q,R=(\tfrac{\sqrt3}{2},\pm\tfrac12)$ y $W=(t,0)$:
$$|t|+\sqrt{\left(t-\tfrac{\sqrt3}{2}\right)^2+\tfrac14}=\tfrac32 .$$

- $t>0$: $\;t=\dfrac{5(3+\sqrt3)}{24}\approx0.98585$ (queda más allá de $QR$).
- $t<0$: $\;t=-\dfrac{5(3-\sqrt3)}{24}\approx-0.26416$ (queda más allá del vértice $P$).

## Qué triángulo cumple la condición

Con centroide $O$ en el origen y circunradio $R_0=\tfrac1{\sqrt3}$, los 6 puntos son:

- $A_P,A_Q,A_R$ a radio $R_0+\tfrac{5(3-\sqrt3)}{24}\approx0.8415$ en las direcciones de los vértices;
- $B_P,B_Q,B_R$ a radio $\approx0.4085$ en las direcciones de los puntos medios de los lados (apotema $=0.2887$, luego quedan fuera).

Los 6 puntos son exteriores a $\triangle PQR$, así que $\triangle XYZ$ no puede estar dentro; y como cada $A_X$ es **antipodal** a $B_X$ respecto de $O$, todo triángulo que mezcle esos dos tiene un lado que pasa por el centroide (corta a $PQR$). Las demás mezclas ($A_P B_Q B_R$, $B_PB_QB_R$, $A_PA_QB_R$, …) dejan a $O$ fuera o producen la figura tipo hexagrama, cortando lados de $PQR$.

Queda solo $\triangle A_PA_QA_R$: equilátero, concéntrico, misma orientación y **conteniendo** a $PQR$, por lo que sus lados no cortan a los de $PQR$.

## Razón

$$\frac{R_0+\frac{5(3-\sqrt3)}{24}}{R_0}=1+\frac{5(3-\sqrt3)}{24}\sqrt3=1+\frac{5(\sqrt3-1)}{8}=\frac{3+5\sqrt3}{8}\approx1.4575 .$$

\boxed{\dfrac{3+5\sqrt{3}}{8}}