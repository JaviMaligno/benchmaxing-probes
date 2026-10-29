## Planteamiento

Con $x+y+z=75$, reescribo las desigualdades:

**Primera:** $x-yz<y-zx \iff (x-y)+z(x-y)<0 \iff (x-y)(1+z)<0$

**Segunda:** $y-zx<z-xy \iff (y-z)+x(y-z)<0 \iff (y-z)(1+x)<0$

## Casos

- **$x<y$, $z>-1$, $y<z$, $x>-1$:** da $x<y<z$ con $x>-1$ (que implica $z>-1$). Región **acotada**.
- **$x<y$, $z>-1$, $y>z$, $x<-1$:** no acotada.
- **$x>y$, $z<-1$, $y<z$, $x>-1$:** no acotada.
- **$x>y$, $z<-1$, $y>z$, $x<-1$:** entonces $y=75-x-z>77$, incompatible con $x>y$. Vacío.

## Región finita

Proyecto sobre el plano $xy$ con $z=75-x-y$. Las condiciones son:
$$x>-1,\qquad y>x,\qquad y<\tfrac{75-x}{2}$$

Vértices del triángulo proyectado:
- $y=x$ con $y=\frac{75-x}{2}$: $x=25 \Rightarrow (25,25)$, es decir $(25,25,25)$.
- $x=-1$ con $y=x$: $(-1,-1)$, es decir $(-1,-1,77)$.
- $x=-1$ con $y=\frac{76}{2}=38$: $(-1,38)$, es decir $(-1,38,38)$.

Área proyectada: base $39$ sobre la recta $x=-1$, altura $26$:
$$\tfrac12\cdot 39\cdot 26 = 507$$

El plano $x+y+z=75$ tiene factor de escala $\sqrt{3}$ respecto a su proyección sobre $xy$ (pues el vector normal $(1,1,1)/\sqrt3$ tiene componente $z$ igual a $1/\sqrt3$):
$$\text{Área} = 507\sqrt{3}$$

Luego $a=507$, $b=3$ y $a+b=510$.

\boxed{510}