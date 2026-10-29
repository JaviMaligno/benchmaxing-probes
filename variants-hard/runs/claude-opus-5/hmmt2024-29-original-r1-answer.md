## Planteamiento

Coloco $A$ en el origen con $AC$ sobre el eje $x$: $C=(7,0)$, $B=(6\cos\alpha,\,6\sin\alpha)$ con $\alpha=\angle A$.

Como $BP\perp AC$, el punto $P$ tiene la misma abscisa que $B$ y está $4$ por debajo:
$$P=(6\cos\alpha,\ 6\sin\alpha-4).$$

En el triángulo $AXC$ se tiene $\angle AXC=180^\circ-60^\circ=120^\circ$ y $\angle A=\alpha$, luego $\angle XCA=60^\circ-\alpha$. Por tanto, con $s=CP$:
$$P=\big(7-s\cos(60^\circ-\alpha),\ s\sin(60^\circ-\alpha)\big).$$

## Ecuaciones

Igualando coordenadas, con $c=\cos\alpha$, $t=\sin\alpha$:
$$s\left(\tfrac{\sqrt3}{2}c-\tfrac12 t\right)=6t-4,\qquad s\left(\tfrac12 c+\tfrac{\sqrt3}{2}t\right)=7-6c.$$

Combinando ambas (una vez multiplicadas por $\sqrt3$ y sumadas/restadas), con $k=2s+6$:
$$ck-6\sqrt3\,t=7-4\sqrt3,\qquad tk+6\sqrt3\,c=7\sqrt3+4.$$

Resolviendo el sistema lineal en $c,t$ (determinante $k^2+108$):
$$c=\frac{(7-4\sqrt3)k+126+24\sqrt3}{k^2+108},\qquad t=\frac{(4+7\sqrt3)k+72-42\sqrt3}{k^2+108}.$$

## Imponiendo $c^2+t^2=1$

Los numeradores dan: coeficiente de $k^2$ igual a $260$, coeficiente de $k$ igual a $0$ (se cancela), término independiente $28080$. Así:
$$260k^2+28080=(k^2+108)^2\ \Longrightarrow\ (k^2)^2-44k^2-16416=0,$$
$$k^2=\frac{44+260}{2}=152\ \Longrightarrow\ k=2\sqrt{38}.$$

De $k=2s+6$ resulta $s=\sqrt{38}-3\approx3.164$.

**Verificación:** $\alpha\approx49.6^\circ$, $6\sin\alpha\approx4.57>4$ (así $P$ queda sobre $AC$), $\angle XCA\approx10.4^\circ>0$, y $P$ cae entre $X$ y $C$; $X$ está dentro de $\overline{AB}$ con $AX\approx1.46$.

$$\boxed{\sqrt{38}-3}$$