## Planteamiento

**Paso 1: El ángulo en $B$.**

Por la ley de cosenos, con $AB=80$, $BC=26$, $AC=102$:
$$\cos B = \frac{80^2+26^2-102^2}{2\cdot 80\cdot 26} = \frac{-3328}{4160} = -\frac45, \qquad \sin B = \frac35.$$

Coloco $B=(0,0)$, $A=(80,0)$, y entonces
$$C = 26\left(-\tfrac45,\ \tfrac35\right) = \left(-\tfrac{104}{5},\ \tfrac{78}{5}\right).$$

**Paso 2: Vértices de los cuadrados (hacia afuera).**

Cada cuadrado se obtiene sumando a los extremos del lado un vector perpendicular de la misma longitud, apuntando *afuera* del triángulo:

- Sobre $AB$ (el triángulo está arriba, el cuadrado va abajo): $X=B+(0,-80)=(0,-80)$, $Y=A+(0,-80)=(80,-80)$.
- Sobre $BC$: perpendicular hacia afuera $= \left(-\tfrac{78}{5},-\tfrac{104}{5}\right)$, luego $Q=\left(-\tfrac{78}{5},-\tfrac{104}{5}\right)$, $P=C+\left(-\tfrac{78}{5},-\tfrac{104}{5}\right)=\left(-\tfrac{182}{5},-\tfrac{26}{5}\right)$.
- Sobre $AC$: perpendicular hacia afuera $= \left(\tfrac{78}{5},\tfrac{504}{5}\right)$ (longitud $102$), luego $M=C+\left(\tfrac{78}{5},\tfrac{504}{5}\right)=\left(-\tfrac{26}{5},\tfrac{582}{5}\right)$, $N=A+\left(\tfrac{78}{5},\tfrac{504}{5}\right)=\left(\tfrac{478}{5},\tfrac{504}{5}\right)$.

**Paso 3: Los puntos medios.**

$$L_1 = \frac{M+P}{2} = \left(-\tfrac{104}{5},\ \tfrac{278}{5}\right),\quad L_2 = \frac{Q+X}{2} = \left(-\tfrac{39}{5},\ -\tfrac{252}{5}\right),\quad L_3 = \frac{N+Y}{2} = \left(\tfrac{439}{5},\ \tfrac{52}{5}\right).$$

**Paso 4: Área de $L_1L_2L_3$.**

 Vectores desde $L_1$:
$$L_2-L_1 = (13,\ -106), \qquad L_3-L_1 = \left(\tfrac{543}{5},\ -\tfrac{226}{5}\right).$$

Área $= \frac12\left| 13\cdot\left(-\tfrac{226}{5}\right) - (-106)\cdot\tfrac{543}{5} \right| = \frac12\cdot\frac{-2938+57558}{5} = \frac12\cdot 10924 = 5462.$

**Verificación (fórmula general).** El mismo cálculo en general da
$$[L_1L_2L_3] = \frac{a^2+b^2+c^2}{4} + \frac{7}{4}[ABC],$$
con $[ABC] = \frac12\cdot 80\cdot 26\cdot\frac35 = 624$. Entonces:
$$\frac{6400+676+10404}{4} + \frac{7\cdot 624}{4} = 4370 + 1092 = 5462. \checkmark$$

$\boxed{5462}$