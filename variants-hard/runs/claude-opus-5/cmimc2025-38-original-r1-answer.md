## Planteamiento

Las raíces del primer factor son $A=-1+2i$, $B=-1-2i$ (conjugadas, fijas). Las del segundo, $z$ y $w$, cumplen
$$zw=25,\qquad z+w=2m .$$

Toda circunferencia que pasa por $A$ y $B$ tiene centro en la mediatriz de $AB$, que es el eje real. Si el centro es $c\in\mathbb{R}$, el radio cumple $R^2=(c+1)^2+4$, y la ecuación se reduce a
$$|x|^2-5=2c(\operatorname{Re}x+1).$$

## Condición sobre $z$

Sea $z=ue^{i\theta}$, $t=\cos\theta$; entonces $w=\tfrac{25}{u}e^{-i\theta}$. Imponiendo la ecuación a $z$ y a $w$ con el **mismo** $c$ y eliminando $2c=\dfrac{u^2-5}{ut+1}$:
$$(625-5u^2)(ut+1)=(u^2-5)(25tu+u^2)\ \Longrightarrow\ (25-u^2)\big(u^2+30ut+25\big)=0 .$$

**Caso 1: $u=|z|=5$.** Entonces $w=\overline{z}$, y las cuatro raíces son dos pares conjugados: siempre concíclicas. Aquí $m=\operatorname{Re}z\in[-5,5]$: un **segmento real de longitud 10**.

**Caso 2: $t=-\dfrac{u^2+25}{30u}$.** Con $p=\tfrac12\!\left(u+\tfrac{25}{u}\right)$, $q=\tfrac12\!\left(u-\tfrac{25}{u}\right)$ (así $p^2-q^2=25$) se tiene $t=-p/15$, y $|t|\le1$ obliga a $p\in[5,15]$. Como $m=p\cos\theta+iq\sin\theta$:
$$X=\operatorname{Re}m=-\frac{p^2}{15},\qquad Y^2=(p^2-25)\Big(1-\frac{p^2}{225}\Big).$$
Sustituyendo $p^2=-15X$:
$$Y^2=-(X+\tfrac53)(X+15)\ \Longleftrightarrow\ X^2+Y^2+\frac{50}{3}X+25=0,$$
es decir la circunferencia de centro $-\tfrac{25}{3}$ y radio
$$R=\sqrt{\frac{625}{9}-25}=\frac{20}{3},$$
recorrida por completo ($X$ va de $-15$ a $-\tfrac53$, exactamente el diámetro).

*(Comprobación estructural: en este caso $2c=\frac{u^2-5}{ut+1}=-30$ siempre, o sea $z$ recorre la única circunferencia por $A,B$ invariante bajo $z\mapsto 25/z$: centro $-15$, radio $10\sqrt2$. Ejemplo: $m=-15$ da raíces $-15\pm10\sqrt2$, concíclicas con $-1\pm2i$.)*

## Longitud total

Los dos conjuntos solo comparten el punto $-\tfrac53$, que no aporta longitud:
$$L=10+2\pi\cdot\frac{20}{3}=10+\frac{40\pi}{3}\approx 51{,}89 .$$

$$\boxed{10+\dfrac{40\pi}{3}}$$