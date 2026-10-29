## Planteamiento

Coloco $A$ en el origen, $B=(b,0)$, $C=(0,c)$, con $b^2+c^2=1444$.

Como $AK=BK=14$, $K$ está en la mediatriz de $AB$: $x_K=b/2$. Como $AL=CL=14$, $y_L=c/2$.

Además $AK=AL=KL=14$, así que $\triangle AKL$ es equilátero. Escribo $K=14(\cos\alpha,\sin\alpha)$, $L=14(\cos\beta,\sin\beta)$ con $\beta=\alpha+60^\circ$. Entonces:
$$b=28\cos\alpha,\qquad c=28\sin\beta.$$

## Condición de la hipotenusa

$$784(\cos^2\alpha+\sin^2\beta)=1444\ \Longrightarrow\ \cos^2\alpha+\sin^2\beta=\tfrac{361}{196}.$$

Desarrollando con $\beta=\alpha+60^\circ$:
$$\cos^2\alpha+\sin^2\beta=1+\tfrac34\cos 2\alpha+\tfrac{\sqrt3}{4}\sin 2\alpha=1+\tfrac{\sqrt3}{2}\cos(2\alpha-30^\circ).$$

Luego, con $\theta=2\alpha-30^\circ$:
$$\tfrac{\sqrt3}{2}\cos\theta=\tfrac{165}{196}\ \Longrightarrow\ \cos\theta=\frac{55\sqrt3}{98},\qquad \sin\theta=\frac{23}{98}.$$

## Áreas

Descompongo: $[ABC]=[ABK]+[AKL]+[ALC]+[BKLC]$.

- $[ABK]=\tfrac{b}{2}\sqrt{196-\tfrac{b^2}{4}}=14\cos\alpha\cdot 14\sin\alpha=98\sin 2\alpha$
- $[ALC]=98\sin 2\beta$
- $[AKL]=\tfrac{\sqrt3}{4}\cdot 196=49\sqrt3$
- $[ABC]=\tfrac12(28\cos\alpha)(28\sin\beta)=392\cos\alpha\sin\beta$

Con $2\alpha=\theta+30^\circ$ y $2\beta=\theta+150^\circ$:
$$98(\sin 2\alpha+\sin 2\beta)=98\cdot 2\sin(\theta+90^\circ)\cos 60^\circ=98\cos\theta=55\sqrt3.$$

$$392\cos\alpha\sin\beta=196\left(\cos\theta+\tfrac{\sqrt3}{2}\right)=110\sqrt3+98\sqrt3=208\sqrt3.$$

## Resultado

$$[BKLC]=208\sqrt3-55\sqrt3-49\sqrt3=104\sqrt3.$$

\boxed{104}