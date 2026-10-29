## Planteamiento

Sea $\theta=\angle XYQ=\angle XZQ$, y $YQ=t$, $QZ=2t$.

**Descomposición del área:**
$$[XYQ]=\tfrac12\cdot XY\cdot YQ\sin\theta=\tfrac12\cdot 5t\sin\theta,\qquad [XZQ]=\tfrac12\cdot XZ\cdot ZQ\sin\theta=\tfrac12\cdot 7\cdot 2t\sin\theta$$
Como $[XYQ]+[XZQ]+[YQZ]=[XYZ]=S$:
$$\frac{[YQZ]}{S}=1-\frac{19\,t\sin\theta}{2S}$$

**Ángulos de la base.** Con $XY=5$, $XZ=7$, $YZ=6$:
$$\cos B=\tfrac15,\ \sin B=\tfrac{2\sqrt6}{5},\qquad \cos C=\tfrac57,\ \sin C=\tfrac{2\sqrt6}{7},\qquad S=6\sqrt6$$

**Condición $YQ/QZ=1/2$.** En $\triangle YQZ$ los ángulos en $Y$ y $Z$ son $B-\theta$ y $C-\theta$, así que por ley de senos
$$\frac{YQ}{QZ}=\frac{\sin(C-\theta)}{\sin(B-\theta)}=\frac12\ \Longrightarrow\ \sin(B-\theta)=2\sin(C-\theta)$$
Desarrollando: $\cos\theta(\sin B-2\sin C)=\sin\theta(\cos B-2\cos C)$, es decir
$$\tan\theta=\frac{-6\sqrt6/35}{-43/35}=\frac{6\sqrt6}{43}\ \Longrightarrow\ \sin\theta=\frac{6\sqrt6}{\sqrt{2065}},\ \cos\theta=\frac{43}{\sqrt{2065}}$$

**Cálculo de $t$.** Se obtiene
$$\sin(B-\theta)=\frac{16\sqrt6}{\sqrt{2065}},\quad \sin(C-\theta)=\frac{8\sqrt6}{\sqrt{2065}},\quad \cos(B-\theta)=\frac{23}{\sqrt{2065}},\quad \cos(C-\theta)=\frac{41}{\sqrt{2065}}$$
$$\sin\angle YQZ=\sin\big((B-\theta)+(C-\theta)\big)=\frac{16\sqrt6\cdot41+23\cdot8\sqrt6}{2065}=\frac{840\sqrt6}{2065}$$
Por ley de senos en $\triangle YQZ$:
$$t=\frac{6\sin(C-\theta)}{\sin\angle YQZ}=\frac{6\cdot 8\sqrt6/\sqrt{2065}}{840\sqrt6/2065}=\frac{2\sqrt{2065}}{35}$$

**Conclusión.** Entonces $t\sin\theta=\dfrac{2\sqrt{2065}}{35}\cdot\dfrac{6\sqrt6}{\sqrt{2065}}=\dfrac{12\sqrt6}{35}=\dfrac{2S}{35}$, y por tanto
$$\frac{[YQZ]}{[XYZ]}=1-\frac{19}{35}=\frac{16}{35}$$

(Verificación numérica: $16/35\approx0.4571$, coincide con el cálculo directo de áreas.)

\boxed{\dfrac{16}{35}}