## Planteamiento

**Paso 1: puntos C y D.** Con $A=(0,0)$, $B=(1,0)$, las circunferencias de radio $1$ centradas en $A$ y $B$ se cortan en $\left(\tfrac12, \pm\tfrac{\sqrt3}{2}\right)$. Tomamos $C=\left(\tfrac12,\tfrac{\sqrt3}{2}\right)$, $D=\left(\tfrac12,-\tfrac{\sqrt3}{2}\right)$, así que $\overline{CD}=\sqrt3$.

**Paso 2: puntos E y F.** Las circunferencias de radio $\sqrt3$ centradas en $C$ y $D$ se cortan sobre el eje $AB$ (ecuador de simetría), en $x$ tal que
$$\left(x-\tfrac12\right)^2+\tfrac34 = 3 \;\Rightarrow\; \left(x-\tfrac12\right)^2=\tfrac94 \;\Rightarrow\; x=-1 \text{ o } x=2.$$
Con la condición $E,A,B,F$ en ese orden: $E=(-1,0)$, $F=(2,0)$, y $\overline{EF}=3$.

**Paso 3: puntos G y H.** Las circunferencias de radio $3$ centradas en $E$ y $F$ se cortan en $x=\tfrac12$ con
$$\left(\tfrac32\right)^2+y^2=9 \;\Rightarrow\; y^2=\tfrac{27}{4} \;\Rightarrow\; y=\pm\tfrac{3\sqrt3}{2}.$$
Como $C$ está arriba y $C,H$ deben quedar en lados opuestos de $AB$: $H=\left(\tfrac12,-\tfrac{3\sqrt3}{2}\right)$.

**Paso 4: área del pentágono $ACFHE$.** Vértices: $A=(0,0)$, $C=\left(\tfrac12,\tfrac{\sqrt3}{2}\right)$, $F=(2,0)$, $H=\left(\tfrac12,-\tfrac{3\sqrt3}{2}\right)$, $E=(-1,0)$.

**Fórmula del shoelace** $\;S=\sum(x_iy_{i+1}-x_{i+1}y_i)$:
- $A\to C$: $0$
- $C\to F$: $\tfrac12\cdot0 - 2\cdot\tfrac{\sqrt3}{2} = -\sqrt3$
- $F\to H$: $2\cdot\left(-\tfrac{3\sqrt3}{2}\right)-0 = -3\sqrt3$
- $H\to E$: $0-(-1)\left(-\tfrac{3\sqrt3}{2}\right) = -\tfrac{3\sqrt3}{2}$
- $E\to A$: $0$

$$S = -\tfrac{11\sqrt3}{2} \quad\Rightarrow\quad \text{Área} = \tfrac{1}{2}|S| = \tfrac{11\sqrt3}{4}.$$

**Verificación por descomposición:** el pentágono se parte en el triángulo $ACF$ (base $AF=2$, altura $\tfrac{\sqrt3}{2}$, área $\tfrac{\sqrt3}{2}$) y el cuadrilátero $AFHE$ (área $\tfrac{9\sqrt3}{4}$); la suma da $\tfrac{11\sqrt3}{4}$. ✓

$$\boxed{\dfrac{11\sqrt{3}}{4}}$$