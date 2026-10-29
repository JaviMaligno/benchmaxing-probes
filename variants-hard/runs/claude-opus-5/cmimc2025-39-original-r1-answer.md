## Planteamiento con coordenadas

Coloco $A=(0,0)$, $C=(112,0)$. De $AB=78$ y $BC=50$:

$$x^2+y^2=6084,\quad (x-112)^2+y^2=2500 \Rightarrow 224x=16128 \Rightarrow x=72,\ y=30$$

Luego $B=(72,30)$ y $[ABC]=\tfrac12\cdot112\cdot30=1680$.

## Vértices de los cuadrados (hacia afuera)

Cada cuadrado se obtiene trasladando el lado por su perpendicular exterior (longitud = lado):

- **$ACMN$**: perpendicular exterior a $AC$ es $(0,-112)$ → $M=(112,-112)$, $N=(0,-112)$.
- **$ABXY$**: perpendicular exterior a $AB$ es $(-30,72)$ → $X=(42,102)$, $Y=(-30,72)$.
- **$BCPQ$**: perpendicular exterior a $BC$ es $(30,40)$ → $P=(142,40)$, $Q=(102,70)$.

(Cada par corresponde a los dos vértices "libres" adyacentes a un mismo vértice del triángulo: $M,P$ junto a $C$; $Q,X$ junto a $B$; $N,Y$ junto a $A$.)

## Puntos medios

$$L_1=\tfrac{M+P}{2}=(127,-36),\qquad L_2=\tfrac{Q+X}{2}=(72,86),\qquad L_3=\tfrac{N+Y}{2}=(-15,-20)$$

## Área

$$\vec{L_1L_2}=(-55,122),\qquad \vec{L_1L_3}=(-142,16)$$

$$[L_1L_2L_3]=\tfrac12\left|(-55)(16)-(122)(-142)\right|=\tfrac12\left|-880+17324\right|=\tfrac{16444}{2}=8222$$

**Verificación con la fórmula general** (se obtiene con números complejos: $L_1=c+\tfrac{i(a-b)}2$, etc.):

$$[L_1L_2L_3]=\frac{a^2+b^2+c^2}{4}+\frac{7}{4}[ABC]=\frac{21128}{4}+\frac{7\cdot1680}{4}=5282+2940=8222$$

\boxed{8222}