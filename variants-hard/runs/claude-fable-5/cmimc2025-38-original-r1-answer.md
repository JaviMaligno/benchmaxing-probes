## Planteamiento

Las raíces de $x^2+2x+5=0$ son $a=-1+2i$ y $b=-1-2i$ (fijas). Las raíces del segundo factor, $r$ y $r'$, cumplen $rr'=25$ (es decir, $r'=25/r$) y $m=\tfrac12\left(r+\tfrac{25}{r}\right)$.

## Condición de conciclicidad

Cuatro puntos son concíclicos (o colineales) si y solo si su razón doble es real:

$$\frac{(a-r)(b-r')}{(a-r')(b-r)}\in\mathbb{R}.$$

Con $r'=25/r$, $ab=5$, $a+b=-2$, el numerador y denominador se reducen a $N=30r-25a-br^2$ y $D=30r-25b-ar^2$, y la condición $\operatorname{Im}(N\bar D)=0$, escribiendo $s=r+\bar r$, $p=|r|^2$, se factoriza limpiamente:

$$(p-25)\,(p+15s+25)=0.$$

Es decir, $r$ debe estar en una de dos circunferencias:

- $|r|=5$, o
- $C_0:\ (x+15)^2+y^2=200$ (centro $-15$, radio $10\sqrt2$), que es ortogonal a $|z|=5$ e invariante bajo $r\mapsto 25/r$.

## Imagen bajo $m=\tfrac12(r+25/r)$

**Caso $|r|=5$:** con $r=5e^{i\theta}$ se obtiene $m=5\cos\theta$, es decir, el **segmento $[-5,5]$** del eje real, de longitud $10$.

**Caso $r\in C_0$:** restando las ecuaciones de circunferencia para $r$ y $r'=25/r$ se llega a la condición equivalente

$$\frac{(m+15)^2}{m^2-25}\in\mathbb{R}_{\le 0}.$$

Poniendo $\frac{(m+15)^2}{m^2-25}=t$, resulta $(1-t)m^2+30m+225+25t=0$ con discriminante $100\,t(t+8)$. Para $-8\le t\le 0$:

$$m=\frac{-15\pm 5i\sqrt{-t(t+8)}}{1-t},$$

que va de $m=-15$ (en $t=0$) a $m=-\tfrac53$ (en $t=-8$), más su reflejo conjugado. Verificando puntos (por ejemplo $t=-4$ da $m=-3+4i$, y $t=-1$ da $m=\tfrac{-15+5\sqrt7\,i}{2}$), todos equidistan de $-\tfrac{25}{3}$:

$$\left|m+\tfrac{25}{3}\right|=\tfrac{20}{3}.$$

Es decir, la imagen es la **circunferencia completa** de centro $-\tfrac{25}{3}$ y radio $\tfrac{20}{3}$ (pasa por $-15$ y $-\tfrac53$), que solo toca al segmento en el punto $-\tfrac53$.

## Perímetro total

$$\underbrace{10}_{\text{segmento }[-5,5]}+\underbrace{2\pi\cdot\tfrac{20}{3}}_{\text{circunferencia}}=10+\frac{40\pi}{3}.$$

$$\boxed{10+\dfrac{40\pi}{3}}$$