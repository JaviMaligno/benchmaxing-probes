## Planteamiento

Coloco $A=(0,0)$, $B=(b,0)$, $C=(0,c)$, con $b^2+c^2=38^2=1444$.

Como $AK=AL=KL=14$, el triángulo $AKL$ es equilátero. Escribo
$$K=14(\cos\theta,\sin\theta),\qquad L=14(\cos\varphi,\sin\varphi),\qquad \varphi=\theta+60^\circ.$$

**Condiciones $BK=14$ y $CL=14$:** el triángulo $ABK$ es isósceles con $AK=BK=14$, luego la proyección de $K$ sobre $AB$ es el punto medio: $b=28\cos\theta$. Análogamente $c=28\sin\varphi$.

**Uso de la hipotenusa:**
$$784(\cos^2\theta+\sin^2(\theta+60^\circ))=1444\ \Longrightarrow\ \cos^2\theta+\sin^2(\theta+60^\circ)=\tfrac{361}{196}.$$
Con $\cos^2\theta=\frac{1+\cos 2\theta}{2}$, $\sin^2(\theta+60^\circ)=\frac{1-\cos(2\theta+120^\circ)}{2}$:
$$1+\tfrac{1}{2}\big[\cos 2\theta-\cos(2\theta+120^\circ)\big]=1+\tfrac{\sqrt3}{2}\sin(2\theta+60^\circ)=\tfrac{361}{196},$$
$$\boxed{\sin(2\theta+60^\circ)=\tfrac{55\sqrt3}{98}}\ \text{(dato clave)}.$$

## Áreas

**Total:**
$$[ABC]=\tfrac12\,bc=392\cos\theta\sin\varphi=196\big[\sin(2\theta+60^\circ)+\sin 60^\circ\big]=110\sqrt3+98\sqrt3=208\sqrt3.$$

**Triángulos laterales:**
$$[ABK]=\tfrac12\cdot 28\cos\theta\cdot 14\sin\theta=98\sin 2\theta,\qquad [ACL]=98\sin 2\varphi,$$
$$[ABK]+[ACL]=98\big[\sin 2\theta+\sin(2\theta+120^\circ)\big]=98\sin(2\theta+60^\circ)=55\sqrt3.$$

**Triángulo equilátero:** $[AKL]=\frac{\sqrt3}{4}\cdot 14^2=49\sqrt3$.

## Resultado

$$[BKLC]=208\sqrt3-55\sqrt3-49\sqrt3=104\sqrt3.$$

\boxed{104}