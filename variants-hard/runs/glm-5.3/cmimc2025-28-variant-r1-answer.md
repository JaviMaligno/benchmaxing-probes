## Planteamiento

Como $PQ$ es diámetro, por el ángulo inscrito en semicírcula (Tales):
$$\angle PSQ = \angle PRQ = 90^\circ.$$

En los triángulos rectángulos:
- $SQ = \sqrt{20^2 - 8^2} = 4\sqrt{21}$,  $PR = \sqrt{20^2-12^2} = 16$.

Pongo coordenadas: $P=(-10,0)$, $Q=(10,0)$, $O=(0,0)$, con $R,S$ sobre el eje $x$. Escribo $u=\sqrt{21}$.

De $QR=12$ y $PR=16$: $R=\left(\tfrac{14}{5},\tfrac{48}{5}\right)$.
De $PS=8$ y $QS=4u$: $S=\left(-\tfrac{34}{5},\tfrac{8u}{5}\right)$.

## Punto $T$ y lados del triángulo $TRS$

Rectas: $PS:\ y=\tfrac{u}{2}(x+10)$ y $QR:\ y=-\tfrac43(x-10)$. Intersecando:
$$T=\left(\frac{96u-506}{25},\ \frac{16(63-8u)}{25}\right)\approx(-2.64,\ 16.86),$$
que está más allá de $R$ y de $S$ en ambas rectas.

**Lados** (usando que $T$ está sobre las rectas $QR$ y $PS$):

Sobre $QR$ (vector unitario $(3,-4)/5$): $TQ=\tfrac54 y_T=\tfrac{4(63-8u)}{5}$, luego
$$c=TR=TQ-QR=\frac{32(6-u)}{5}.$$

Sobre $PS$ (vector unitario $(2,u)/5$): $TP=\tfrac5u y_T=\tfrac{16(3u-8)}{5}$, luego
$$b=TS=TP-PS=\frac{24(2u-7)}{5}.$$

Por Ptolemeo en $PQRS$: $PQ\cdot RS+QR\cdot PS=PR\cdot QS$, de donde
$$a=RS=\frac{16u-24}{5}=\frac{8(2u-3)}{5}.$$

## Excentro opuesto a $T$

El centro $J$ del excírculo opuesto a $T$ es
$$J=\frac{-aT+bR+cS}{-a+b+c}.$$

**Denominador:** $-a+b+c=\frac{-(16u-24)+(48u-168)+(192-32u)}{5}=\frac{48}{5}$ (los términos en $u$ se cancelan).

**Coordenada $y$ del numerador** (con $y_T=\tfrac{16(63-8u)}{25}$, $y_R=\tfrac{48}{5}$, $y_S=\tfrac{8u}{5}$; todo sobre $125$):
$$-a\,y_T = \frac{16(4200-1200u)}{125},\quad b\,y_R=\frac{11520u-40320}{125},\quad c\,y_S=\frac{7680u-26880}{125}.$$
Sumando: $\dfrac{(67200-40320-26880)+(-19200+11520+7680)u}{125}=0$.

**¡$y_J=0$!** El excentro está sobre la recta $PQ$.

**Coordenada $x$ del numerador** (sobre $125$):
$$-a\,x_T=\frac{10400u-44400}{125},\quad b\,x_R=\frac{3360u-11760}{125},\quad c\,x_S=\frac{5440u-32640}{125},$$
que suman $\dfrac{19200u-88800}{125}$. Por tanto
$$x_J=\frac{19200u-88800}{125}\cdot\frac{5}{48}=16u-74.$$

## Verificación conceptual

Esto cuadra con la geometría: $J$ está sobre la bisectriz interna del ángulo entre las rectas $PS$ y $QR$; un punto $X$ sobre $PQ$ equidista de esas dos rectas cuando $XP\cdot\sin\angle QPS = XQ\cdot\sin\angle PQR$, es decir $u\cdot XP=4\cdot XQ$, cuya solución es exactamente $x=16u-74$.

Como $O=(0,0)$ y $J=(16\sqrt{21}-74,\ 0)$:
$$OJ = 74-16\sqrt{21}\approx 0.6788.$$

$$\boxed{74-16\sqrt{21}}$$