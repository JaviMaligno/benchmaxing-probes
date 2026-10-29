## Planteamiento

En el plano $x+y+z=75$ reescribimos las desigualdades:

**Primera:** $x-yz<y-zx \iff (x-y)+z(x-y)<0 \iff (x-y)(1+z)<0$

**Segunda:** $y-zx<z-xy \iff (y-z)+x(y-z)<0 \iff (y-z)(1+x)<0$

## Análisis de casos

Hay cuatro combinaciones de signos:

1. $x<y$, $z>-1$, $y<z$, $x>-1$ → $x<y<z$ con $x>-1$ (las otras condiciones son automáticas).
2. $x>y>z$ con $x<-1$ y $z<-1$ → imposible: los tres serían $<-1$ y no sumarían $75$.
3. $x<y$, $y>z>-1$, $x<-1$ → región no acotada.
4. $y<z<-1$, $x>-1$ → región no acotada.

Por tanto la región finita es la del caso 1.

## Cálculo del área

Usando $z=75-x-y$ como parametrización, las condiciones $x>-1$, $x<y$, $y<z$ dan:

$$-1<x,\qquad x<y,\qquad y<\frac{75-x}{2}$$

Los vértices en el plano $(x,y)$ son $(-1,-1)$, $(-1,38)$ y $(25,25)$ (donde $x<y<\frac{75-x}{2}$ se degenera).

Área proyectada: base vertical de longitud $38-(-1)=39$ y altura horizontal $25-(-1)=26$:

$$A_{\text{proy}}=\tfrac12\cdot 39\cdot 26=507$$

El factor de distorsión al pasar del plano $xy$ al plano $x+y+z=75$ es $\sqrt{1+1+1}=\sqrt 3$, así que

$$A=507\sqrt{3}$$

Con $a=507$, $b=3$ (libre de cuadrados): $a+b=510$.

\boxed{510}