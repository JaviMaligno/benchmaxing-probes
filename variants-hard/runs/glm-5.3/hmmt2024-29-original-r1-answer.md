## Planteamiento

Coloco $A=(0,0)$ y $C=(7,0)$. Sea $\alpha = \angle BAC$, y escribo $c=\cos\alpha$, $s=\sin\alpha$, con $s>0$. Como $AB=6$:
$$B=(6c,\,6s).$$

Como $BP\perp AC$, el segmento $BP$ es vertical, y como $BP=4$ (con $P$ debajo de $B$):
$$P=(6c,\,6s-4).$$

## Condición del ángulo de 60°

Sea $\beta = \angle ACX$. Como $X\in\overline{AB}$, la semirrecta $XB$ apunta en dirección $\alpha$, y la semirrecta $XC$ apunta en dirección $-\beta$. Entonces
$$\angle BXC = \alpha+\beta = 60^\circ \implies \beta = 60^\circ-\alpha,$$
de donde
$$\cos\beta = \frac{c+\sqrt3\,s}{2},\qquad \sin\beta=\frac{\sqrt3\,c-s}{2}.$$

## Ecuaciones

Sea $r=CP$. Como $P\in\overline{CX}$, recorriendo desde $C$ en dirección a $X$:
$$P=(7-r\cos\beta,\; r\sin\beta).$$

Igualando con $(6c,\,6s-4)$ y sustituyendo $\cos\beta,\sin\beta$ (multiplicando por 2):

$$(r+12)c+\sqrt3\,r\,s=14 \qquad (i)$$
$$\sqrt3\,r\,c-(r+12)s=-8 \qquad (ii)$$

## Resolver el sistema

Es un sistema lineal en $(c,s)$. Con determinante $D=(r+12)^2+3r^2>0$, la regla de Cramer da:
$$c=\frac{14(r+12)-8\sqrt3\,r}{D},\qquad s=\frac{8(r+12)+14\sqrt3\,r}{D}.$$

Imponiendo $c^2+s^2=1$:
$$\big[14(r+12)-8\sqrt3\,r\big]^2+\big[8(r+12)+14\sqrt3\,r\big]^2=D^2.$$

Expandiendo, las cruzadas con $\sqrt3$ se cancelan y queda
$$260(r+12)^2+780r^2=D^2 \implies 260D=D^2 \implies D=260.$$

Es decir:
$$(r+12)^2+3r^2=260 \implies 4r^2+24r-116=0 \implies r^2+6r-29=0,$$
$$r=-3\pm\sqrt{38}.$$

Como $r>0$, tomamos $r=\sqrt{38}-3\approx 3.164$.

**Verificación de consistencia:** con este $r$ se obtiene $\alpha\approx 49.6^\circ$, $\beta\approx 10.4^\circ$, $AX=14\sin\beta/\sqrt3\approx 1.46\in(0,6)$ y $CP\approx 3.16 < CX\approx 6.16$; es decir, $X$ está en el lado $AB$ y $P$ en el segmento $CX$, con $BP=4$ exacto. ✓

$$\boxed{\sqrt{38}-3}$$