## Solución

**Paso 1: Longitudes de los lados.**
$$AB = 4+16+8 = 28, \qquad AC = 13+52+26 = 91.$$
Nótese que $\frac{AF}{AD}=\frac{FG}{DE}=\frac{GC}{EB}=\frac{13}{4}$, es decir, $D\leftrightarrow F$, $E\leftrightarrow G$, $B\leftrightarrow C$.

**Paso 2: Determinar $\sin\theta$, donde $\theta = \angle A$.**
El cuadrilátero $DEGF$ es el triángulo $AEG$ menos el triángulo $ADF$:
$$[DEGF] = \tfrac12(20\cdot 65)\sin\theta - \tfrac12(4\cdot 13)\sin\theta = 624\sin\theta = 288 \implies \sin\theta = \frac{6}{13}.$$

**Paso 3: Coordenadas afines.**
Uso la base $(\vec e_1,\vec e_2)$ a lo largo de $AB$ y $AC$; el área en estas coordenadas es el determinante por $\sin\theta$:
$$D=(4,0),\ E=(20,0),\ B=(28,0),\qquad F=(0,13),\ G=(0,65),\ C=(0,91).$$
Como $M$ es el reflejo de $D$ respecto a $F$, y $N$ el de $G$ respecto a $E$:
$$M = 2F-D = (-4,26),\qquad N = 2E-G = (40,-65).$$

**Paso 4: Área del heptágono $AFNBCEM$ (polígono simple, como en la figura).**
Con vértices $A(0,0),\,F(0,13),\,N(40,-65),\,B(28,0),\,C(0,91),\,E(20,0),\,M(-4,26)$, la fórmula del shoelace da:
$$0 \;-\; 520 \;+\; 1820 \;+\; 2548 \;-\; 1820 \;+\; 520 \;+\; 0 = 2548,$$
$$[\,AFNBCEM\,] = \tfrac12\cdot 2548\cdot\sin\theta = 1274\cdot\frac{6}{13} = 588.$$

(De hecho, coincide con $[ABC] = \tfrac12\cdot 28\cdot 91\cdot\sin\theta = 588$.)

$$\boxed{588}$$