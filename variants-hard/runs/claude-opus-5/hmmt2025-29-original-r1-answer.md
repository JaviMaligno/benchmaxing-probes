## Planteamiento

Coloco $A=(0,0)$, $B=(L,0)$, $C=(L,24)$, $D=(0,24)$ con $L=AB$, y $X=(x,y)$.

**Condición $\angle AXB=90^\circ$:** $x(x-L)+y^2=0$, es decir $x^2+y^2=Lx$. De ahí:
$$XA^2=Lx,\qquad XB^2=L(L-x)$$
$$XD^2=Lx-48y+576,\qquad XC^2=L(L-x)-48y+576$$

**Ángulos en $X$:** en $\triangle AXD$, $AD=24=2\cdot13\sin\angle AXD\Rightarrow \sin=\tfrac{12}{13}$, y por ser acutángulo $\cos=\tfrac{5}{13}$. En $\triangle BXC$, $24=2\cdot15\sin\angle BXC\Rightarrow\sin=\tfrac45$, $\cos=\tfrac35$.

**Áreas:** la distancia de $X$ a $AD$ es $x$, luego $[AXD]=12x=\tfrac12 XA\cdot XD\cdot\tfrac{12}{13}\Rightarrow XA\cdot XD=26x$. Análogamente $XB\cdot XC=30(L-x)$.

## Dos ecuaciones

Ley de cosenos en $\triangle AXD$:
$$576=Lx+(Lx-48y+576)-2(26x)\tfrac{5}{13}\ \Rightarrow\ 48y=2x(L-10)$$

Ley de cosenos en $\triangle BXC$:
$$576=2L(L-x)-48y+576-2(30)(L-x)\tfrac35\ \Rightarrow\ 48y=(L-x)(L-18)$$

Igualando: $x(L-10)=(L-x)(L-18)\Rightarrow x=\dfrac{L(L-18)}{2(L-14)}$.

Usando además $XA^2\cdot XD^2=676x^2$ con $Lx-48y+576=576+20x-Lx$:
$$L(576+20x-Lx)=676x\ \Rightarrow\ x=\frac{576L}{L^2-20L+676}$$

## Resolución

$$(L-18)(L^2-20L+676)=1152(L-14)\ \Longrightarrow\ L^3-38L^2-116L+3960=0$$
$$(L-10)(L^2-28L-396)=0$$

La raíz $L=10$ da $y=0$ (degenerada), así que $L^2-28L-396=0$, esto es $L=14+4\sqrt{37}\approx38.33$.

Verificación: $x\approx16.0$, $y\approx18.9$, con $0<x<L$ y $0<y<24$, así que $X$ está interior y ambos triángulos son acutángulos.

$$\boxed{14+4\sqrt{37}}$$