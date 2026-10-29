## Resolución

**Simplificación de las desigualdades.** Trabajando en el plano $x+y+z=87$:

- $x-yz<y-zx \iff (x-y)+z(x-y)<0 \iff (x-y)(1+z)<0$
- $y-zx<z-xy \iff (y-z)+x(y-z)<0 \iff (y-z)(1+x)<0$

Cada desigualdad divide el plano en regiones según los signos de los factores, lo que produce tres regiones convexas disjuntas. La región **acotada** corresponde al caso:

$$x-y<0,\quad 1+z>0,\quad y-z<0,\quad 1+x>0,$$

es decir, $-1<x<y<z$ (la condición $z>-1$ es automática pues $z>y>x>-1$).

**Descripción de la región.** Con $z=87-x-y$, las condiciones son:

- $x>-1$
- $y>x$
- $y<z \iff y<87-x-y \iff y<\dfrac{87-x}{2}$

Para que exista $y$, se necesita $x<\dfrac{87-x}{2}\iff x<29$. En el plano $(x,y)$ la región es el triángulo con vértices:

$$(-1,-1),\qquad \left(-1,\tfrac{88}{2}\right)=(-1,44),\qquad (29,29).$$

**Área de la proyección.** Base vertical en $x=-1$: longitud $44-(-1)=45$. Altura horizontal hasta $x=29$: $30$. Entonces:

$$\text{Área}_{xy}=\frac{1}{2}\cdot 45\cdot 30=675.$$

**Corrección por la inclinación del plano.** El plano $x+y+z=87$ tiene normal $(1,1,1)$; al proyectar sobre el plano $xy$ el área se reduce por el factor $\cos\theta = \frac{1}{\sqrt{3}}$. Por tanto, el área real es:

$$675\cdot\sqrt{3}=675\sqrt{3}.$$

Así $a=675$, $b=3$ (libre de cuadrados), y $a+b=678$.

$$\boxed{678}$$