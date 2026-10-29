## Resolución

**Coordenadas del triángulo.** Coloco $A=(0,0)$, $C=(112,0)$. Con $AB=78$ y $BC=50$:
$x^2+y^2=6084$, $(x-112)^2+y^2=2500$. Restando: $224x=16128 \Rightarrow x=72$, $y^2=900 \Rightarrow y=30$. Así $B=(72,30)$.

**Cuadrados exteriores.**

- $ACMN$ sobre $AC$, hacia abajo (lado opuesto a $B$): $M=(112,-112)$, $N=(0,-112)$.
- $BCPQ$ sobre $BC$: $\vec{BC}=(40,-30)$, longitud 50; la perpendicular exterior (alejándose de $A$) es $(30,40)$. Entonces $P=C+(30,40)=(142,40)$ y $Q=B+(30,40)=(102,70)$.
- $ABXY$ sobre $AB$: $\vec{AB}=(72,30)$, longitud 78; la perpendicular exterior (alejándose de $C$) es $(-30,72)$. Entonces $X=B+(-30,72)=(42,102)$ y $Y=A+(-30,72)=(-30,72)$.

**Puntos medios.**

$$L_1=\tfrac{M+P}{2}=(127,-36),\quad L_2=\tfrac{Q+X}{2}=(72,86),\quad L_3=\tfrac{N+Y}{2}=(-15,-20)$$

**Área por fórmula del zapato (shoelace).** Con $L_2-L_1=(-55,122)$ y $L_3-L_1=(-142,16)$:

$$\text{Área}=\tfrac12\left|(-55)(16)-(122)(-142)\right|=\tfrac12\left|-880+17324\right|=\tfrac{16444}{2}=8222$$

$$\boxed{8222}$$