## Planteamiento

Coloco $P=(0,0)$, $Q=(c,0)$, $R=(0,b)$, con $b^2+c^2=(4\sqrt{301})^2=4816$.

Como $PX=QX=26$, el punto $X$ está en la mediatriz de $PQ$: $X=\left(\tfrac{c}{2},h\right)$ con $\tfrac{c^2}{4}+h^2=676$.
Como $PY=RY=26$, análogamente $Y=\left(k,\tfrac{b}{2}\right)$ con $k^2+\tfrac{b^2}{4}=676$.

**Condición $XY=26$:**
$$\left(\tfrac{c}{2}-k\right)^2+\left(h-\tfrac{b}{2}\right)^2=676$$
Al expandir y usar $k^2=676-\tfrac{b^2}{4}$, $h^2=676-\tfrac{c^2}{4}$, los términos cuadráticos se cancelan:
$$1352-ck-hb=676\quad\Longrightarrow\quad ck+hb=676.$$

## Parametrización angular

Escribo $b=52\sin B$, $c=52\sin C$ (ángulos del triángulo en $Q$ y $R$), de donde $h=26\cos C$ y $k=26\cos B$. Entonces:
$$ck+hb=1352\big(\sin C\cos B+\cos C\sin B\big)=1352\sin(B+C)=676\ \Rightarrow\ \sin(B+C)=\tfrac12 .$$

De $b^2+c^2=4816$: $\ \sin^2B+\sin^2C=\dfrac{4816}{2704}=\dfrac{301}{169}$, y como $\sin^2B+\sin^2C=1-\cos(B+C)\cos(B-C)$:
$$\cos(B+C)\cos(B-C)=-\tfrac{132}{169}.$$
Esto exige $\cos(B+C)<0$, luego $B+C=150^\circ$, $\cos(B+C)=-\tfrac{\sqrt3}{2}$ y
$$\cos(B-C)=\frac{88\sqrt3}{169}.$$

## Áreas

- $[PQR]=\tfrac{bc}{2}=1352\sin B\sin C=676\big(\cos(B-C)+\tfrac{\sqrt3}{2}\big)=690\sqrt3$
- $[PXY]=\tfrac{\sqrt3}{4}\cdot 26^2=169\sqrt3$ (triángulo equilátero)
- $[PQX]+[PYR]=338(\sin 2C+\sin 2B)=676\sin(B+C)\cos(B-C)=338\cdot\tfrac{88\sqrt3}{169}=176\sqrt3$

Descomponiendo el triángulo: $[QXYR]=[PQR]-[PXY]-[PQX]-[PYR]$:
$$[QXYR]=690\sqrt3-169\sqrt3-176\sqrt3=345\sqrt3 .$$

Verificación numérica: $B\approx 87{,}8^\circ$, $C\approx 62{,}2^\circ$, $b\approx 51{,}96$, $c\approx 46{,}0$, y la fórmula de Gauss (shoelace) sobre $Q(46;0)$, $X(23;12{,}13)$, $Y(1{,}0;25{,}98)$, $R(0;51{,}96)$ da $\approx 597{,}4=345\sqrt3$.

$$\boxed{345}$$