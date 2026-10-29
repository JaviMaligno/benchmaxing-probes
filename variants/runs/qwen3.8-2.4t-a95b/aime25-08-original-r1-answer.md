La primera ecuación $|25+20i-z|=5$ es una circunferencia con centro en $(25,20)$ y radio $5$.

La segunda ecuación $|z-4-k|=|z-3i-k|$ es la mediatriz del segmento que une los puntos $4+k=(k+4,0)$ y $3i+k=(k,3)$.

Sea $z=x+yi$. Igualando distancias al cuadrado:

$$(x-k-4)^2+y^2=(x-k)^2+(y-3)^2$$

Expandiendo y simplificando:

$$(x-k)^2-8(x-k)+16+y^2=(x-k)^2+y^2-6y+9$$

$$-8(x-k)+16=-6y+9$$

$$-8x+8k+16=-6y+9$$

$$8x-6y=8k+7$$

Esta es una recta. Para que el sistema tenga exactamente una solución, la recta debe ser tangente a la circunferencia, es decir, la distancia del centro $(25,20)$ a la recta debe ser igual al radio $5$.

La distancia del punto $(25,20)$ a la recta $8x-6y-(8k+7)=0$ es:

$$d=\frac{|8(25)-6(20)-(8k+7)|}{\sqrt{8^2+6^2}}=\frac{|200-120-8k-7|}{10}=\frac{|73-8k|}{10}$$

Igualando a $5$:

$$\frac{|73-8k|}{10}=5 \implies |73-8k|=50$$

Esto da dos casos:

- $73-8k=50 \implies 8k=23 \implies k=\frac{23}{8}$
- $73-8k=-50 \implies 8k=123 \implies k=\frac{123}{8}$

La suma de los posibles valores de $k$ es:

$$\frac{23}{8}+\frac{123}{8}=\frac{146}{8}=\frac{73}{4}$$

Como $\gcd(73,4)=1$, tenemos $m=73$ y $n=4$. Por lo tanto:

$$m+n=73+4=77$$

$\boxed{77}$