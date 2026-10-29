## Planteamiento

Uso coordenadas. Coloco $B=(0,0)$, $C=(26,0)$. Para $A=(x,y)$ con $AB=80$, $AC=102$:

$$x^2+y^2=6400,\qquad (x-26)^2+y^2=10404$$

Restando: $52x-676=-4004 \Rightarrow x=-64$, y entonces $y^2=6400-4096=2304 \Rightarrow y=48$. Así $A=(-64,48)$, con área de $ABC$ igual a $\tfrac12\cdot26\cdot48=624$ (coincide con Herón).

## Construcción de los cuadrados (hacia afuera)

**Cuadrado $ABXY$** (lado opuesto a $C$): $X = B+(-48,-64)=(-48,-64)$, $Y = A+(-48,-64)=(-112,-16)$.

**Cuadrado $BCPQ$** (debajo de $BC$): $P=(26,-26)$, $Q=(0,-26)$.

**Cuadrado $ACMN$** (lado opuesto a $B$): el vector normal exterior es $(48,90)$ (ya con longitud $102$), así que $M=C+(48,90)=(74,90)$, $N=A+(48,90)=(-16,138)$.

## Puntos medios

$$L_1=\text{mid}(M,P)=\left(\tfrac{74+26}{2},\tfrac{90-26}{2}\right)=(50,32)$$
$$L_2=\text{mid}(Q,X)=\left(\tfrac{0-48}{2},\tfrac{-26-64}{2}\right)=(-24,-45)$$
$$L_3=\text{mid}(N,Y)=\left(\tfrac{-16-112}{2},\tfrac{138-16}{2}\right)=(-64,61)$$

## Área por fórmula del zapatero

$$\text{Área}=\tfrac12\left|50(-45-61)+(-24)(61-32)+(-64)(32+45)\right|$$
$$=\tfrac12\left|-5300-696-4928\right|=\tfrac12\cdot10924=5462$$

**Verificación:** existe la identidad general $[L_1L_2L_3]=\tfrac74 S+\tfrac{a^2+b^2+c^2}{4}$ (la comprobé con un triángulo equilátero de lado 1, donde ambos lados dan $\tfrac{7\sqrt3+12}{16}$). Aquí: $\tfrac74\cdot624+\tfrac{6400+676+10404}{4}=1092+4370=5462$ ✓.

$$\boxed{5462}$$