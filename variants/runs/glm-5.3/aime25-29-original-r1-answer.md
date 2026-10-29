## Planteamiento

Coloco $A$ en el origen, con $B=(u,0)$ y $C=(0,v)$, de modo que $u^2+v^2=BC^2=38^2=1444$.

**Clave 1: mediatrices.** Como $AK=BK=14$, el punto $K$ equidista de $A$ y $B$, así que $K$ está sobre la mediatriz de $AB$. Análogamente, $AL=CL=14$ pone a $L$ sobre la mediatriz de $AC$.

Escribo $K=14(\cos\alpha,\operatorname{sen}\alpha)$ y $L=14(\cos\beta,\operatorname{sen}\beta)$ con $\alpha,\beta\in(0°,90°)$ (ambos puntos son interiores). Entonces:
$$K=\Big(\tfrac{u}{2},\,\cdot\Big)\Rightarrow u=28\cos\alpha,\qquad L=\Big(\cdot,\tfrac{v}{2}\Big)\Rightarrow v=28\operatorname{sen}\beta.$$

**Clave 2: condiciones restantes.**
- $KL=14$: como $|K|=|L|=14$, se sigue $\cos(\alpha-\beta)=\tfrac12$, es decir $|\alpha-\beta|=60°$.
- $BC=38$:
$$\cos^2\alpha+\operatorname{sen}^2\beta=\frac{1444}{784}=\frac{361}{196}.$$
Usando $\cos^2\alpha+\operatorname{sen}^2\beta = 1+\tfrac{\cos 2\alpha-\cos 2\beta}{2}=1-\operatorname{sen}(\alpha+\beta)\operatorname{sen}(\alpha-\beta)$:
$$\operatorname{sen}(\alpha+\beta)\operatorname{sen}(\alpha-\beta)=-\frac{165}{196}.$$
Como $\alpha,\beta\in(0°,90°)$, tenemos $\operatorname{sen}(\alpha+\beta)>0$, así que $\operatorname{sen}(\alpha-\beta)<0$; por lo tanto $\beta=\alpha+60°$ y
$$\operatorname{sen}(\alpha+\beta)=\frac{165}{196}\cdot\frac{2}{\sqrt3}=\frac{55\sqrt3}{98}.$$
(Esto ya fija todo lo que hace falta; no hace falta elegir entre las dos soluciones de $\alpha$.)

## Área del cuadrilátero

La cadena $B\!\to\!K\!\to\!L\!\to\!C$ divide al triángulo, así que
$$[BKLC]=[ABC]-[ABK]-[AKL]-[ALC].$$

- $[ABC]=\tfrac12 uv=392\cos\alpha\operatorname{sen}\beta=196\big(\operatorname{sen}(\alpha+\beta)+\operatorname{sen}(\beta-\alpha)\big)=196\Big(\tfrac{55\sqrt3}{98}+\tfrac{\sqrt3}{2}\Big)=208\sqrt3.$
- $[ABK]=\tfrac12\cdot u\cdot(14\operatorname{sen}\alpha)=98\operatorname{sen}2\alpha$ y $[ALC]=\tfrac12\cdot v\cdot(14\cos\beta)=98\operatorname{sen}2\beta$, luego
$$[ABK]+[ALC]=98\big(\operatorname{sen}2\alpha+\operatorname{sen}2\beta\big)=98\cdot 2\operatorname{sen}(\alpha+\beta)\cos(\alpha-\beta)=98\cdot\frac{55\sqrt3}{98}=55\sqrt3.$$
- $[AKL]=\tfrac{\sqrt3}{4}\cdot 14^2=49\sqrt3$ (equilátero).

Por lo tanto:
$$[BKLC]=208\sqrt3-55\sqrt3-49\sqrt3=104\sqrt3.$$

**Verificación numérica.** Con $\operatorname{sen}\alpha=\tfrac17$, $\cos\alpha=\tfrac{4\sqrt3}{7}$, $\operatorname{sen}\beta=\tfrac{13}{14}$, $\cos\beta=\tfrac{3\sqrt3}{14}$ queda $B=(16\sqrt3,0)$, $C=(0,26)$ (con $AB^2+AC^2=768+676=1444$ ✓), $K=(8\sqrt3,2)$, $L=(3\sqrt3,13)$, y se comprueba directamente que $AK=AL=BK=CL=KL=14$, con $K,L$ interiores. El shoelace con esos vértices da exactamente $104\sqrt3\approx 180.13$. ✓

Así, $n=104$.

$\boxed{104}$