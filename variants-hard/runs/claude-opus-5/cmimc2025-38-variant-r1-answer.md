## Planteamiento

Las raíces de $x^2+4x+5=0$ son $A=-2+i$, $B=-2-i$. Como son conjugadas, **toda** circunferencia que pase por ellas tiene centro $c$ en el eje real, con
$$R^2=(c+2)^2+1 .$$

Si $r,s$ son las raíces de $x^2-2mx+25=0$, entonces $rs=25$ y $2m=r+s$. Escribo $r=\rho e^{i\alpha}$, $s=\tfrac{25}{\rho}e^{-i\alpha}$.

La condición de que $r$ (y $s$) esté en esa circunferencia es $|r|^2-5=2c(\operatorname{Re} r+2)$:
$$\rho^2-5=2c(\rho u+2),\qquad \frac{625}{\rho^2}-5=2c\Big(\frac{25}{\rho}u+2\Big),\qquad u=\cos\alpha .$$

Eliminando $c$ y simplificando se obtiene
$$(\rho^2-25)\big[\rho^2+15\rho u+25\big]=0 .$$

## Caso A: $\rho=5$

Entonces $s=\bar r$, con $|r|=5$, y $m=5\cos\alpha$ es real con $|m|\le 5$; el centro existe ($c=\tfrac{10}{m+2}$, y en $m=-2$ los cuatro puntos son colineales). Esto da el **segmento** $[-5,5]$ del eje real: longitud $10$.

## Caso B: $\rho^2+15\rho u+25=0$

Esto es $|r|^2+15\operatorname{Re}r+25=0$, es decir $r$ (y automáticamente $s=25/r$) está en la circunferencia fija de centro $-\tfrac{15}{2}$ y radio $\tfrac{5\sqrt5}{2}$ (y resulta $c=-\tfrac{15}{2}$ siempre).

Con $P=\tfrac12\left(\rho+\tfrac{25}{\rho}\right)$ y $\cos\alpha=-\tfrac{2P}{15}$:
$$\operatorname{Re}m=-\frac{2P^2}{15},\qquad \operatorname{Im}m=\pm\frac{1}{15}\sqrt{(P^2-25)(225-4P^2)},\qquad P\in[5,\tfrac{15}{2}].$$

Poniendo $x=-\tfrac{2P^2}{15}$ (luego $P^2=-\tfrac{15x}{2}$, con $x\in[-\tfrac{15}{2},-\tfrac{10}{3}]$):
$$y^2=\frac{1}{225}\Big(-\tfrac{15x}{2}-25\Big)(225+30x)=-x^2-\frac{65}{6}x-25,$$
o sea
$$x^2+y^2+\frac{65}{6}x+25=0,$$
una circunferencia de centro $-\tfrac{65}{12}$ y radio
$$R=\sqrt{\frac{4225}{144}-25}=\frac{25}{12}.$$
El rango de $x$ coincide exactamente con $-\tfrac{65}{12}\pm\tfrac{25}{12}$, así que se recorre la circunferencia completa: longitud $2\pi\cdot\tfrac{25}{12}=\tfrac{25\pi}{6}$.

## Total

Las dos piezas solo se cortan en el punto $m=-\tfrac{10}{3}$ (longitud nula), de modo que

$$10+\frac{25\pi}{6}$$

$\boxed{10+\dfrac{25\pi}{6}}$